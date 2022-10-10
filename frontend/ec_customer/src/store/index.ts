import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import fileManagement from "./modules/fileManagement"; 
import shoppingCart from "./modules/shoppingCart";
import itemList from "./modules/itemList";

export default createStore({
  modules: {
    auth,
    fileManagement,
    shoppingCart,
    itemList,
  },
  plugins: [createPersistedState()],
})
