<template>
  <div class="hello">
    <h1>很深很深的科技</h1>
    <div class="information-box">
      <div class="information-box-head">
        <div style="display: flex">
          <div style="cursor: pointer;" class="cptn-wrap">
            <img class="cptn-img lazy"  width="556" height="314" src="https://hcdn1.luffycity.com/static/frontend/article/2018/2/head_img/1519728419.8091352.jpeg" alt="">
            <div class="cptn"></div>
          </div>
          <div>
            <div style="cursor: pointer;" class="cptn-wrap right-wrap">
              <img class="cptn-img lazy" width="272" height="154" src="https://hcdn1.luffycity.com/static/frontend/article/2017/11/head_img/1512038674.9731805.jpeg" alt="">
              <div class="cptn top-article-tit"></div>
            </div>
            <div style="cursor: pointer;" class="cptn-wrap right-wrap">
              <img class="cptn-img lazy" width="272" height="154" src="https://hcdn1.luffycity.com/static/frontend/article/2017/12/head_img/1512128547.2978053.jpeg" alt="">
              <div class="cptn top-article-tit"></div>
            </div>
          </div>
        </div>
        <div class="item_Wrap">
          <ul style="display: flex;margin:25px 0"></ul>
          <ul>
      <li v-for="item in newsList" class="news-item-wrap">
        <div style="width: 282px; height: 159px; overflow: hidden">
          <img v-bind:src="item.head_img" alt="" width="282" height="159">
        </div>
        <div class="new-list">
          <router-link :to="{'path':'/newsdetail/'+item.id}">
            <h3 class="news-tit">{{item.title}}</h3>
            <div style="margin-bottom: 20px; display: flex; align-items: center">
              <time>3小时前</time>
              <span class="arc-time im-left view-num-bkg">阅读：{{item.view_num}}</span>
              <span class="arc-time im-left evaluation-num-bkg">评论：{{item.comment_num}}</span>
              <span class="arc-time im-left love-num-bkg">收藏：{{item.collect_num}}</span>
            </div>
            <p class="news-dec">{{item.brief}}</p>
            <p style="text-align: left">
              <span class="name-time-tag">
                #{{item.source.name}}#
              </span>
            </p>
          </router-link>
        </div>
      </li>
    </ul>
        </div>
      </div>
      <div class="slideWrap" style="width: 340px;background-color: aquamarine">
        <h1>广告</h1>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'News',
    data() {
      return {
        newsList: []
      }
    },
    mounted: function () {
      this.initArticle()
    },
    methods: {
      initArticle: function () {
        var that = this
        this.$axios.request({
          url: 'http://127.0.0.1:8000/news/',
          method: 'GET'
        }).then(function (response) {
          console.log(response.data)
          that.newsList = response.data
        })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul li{
  list-style: none;
}
  .news-item-wrap{
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    width: 100%;
    height: 190px;
    padding-bottom: 30px;
    border-bottom: 1px solid #ededed;
    margin-bottom: 30px;
    cursor: pointer;
  }
  .information-box {
    width: 1203px;
    margin: 0 auto;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    padding-top: 40px;
}
  .new-list{
    margin-left: 30px;
  }
  .news-tit{
    font-size: 20px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    color: #414a60;
    width: 485px;
    letter-spacing: .32px;
    margin: 0 0 16px;
  }
  .view-num-bkg {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARCAMAAAD5TTx4AAAAZlBMV…qmpInoVGTzVLQwFtRv3x/DklvCNIXFpXrJTxEuBD83/QGksAmsvSW/fAAAAABJRU5ErkJggg==) no-repeat 0 5px;
    background-size: 14px 8px;
}
  .im-left {
    display: inline-block;
    margin-left: 30px;
    padding-left: 20px;
}
  .arc-time {
    font-size: 13px;
    color: #9b9b9b;
    letter-spacing: .28px;
}
  .evaluation-num-bkg {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAMAAACTisy7AAAAS1BMV…ii3rIJ8xkPj9LNc8vWfGZm+IyqbcDOoDgBPeWNbsd+4a8vaswFwq0u8egAAAAASUVORK5CYII=) no-repeat 0 4px;
    background-size: 14px 13px;
}
  .love-num-bkg {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAWCAMAAAACYceEAAAAWlBMV…qGD2v4d7nvLXwBk3LG1S5corDFVa4nV9xJnYy45yx+/AMGsQq9IJEmjwAAAABJRU5ErkJggg==) no-repeat 0 5px;
    background-size: 10px 9px;
}
  .news-dec {
    font-size: 14px;
    color: #666;
    letter-spacing: .22px;
    height: 50px;
    margin-bottom: 10px;
    width: 485px;
}
  .name-time-tag {
    font-size: 14px;
    color: #999;
    display: inline-block;
    letter-spacing: .22px;
    margin-right: 20px;
}
  .information-box-head {
    width: 834px;
    margin-right: 30px;
    overflow: hidden;
}
  .cptn-wrap {
    width: 556px;
    margin-right: 6px;
    position: relative;
    overflow: hidden;
}
  .cptn-img {
    left: 0;
    bottom: 0;
    position: relative;
}
  .cptn {
    background: rgba(0,0,0,.3);
    width: 100%;
    min-height: 55px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    font-size: 18px;
    color: #fff;
    letter-spacing: .4px;
    line-height: 26px;
    padding-left: 30px;
    bottom: -34%;
    position: absolute;
    left: 0;
    overflow: hidden;
    transition: all .3s;
}
  .top-article-tit {
    font-size: 14px;
    color: #fff;
    letter-spacing: .31px;
    padding-left: 14px;
    min-height: 30px;
}
  img {
    vertical-align: middle;
    border-right:0;
}

</style>
