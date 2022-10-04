import type { ItemType } from "@/interfaces/Cart";
import { CartMutationEnum } from "@/enum/Mutation";


export interface cartState {
  itemList: ItemType[],
  currency: string,
  isOpenCart: boolean,
}

export default {
  namespaced: true,
  state: {
    currency: 'VND',
    itemList: [],
    isOpenCart: false,
  } as cartState,
  getters: {
    numberOfUniqueItems: (state: cartState) => state.itemList.length,
    ItemAmount: (item: ItemType) => item.quantity * item.unitPrice,
    currency: (state: cartState) => state.currency,
    itemList: (state: cartState) => state.itemList,
    isOpenCart: (state: cartState) => state.isOpenCart,
  },
  actions: {
    addToCart({ commit }, item: ItemType) {
      commit(CartMutationEnum.addToCart.replace(CartMutationEnum.module, ''), item)
    },
    removeFromCart({ commit }, item:ItemType) {
      commit(CartMutationEnum.removeFromCart.replace(CartMutationEnum.module, ''), item)
    },
    toggleCart({ commit } ) {
      commit(CartMutationEnum.toggleCart.replace(CartMutationEnum.module, ''))
    },
  },
  mutations: {
    addToCart: (state: cartState, item: ItemType) => {
      state.itemList.push(item)
    },
    removeFromCart: (state: cartState, item: ItemType) => {
      state.itemList = state.itemList.filter(obj => obj.id !== item.id)
    },
    increaseQuantity: (state: cartState, item: ItemType) => {
      state.itemList.map(obj => obj === item ? item.quantity++ : item)
    },
    decreaseQuantity: (state: cartState, item: ItemType) => {
      state.itemList.map(obj => obj === item && item.quantity > 0 ? item.quantity-- : item)
    },
    toggleCart: (state: cartState) => {
      state.isOpenCart = !state.isOpenCart
    }
  },
}
