<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>用户管理</span>
          <el-button style="float: right; padding: 3px 0" type="text">添加用户</el-button>
        </div>
        <el-table
          :data="users"
          stripe
          style="width: 100%"
        >
          <el-table-column
            prop="username"
            label="用户名"
          ></el-table-column>
          <el-table-column
            prop="mobile"
            label="手机号"
          ></el-table-column>
          <el-table-column
            prop="id_name"
            label="姓名"
          ></el-table-column>
          <el-table-column
            prop="occupation"
            label="职业"
          ></el-table-column>
          <el-table-column
            prop="group"
            label="区域组"
          ></el-table-column>
          <el-table-column
            prop="role"
            label="角色"
          ></el-table-column>
          <el-table-column
            label="操作"
          >
            <template slot-scope="scope">
              <el-button type="text" size="small">查看</el-button>
              <el-button type="text" size="small" @click="showModal('edit', scope.$index)">编辑</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <!-- user modal -->
    <el-dialog
      :title="userAdd ? '添加用户' : '编辑用户'"
      :visible.sync="userModalShow"
    >
      <el-form
        :model="currentUser"
        label-width="80px"
        ref="userForm"
      >
        <el-form-item label="手机号">
          <el-input
            v-model="currentUser.mobile"
            placeholder="手机号／用户登入"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            v-model="currentUser.password"
            placeholder="密码"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="身份证号">
          <el-input
            v-model="currentUser.id_number"
            placeholder="18位身份证号"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input
            v-model="currentUser.id_name"
            placeholder="请输入身份证上的姓名"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="信用代码">
          <el-input
            v-model="currentUser.credit_code"
            placeholder="统一社会信用代码"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="职业">
          <el-input
            v-model="currentUser.occupation"
            placeholder="请输入用户的职业"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="区域组">
          <el-input
            v-model="currentUser.group"
            placeholder="用户所属区域组"
          >
          </el-input>
        </el-form-item>
        <div slot="footer" class="dialog-footer">
          <el-button @click="userModalShow = false">取 消</el-button>
          <el-button type="primary" @click="submitUser()">确 定</el-button>
        </div>
      </el-form>
    </el-dialog>
  </el-row>
</template>

<script>
  export default {
    data() {
      return {
        users: [],
        userAdd: false,
        userModalShow: false,
        currentUser: {},
        currentIndex: null,
      }
    },
    created() {
      this.getUsers()
    },
    methods: {
      getUsers() {
        this.axios.get('/accounts/users/')
        .then(res => {
          if(res.status == 200) {
            this.users = res.data
          } else {
            this.$notify.error({
              title: '获取用户失败',
              duration: 20000,
              message: '错误代码：' + res.status + ' 请刷新或联系管理员'
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      showModal(action, index) {
        console.log(11111)
      },
      submitUser() {
        console.log('submit user')
      },
    },
  }
</script>
