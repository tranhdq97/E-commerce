import { createApp } from 'vue'
import VueCookies from "vue-cookies"
import App from './App.vue'
import router from './router'
import store from './store'

import './assets/styles/main.scss'
import authAxios from './services/api'
import { TokenEnum } from './enum/Token'
import { RouterEnum } from './enum/Router'
import { AuthDispatchEnum } from './enum/Dispatch'
import auth from './store/modules/auth'

authAxios.interceptors.request.use(
  function(config) {
    config.headers.Authorization = "Bearer " + VueCookies.get(TokenEnum.access)
    return config
  },
  function(error) {
    return Promise.reject(error)
  }
)
authAxios.interceptors.response.use(
  function(config) {
    return config
  },
  async function(error) {
    if (error.response.status === 401) {
      if (VueCookies.get(TokenEnum.refresh)) {
        await store.dispatch(AuthDispatchEnum.refreshToken)
        return authAxios(error.config)
      } else {
        alert("You have to login first")
        router.push(RouterEnum.login)
      }
      return
    }
    return Promise.reject(error)
  }
)

const app = createApp(App)
app.use(router)
app.use(store)
app.use(VueCookies)
app.directive('click-outside', {
  mounted(el, binding, vnode) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event, el);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  }
});
app.mount('#app')
