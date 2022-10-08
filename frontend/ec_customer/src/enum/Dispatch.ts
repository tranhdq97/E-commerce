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
  addItemToCart = 'shoppingCart/addToCart',
  removeItemFromCart = 'shoppingCart/removeFromCart',
  toggleCart = 'shoppingCart/toggleCart',
  closeCart = 'shoppingCart/closeCart',
}
