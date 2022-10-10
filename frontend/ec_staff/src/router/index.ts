import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
import ForgotPassword from '@/views/ForgotPassword.vue'
import { RouterEnum } from '@/interfaces/enum/Router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: RouterEnum.home,
      name: RouterEnum.homeName,
      component: Home
    },
    {
      path: RouterEnum.about,
      name: RouterEnum.aboutName,
      component: About
    },
    {
      path: RouterEnum.login,
      name: RouterEnum.loginName,
      component: SignIn
    },
    {
      path: RouterEnum.register,
      name: RouterEnum.registerName,
      component: SignUp
    },
    {
      path: RouterEnum.forgotPassword,
      name: RouterEnum.forgotPasswordName,
      component: ForgotPassword
    },
  ]
})

export default router
