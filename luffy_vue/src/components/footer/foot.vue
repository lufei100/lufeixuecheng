<template>
  <div class="footWrap">
    <div class="main">
      <ul class="foot-link">
        <li v-for="item in guid">
          <a>{{item}}</a>
        </li>
      </ul>
      <p class="base-style">Copyright &copy; Luffycity.com版权所有</p>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        guid: ['关于我们', '联系我们', '商务合作', '帮助中心', '意见反馈', '新手指南']
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .footWrap {
    width: 100%;
    height: 128px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #25292E;
  }

  .main {
    width: 435px;
  }

  .foot-link {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;

  }

  .foot-link > li {
    list-style: none;
    width: 14%;
    font-size: 14px;
    color: #FFFFFF;
    letter-spacing: 0.22px;
    cursor: pointer;
  }

  .base-style {
    font-size: 14px;
    color: #FFFFFF;
    letter-spacing: 0.22px;
    display: flex;
    justify-content: center;
  }

  .foot-link > li a {
    color: white;
  }
</style>
