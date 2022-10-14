import axios from "axios"
import type { Product } from "@/interfaces/Product"
import { ProductApiEnum } from "@/enum/api/Product"
import type { CommonMaster } from "@/interfaces/Master"
import { ProductDispatchEnum } from "@/enum/Dispatch"
import authAxios from "@/services/api"

export interface ProductState {
  productList: Array<Product>,
  category: CommonMaster | null,
}

export default {
  namespaced: true,
  state: {
    productList: [],
    category: null,
  } as ProductState,
  getters: {
    productList: (state: ProductState) => state.productList.sort(
      (firstItem, secondItem) => firstItem.name < secondItem.name ? -1 : 1
    ),
  },
  actions: {
    async addNewProduct ({ state }, newProduct: Product) {
      const resp = await authAxios.post(ProductApiEnum.create, newProduct)
      if (!state.productList.some((item) => item.id === resp.data.id)) {
        state.productList.push({ id: resp.data.id, name: resp.data.name })
      }
      return resp
    },
    async selectCategory({ state, dispatch }, category: CommonMaster) {
      state.category = category
      await dispatch(ProductDispatchEnum.getProductList, {}, { root: true })
    },
    async getProductList({ state }) {
      const param = state.category ? '?category_id=' + state.category.id : ''
      const resp = await axios.get(ProductApiEnum.list + param)
      state.productList = resp.data.results
    },
  },
  mutations: {
  }
}
