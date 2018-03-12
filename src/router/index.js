import Vue from 'vue'
import Router from 'vue-router'
import Base from 'pages/Base'
import Login from 'pages/Login'
import AssetList from 'pages/asset/AssetList'
import Home from 'pages/Home'
import UserList from 'pages/accounts/UserList'
import GroupList from 'pages/accounts/GroupList'
import RoleList from 'pages/accounts/RoleList'
import AssetsList from 'pages/assets/AssetsList'
import CategoryList from 'pages/assets/CategoryList'
import store from '../store/store'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      name: '登入',
      component: Login
    },
    {
      path: '/',
      name: 'Dashboard',
      component: Base,
      redirect: 'home',
      children: [
        {path: 'home', component: Home, name: '首页'},
        {
          path: 'group_list',
          component: GroupList,
          name: '区域组管理',
          meta: {
            requireAuth: true
          }
        },
      ]
    },
    {
      path: '/accounts',
      name: '会员管理',
      component: Base,
      redirect: '/accounts/user_list',
      children: [
        {
          path: 'user_list',
          component: UserList,
          name: '会员信息',
          meta: {
            requireAuth: true
          }
        },
        {
          path: 'role_list',
          component: RoleList,
          name: '角色管理',
          meta: {
            requireAuth: true
          }
        }
      ]
    },
    {
      path: '/assets',
      name: '推介资产管理',
      component: Base,
      redirect: '/assets/assets_list',
      children: [
        {
          path: 'assets_list',
          component: AssetsList,
          name: '推介资产信息',
          meta: {
            requireAuth: true
          }
        },
        {
          path: 'category_list',
          component: CategoryList,
          name: '资产种类管理',
          meta: {
            requireAuth: true
          }
        }
      ]
    },
  ]
})

router.beforeEach((to, from, next) => {
  if(to.meta.requireAuth) {
    if(store.state.user.token) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
})

export default router
