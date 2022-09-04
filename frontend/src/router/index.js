import { createRouter, createWebHistory } from "vue-router";

// import store from "../store";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Login from "../views/Login.vue";
import SignUp from "../views/SignUp.vue";
import Team from "../views/Team.vue";
import Contact from "../views/Contact.vue";
import Settings from "../views/Settings.vue";
import Profile from "../views/Profile.vue";

const router = createRouter({
  base: process.env.BASE_URL,
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/login", component: Login, meta: { guest: true } },
    { path: "/signup", component: SignUp, meta: { guest: true } },
    { path: "/team", component: Team },
    { path: "/contact", component: Contact },
    { path: "/settings", component: Settings, meta: { requiresAuth: true } },
    { path: "/profile", component: Profile, meta: { requiresAuth: true } },
  ],
});

// router.beforeEach((to, from, next) => {
//   if (to.matched.some((record) => record.meta.requiresAuth)) {
//     console.log("XXX");
//     if (store.getters.isAuthenticated) {
//       next();
//       return;
//     }
//     next("/login");
//   } else {
//     next();
//   }
// });

// router.beforeEach((to, from, next) => {
//   if (to.matched.some((record) => record.meta.guest)) {
//     if (store.getters.isAuthenticated) {
//       next("/");
//       return;
//     }
//     next();
//   } else {
//     next();
//   }
// });

export default router;
