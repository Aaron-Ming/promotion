<template>
  <section class="content-header">
    <el-breadcrumb class="app-levelbar" separator="/">
      <el-breadcrumb-item v-for="(item,index)  in levelList" :key="item.path">
        <span v-if='item.redirect==="noredirect"||index==levelList.length-1' class="no-redirect">{{item.name}}</span>
        <router-link v-else :to="item.redirect||item.path">{{item.name}}</router-link>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </section>
</template>

<script>
  export default {
    data() {
      return {
        levelList: null
      }
    },
    created() {
      this.getBreadcrumb()
    },
    watch: {
      $route() {
        this.getBreadcrumb()
      }
    },
    methods: {
      getBreadcrumb() {
        let matched = this.$route.matched.filter(item => item.name)
        const first = matched[0]
        if (first && (first.name !== 'Dashboard' || first.path !== '')) {
          matched = [{ name: 'Dashboard', path: '/' }].concat(matched)
        }
        this.levelList = matched
      }
    }
  }
</script>
