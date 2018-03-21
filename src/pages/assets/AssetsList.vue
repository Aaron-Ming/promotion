<template>
  <el-row>
    <el-col :xs="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>推介资产管理</span>
          <el-button style="float: right; padding: 3px 0" type="text" @click="showModal('add')">添加资产</el-button>
        </div>
        <el-table
          :data="properties"
          stripe
          style="width: 100%"
        >
          <el-table-column
            type="index"
            label="ID"
          >
          </el-table-column>
          <el-table-column
            prop="title"
            label="资产标题"
          >
          </el-table-column>
          <el-table-column
            prop="debt_type"
            label="资产类型"
          >
          </el-table-column>
          <el-table-column
            prop="mortgagor"
            label="抵押人"
          >
          </el-table-column>
          <el-table-column
            prop="contacts"
            label="联系人"
          >
          </el-table-column>
          <el-table-column
            prop="pub_time"
            label="发布时间"
          >
          </el-table-column>
          <el-table-column
            label="操作"
          >
            <template slot-scope="scope">
              <el-button type="text" size="mini" @click="showModal('show', scope.$index)">查看 | 编辑</el-button>
              <el-button type="text" style="color: #f56c6c" size="mini" @click="deleteProperty(scope.$index)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <!-- add/edit modal -->
    <el-dialog
      :title="propertyAdd ? '添加资产' : '查看 | 编辑资产信息'"
      :visible.sync="propertyModal"
      custom-class="asset-modal"
    >
      <el-switch
        style="margin-bottom: 20px; text-align: right;"
        v-model="inputSwitch"
        active-color="#13ce66"
        inactive-color="#ff4949"
        active-text="查看"
        inactive-text="编辑">
      </el-switch>

      <el-form :model="currentProperty" label-width="80px" ref="categoryForm">
        <el-form-item label="资产标题">
          <el-input v-model="currentProperty.title" :disabled="inputSwitch"></el-input>
        </el-form-item>

        <el-form-item label="资产类型">
          <el-select v-model="currentProperty.debt_type" placeholder="请选择资产类型" :disabled="inputSwitch">
            <el-option
              v-for="item in selectData.debType"
              :key="item.debTypeId"
              :label="item.debTypeName"
              :value="item.debTypeName">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="资产说明">
          <el-input type="textarea" v-model="currentStr.propertyInstr" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="配套信息">
          <el-input type="textarea" v-model="currentStr.propertyParms" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="债权机构">
          <el-input v-model="currentProperty.bond_institution" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="债务人">
          <el-input v-model="currentProperty.obligor" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="保证人">
          <el-input v-model="currentProperty.guarantee" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="抵押人">
          <el-input v-model="currentProperty.mortgagor" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="资产亮点">
          <el-input  type="textarea" v-model="currentStr.propertySpot" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="联系人">
          <el-input v-model="currentProperty.contacts" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="联系人电话">
          <el-input v-model="currentProperty.c_phone" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="传真">
          <el-input v-model="currentProperty.fax" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="通讯地址">
          <el-input v-model="currentProperty.p_address" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="交易对象">
          <el-input v-model="currentProperty.transaction" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="声明">
          <el-input v-model="currentProperty.statement" :disabled="inputSwitch"></el-input>
        </el-form-item>
        <el-form-item label="资产种类">
          <el-select v-model="currentProperty.category_name" placeholder="请选择资产类型" :disabled="inputSwitch">
            <el-option
              v-for="item in selectData.categorys"
              :key="item.id"
              :label="item.category_name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="详情图片">
          <div v-for="(imgInput, index) in imgBuildParm.middle">
            <input type="file" @change="tirggerFile(index, 'middle', $event)" v-show="modalButton"/>
            <i class="el-icon-circle-close
" style="color: #F56C6C" @click="autoDelImg('middle', index)" v-show="modalButton"></i>
            <div>
              <img style="height: 150px" :src="imgInput.src" alt="" v-show="imgInput.show">
            </div>
          </div>
          <button type="submit" @click="autoAddImg('middle')" v-show="modalButton">添加</button>
        </el-form-item>

        <el-form-item label="封面图片">
          <div v-for="(imgInput, index) in imgBuildParm.small">
            <input type="file" @change="tirggerFile(index, 'small', $event)" v-show="modalButton"/>
            <div>
              <img style="height: 100px" :src="imgInput.src" alt="" v-show="imgInput.show">
            </div>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer" v-show="modalButton">
        <el-button @click="propertyModal = false">取 消</el-button>
        <el-button type="primary" @click="submitProperty">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
  import chinese from 'src/common/chinese'
  export default {
    data() {
      return {
        activeUser: this.$store.state.user,
        modalButton: false,
        inputSwitch: true,
        imgBuildParm: {},
        selectData: {
          debType: [{
            debTypeId: 1,
            debTypeName: '企业'
          }, {
            debTypeId: 2,
            debTypeName: '个人'
          }],
          categorys: []
        },
        currentStr: {},
        properties: [],
        propertyModal: false,
        propertyAdd: false,
        currentProperty: {},
        currentIndex: null,
        propertyUrl: '/assets/properties/'
      }
    },
    created() {
      this.getProperties()
      this.initImgBuilder()
    },
    watch: {
      inputSwitch: function() {
        if (this.inputSwitch === true) {
          this.modalButton = false
        } else {
          this.modalButton = true
        }
      }
    },
    methods: {
      initImgBuilder() {
        let imgInit = {'middle': [], 
                       'small': [{
                         'src': null,
                         'id': null,
                         'show': false,
                       }]
                    }
        this.imgBuildParm = imgInit
      },
      tirggerFile: function(index, imgsize, event) {
        let imgBuilder = this.currentProperty.assets_imgs
        let file = event.target.files || event.dataTransfer.files;  
        if (!file.length) return;
        let leng = file.length
        for (let i = 0; i < leng; i++) {
          let reader = new window.FileReader()
          reader.readAsDataURL(file[i])
          reader.onload = function (event) {
            imgBuilder[imgsize][index].src = event.target.result
            imgBuilder[imgsize][index].show = true
          }
        }
      },
      autoAddImg(imgSize) {
        let newImgObj = {'src': null, 'id': null, 'show': false}
        let currentPropertyImg = this.currentProperty.assets_imgs
        currentPropertyImg[imgSize].push(newImgObj)
      },
      autoDelImg(imgSize, index) {
        let currentPropertyImg = this.currentProperty.assets_imgs
        currentPropertyImg[imgSize].splice(index, 1)
      },
      getCategorys() {
        this.axios.get('/assets/categorys/')
        .then(res => {
          if (res.status == 200) {
            this.selectData.categorys = res.data
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '获取资产类别失败，请联系管理员'
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      getProperties() {
        this.axios.get(this.propertyUrl)
        .then(res => {
          if (res.status == 200) {
            this.properties = res.data
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '获取资产列表失败，请联系管理员'
            })
          }
        }).catch(error => {
          console.log(error)
        })
      },
      showModal(action, index) {
        this.getCategorys()
        if(action == 'add') {
          this.propertyAdd = true
          if(this.currentProperty.id) {
            this.currentProperty = {}
            this.currentStr = {}
            this.initImgBuilder()
          }
          this.currentProperty.assets_imgs = this.imgBuildParm
        } else if(index>=0) {
          this.propertyAdd = false
          this.currentIndex = index
          this.currentProperty = Object.assign({}, this.properties[index])
          this.imgBuildParm = this.currentProperty.assets_imgs
          this.dictToStr()
          this.modalButton = false
          this.inputSwitch = true
        }
        this.propertyModal = true
      },
      detailUrl() {
        return this.propertyUrl + this.currentProperty.id + '/'
      },
      formatDict(obj) {
        let reStr = ''
        for (let key of Object.keys(obj)) {
          reStr += key+'：'+obj[key]+'\n'
        }
        return reStr
      },
      formatStr(str) {
        if (str === undefined) {
          this.$notify.error({
            title: '出错了',
            duration: 0,
            message: '资产资产说明、配套信息、资产亮点不能为空'
          })
        }
        let keyVal = null
        let reDict = {}
        let strArr = str.split('\n')
        if (strArr[strArr.length-1] === '') {
          strArr.pop()
        }
        for (let v of strArr) {
          if (v.includes('：') == true) {
            keyVal = v.split('：')
          } else if (v.includes(':') == true) {
            keyVal = v.split(':')
          } else {
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '请检查资产资产说明、配套信息、资产亮点输入格式'
            })
            return
          }
          if (keyVal != null) {
            let realDictVal = keyVal[1]
            let tmpDictVal = parseFloat(keyVal[1])
            if (isNaN(tmpDictVal) === false) {
              reDict[keyVal[0]] = tmpDictVal
            } else {
              reDict[keyVal[0]] = realDictVal
            }
          }
        }
        return reDict
      },
      dictToStr() {
        const propertyInstr = this.currentProperty.instruction
        const propertyParms = this.currentProperty.parms
        const propertySpot = this.currentProperty.spot
        this.currentStr.propertyInstr = this.formatDict(propertyInstr)
        this.currentStr.propertyParms = this.formatDict(propertyParms)
        this.currentStr.propertySpot = this.formatDict(propertySpot)
      },
      strToDict() {
        this.currentProperty.instruction = this.formatStr(this.currentStr.propertyInstr)
        this.currentProperty.parms = this.formatStr(this.currentStr.propertyParms)
        this.currentProperty.spot = this.formatStr(this.currentStr.propertySpot)
      },
      setProCate(category, setType) {
        let newProCate = null
        if (setType == 'id') {
          newProCate = this.selectData.categorys.filter(el => {
            return el.id == category
          })
          this.currentProperty.category_name = newProCate[0].category_name
        } else if (setType == 'name') {
          newProCate = this.selectData.categorys.filter(el => {
            return el.category_name == category
          })
          this.currentProperty.category_id = newProCate[0].id
        }
      },
      submitProperty() {
        let submitUrl =  this.propertyUrl
        let method = 'post'
        this.strToDict()
        if(!this.propertyAdd) {
          submitUrl = this.detailUrl()
          method = 'put'
        }
        if (this.currentProperty.hasOwnProperty('category_name') == true) {
          this.currentProperty.category_id = this.currentProperty.category_name
          delete this.currentProperty.category_name
        }
        if (isNaN(this.currentProperty.category_id) == true) {
          this.setProCate(this.currentProperty.category_id, 'name')
        }
        this.currentProperty.author_id = parseInt(this.activeUser.user_id)
        this.axios({
          method: method,
          data: this.currentProperty,
          url: submitUrl
        }).then(res => {
          if(res.status<400) {
            if(this.propertyAdd) {
              this.properties.push(res.data)
            } else {
              this.properties.splice(this.currentIndex, 1, this.currentProperty)
            }
            this.$message({
              message: '操作成功！',
              type: 'success'
            })
            this.setProCate(this.currentProperty.category_id, 'id')
          } else {
            let errorMsg = ''
            this.$notify.error({
              title: '出错了',
              duration: 0,
              message: '添加或修改资产信息失败，请联系管理员'
            })
          }
          this.propertyModal = false
        }).catch(error => {
          console.log(error)
        })
      },
      deleteProperty(index) {
        let delConfirmType = 'success'
        let delConfirmMsg = '删除成功!'
        this.currentIndex = index
        this.currentProperty = Object.assign({}, this.properties[this.currentIndex])
        this.$confirm('是否删除此类型', '警告', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.axios({
            method: 'delete',
            url: this.detailUrl()
          }).then(res => {
            if (res.status<400) {
              delConfirmMsg = '删除' + this.currentProperty.title + '成功!'
              this.properties.splice(this.currentIndex, 1)
            } else {
              this.$notify.error({
                title: '出错了',
                duration: 0,
                message: res.data
              })
              delConfirmType = 'info'
              delConfirmMsg = '已取消删除!'
            }
            this.$message({
              type: delConfirmType,
              message: delConfirmMsg
            });
          }).catch(error => {
            console.log(error)
          });
        });
      }
    },
  }
</script>

<style>
  .asset-modal > .el-dialog__body {
    padding: 20px 20px !important;
  }
</style>
