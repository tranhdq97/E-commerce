import { RouterEnum } from "@/enum/Router"
import { SideBarEnum } from "@/enum/SideBar"

export interface SideBarState {
  isOpenSideBar: boolean,
  selectedMainRoute: string,
  selectedSubRoute:string,
}

export interface RouteSelection {
  mainRoute: string,
  subRoute: string,
}

export default {
  namespaced: true,
  state: {
    isOpenSideBar: false,
    selectedMainRoute: SideBarEnum.products,
    selectedSubRoute: RouterEnum.categoriesName,
  } as SideBarState,
  getters: {
    isOpenSideBar: (state: SideBarState) => state.isOpenSideBar,
    selectedMainRoute: (state: SideBarState) => state.selectedMainRoute,
    selectedSubRoute: (state: SideBarState) => state.selectedSubRoute,
  },
  actions: {
    toggleSideBar({ state }) {
      state.isOpenSideBar = !state.isOpenSideBar
    },
    closeSideBar({ state }) {
      state.isOpenSideBar = false
    },
    selectRoute({ state }, route: RouteSelection) {
      state.selectedMainRoute = route.mainRoute
      state.selectedSubRoute = route.subRoute
    },
  },
  mutations: {
  }
}
