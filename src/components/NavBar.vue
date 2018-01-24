<template>
  <header class="main-header">
    <a href="javascript:void(0);" class="logo">
      <span class="logo-mini" v-show="logoMini">
        <b>OP</b>
      </span>
      <span class="logo-lg" v-show="!logoMini">
        <b>运维平台</b>
      </span>
    </a>
    <nav class="op-navbar">
      <a href="javascript:void(0);" class="sidebar-toggle">
        <i class="fa fa-bars"></i>
        <span class="sr-only">小菜单</span>
      </a>
      <!-- 右上角菜单 -->
      <div class="op-navbar-custom-menu">
        <el-dropdown trigger="click" @command="handleCommand">
          <span class="el-dropdown-link">
            <img :src="user.avatar || 'img/user2-160x160.jpg'" class="user-image">
            {{ user.name }}
            <i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="logout">登出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </nav>
  </header>
</template>

<script>
  import { mapState } from 'vuex'
  import * as types from 'src/store/types'
  export default {
    data() {
      return {}
    },
    computed: {
      ...mapState([
        'user'
      ])
    },
    props: {
      logoMini: {
        default: false
      }
    },
    methods: {
      logout() {
        this.axios.post('/v1/user/logout', {user_id: this.$store.state.user.user_id})
        .then(resposn => {
          let logoutData = resposn.data
          if(logoutData.status == '2001' || logoutData.status == '4001') {
            this.$store.commit(types.LOGOUT)
            this.$router.push({path: '/login'})
          } else {
            this.swal('Oops! 登出失败了哎', 'error')
          }
        })
        .catch(error => {
          console.log(error)
          this.swal('Oops! 出错了', error, 'error')
        })
      },
      handleCommand(command) {
        if(command=='logout') {
          this.logout()
        }
      }
    }
  }
</script>

<style>
  .main-header {
    position: relative;
    max-height: 100px;
    background-color: #3c8dbc;
  }
  .main-header .logo .logo-lg {
    display: block;
  }
  .main-header .logo {
    background-color: #367fa9;
    color: #fff;
    border-bottom: 0 solid transparent;
  }
  .main-header .logo {
    -webkit-transition: width 0.3s ease-in-out;
    -o-transition: width 0.3s ease-in-out;
    transition: width 0.3s ease-in-out;
    display: block;
    float: left;
    height: 50px;
    font-size: 20px;
    line-height: 50px;
    text-align: center;
    width: 230px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    padding: 0 15px;
    font-weight: 300;
    overflow: hidden;
    box-sizing: border-box;
  }
  .main-header .op-navbar {
    -webkit-transition: margin-left 0.3s ease-in-out;
    -o-transition: margin-left 0.3s ease-in-out;
    transition: margin-left 0.3s ease-in-out;
    margin-bottom: 0;
    margin-left: 230px;
    border: none;
    min-height: 50px;
    border-radius: 0;
  }
  .main-header .sidebar-toggle {
    float: left;
    padding: 15px 15px;
    font-family: fontAwesome;
    color: #fff;
  }
  .main-header .op-navbar-custom-menu {
    float: right;
    margin-right: 15px;
    padding-left: 15px;
  }
  .op-navbar-custom-menu .el-dropdown-link {
    color: #fff;
    cursor: pointer;
  }
  .op-navbar-custom-menu .el-dropdown {
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .op-navbar-custom-menu .user-image {
    float: left;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    margin-right: 10px;
    margin-top: -2px;
  }
  .logo {
    height: 50px;
    background-color: #367fa9 !important;
    color: #fff;
    line-height: 50px;
    text-align: center;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 20px;
  }
</style>
