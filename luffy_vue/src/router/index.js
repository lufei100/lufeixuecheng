import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index/index'
import Course from '@/components/course/course'
import CourseDetailPage1 from '@/components/course/detail/page1'

import Micro from '@/components/micro/micro'
import MicroDetailPage1 from '@/components/micro/detail/page1'

import News from '@/components/news/news'
import NotFound from '@/components/404'

import Login from '@/components/account/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Index
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/course',
      name: 'course',
      component: Course,
    },
    {
      path: '/course/detail/:id/',
      name: 'course-detail',
      component: CourseDetailPage1
    },
    {
      path: '/micro',
      name: 'micro',
      component: Micro
    },
        {
      path: '/micro/detail/:id/',
      name: 'micro-detail',
      component: MicroDetailPage1
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '*',
      component: NotFound
    }
  ],
  mode: 'history'
})
