// import './common/rem'
import Vue from 'vue'
import App from './app.vue'
import axios from './http'
import router from './router'
import store from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'font-awesome/css/font-awesome.min.css'
import 'datatables.net-bs/css/dataTables.bootstrap.css'
import 'bootstrap/dist/css/bootstrap.css'
import DataTable from 'datatables.net-bs/js/dataTables.bootstrap.js'

Vue.use(ElementUI)

Vue.prototype.axios = axios

new Vue({
    el: '#dashboard',
    router,
    store,
    template: '<App/>',
    components: {
        App
    }
})
