<template>
  <div class="login">
    <el-row>
      <el-col :span="12" :offset="6">
        <h1>欢迎登入运维平台</h1>
        <small v-show="!loginStatus.success">{{ loginStatus.msg }}</small>
        <el-form ref="userForm" :model="userForm" :rules="rules" label-width="80px">
          <el-form-item label="用户名" prop="user">
            <el-input v-model="userForm.user" placeholder="邮箱"></el-input>
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
          user: '',
          password: ''
        },
        rules: {
          user: [
            {required: true, message: '请输入登入邮箱', trigger: 'blur'},
            {type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur,change'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        },
        loginStatus: {
          success: true,
          msg: ''
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
            this.axios.post('/v1/user/login', this.userForm)
            .then(response => {
              let loginData = response.data
              if(loginData.status == '2000' && loginData.success == true) {
                this.$store.commit(types.LOGIN, loginData)
                this.$router.push({path: this.redirect})
              } else {
                this.loginStatus.success = loginData.success
                this.loginStatus.msg = loginData.msg
              }
            })
            .catch(error => {
              console.log(error)
              this.swal('Oops! 出错了', error, 'error')
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
