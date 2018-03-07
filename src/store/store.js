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
    username: getStorage('username') || '',
    user_id: getStorage('user_id') || '',
    token: getStorage('token') || '',
    is_superuser: getStorage('is_superuser') || '',
    is_staff: getStorage('is_staff') || '',
    id_name: getStorage('id_name') || '',
    profile_id: getStorage('profile_id') || '',
    group_id: getStorage('group_id') || '',
    group_name: getStorage('group_name') || '',
    role_id: getStorage('role_id') || '',
    role_name: getStorage('role_name') || '',
    role_level: getStorage('role_level') || '',
  },
}

const getters = {}

const user_fields = [
  'token', 'username', 'user_id', 'is_superuser',
  'is_staff', 'profile_id', 'id_name', 'group_id',
  'group_name', 'role_id', 'role_name', 'role_level'
]

const mutations = {
  [types.LOGIN]: (state, data) => {
    for(var field of user_fields) {
      setStorage(field, data[field])
    }
    state.user = data
  },
  [types.LOGOUT]: (state) => {
    for(var field of user_fields) {
      localStorage.removeItem(field)
    }
    state.user = {
      username: '',
      user_id: '',
      token: '',
      is_staff: '',
      is_superuser: '',
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
