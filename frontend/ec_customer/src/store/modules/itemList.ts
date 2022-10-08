import { orderFactorIconEnum, orderFactorNameEnum, orderFactorPropertyEnum } from "@/enum/OrderMapping";
import type { ItemType } from "@/interfaces/Cart";
import type { OrderFactorType } from "@/interfaces/OrderFactorType";


const item = {
  id: 0,
  name: "Fruitylici asdasd",
  quantity: 10,
  photo: "https://imagecolorpicker.com/imagecolorpicker.png",
  unitPrice: 1500,
  isAdded: false,
  numStars: 0,
  orderQuantity: 0,
  numVotes: 1223,
  numOrders: 12000,
  category: {
    id: 1,
    name: 'X'
  }
}
const array = [...Array(15).keys()]
const itemList = array.map(idx => {
  const newItem = { ...item }
  newItem.category = { id: idx, name: 'X'}
  newItem.id = idx
  newItem.name += idx.toString()
  newItem.quantity += idx
  newItem.unitPrice += idx
  newItem.numStars += idx
  newItem.numVotes += idx
  newItem.numOrders += idx
  newItem.numStars += idx
  newItem.numVotes += idx
  newItem.numOrders += idx
  newItem.category.name += idx.toString()
  return newItem
})
itemList[0].quantity = 0

export interface cartState {
  itemList: Array<ItemType>,
  currency: string,
  orderFactor: OrderFactorType,
  isDesc: boolean,
}

export default {
  namespaced: true,
  state: {
    currency: 'VND',
    itemList: itemList,
    orderFactor: {
      name: orderFactorNameEnum.all,
      icon: orderFactorIconEnum.all,
      isAllMode: false,
      property: null,
    },
    isDesc: false,
  } as cartState,
  getters: {
    addedItemList : (state: cartState) => state.itemList.filter(item => item.isAdded),
    currency: (state: cartState) => state.currency,
    itemList: (state: cartState) => { 
      const property = state.orderFactor.property
      if (property) {
        if (state.isDesc) {
          return state.itemList.sort((firstItem, secondItem) => {
            if (property === orderFactorPropertyEnum.category) {
              return firstItem[property].id < secondItem[property].id ? -1 : 1
            } else {
              return firstItem[property] < secondItem[property] ? -1 : 1
            }
          })
        } else {
          return state.itemList.sort((firstItem, secondItem) => {
            if (property === orderFactorPropertyEnum.category) {
              return firstItem[property].id > secondItem[property].id ? -1 : 1
            } else {
              return firstItem[property] > secondItem[property] ? -1 : 1
            }
          })
        }
      } else {
        return { ...state.itemList }
      }
    },
    isMaximun: (item: ItemType) => item.orderQuantity >= item.quantity,
    isMinimum: (item: ItemType) => item.orderQuantity <= 0,
    orderFactor: (state: cartState) => state.orderFactor,
    isDesc: (state: cartState) => state.isDesc,
  },
  actions: {
    addToCart: ({ state }, item: ItemType) => {
      const stateItem = state.itemList.filter(obj => obj.id === item.id)[0]
      stateItem.orderQuantity += 1
      stateItem.isAdded = true
      state.itemList.push(state.itemList.splice(state.itemList.indexOf(stateItem), 1)[0])
    },
    removeFromCart: ({ state }, item: ItemType) => {
      const stateItem = state.itemList.filter(obj => obj.id === item.id)[0]
      stateItem.orderQuantity = 0
      stateItem.isAdded = false
    },
    increaseQuantity: ({ state }, item: ItemType) => {
      const stateItem = state.itemList.filter(obj => obj.id === item.id)[0]
      stateItem.orderQuantity < stateItem.quantity ? stateItem.orderQuantity++ : null
    },
    decreaseQuantity: ({ state }, item: ItemType) => {
      const stateItem = state.itemList.filter(obj => obj.id === item.id)[0]
      stateItem.orderQuantity > 1 ? stateItem.orderQuantity-- : null
    },
    resetQuantity: ({ state }, item: ItemType) => {
      const stateItem = state.itemList.filter(obj => obj.id === item.id)[0]
      stateItem.orderQuantity = 1
    },
    orderItemList: ({ state }, factor: OrderFactorType) => {
      if (factor === state.orderFactor) {
        state.isDesc = !state.isDesc
      } else {
        state.orderFactor = factor
      }
    },
  },
  mutations: {
  },
}
