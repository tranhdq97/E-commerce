import type { ItemType } from "@/interfaces/Cart";
import { CartMutationEnum } from "@/enum/Mutation";
import { ItemListDispatchEnum } from "@/enum/Dispatch";

export interface cartState {
  currency: string,
  isOpenCart: boolean,
}

export default {
  namespaced: true,
  state: {
    isOpenCart: false,
  } as cartState,
  getters: {
    isOpenCart: (state: cartState) => state.isOpenCart,
  },
  actions: {
    removeFromCart({ dispatch }, item: ItemType) {
      dispatch(ItemListDispatchEnum.removeFromCart, item, { root: true })
    },
    toggleCart({ commit } ) {
      commit(CartMutationEnum.toggleCart.replace(CartMutationEnum.module, ''))
    },
    closeCart({ state }) {
      state.isOpenCart = false
    }
  },
  mutations: {
    toggleCart: (state: cartState) => {
      state.isOpenCart = !state.isOpenCart
    }
  },
}
