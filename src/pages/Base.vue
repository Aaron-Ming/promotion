<template>
  <div class="wrapper">
    <!-- 页面头信息 -->
    <nav-bar :logoMini="logo_mini"/>
    <!-- 侧边栏 -->
    <aside-menu/>
    <div class="content-wrapper">
      <breadcrumb/>
      <!-- content -->
      <section class="content">
        <router-view/>
      </section>
    </div>
  </div>
</template>

<script>
  import AsideMenu from 'components/aside/AsideMenu'
  import NavBar from 'components/NavBar'
  import Breadcrumb from 'components/Breadcrumb'
  export default {
    data() {
      return {
        logo_mini: false,
      }
    },
    components: {
      AsideMenu, NavBar, Breadcrumb
    }
  }
</script>

<style>
  .wrapper {
    height: 100%;
    /*position: relative;*/
    overflow-x: hidden;
    overflow-y: auto;
  }
  .wrapper:before,
  .wrapper:after {
    content: " ";
    display: table;
  }
  .wrapper:after {
    clear: both;
  }
  .wrapper a {
    text-decoration: none;
  }
  .content-wrapper {
    min-height: 100%;
    -webkit-transition: -webkit-transform 0.3s ease-in-out, margin 0.3s ease-in-out;
    -moz-transition: -moz-transform 0.3s ease-in-out, margin 0.3s ease-in-out;
    -o-transition: -o-transform 0.3s ease-in-out, margin 0.3s ease-in-out;
    transition: transform 0.3s ease-in-out, margin 0.3s ease-in-out;
    margin-left: 230px;
  }
  .content-header {
    position: relative;
    padding: 15px 15px 0 15px;
  }
  .content {
    min-height: 250px;
    padding: 15px;
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
  }
</style>
