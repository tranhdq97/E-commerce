import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import fileManagement from "./modules/fileManagement"; 
import shoppingCart from "./modules/shoppingCart";

export default createStore({
  modules: {
    auth,
    fileManagement,
    shoppingCart,
  },
  plugins: [createPersistedState()],
})
