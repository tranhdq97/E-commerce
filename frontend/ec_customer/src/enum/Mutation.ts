export enum AuthMutationEnum {
  setUser = "setUser",
  removeUser = "removeUser",
}

export enum CartMutationEnum {
  module = 'shoppingCart/',
  addToCart = 'shoppingCart/addToCart',
  removeFromCart = 'shoppingCart/removeFromCart',
  increaseItemQuantity = 'shoppingCart/increaseQuantity',
  decreaseItemQuantity = 'shoppingCart/decreaseQuantity',
  toggleCart = 'shoppingCart/toggleCart',
}
