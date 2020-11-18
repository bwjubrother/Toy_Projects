import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import VideoView from '../views/VideoView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/MovieView',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/VideoView',
    name: 'VideoView',
    component: VideoView
  },
  {
    path: '/',
    name: 'Home',
    component: MovieView
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
