<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>用户管理</span>
          <el-button
            style="float: right; padding: 3px 0"
            type="text"
            @click="showModal('add')">添加用户</el-button>
        </div>
        <el-table
          :data="users"
          stripe
          style="width: 100%"
        >
          <el-table-column
            prop="mobile"
            label="手机号"
          ></el-table-column>
          <el-table-column
            prop="id_name"
            label="姓名"
          ></el-table-column>
          <el-table-column
            prop="occupation"
            label="职业"
          ></el-table-column>
          <el-table-column
            prop="group_name"
            label="区域组"
          ></el-table-column>
          <el-table-column
            prop="role_name"
            label="角色"
          ></el-table-column>
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
    <!-- user modal -->
    <el-dialog
      :title="userAdd ? '添加用户' : '编辑用户'"
      :visible.sync="userModalShow"
    >
      <el-form
        :model="currentUser"
        :rules="userRules"
        label-width="80px"
        ref="userForm"
      >
        <el-form-item label="手机号" prop="mobile">
          <el-input
            v-model="currentUser.mobile"
            placeholder="手机号／用户登入"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="密码" v-if="userAdd"
          prop="password"
          :rules="[{required: true, message: '请设置一个密码', trigger: 'blur'}]"
        >
          <el-input
            v-model="currentUser.password"
            type="password"
            placeholder="密码"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="身份证号" prop="id_number">
          <el-input
            v-model="currentUser.id_number"
            placeholder="18位身份证号"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="id_name">
          <el-input
            v-model="currentUser.id_name"
            placeholder="请输入身份证上的姓名"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="信用代码">
          <el-input
            v-model="currentUser.credit_code"
            placeholder="统一社会信用代码"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="职业">
          <el-input
            v-model="currentUser.occupation"
            placeholder="请输入用户的职业"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="区域组" prop="group">
          <el-select v-model="currentUser.group" placeholder="请选择区域"
          filterable>
            <el-option
              v-for="group in selectData.groups"
              :key="group.id"
              :label="group.group_name"
              :value="group.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="角色" prop="role">
          <el-select v-model="currentUser.role" placeholder="请选择角色"
            disabled>
            <el-option
              v-for="role in selectData.roles"
              :key="role.id"
              :label="role.role_name"
              :value="role.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="userModalShow = false">取 消</el-button>
        <el-button type="primary" @click="submitUser()">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
  export default {
    data() {
      return {
        users: [],
        userAdd: false,
        userModalShow: false,
        currentUser: {},
        currentIndex: null,
        selectData: {
          roles: [],
          groups: [],
        },
        userRules: {
          mobile: [
            {required: true, message: '请输入手机号', trigger: 'change, blur'},
            {validator: this.checkMobile, trigger: 'blur'}
          ],
          id_number: [
            {required: true, message: '请输入身份证号', trigger: 'change, blur'},
            {validator: this.checkIdNumber, trigger: 'change, blur'}
          ],
          id_name: [
            {required: true, message: '请输入姓名', trigger: 'change, blur'}
          ],
          group: [
            {required: true, message: '请选择区域', trigger: 'change', type: 'number'}
          ],
          role: [
            {required: true, message: '请选择角色', trigger: 'change', type: 'number'}
          ],
        },
      }
    },
    created() {
      this.getUsers()
    },
    methods: {
      getUsers() {
        this.axios.get('/accounts/users/')
        .then(res => {
          if(res.status == 200) {
            this.users = res.data
          } else {
            this.$notify.error({
              title: '获取用户失败',
              duration: 20000,
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getRoles() {
        if(this.selectData.roles.length > 0) {
          if(this.userAdd) {
            const defaultRole = this.selectData.roles.filter(el => {
              return el.role_level == 4
            })
            this.currentUser.role = defaultRole[0].id
          }
          return false
        }
        this.axios.get('/accounts/roles/')
        .then(res => {
          if(res.status == 200) {
            this.selectData.roles = res.data
            if(this.userAdd) {
              const defaultRole = res.data.filter(el => {
                return el.role_level == 4
              })
              this.currentUser.role = defaultRole[0].id
            }
          } else {
            this.$notify.error({
              title: '获取角色失败',
              duration: 20000,
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getGroups() {
        if(this.selectData.groups.length > 0) {
          return false
        }
        this.axios.get('/accounts/groups/')
        .then(res => {
          if(res.status == 200) {
            this.selectData.groups = res.data
          } else {
            this.$notify.error({
              title: '获取区域组失败',
              duration: 20000,
              message: this.$format('错误代码：{0}, 请刷新或联系管理员', res.status)
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      setCurrentUser(index) {
        if(this.userAdd && this.currentUser.id) {
          this.currentUser = {role: this.currentUser.role || null}
        } else if(index>=0) {
          this.currentUser = Object.assign({}, this.users[index])
          this.currentIndex = index
        }
      },
      showModal(action, index) {
        this.userAdd = action == 'add'
        this.getGroups()
        this.getRoles()
        this.setCurrentUser(index)
        this.userModalShow = true
      },
      submitUser() {
        this.$refs['userForm'].validate((valid) => {
          if(valid) {
            const method = this.userAdd ? 'post' : 'put'
            const submitApi = this.userAdd ? '/accounts/users/' : '/accounts/users/' + this.currentUser.id + '/'
            const msg = this.userAdd ? '添加' : '修改'
            this.axios({
              method: method,
              url: submitApi,
              data: this.currentUser
            }).then(res => {
              const user = res.data
              if(this.userAdd && res.status == 201) {
                this.currentUser.id = user.id
                this.users.push(user)
                this.$message({
                  message: '用户添加成功',
                  type: 'success'
                })
              } else if(res.status == 200) {
                this.users.splice(this.currentIndex, 1, user)
                this.$message({
                  message: '用户编辑成功',
                  type: 'success'
                })
              } else {
                this.$notify.error({
                  title: '用户'+ msg +'失败',
                  duration: 0,
                  message: '错误代码: '+ res.status +', 请联系管理员'
                })
              }
            }).catch(error => {
              console.log(error)
            })
            this.userModalShow = false
          } else {
            console.log('submit error')
            return false
          }
        })
      },
      checkMobile(rule, value, callback) {
        if(!value) {
          return callback(new Error('请输入手机号'))
        }
        setTimeout(() => {
          const reg = /^1[0-9]{10}$/
          if(!reg.test(value)) {
            callback(new Error('请输入正确的手机号'))
          } else {
            const checkUrl = '/accounts/check_mobile/'
            this.axios.get(checkUrl, {
              params: {mobile: value}
            }).then(res => {
              const resData = res.data
              if(resData.is_used) {
                callback(new Error('手机号已被注册，请更换'))
              } else {
                callback()
              }
            })
          }
        }, 1000)
      },
      checkIdNumber(rule, value, callback) {
        // 验证身份证号
        if(typeof value !== 'string'){
          return callback(new Error('非法字符串'))
        }
        var city = {11:"北京",12:"天津",13:"河北",14:"山西",15:"内蒙古",21:"辽宁",22:"吉林",23:"黑龙江 ",31:"上海",32:"江苏",33:"浙江",34:"安徽",35:"福建",36:"江西",37:"山东",41:"河南",42:"湖北 ",43:"湖南",44:"广东",45:"广西",46:"海南",50:"重庆",51:"四川",52:"贵州",53:"云南",54:"西藏 ",61:"陕西",62:"甘肃",63:"青海",64:"宁夏",65:"新疆",71:"台湾",81:"香港",82:"澳门",91:"国外"};
        var birthday = value.substr(6, 4) + '/' + Number(value.substr(10, 2)) + '/' + Number(value.substr(12, 2));
        var d = new Date(birthday);
        var newBirthday = d.getFullYear() + '/' + Number(d.getMonth() + 1) + '/' + Number(d.getDate());
        var currentTime = new Date().getTime();
        var time = d.getTime();
        var arrInt = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
        var arrCh = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'];
        var sum = 0, i, residue;
        if(!/^\d{17}(\d|x)$/i.test(value)) {
          return callback(new Error('非法身份证'))
        }
        if(city[value.substr(0,2)] === undefined) {
          return callback(new Error("非法地区"))
        }
        if(time >= currentTime || birthday !== newBirthday) {
          return callback(new Error('非法生日'))
        }
        for(i=0; i<17; i++) {
          sum += value.substr(i, 1) * arrInt[i];
        }
        residue = arrCh[sum % 11];
        if (residue !== value.substr(17, 1)) {
          return callback(new Error('非法身份证哦'))
        }
        // return city[value.substr(0,2)]+","+birthday+","+(value.substr(16,1)%2?" 男":"女")
        callback()
      },
    },
  }
</script>
