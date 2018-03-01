<template>
    <div style="min-height: 500px">
            <div v-for="(item,key) in data" style="margin-top: 20px;">
      <router-link :to="{'path':'/micro/detail/'+item.id }">
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
  name: 'HelloWorld',
  data () {
    return {
        data:null,

    }
  },
  mounted(){
    this.initMicro()
  },
  methods :{
      fun () {
        alert(123)
    },
    initMicro(){
        var that = this;
        var url = this.$store.state.apiList.micros;
        this.$axios.request({
          url: url,
          method: "GET",
          responseType: 'json'
        }).then(function (response) {
          that.data = response.data.data


        })
    }
  }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
