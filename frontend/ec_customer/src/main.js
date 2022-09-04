import { createApp } from "vue";
import axios from "axios";
import VueCookies from "vue-cookies";

import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/main.css";

axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";
// axios.interceptors.response.use(undefined, function (error) {
//   if (error) {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
//       originalRequest._retry = true;
//       store.dispatch("logOut");
//       return router.push("/login");
//     }
//   }
// });

createApp(App).use(store).use(router).use(VueCookies).mount("#app");
