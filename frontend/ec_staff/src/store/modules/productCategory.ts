import { CommonApiEnum, MasterNameEnum, ProductCategoryEnum } from "@/enum/api/Common"
import { DefaultMasterApiEnum, ProductCategoryApiEnum } from "@/enum/api/Master"
import type { CommonMaster } from "@/interfaces/Master"
import axios from "axios"
import authAxios from "@/services/api"
import type { CategorySaleAmountType, CategorySaleQuantityType, NewCategoryType, SaleOverviewType } from "@/interfaces/ProductCategory"

export interface CategoryState {
  categoryList: Array<CommonMaster>,
  saleQuantityOverviewData: SaleOverviewType,
  saleAmountOverviewData: SaleOverviewType,
}

export default {
  namespaced: true,
  state: {
    categoryList: [],
    saleQuantityOverviewData: {
      labels: [],
      datasets: [],
    },
    saleAmountOverviewData: {
      labels: [],
      datasets: [],
    },
  } as CategoryState,
  getters: {
    categoryList: (state: CategoryState) => state.categoryList.sort(
      (firstItem, secondItem) => firstItem.name < secondItem.name ? -1 : 1
    ),
    saleQuantityOverviewData: (state: CategoryState) => state.saleQuantityOverviewData,
    saleAmountOverviewData: (state: CategoryState) => state.saleAmountOverviewData,
  },
  actions: {
    async addNewCategory ({ state }, newCategory: NewCategoryType) {
      const resp = await authAxios.post(
        DefaultMasterApiEnum.create.replace(CommonApiEnum.masterName, MasterNameEnum.productCategory
      ), {
        name: newCategory.name,
      })
      if (!state.categoryList.some((item) => item.id === resp.data.id)) {
        state.categoryList.push({
          id: resp.data.id,
          name: resp.data.name,
          color: "#" + Math.floor(Math.random()*16777215).toString(16),
          numChildren: 0,
        })
      }
      return resp
    },
    async getCategoryList({ state }) {
      const resp = await axios.get(
        DefaultMasterApiEnum.list.replace(CommonApiEnum.masterName, MasterNameEnum.productCategory)
      )
      state.categoryList = [ ...resp.data ]
      state.categoryList.map((item: CommonMaster) => {
        item.color = "#" + Math.floor(Math.random()*16777215).toString(16)
        item.numChildren = Math.floor(Math.random() * 100)
        // const param = state.category ? '?category_id=' + item.id : ''
        // const resp = axios.get(ProductApiEnum.list + param)
        // resp.data ? item.numChildren = resp.data.count : 0
      })
    },
    async updateSaleQuantityOverview({ state }, option: CommonMaster) {
      const resp = await authAxios.get(
        ProductCategoryApiEnum.getSaleQuantityOverview + '?' + ProductCategoryEnum.filterById + '=' + option.id.toString()
      )
      state.saleQuantityOverviewData = {
        labels: resp.data.timestamps,
        datasets: [],
      }
  
      resp.data.datasets.map((categoryObject: CategorySaleQuantityType) => {
        const filteredList = state.categoryList.filter((item) => item.id === categoryObject.id ? true : false)
        const color = filteredList.length > 0 ? filteredList[0].color : "#ffffff"
        state.saleQuantityOverviewData.datasets.push({
          label: categoryObject.name.toUpperCase(),
          backgroundColor: color,
          borderColor: color,
          data: categoryObject.quantity,
          tension: 0.3,
        })
      })
    },
    async updateSaleAmountOverview({ state }, option: CommonMaster) {
      const resp = await authAxios.get(
        ProductCategoryApiEnum.getSaleAmountOverview + '?' + ProductCategoryEnum.filterById + '=' + option.id.toString()
      )
      state.saleAmountOverviewData = {
        labels: resp.data.timestamps,
        datasets: [],
      }
      resp.data.datasets.map((categoryObject: CategorySaleAmountType) => {
        const filteredList = state.categoryList.filter((item) => item.id === categoryObject.id ? true : false)
        const color = filteredList.length > 0 ? filteredList[0].color : "#ffffff"
        state.saleAmountOverviewData.datasets.push({
          label: categoryObject.name.toUpperCase(),
          backgroundColor: color,
          borderColor: color,
          data: categoryObject.amount,
          tension: 0.3
        })
      })
    }
  },
  mutations: {}
}
