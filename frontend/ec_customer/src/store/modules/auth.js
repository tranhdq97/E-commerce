import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  namespaced: true,
  state: {
    user: null,
  },
  getters: {
    isAuthenticated: (state) => !!state.user,
    stateUser: (state) => state.user,
  },
  actions: {
    // eslint-disable-next-line
    async register({}, User) {
      console.log("In register: ", User);
      const resp = await axios.post("customer/customer/create", {
        email: User.email,
        password: User.password,
      });
      return resp;
    },
    async login({ dispatch }, User) {
      const resp = await axios.post("customer/auth/token", {
        email: User.email,
        password: User.password,
        provider: User.provider,
      });
      VueCookies.set("access_token", resp.data.access);
      VueCookies.set("refresh_token", resp.data.refresh);
      await dispatch("getMe");
    },
    async logout({ commit }) {
      commit("removeUser");
      VueCookies.remove("access_token");
      VueCookies.remove("refresh_token");
    },
    async getMe({ commit, dispatch }) {
      const resp = await axios.get("customer/auth/get-me", {
        headers: {
          'Authorization': "Bearer " + VueCookies.get('access_token'),
        }
      });
      if (resp.data.info && resp.data.info.photo_id) {
        const avatar = await dispatch("getAvatar", resp.data.info.photo_id);
        resp.data.info.avatar = avatar;
      }
      commit("setUser", resp.data)
    },
    // eslint-disable-next-line
    async getAvatar({}, avatarId) {
      const resp = await axios.get("storage/file-management/" + avatarId + "/detail", {
        headers: {
          'Authorization': "Bearer " + VueCookies.get('access_token'),
        }
      });
      return resp.data.file;
    },
    async updateUser({commit}, userInfo) {
      commit('setUser', userInfo);
    }
  },
  mutations: {
    setUser(state, data) {
      state.user = data;
    },
    removeUser(state) {
      state.user = null;
    },
  },
};
