export enum AuthDispatchEnum {
  login = 'auth/login',
  logout = 'auth/logout',
  register = 'auth/register',
  refreshToken = 'auth/refreshToken',
  getMe = 'auth/getMe'
}

export enum FileManagementDispatchEnum {
  getFile = 'fileManagement/getFile',
  uploadFile = 'fileManagement/uploadFile',
}

export enum SideBarDispatchEnum {
  toggleSideBar = 'sideBar/toggleSideBar',
  closeSideBar = 'sideBar/closeSideBar',
  selectRoute = 'sideBar/selectRoute',
}

export enum ProductCategoryDispatchEnum {
  addNewCategory = 'productCategory/addNewCategory',
  getCategoryList = 'productCategory/getCategoryList',
}

export enum ProductDispatchEnum {
  addNewProduct = 'product/addNewProduct',
  selectCategory = 'product/selectCategory',
  getProductList = 'product/getProductList',
}
