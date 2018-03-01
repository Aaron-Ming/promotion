<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>用户管理</span>
          <el-button
            style="float: right; padding: 3px 0"
            type="text"
            @click="showModal('add')">添加用户</el-button>
        </div>
        <el-table
          :data="users"
          stripe
          style="width: 100%"
        >
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
            prop="group_name"
            label="区域组"
          ></el-table-column>
          <el-table-column
            prop="role_name"
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
        <el-form-item label="密码" v-if="userAdd">
          <el-input
            v-model="currentUser.password"
            type="password"
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
          <el-select v-model="currentUser.group" placeholder="请选择区域"
          filterable>
            <el-option
              v-for="group in selectData.groups"
              :key="group.id"
              :label="group.group_name"
              :value="group.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="currentUser.role" placeholder="请选择角色"
            disabled>
            <el-option
              v-for="role in selectData.roles"
              :key="role.id"
              :label="role.role_name"
              :value="role.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="userModalShow = false">取 消</el-button>
        <el-button type="primary" @click="submitUser()">确 定</el-button>
      </div>
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
        selectData: {
          roles: [],
          groups: [],
        },
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
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getRoles() {
        if(this.selectData.roles.length > 0) {
          if(this.userAdd) {
            const defaultRole = this.selectData.roles.filter(el => {
              return el.role_level == 4
            })
            this.currentUser.role = defaultRole[0].id
          }
          return false
        }
        this.axios.get('/accounts/roles/')
        .then(res => {
          if(res.status == 200) {
            this.selectData.roles = res.data
            if(this.userAdd) {
              const defaultRole = res.data.filter(el => {
                return el.role_level == 4
              })
              this.currentUser.role = defaultRole[0].id
            }
          } else {
            this.$notify.error({
              title: '获取角色失败',
              duration: 20000,
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getGroups() {
        if(this.selectData.groups.length > 0) {
          return false
        }
        this.axios.get('/accounts/groups/')
        .then(res => {
          if(res.status == 200) {
            this.selectData.groups = res.data
          } else {
            this.$notify.error({
              title: '获取区域组失败',
              duration: 20000,
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      setCurrentUser(index) {
        if(this.userAdd && this.currentUser.id) {
          this.currentUser = {role: this.currentUser.role || null}
        } else if(index>=0) {
          this.currentUser = Object.assign({}, this.users[index])
          this.currentIndex = index
        }
      },
      showModal(action, index) {
        this.userAdd = action == 'add'
        this.getGroups()
        this.getRoles()
        this.setCurrentUser(index)
        this.userModalShow = true
      },
      submitUser() {
        const method = this.userAdd ? 'post' : 'put'
        const submitApi = this.userAdd ? '/accounts/users/' : this.$format('/accounts/users/{0}/', this.currentUser.id)
        this.axios({
          method: method,
          url: submitApi,
          data: this.currentUser
        }).then(res => {
          console.log(res)
          if(res.status == 201) {
            const user = res.data
            this.currentUser.id = user.id
            this.users.push(user)
            this.$message({
              message: '用户添加成功',
              type: 'success'
            })
          } else {
            this.$notify.error({
              title: '用户添加失败',
              duration: 0,
              message: this.$format('错误代码：{0}, 请联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
        this.userModalShow = false
      },
    },
  }
</script>
