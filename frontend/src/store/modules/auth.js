import axios from "axios";

const state = {
  user: null,
};
const getters = {
  isAuthenticated: (state) => !!state.user,
  stateUser: (state) => state.user,
};
const actions = {
  async Register({ dispatch }, form) {
    await axios.post("register", form);
    const UserForm = new FormData();
    UserForm.append("username", form.username);
    UserForm.append("password", form.password);
    UserForm.append("provider", "staff");
    await dispatch("LogIn", UserForm);
  },
  async LogIn({ commit }, User) {
    await axios.post("login", User);
    await commit("setUser", User.get("username"));
  },
  async LogOut({ commit }) {
    const user = null;
    commit("logout", user);
  },
};
const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  logOut(state) {
    state.user = null;
  },
};
export default {
  state,
  getters,
  actions,
  mutations,
};
