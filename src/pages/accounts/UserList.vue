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
          <el-button
            v-if="activeUser.role_level < 3"
            style="float: right; padding: 3px 10px"
            type="text"
            @click="checkActiveType()"
          >{{ checkTypeData.btnText }}</el-button>
        </div>
        <el-table
          :data="users"
          stripe
          style="width: 100%"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="身份证号">
                  <span>{{ props.row.id_number }}</span>
                </el-form-item>
                <el-form-item label="信用代码">
                  <span>{{ props.row.credit_code }}</span>
                </el-form-item>
                <el-form-item label="身份证正面">
                  <img :src="props.row.id_face" class="expand-img">
                </el-form-item>
                <el-form-item label="身份证反面">
                  <img :src="props.row.id_back" class="expand-img">
                </el-form-item>
                <el-form-item label="营业执照">
                  <img :src="props.row.license" class="expand-img">
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
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
            label="激活"
          >
            <template slot-scope="scope">
              <span v-if="scope.row.active">已激活</span>
              <span v-else>未激活</span>
            </template>
          </el-table-column>
          <el-table-column
            label="操作"
          >
            <template slot-scope="scope">
              <!-- <el-button type="text" size="small"
                v-if="activeUser.is_superuser == 'true'"
                @click="setGroupAdmin(scope.$index)">设为组长</el-button> -->
              <el-button
                v-if="activeUser.role_level < scope.row.role_level && !scope.row.active"
                type="text" size="small"
                style="color: #67c23a"
                @click="changeActive(true, scope.row.id, scope.$index)"
              >激活</el-button>
              <el-button
                v-if="activeUser.role_level < scope.row.role_level && scope.row.active"
                type="text" size="small"
                style="color: #f56c6c"
                @click="changeActive(false, scope.row.id, scope.$index)"
              >失效</el-button>
              <el-button type="text" size="small"
                v-if="activeUser.role_level < scope.row.role_level || activeUser.profile_id == scope.row.id"
                @click="showModal('edit', scope.$index)"
              >编辑</el-button>
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
        label-width="90px"
        ref="userForm"
      >
        <el-form-item label="手机号" prop="mobile">
          <el-input
            v-model="currentUser.mobile"
            placeholder="手机号／用户登入"
            :disabled="!userAdd"
          >
          </el-input>
        </el-form-item>
        <div class="change-pwd-btn">
          <el-button type="text" size="small"
            v-if="activeUser.role_level < currentUser.role_level || activeUser.profile_id == currentUser.id"
            @click="restPWD = !restPWD; if(!restPWD) {delete currentUser['password']}"
          >{{restPWD ? '取消修改' : '修改密码'}}</el-button>
        </div>
        <el-form-item label="密码" v-if="userAdd || restPWD"
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
        <el-form-item label="区域组" prop="group">
          <el-select v-model="currentUser.group"
            placeholder="请选择区域"
            filterable
            :disabled="activeUser.is_superuser == 'false'"
          >
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
          <el-select v-model="currentUser.role"
            placeholder="请选择角色"
            :disabled="activeUser.role_level > 2 && activeUser.role_level !== '' || activeUser.profile_id == currentUser.id"
          >
            <el-option
              v-for="role in selectData.roles"
              :key="role.id"
              :label="role.role_name"
              :value="role.id"
              :disabled="activeUser.role_level >= role.role_level"
            >
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="姓名" prop="id_name">
          <el-input
            v-model="currentUser.id_name"
            placeholder="请输入身份证上的姓名"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="身份证号" prop="id_number"
          v-if="currentUser.role > 3"
        >
          <el-input
            v-model="currentUser.id_number"
            placeholder="18位身份证号"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="身份证正面"
          v-if="currentUser.role > 3"
        >
          <input ref="id_face" type="file" name="id_face" @change="imgChange('id_face')" id="id_face">
        </el-form-item>
        <img :src="currentUser.id_face" class="user-img" v-if="imgShow.id_face && currentUser.role > 3"
          id="id_face_src"
        >
        <el-form-item label="身份证反面"
          v-if="currentUser.role > 3"
        >
          <input ref="id_back" type="file" name="id_back" @change="imgChange('id_back')" id="id_back">
        </el-form-item>
        <img :src="currentUser.id_back" class="user-img" v-if="imgShow.id_back && currentUser.role > 3"
          id="id_back_src"
        >
        <el-form-item label="信用代码"
          v-if="currentUser.role > 3"
        >
          <el-input
            v-model="currentUser.credit_code"
            placeholder="统一社会信用代码"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="职业"
          v-if="currentUser.role > 3"
        >
          <el-input
            v-model="currentUser.occupation"
            placeholder="请输入用户的职业"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="营业执照"
          v-if="currentUser.role > 3"
        >
          <input ref="license" type="file" name="license" @change="imgChange('license')" id="license">
        </el-form-item>
        <img :src="currentUser.license" class="user-img" v-if="imgShow.license && currentUser.role > 3"
          id="license_src"
        >
      </el-form>
      <el-alert
          v-if="selectData.selectedGroupAdmin"
          title="如果该组已有组长，则原组长会被降级为组业务员"
          type="warning"
          close-text="知道了"
        >
        </el-alert>
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
        activeUser: this.$store.state.user,
        users: [],
        userAdd: false,
        userModalShow: false,
        restPWD: false,
        currentUser: {},
        currentIndex: null,
        selectData: {
          roles: [],
          groups: [],
          selectedGroupAdmin: false,
        },
        imgShow: {
          id_face: false,
          id_back: false,
          license: false
        },
        checkTypeData: {
          btnText: '查看未激活',
          is_active: true
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
    watch: {
      'currentUser.role'(val) {
        const roles = this.selectData.roles.filter(el => {
          return el.id == val
        })
        if(roles.length > 0) {
          const role = roles[0]
          if(role.role_level == 2) {
            this.selectData.selectedGroupAdmin = true
          }
        }
      },
    },
    created() {
      this.getUsers()
    },
    methods: {
      getUsers(is_active=true) {
        this.axios.get('/accounts/users/', {
          params: {
            active: is_active
          }
        })
        .then(res => {
          if(res.status == 200) {
            this.users = res.data
          } else {
            this.$notify.error({
              title: '获取用户失败',
              duration: 20000,
              message: '错误代码：'+res.status+', 请刷新或联系管理员'
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      checkActiveType() {
        if(this.checkTypeData.is_active) {
          this.checkTypeData.is_active = false
          this.checkTypeData.btnText = '查看全部'
          this.getUsers(false)
        } else {
          this.checkTypeData.is_active = true
          this.checkTypeData.btnText = '查看未激活'
          this.getUsers(true)
        }
      },
      setDefaultRole(roleData) {
        if(this.userAdd && this.activeUser.role_level > 2) {
          const defaultRole = roleData.filter(el => {
            return el.role_level == 4
          })
          this.currentUser.role = defaultRole[0].id
        }
      },
      getRoles() {
        if(this.selectData.roles.length > 0) {
          this.setDefaultRole(this.selectData.roles)
          return
        }
        this.axios.get('/accounts/roles/')
        .then(res => {
          if(res.status == 200) {
            this.selectData.roles = res.data
            this.setDefaultRole(res.data)
          } else {
            this.$notify.error({
              title: '获取角色失败',
              duration: 20000,
              message: '错误代码：'+res.status+', 请刷新或联系管理员',
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getGroups() {
        if(this.activeUser.role_level > 1) {
          this.selectData.groups = [
            {
              id: parseInt(this.activeUser.group_id),
              group_name: this.activeUser.group_name,
            }
          ]
          this.currentUser.group = parseInt(this.activeUser.group_id)
          return
        }
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
              message: '错误代码：'+ res.status + '请刷新或联系管理员'
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      showModal(action, index=-1) {
        this.restPWD = false
        delete this.currentUser['password']
        if(index >= 0) {
          if(this.currentUser.id != this.users[index].id) {
            this.currentUser = Object.assign({}, this.users[index])
            this.currentIndex = index
          }
        } else if(this.currentUser.id) {
          this.currentUser = {}
        }
        this.userAdd = action == 'add'
        this.getGroups()
        this.getRoles()
        this.userModalShow = true
        this.selectData.selectedGroupAdmin = false
        this.imgShow = {
          id_face: false,
          id_back: false,
          license: false
        }
        for(let filed in this.imgShow) {
          if(this.currentUser[filed]) {
            this.imgShow[filed] = true
            console.log(this.currentUser[filed])
            // document.getElementById(filed).value = null
          }
        }
      },
      updataCurrentUser() {
        if(this.currentUser.role_level) {
          delete this.currentUser['role_level']
        }
        for(let filed in this.imgShow) {
          if(this.currentUser[filed] && !this.currentUser[filed].startsWith('data:image')) {
            delete this.currentUser[filed]
          }
        }
      },
      imgChange(fileID) {
        const srcId = fileID + '_src'
        console.log(srcId)
        const that = this
        const img = this.$refs[fileID].files[0]
        const imgSize = img.size && img.size / Math.pow(1000, 2)
        const reader = new FileReader()
        reader.onload = (e) => {
          that.currentUser[fileID] = reader.result
          that.imgShow[fileID] = true
          document.getElementById(srcId).src = reader.result
        }
        reader.readAsDataURL(img)
      },
      submitUser() {
        this.$refs['userForm'].validate((valid) => {
          if(valid) {
            const method = this.userAdd ? 'post' : 'put'
            const submitApi = this.userAdd ? '/accounts/users/' : '/accounts/users/' + this.currentUser.id + '/'
            const msg = this.userAdd ? '添加' : '修改'
            this.updataCurrentUser()
            this.axios({
              method: method,
              url: submitApi,
              data: this.currentUser,
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
                this.currentUser = user
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
      changeActive(is_active, ID, index) {
        const actionAPI = '/accounts/users/' + ID + '/'
        const desc = is_active ? '请确认信息是否符合要求，激活后可以正常登入' : '失效后将不可登入应用'
        const msg = is_active ? '激活此用户？' : '失效此用户？'
        this.$confirm(desc, msg, {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          let updatedUser = Object.assign({}, this.users[index])
          updatedUser.active = is_active
          delete updatedUser['role_level']
          this.axios.put(actionAPI, updatedUser).then(res => {
            if(res.status == 200) {
              this.users.splice(index, 1, res.data)
              this.$message({
                message: '设置成功',
                type: 'success'
              })
            } else {
              this.$notify.error({
                title: '操作失败',
                duration: 0,
                message: '错误代码: '+ res.status +', 请联系管理员'
              })
            }
          }).catch(error => {
            console.log(error)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          })
        })
      },
      // setGroupAdmin(index) {
      //   //设置组长，实现方式有问题，后期再考虑下怎么做
      //   this.$confirm('如果该组存在组长则会被此用户取代', '确认设置？', {
      //     confirmButtonText: '确定',
      //     cancelButtonText: '取消',
      //     type: 'warning'
      //   }).then(() => {
      //     this.currentUser = Object.assign({}, this.users[index])
      //     this.currentIndex = index
      //     const submitApi = this.userAdd ? '/accounts/users/' : '/accounts/users/' + this.currentUser.id + '/'
      //     this.getRoles()
      //     const groupAdmins = this.selectData.roles.filter(el => {
      //       return el.role_level == 2
      //     })
      //     const role_id = groupAdmins[0].id
      //     this.currentUser.role = role_id
      //     this.axios.put(submitApi, this.currentUser)
      //     .then(res => {
      //       if(res.status == 200) {
      //         this.users.splice(this.currentIndex, 1, user)
      //         this.$message({
      //           message: '设置成功',
      //           type: 'success'
      //         })
      //       } else {
      //         this.$notify.error({
      //           title: '设置组长失败',
      //           duration: 0,
      //           message: '错误代码: '+ res.status +', 请联系管理员'
      //         })
      //       }
      //     }).catch(error => {
      //       console.log(error)
      //     })
      //   }).catch(() => {
      //     console.log(22222)
      //     this.$message({
      //       type: 'info',
      //       message: '已取消组长设置'
      //     })
      //   })
      // },
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
              params: {
                is_add: this.userAdd,
                profile_id: this.currentUser.id,
                mobile: value,
              }
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

<style>
  .user-img {
    margin-left: 110px;
    height: 100px;
  }
  .expand-img {
    width: 300px;
  }
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 48%;
  }
  .change-pwd-btn {
    padding-bottom: 10px;
    margin-left: 100px;
  }
</style>
