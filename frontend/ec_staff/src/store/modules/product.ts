import axios from "axios"
import type { Product, ProductQuantity } from "@/interfaces/Product"
import { ProductApiEnum } from "@/enum/api/Product"
import type { CommonMaster } from "@/interfaces/Master"
import { ProductDispatchEnum } from "@/enum/Dispatch"
import authAxios from "@/services/api"
import { CommonApiEnum } from "@/enum/api/Common"

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
        state.productList.push({ ...resp.data })
      }
      return resp
    },
    async updateQuantity ({ state }, productQuantity: ProductQuantity) {
      const resp = await authAxios.put(
        ProductApiEnum.update_quantity.replace(CommonApiEnum.id, productQuantity.id.toString()), { quantity: Number(productQuantity.quantity), }
      )
      state.productList.map((item: Product) => {
        item.id === productQuantity.id ? item.quantity = resp.data.quantity : null
      })
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
