import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: Cookie.get('username'),
    token: Cookie.get('token')
  },
  mutations: {
    saveToken: function (state, data) {
      state.username = data.username
      state.token = data.token
      Cookie.set('username', data.username, '20min')
      Cookie.set('token', data.token, '20min')
    },
    clearToken: function (state) {
      state.username = null
      state.token = null
      Cookie.remove('username')
      Cookie.remove('token')
    }
  }
})
