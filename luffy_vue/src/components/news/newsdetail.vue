<template>
  <div class='hello'>
    <h1>欢迎访问深科技详细页面</h1>
    <hr>
    <br>
    <h2 class='article-title'>{{title}}</h2>
    <div style='margin-top: 18px; margin-bottom: 30px; display: flex; align-items: center'>
      <time class='arc-time'>2周前</time>
      <div class='arc-time view-num view'>阅读{{view_num}}</div>
      <div class='arc-time view-num like'>点赞{{agree_num}}</div>
      <div class='arc-time view-num love'>收藏{{collect_num}}</div>
    </div>
    <div class='main-cont'>
      {{content}}
      <br>
      <br>
      <div style='margin-top: 21px; display: flex; align-items: center; margin-bottom: 68px'>
        <div>#{{source.name}}#</div>
        <div style='cursor: pointer;margin-left:auto;margin-right: 30px;' class='like-btn' @click='agree()'>
          <span class='like-num'>点赞{{agree_num}}</span>
        </div>
        <div style='cursor: pointer' class='like-btn love-bkg' @click='love()'>
          <span class='love-num'>收藏{{collect_num}}</span>
        </div>
      </div>
    </div>
    <div class='comment-wrap' style='padding-bottom: 300px'>
      <div style='display: flex'>
        <div style='width: 42px; height: 42px; border-radius: 42px; overflow: hidden'>
          <img width='100%' alt=''>
        </div>
        <div style='width: 100%; margin-left: 24px; border: 1px solid #E8E8E8'>
          <div style='height: 48px; padding: 0 25px;'>
            <input v-model.lazy="comment_count" placeholder='写下您的评论'
                   style='outline: none; border: none; width: 90%; height: 100%; overflow-y: scroll; padding: 15px 0; box-sizing: border-box'
                   type='text'>

          </div>
          <div style='position: absolute; margin-top: -48px;' @click='comments()'>
            <div style='cursor: pointer; position: absolute; margin-left: 660px; text-align: center;
            line-height: 48px; width: 100px; height: 48px; background: #7ED321; font-size: 14px;
            color: #FFFFFF;letter-spacing: 0.22px'>发表评论
            </div>
          </div>

        </div>
      </div>
      <ul style='margin-top: 20px'>
        <li v-for='item in comment_list'>
          {{item.content}}
        </li>
      </ul>
      <div class='deal-wrap' style='text-align: center'>
        <img style='margin-top: 92px' width='272' height='185'
             src='data:image/png;base64,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'
             alt=''>
        <span class='null-text'>还没有人来评论，赶紧抢占沙发吧！！</span>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: 'Index',
    data() {
      return {
        comment_count: '',
        comment_list: '',
        title: '',
        view_num: '',
        agree_num: '',
        collect_num: '',
        content: '',
        source: '',
        agree_status: false,
        collect_status: false
      }
    },
    mounted: function () {
      this.initNewsDetail()
      this.initComment()
    },
    methods: {
      initNewsDetail() {
        var nid = this.$route.params.id
        var that = this
        var url = 'http://127.0.0.1:8000/news/' + nid + '.json'
        this.$axios.request({
          url: url,
          method: 'GET',
          responseType: 'json'
        }).then(function (response) {
          that.title = response.data.title
          that.view_num = response.data.view_num
          that.agree_num = response.data.agree_num
          that.collect_num = response.data.collect_num
          that.content = response.data.content
          that.source = response.data.source
        })
      },
      initComment() {
        var nid = this.$route.params.id
        var that = this
        var user = this.$store.state
        var url = 'http://127.0.0.1:8000/comment/' + nid + '.json'
        if (user) {
          this.$axios.request({
            url: url,
            method: 'GET',
            responseType: 'json'
          }).then(function (response) {
            that.comment_list = response.data
          })
        } else {
          that.$route.push('/login')
        }

      },
      agree() {
        var nid = this.$route.params.id
        var that = this
        var user = this.$store.state.username
        console.log(user.username)
        var url = 'http://127.0.0.1:8000/news/' + nid + '.json'
        if (user) {
          if (!this.agree_status) {
            that.agree_num = that.agree_num + 1
            this.$axios.request({
              url: url,
              method: 'PUT',
              params: {
                article_id: nid,
                agree_num: that.agree_num,
                agree_info: 'agree_info'
              },
              responseType: 'json'
            }).then(function (response) {
              alert(response.data.msg)
            })
          } else {
            that.agree_num = that.agree_num - 1
            alert('取消点赞')
          }
        } else {
          alert("登陆错误")
        }

        that.agree_status = !that.agree_status
      },
      love() {
        var nid = this.$route.params.id
        var that = this

        var url = 'http://127.0.0.1:8000/news/' + nid + '.json'
        if (!this.collect_status) {
          that.collect_num = that.collect_num + 1
          this.$axios.request({
            url: url,
            method: 'PUT',
            params: {
              article_id: nid,
              collect_num: that.collect_num,
              collect_info: 'collect_info'
            },
            responseType: 'json'
          }).then(function (response) {
            alert(response.data.msg)
          })
        } else {
          that.collect_num = that.collect_num - 1
          alert('取消收藏')
        }
        that.collect_status = !that.collect_status
      },
      comments() {
        var nid = this.$route.params.id
        var that = this
        var url = 'http://127.0.0.1:8000/comment/' + nid + '.json'
        this.$axios.request({
          url: url,
          method: 'POST',
          responseType: 'json',
          params: {
            comment_count: this.comment_count
          },
        }).then(function (response) {
          that.comment_list = response.data
          that.comment_count = ''
        })
      }

    }
  }
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
  .deal-wrap {
    margin-bottom: 88px;
  }

  .null-text {
    margin-top: 50px;
    color: #c5c3c3;
  }

  .null, .null-text {
    font-size: 20px;
    letter-spacing: .32px;
    display: block;
  }

  .article-title {
    font-size: 24px;
    color: #4a4a4a;
    letter-spacing: .53px;
  }

  .view-num {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    margin-left: 24px;
    height: 38px;
    padding-left: 20px;
  }

  .arc-time {
    font-size: 13px;
    color: #9b9b9b;
    letter-spacing: .28px;
  }

  .main-cont {
    font-size: 15px;
    color: #666;
    letter-spacing: .33px;
  }

  .hello {
    width: 80%;
    margin: 0 auto;
  }

  .like-num, .love-num {
    display: block;
    margin-left: 5px;
  }

  .like-btn {
    width: 114px;
    height: 38px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    border: 1px solid #5e5e5e;
    border-radius: 54px;
  }

  .like-btn {
    font-size: 12px;
    color: #5e5e5e;
    letter-spacing: .26px;
  }
</style>
