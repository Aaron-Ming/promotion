<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>用户管理</span>
          <el-button style="float: right; padding: 3px 0" type="text">添加用户</el-button>
        </div>
        
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    data() {
      return {
        users: []
      }
    }
  }
</script>
