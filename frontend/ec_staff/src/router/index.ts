import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: SignIn
    },
    {
      path: '/register',
      name: 'register',
      component: SignUp
    },
  ]
})

export default router
