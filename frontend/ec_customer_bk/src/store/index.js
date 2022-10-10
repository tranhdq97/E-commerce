import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";

export default createStore({
  // state: {
  //   user: null,
  // },
  // getters: {
  //   isAuthenticated: (state) => state.user != null,
  //   stateUser: (state) => state.user,
  // },
  // mutations: {
  //   setUser(state, email) {
  //     state.user = email;
  //   },
  //   removeUser(state) {
  //     state.user = null;
  //   },
  // },
  // actions: {
  //   async register({ dispatch }, form) {
  //     await axios.post("register", form);
  //     let UserForm = new FormData();
  //     UserForm.append("username", form.username);
  //     UserForm.append("password", form.password);
  //     await dispatch("LogIn", UserForm);
  //   },
  //   // eslint-disable-next-line no-unused-vars
  //   async logIn({ commit }, user) {
  //     try {
  //       const response = await axios.post("auth/token", {
  //         email: user.email,
  //         password: user.password,
  //       });
  //       console.log(response);
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   },
  //   async logOut({ commit }) {
  //     commit("removeUser");
  //   },
  // },
  modules: {
    auth,
  },
  plugins: [createPersistedState()],
});
