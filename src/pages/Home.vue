<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>欢迎来到资产推介平台管理后台, 接下来要去往：</span>
        </div>
        <div v-for="menu in menus">
          <router-link :to="menu.path">{{ menu.name }}</router-link>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import menuData from 'components/aside/model/menuData'
  export default {
    data() {
      return {
        menus: menuData
      }
    }
  }
</script>
