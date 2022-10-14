import { CommonApiEnum, MasterNameEnum } from "@/enum/api/Common"
import { ProductCategoryApiEnum } from "@/enum/api/Master"
import type { CommonMaster } from "@/interfaces/Master"
import axios from "axios"
import authAxios from "@/services/api"

export interface CategoryState {
  categoryList: Array<CommonMaster>,
}

export default {
  namespaced: true,
  state: {
    categoryList: [],
  } as CategoryState,
  getters: {
    categoryList: (state: CategoryState) => state.categoryList.sort(
      (firstItem, secondItem) => firstItem.name < secondItem.name ? -1 : 1
    ),
  },
  actions: {
    async addNewCategory ({ state }, newCategory: CommonMaster) {
      const resp = await authAxios.post(
        ProductCategoryApiEnum.create.replace(CommonApiEnum.masterName, MasterNameEnum.productCategory
      ), {
        name: newCategory.name,
      })
      if (!state.categoryList.some((item) => item.id === resp.data.id)) {
        state.categoryList.push({ id: resp.data.id, name: resp.data.name })
      }
      return resp
    },
    async getCategoryList({ state }) {
      const resp = await axios.get(
        ProductCategoryApiEnum.list.replace(CommonApiEnum.masterName, MasterNameEnum.productCategory)
      )
      state.categoryList = resp.data
    },
  },
  mutations: {
  }
}
