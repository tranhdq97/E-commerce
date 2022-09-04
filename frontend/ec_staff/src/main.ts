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

app.mount('#app')
