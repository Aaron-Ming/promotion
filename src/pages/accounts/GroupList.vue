<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>区域组管理</span>
          <el-button style="float: right; padding: 3px 0" type="text">添加区域</el-button>
        </div>
        <div class="dataTable_wrapper">
          <table id="groupTable" class="table table-striped table-bordered table-hover" cellspacing="0" width="100%">
            <thead>
              <tr>
                <th>ID</th>
                <th>区域名称</th>
                <th>别名</th>
                <th>组管理员</th>
                <th>操作</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(group, index) in groups"
                :key="group.id"
              >
                <td>{{ group.id }}</td>
                <td>{{ group.group_name }}</td>
                <td>{{ group.alias_name }}</td>
                <td>{{ group.group_admin }}</td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import chinese from 'src/common/chinese'
  export default {
    data() {
      return {
        groups: [],
        dataTable: null,
      }
    },
    created() {
      this.renderDataTable()
    },
    methods: {
      renderDataTable() {
        if(this.dataTable){
          this.dataTable.destroy()
          this.dataTable = null
        }
        setTimeout(() => {
          this.dataTable = $('#groupTable').DataTable({
            'language': chinese,
            'autoWidth': false,
            'bJQueryUI': true,
          })
        })
      },
    },
  }
</script>
