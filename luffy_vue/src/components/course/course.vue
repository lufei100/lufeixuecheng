<template>
  <div style="width: 980px;margin: 0 auto;">
    <div v-for="(item,key) in courseList" style="margin-top: 20px;">
      <router-link :to="{'path':'/course/detail/'+item.id }">
        <div>{{item.name}}</div>
        <div>{{item.brief}}</div>
        <span>难度：{{item.level}}</span>
        <span></span>
      </router-link>
    </div>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        msg: '课程页面',
        courseList: []
      }
    },
    mounted: function () {
      this.initCourses()
    },
    methods: {
      initCourses: function () {
        let that = this
        this.$axios.request({
          url: this.$store.state.apiList.courses,
          method: 'GET',
        }).then(function (response) {
          if (response.data.status) {
            that.courseList = response.data.data
          }
        }).catch(function (response) {
          console.log(response)
        })

      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
