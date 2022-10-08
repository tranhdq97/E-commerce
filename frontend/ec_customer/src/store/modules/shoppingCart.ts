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
    toggleCart({ commit, state } ) {
      console.log('---> ', state.isOpenCart)
      commit(CartMutationEnum.toggleCart.replace(CartMutationEnum.module, ''))
    },
    closeCart({ state }) {
      state.isOpenCart = false
    }
  },
  mutations: {
    addToCart: (state: cartState, item: ItemType) => {
      item.orderQuantity += 1
      state.itemList.push(item)
    },
    removeFromCart: (state: cartState, item: ItemType) => {
      item.orderQuantity = 0
      state.itemList = state.itemList.filter(obj => obj.id !== item.id)
    },
    increaseQuantity: (state: cartState, item: ItemType) => {
      state.itemList.map(obj => obj === item && obj.orderQuantity < obj.quantity ? obj.orderQuantity += 1 : obj)
    },
    decreaseQuantity: (state: cartState, item: ItemType) => {
      state.itemList.map(obj => obj === item && obj.orderQuantity > 1 ? obj.orderQuantity -= 1 : obj)
    },
    toggleCart: (state: cartState) => {
      state.isOpenCart = !state.isOpenCart
    }
  },
}
