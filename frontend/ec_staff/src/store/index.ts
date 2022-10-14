import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import fileManagement from "./modules/fileManagement";
import sideBar from "./modules/sideBar";
import productCategory from "./modules/productCategory";
import product from "./modules/product";

export default createStore({
  modules: {
    auth,
    fileManagement,
    sideBar,
    productCategory,
    product,
  },
  plugins: [createPersistedState()],
})
