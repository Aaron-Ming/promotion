import Vuex from 'vuex'
import Vue from 'vue'
import * as types from './types'

Vue.use(Vuex)

const getStorage = function (key) {
  return localStorage.getItem(key)
}

const setStorage = function (key, value) {
  localStorage.setItem(key, value)
}

const state = {
  user: {
    name: getStorage('username') || '',
    depatment: getStorage('user_depatment') || '',
    user_id: getStorage('user_id') || '',
    token: getStorage('token') || '',
    avatar: getStorage('user_avatar') || '',
  },
}

const getters = {}

const mutations = {
  [types.LOGIN]: (state, data) => {
    setStorage('token', data.token)
    setStorage('username', data.name)
    setStorage('user_depatment', data.depatment)
    setStorage('user_id', data.user_id)
    setStorage('user_avatar', data.avatar)
    state.user = data
  },
  [types.LOGOUT]: (state) => {
    localStorage.removeItem('token');
    state.user = {
      name: '',
      depatment: '',
      user_id: '',
      token: ''
    }
  },
}

const actions = {}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
