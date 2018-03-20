<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>资产类别管理</span>
          <el-button style="float: right; padding: 3px 0" type="text" @click="showModal('add')">添加类型</el-button>
        </div>
        <el-table
          :data="categorys"
          stripe
          style="width: 100%"
        >
          <el-table-column
            type="index"
            label="ID"
          >
          </el-table-column>
          <el-table-column
            prop="category_name"
            label="种类名称"
          >
          </el-table-column>
          <el-table-column
            label="操作"
          >
            <template slot-scope="scope">
              <el-button type="primary" size="mini" @click="showModal('edit', scope.$index)">编辑</el-button>
              <el-button type="danger" size="mini" @click="deleteCategory(scope.$index)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <!-- add/edit modal -->
    <el-dialog
      :title="categoryAdd ? '添加种类' : '编辑种类'"
      :visible.sync="categoryModal"
    >
      <el-form :model="currentCategory" label-width="80px" ref="categoryForm">
        <el-form-item label="类型名称">
          <el-input v-model="currentCategory.category_name"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="categoryModal = false">取 消</el-button>
        <el-button type="primary" @click="submitCategory">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
  import chinese from 'src/common/chinese'
  export default {
    data() {
      return {
        categorys: [],
        categoryModal: false,
        categoryAdd: false,
        currentCategory: {},
        currentIndex: null,
        categoryDel: false,
        categoryUrl: '/assets/categorys/'
      }
    },
    created() {
      this.getCategorys()
    },
    methods: {
      getCategorys() {
        this.axios.get('/assets/categorys/')
        .then(res => {
          if (res.status == 200) {
            this.categorys = res.data
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '错误代码: ' + res.status
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      showModal(action, index) {
        if(action == 'add') {
          this.categoryAdd = true
          if(this.currentCategory.id) {
            this.currentCategory = {}
          }
        } else if(index>=0) {
          this.currentIndex = index
          this.currentCategory = Object.assign({}, this.categorys[index])
        }
        this.categoryModal = true
      },
      detailUrl() {
        return this.categoryUrl + this.currentCategory.id + '/'
      },
      submitCategory() {
        let submitUrl =  '/assets/categorys/'
        let method = 'post'
        if(!this.categoryAdd) {
          submitUrl = this.detailUrl()
          method = 'put'
        }
        this.axios({
          method: method,
          data: this.currentCategory,
          url: submitUrl
        }).then(res => {
          if(res.status<400) {
            if(this.categoryAdd) {
              this.categorys.push(res.data)
            } else {
              this.categorys.splice(this.currentIndex, 1, this.currentCategory)
            }
            this.$message({
              message: '操作成功！',
              type: 'success'
            })
          } else {
            let errorMsg = ''
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: res.data
            })
          }
          this.categoryModal = false
        }).catch(error => {
          console.log(error)
        })
      },
      deleteCategory(index) {
        let delConfirmType = 'success'
        let delConfirmMsg = '删除成功!'
        this.currentIndex = index
        this.currentCategory = Object.assign({}, this.categorys[this.currentIndex])
        this.$confirm('是否删除此类型', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.axios({
            method: 'delete',
            url: this.detailUrl()
          }).then(res => {
            if (res.status<400) {
              delConfirmMsg = '删除' + this.currentCategory.category_name + '成功!'
              this.categorys.splice(this.currentIndex, 1)
            } else {
              this.$notify.error({
                title: '出错了',
                duration: 0,
                message: res.data
              })
              delConfirmType = 'info'
              delConfirmMsg = '已取消删除!'
            }
            this.$message({
              type: delConfirmType,
              message: delConfirmMsg
            });
          }).catch(error => {
            console.log(error)
          });
        });
      }
    },
  }
</script>
