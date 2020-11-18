import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  { 
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  { 
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  { 
    path: '/articles',
    name: 'ArticleListView',
    component: ArticleListView
  },
  { 
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
