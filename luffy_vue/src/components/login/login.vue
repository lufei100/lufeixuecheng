<template>
  <div class="hello">
    <h1>欢迎登录</h1>
    <input type="text" v-model="username" placeholder="请输入用户名">
    <br>
    <br>
    <input type="text" v-model="password" placeholder="请输入密码">
    <br>
    {{msg}}
    <br>
    <button><a @click="doLogin">登录</a></button>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      msg: ''
    }
  },
  methods: {
    doLogin () {
      var that = this
      this.$axios.request({
        url: 'http://127.0.0.1:8000/login/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password
        },
        responseType: 'json'
      }).then(function (response) {
        if (response.data.code=='1000') {
          console.log(response.data.code)
          that.$store.commit('saveToken', response.data)
          that.$router.push('/index')
        } else{
          that.msg = response.data.msg
          that.username = ''
          that.password = ''
        }

      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
