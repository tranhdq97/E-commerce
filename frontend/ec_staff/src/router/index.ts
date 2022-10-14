import { createRouter, createWebHistory } from 'vue-router'
import SignIn from '@/views/SignIn.vue'
import SignUp from '@/views/SignUp.vue'
import ForgotPassword from '@/views/ForgotPassword.vue'
import Products from '@/views/Products.vue'
import Categories from '@/views/Categories.vue'
import Discounts from '@/views/Discounts.vue'
import { RouterEnum } from '@/enum/Router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: RouterEnum.home,
      name: RouterEnum.homeName,
      component: Categories,
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
    {
      path: RouterEnum.products,
      name: RouterEnum.productsName,
      component: Products,
    },
    {
      path: RouterEnum.categories,
      name: RouterEnum.categoriesName,
      component: Categories,
    },
    {
      path: RouterEnum.discounts,
      name: RouterEnum.discountsName,
      component: Discounts,
    },
  ]
})

export default router
