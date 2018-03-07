<template>
  <div class="login">
    <el-row>
      <el-col :span="12" :offset="6">
        <h1>欢迎登入资产管理平台</h1>
        <el-form ref="userForm" :model="userForm" :rules="rules" label-width="80px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="userForm.username" placeholder="邮箱"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="userForm.password" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" round size="medium" native-type="button" style="width: 100%" @click="login">登入</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import * as types from 'src/store/types'
  export default {
    data() {
      return {
        userForm: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            {required: true, message: '请输管理员账号', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        },
        redirect: '/'
      }
    },
    created() {
      let redirect = decodeURIComponent(this.$route.query.redirect || '/')
      this.redirect = redirect
      if(this.$store.state.user.token){
        this.$router.push({path: redirect})
      }
    },
    methods: {
      login() {
        this.$refs['userForm'].validate((valid) => {
          if(valid) {
            this.axios.post('/accounts/login/', this.userForm)
            .then(res => {
              if(res.status == 400) {
                this.$message({
                  showClose: true,
                  message: '用户名／密码错误',
                  type: 'error',
                  duration: 0,
                })
              } else if(res.status == 403) {
                this.$message({
                  showClose: true,
                  message: res.data.error_msg,
                  type: 'error',
                  duration: 0,
                })
              } else {
                this.$store.commit(types.LOGIN, res.data)
                this.$router.push({path: this.redirect})
              }
            })
            .catch(error => {
              console.log(error)
            })
          } else {
            console.log('error login')
            return false
          }
        })
      }
    }
  }
</script>

<style>
  .login {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
