import { createApp } from 'vue'
import VueCookies from "vue-cookies";
import App from './App.vue'
import router from './router'
import store from './store'

import './assets/styles/main.scss'

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
