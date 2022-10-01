import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import fileManagement from "./modules/fileManagement"; 

export default createStore({
  modules: {
    auth,
    fileManagement,
  },
  plugins: [createPersistedState()],
})
