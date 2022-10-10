export enum AuthDispatchEnum {
  login = 'auth/login',
  logout = 'auth/logout',
  register = 'auth/register',
  refreshToken = 'auth/refreshToken',
  getMe = 'auth/getMe'
}

export enum FileManagementDispatchEnum {
  getFile = 'fileManagement/getFile'
}

export enum CartDispatchEnum {
  removeItemFromCart = 'shoppingCart/removeFromCart',
  toggleCart = 'shoppingCart/toggleCart',
  closeCart = 'shoppingCart/closeCart',
}

export enum ItemListDispatchEnum {
  addToCart = 'itemList/addToCart',
  removeFromCart = 'itemList/removeFromCart',
  increaseQuantity = 'itemList/increaseQuantity',
  decreaseQuantity = 'itemList/decreaseQuantity',
  resetQuantity = 'itemList/resetQuantity',
  orderItemList = 'itemList/orderItemList',
}
