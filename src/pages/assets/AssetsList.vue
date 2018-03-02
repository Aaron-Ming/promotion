<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>推介资产管理</span>
          <el-button style="float: right; padding: 3px 0" type="text" @click="showModal('add')">添加资产</el-button>
        </div>
        <el-table
          :data="properties"
          stripe
          style="width: 100%"
        >
          <el-table-column
            type="index"
            label="ID"
          >
          </el-table-column>
          <el-table-column
            prop="title"
            label="资产标题"
          >
          </el-table-column>
          <el-table-column
            prop="debt_type"
            label="资产类型"
          >
          </el-table-column>
          <el-table-column
            prop="mortgagor"
            label="抵押人"
          >
          </el-table-column>
          <el-table-column
            prop="contacts"
            label="联系人"
          >
          </el-table-column>
          <el-table-column
            prop="pub_time"
            label="发布时间"
          >
          </el-table-column>
          <el-table-column
            label="操作"
          >
            <template slot-scope="scope">
              <el-button type="text" size="small">查看</el-button>
              <el-button type="text" size="small" @click="showModal('edit', scope.$index)">编辑</el-button>
              <el-button type="text" size="small" @click="deleteProperty(scope.$index)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <!-- add/edit modal -->
    <el-dialog
      :title="propertyAdd ? '添加资产' : '编辑资产信息'"
      :visible.sync="propertyModal"
    >
      <el-form :model="currentProperty" label-width="80px" ref="categoryForm">
        <el-form-item label="资产标题">
          <el-input v-model="currentProperty.title"></el-input>
        </el-form-item>
        <el-form-item label="资产类型">
          <el-input v-model="currentProperty.debt_type"></el-input>
        </el-form-item>
        <el-form-item label="资产说明">
            <el-input type="textarea" v-model="propertyInstr"></el-input>
        </el-form-item>
        <el-form-item label="配套信息">
            <el-input type="textarea" v-model="propertyParms"></el-input>
        </el-form-item>


        <el-form-item label="债权机构">
            <el-input v-model="currentProperty.bond_institution"></el-input>
        </el-form-item>

        <el-form-item label="债务人">
            <el-input v-model="currentProperty.obligor"></el-input>
        </el-form-item>

        <el-form-item label="保证人">
            <el-input v-model="currentProperty.guarantee"></el-input>
        </el-form-item>

        <el-form-item label="抵押人">
            <el-input v-model="currentProperty.mortgagor"></el-input>
        </el-form-item>

        <el-form-item label="资产亮点">
            <el-input v-model="currentProperty.propertySpot"></el-input>
        </el-form-item>

        <el-form-item label="联系人">
            <el-input v-model="currentProperty.contacts"></el-input>
        </el-form-item>

        <el-form-item label="联系人电话">
            <el-input v-model="currentProperty.c_phone"></el-input>
        </el-form-item>

        <el-form-item label="传真">
            <el-input v-model="currentProperty.fax"></el-input>
        </el-form-item>

        <el-form-item label="通讯地址">
            <el-input v-model="currentProperty.p_address"></el-input>
        </el-form-item>

        <el-form-item label="交易对象">
            <el-input v-model="currentProperty.transaction"></el-input>
        </el-form-item>

        <el-form-item label="声明">
            <el-input v-model="currentProperty.statement"></el-input>
        </el-form-item>



      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="propertyModal = false">取 消</el-button>
        <el-button type="primary" @click="submitProperty">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
  import chinese from 'src/common/chinese'
  export default {
    data() {
      return {
        propertyInstr: '',
        propertyParms: '',
        propertySpot: '',
        properties: [],
        propertyModal: false,
        propertyAdd: false,
        currentProperty: {},
        currentIndex: null,
        propertyUrl: '/assets/properties/'
      }
    },
    created() {
      this.getProperties()
    },
    methods: {
      getProperties() {
        this.axios.get(this.propertyUrl)
        .then(res => {
          if (res.status == 200) {
            this.properties = res.data
            console.log(this.properties)
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
          this.propertyAdd = true
          if(this.currentProperty.id) {
            this.currentProperty = {}
          }
        } else if(index>=0) {
          this.currentIndex = index
          this.currentProperty = Object.assign({}, this.properties[index])
        }
        this.propertyModal = true
      },
      detailUrl() {
        return this.propertyUrl + this.currentProperty.id + '/'
      },
      test() {
        return 'aaa'
      },
      submitProperty() {
        let submitUrl =  this.propertyUrl
        let method = 'post'
        if(!this.propertyAdd) {
          submitUrl = this.detailUrl()
          method = 'put'
        }
        this.axios({
          method: method,
          data: this.currentProperty,
          url: submitUrl
        }).then(res => {
          if(res.status<400) {
            if(this.propertyAdd) {
              this.properties.push(res.data)
            } else {
              this.properties.splice(this.currentIndex, 1, this.currentProperty)
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
          this.propertyModal = false
        }).catch(error => {
          console.log(error)
        })
      },
      deleteProperty(index) {
        let delConfirmType = 'success'
        let delConfirmMsg = '删除成功!'
        this.currentIndex = index
        this.currentProperty = Object.assign({}, this.properties[this.currentIndex])
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
              delConfirmMsg = '删除' + this.currentProperty.title + '成功!'
              this.properties.splice(this.currentIndex, 1)
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
