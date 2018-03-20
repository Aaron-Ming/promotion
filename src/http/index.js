import axios from 'axios'
import store from '../store/store'
import router from '../router'
import * as types from '../store/types'

// const qs = require('qs')

const instance = axios.create({
  validateStatus (status) {
    return status >= 200 && status <= 500
  },
  // transformRequest: [function(data){
  //   data = qs.stringify(data)
  //   return data
  // }],
  timeout: 5000,
})

instance.defaults.xsrfHeaderName = 'X-CSRFToken'
instance.defaults.xsrfCookieName = 'csrftoken'

instance.interceptors.request.use(
  config => {
    if(store.state.user.token) {
      config.headers.Authorization = 'Token ' + `${store.state.user.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

instance.interceptors.response.use(response => {
  const status = response.status
  switch(status) {
    case 401:
      store.commit(types.LOGOUT)
      router.replace({
        path: '/login',
        query: {redirect: router.currentRoute.fullPath}
      })
      return false
  }
  return response
},
error => {
  return Promise.reject(error.response.data)
})

export default instance