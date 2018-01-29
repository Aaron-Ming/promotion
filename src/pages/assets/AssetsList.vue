<template>
    <el-row>
        <el-col :xs="12">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>所有资产</span>
                    <el-button style="float: right; padding: 3px 0" type="text">添加资产</el-button>
                </div>
                <el-table :data="groups" stripe style="width: 100%">
                    <el-table-column prop="id" label="ID">
                    </el-table-column>
                    <el-table-column prop="title" label="资产标题">
                    </el-table-column>
                    <el-table-column prop="debt_type" label="债务类型">
                    </el-table-column>
                    <el-table-column prop="instruction" label="资产说明">
                    </el-table-column>
                    <el-table-column prop="parms" label="配套信息">
                    </el-table-column>
                    <el-table-column prop="bond_institution" label="债券机构">
                    </el-table-column>
                    <el-table-column prop="obligor" label="债务人">
                    </el-table-column>
                    <el-table-column prop="guarantee" label="保证人">
                    </el-table-column>
                    <el-table-column prop="mortgagor" label="抵押人">
                    </el-table-column>
                    <el-table-column prop="spot" label="资产亮点">
                    </el-table-column>
                    <el-table-column prop="contacts" label="联系人">
                    </el-table-column>
                    <el-table-column prop="c_phone" label="联系人电话">
                    </el-table-column>
                    <el-table-column prop="fax" label="传真">
                    </el-table-column>
                    <el-table-column prop="p_address" label="通讯地址">
                    </el-table-column>
                    <el-table-column prop="transaction" label="交易对象">
                    </el-table-column>
                    <el-table-column prop="statement" label="声明">
                    </el-table-column>
                    <el-table-column prop="pub_time" label="发布时间">
                    </el-table-column>
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button type="text" size="small">查看</el-button>
                            <el-button type="text" size="small">编辑</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-card>
        </el-col>
        <!-- add/edit modal -->
        <!-- <el-dialog :title="groupAdd ? 添加区域 : 编辑区域" :visible.sync="groupModal">
            <el-form :model="currentGroup" label-width="80px" ref="groupForm">
                <el-form-item label="区域名称">
                    <el-input v-model="currentGroup.group_name"></el-input>
                </el-form-item>
                <el-form-item label="区域别名">
                    <el-input v-model="currentGroup.alias_name" placeholder="英文／拼音 不能重复"></el-input>
                </el-form-item>
                <el-form-item label="管理员">
                    <el-input v-model="currentGroup.group_admin"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="groupModal = false">取 消</el-button>
                <el-button type="primary" @click="groupModal = false">确 定</el-button>
            </div>
        </el-dialog> -->
    </el-row>
</template>
<script>
export default {
    data() {
        return {}
    }
}
</script>