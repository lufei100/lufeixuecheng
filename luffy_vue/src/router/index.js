import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index/index'
import News from '@/components/news/news'
import NewsDetail from '@/components/news/newsdetail'
import Login from '@/components/login/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/newsdetail/:id',
      name: 'NewsDetail',
      component: NewsDetail
    }
  ],
  mode: 'history'
})
