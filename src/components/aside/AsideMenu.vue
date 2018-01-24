<template>
  <aside class="main-sidebar">
    <el-menu
    :default-active="$route.path"
    :router="true"
    :unique-opened="true"
    class="el-menu-vertical-demo"
    background-color="#222d32"
    text-color="#fff"
    active-text-color="#ffd04b"
    >
      <template v-for="(menu, m_index) in menues">
        <el-submenu
        v-if="menu.treeview && menu.treeviews.length"
        :index="menu.path"
        :key="'aside_menu_' + m_index">
          <template slot="title">
            <i :class="'fa ' + menu.icon"></i>
            <span>{{ menu.name }}</span>
          </template>
          <el-menu-item
          v-for="(item, sub_index) in menu.treeviews"
          :index="item.path"
          :key="'aside_submenu_' + m_index + sub_index">
          {{ item.name }}
          </el-menu-item>
        </el-submenu>
        <el-menu-item v-else
        :index="menu.path">
          <i :class="'fa ' + menu.icon"></i>
          <span slot="title">
            {{ menu.name }}
          </span>
        </el-menu-item>
      </template>
    </el-menu>
  </aside>
</template>

<script>
  import menuData from './model/menuData'
  export default {
    name: 'AsideMenu',
    data() {
      return {
        menues: menuData
      }
    }
  }
</script>

<style>
  .main-sidebar {
    position: absolute;
    top: 0;
    left: 0;
    padding-top: 50px;
    min-height: 100%;
    width: 230px;
    -webkit-transition: -webkit-transform 0.3s ease-in-out, width 0.3s ease-in-out;
    -moz-transition: -moz-transform 0.3s ease-in-out, width 0.3s ease-in-out;
    -o-transition: -o-transform 0.3s ease-in-out, width 0.3s ease-in-out;
    transition: transform 0.3s ease-in-out, width 0.3s ease-in-out;
  }
</style>
