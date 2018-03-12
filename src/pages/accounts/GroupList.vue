<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>区域组管理</span>
          <el-button style="float: right; padding: 3px 0" type="text" @click="showModal('add')">添加区域</el-button>
        </div>
        <el-table
          :data="groups"
          stripe
          style="width: 100%"
        >
          <el-table-column
            prop="id"
            label="ID"
          >
          </el-table-column>
          <el-table-column
            prop="group_name"
            label="区域名称"
          >
          </el-table-column>
          <el-table-column
            prop="alias_name"
            label="别名"
          >
          </el-table-column>
          <el-table-column
            prop="group_admin_name"
            label="管理员"
          >
          </el-table-column>
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
    <!-- add/edit modal -->
    <el-dialog
      :title="groupAdd ? '添加区域' : '编辑区域'"
      :visible.sync="groupModal"
    >
      <el-form :model="currentGroup" label-width="80px" ref="groupForm">
        <el-form-item label="区域名称">
          <el-input v-model="currentGroup.group_name"></el-input>
        </el-form-item>
        <el-form-item label="区域别名">
          <el-input v-model="currentGroup.alias_name" placeholder="英文／拼音 不能重复"></el-input>
        </el-form-item>
        <!-- <el-form-item label="管理员">
          <el-input v-model="currentGroup.group_admin"></el-input>
        </el-form-item> -->
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="groupModal = false">取 消</el-button>
        <el-button type="primary" @click="submitGroup">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
  export default {
    data() {
      return {
        groups: [],
        groupModal: false,
        groupAdd: false,
        currentGroup: {},
        currentIndex: null,
      }
    },
    created() {
      this.getGroups()
    },
    methods: {
      getGroups() {
        this.axios.get('/accounts/groups/')
        .then(res => {
          if(res.status == 200) {
            this.groups = res.data
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '错误代码: ' + res.status
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      showModal(action, index) {
        if(action == 'add') {
          this.groupAdd = true
          if(this.currentGroup.id) {
            this.currentGroup = {}
          }
        } else if(index>=0) {
          this.currentIndex = index
          this.currentGroup = Object.assign({}, this.groups[index])
        }
        this.groupModal = true
      },
      detailUrl() {
        return '/accounts/groups/' + this.currentGroup.id + '/'
      },
      submitGroup() {
        let submitUrl = '/accounts/groups/'
        let method = 'post'
        if(!this.groupAdd) {
          submitUrl = this.detailUrl()
          method = 'put'
        }
        this.axios({
          method: method,
          data: this.currentGroup,
          url: submitUrl
        }).then(res => {
          if(res.status<400) {
            if(this.groupAdd) {
              this.groups.push(res.data)
            } else {
              this.groups.splice(this.currentIndex, 1, this.currentGroup)
            }
            this.$message({
              message: '操作成功！',
              type: 'success'
            })
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: res.data
            })
          }
          this.groupModal = false
        }).catch(error => {
          console.log(error)
        })
      },
    },
  }
</script>
