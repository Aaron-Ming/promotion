<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>资产类别管理</span>
          <el-button style="float: right; padding: 3px 0" type="text" @click="showModal('add')">添加种类</el-button>
        </div>
        <el-table
          :data="categorys"
          stripe
          style="width: 100%"
        >
          <el-table-column
            prop="id"
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
              <el-button type="text" size="small">查看</el-button>
              <el-button type="text" size="small">编辑</el-button>
              <el-button type="danger" size="mini" @click="deleteCategory(scope.row.id)">删除</el-button>
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
        delCategoryId: {},
      }
    },
    created() {
      this.getCategorys()
    },
    methods: {
      showModal(action) {
        if(action == 'add') {
          this.categoryAdd = true
        }
        this.categoryModal = true
      },
      submitCategory() {
        this.axios.post('/assets/category_create/', this.currentCategory)
        .then(response => {
          if (response.data.success == true) {
            console.log('lsdjflskaaaaaaaaa')
            this.currentCategory.id = response.data.data
            this.categorys.push(this.currentCategory)
            this.categoryModal = false
            console.log(response)
          } else {
            console.log('submitCategory error....')
          }
          
        }).catch(error => {
          console.log(error)
        })
      },
      getCategorys() {
        this.axios.get('/assets/category_list/')
        .then(response => {
          if (response.data.success == true) {
            this.categorys = response.data.data
          } else {
            console.log('error11111111111')
          }
        })
      },
      deleteCategory(category_id) {
        console.log(category_id)
        this.delCategoryId.id = category_id
        this.axios.post('/assets/category_delete/', this.delCategoryId)
        
      },
    },
    
  }
</script>
