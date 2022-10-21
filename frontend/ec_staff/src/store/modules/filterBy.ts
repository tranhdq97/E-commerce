import { CommonApiEnum, MasterNameEnum } from "@/enum/api/Common"
import { DefaultMasterApiEnum } from "@/enum/api/Master"
import type { CommonMaster } from "@/interfaces/Master"
import axios from "axios"

export interface FilterByState {
  filterByList: Array<CommonMaster>
}

export default {
  namespaced: true,
  state: {
    filterByList: []
  } as FilterByState,
  getters: {
    filterByList: (state: FilterByState) => state.filterByList.sort(
      (firstItem, secondItem) => firstItem.name < secondItem.name ? -1 : 1
    ),
  },
  actions: {
    async getFilterByList({ state }) {
      const resp = await axios.get(
        DefaultMasterApiEnum.list.replace(CommonApiEnum.masterName, MasterNameEnum.filterBy)
      )
      state.filterByList = resp.data
    }
  },
  mutations: {}
}
