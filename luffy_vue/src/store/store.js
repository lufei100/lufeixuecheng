import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
  // 组件中通过 this.$store.state.username 调用
  state: {
    username: Cookie.get('username'),
    token: Cookie.get('token'),
    apiList: {
      auth: 'http://127.0.0.1:8000/api/v1/auth/',
      courses: 'http://127.0.0.1:8000/api/v1/courses/',
      pricePolicy: 'http://127.0.0.1:8000/api/v1/price_policy/',
      shopCar: 'http://127.0.0.1:8000/api/v1/shop_car/',
      micros: 'http://127.0.0.1:8000/api/v1/micros/',
    }
  },
  getters: {
    // 组件中通过 this.$store.getters.uuuu 调用
    isLogin: function (state) {
      return state.token;
    }

  },
  mutations: {
    // 组件中通过 this.$store.commit(参数)  调用
    saveToken: function (state, userToken) {
      state.username = userToken.name;
      state.token = userToken.token;
      Cookie.set("username", userToken.name, "20min")
      Cookie.set("token", userToken.token, "20min")

    },
    clearToken: function (state) {
      state.username = null
      state.token = null
      Cookie.remove('username')
      Cookie.remove('token')

    }
  },
  actions: {
    actionFunc1(context, params) {
      // context.commit('isLogin')

    },
    actionFunc2({commit}, params) {
      // context.commit('isLogin')
    }
  },
  modules: {
    a: {
      state: {},
      getters: {}
    },
    b: {
      state: {},
      getters: {}
    }
  }
})
