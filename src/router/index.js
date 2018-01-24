import Vue from 'vue'
import Router from 'vue-router'
import Base from 'pages/Base'
import Login from 'pages/Login'
import AssetList from 'pages/asset/AssetList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: '登入',
      component: Login
    },
    {
      path: '/',
      name: '资产管理',
      component: Base,
      redirect: 'assets',
      children: [
        {path: 'assets', component: AssetList, name: '所有资产'}
      ]
    }
  ]
})