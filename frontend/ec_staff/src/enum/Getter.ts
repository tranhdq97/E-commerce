export enum AuthGetterEnum {
  stateUser = "auth/stateUser",
  isAuthenticated = "auth/isAuthenticated",
}

export enum SideBarGetterEnum {
  isOpenSideBar = 'sideBar/isOpenSideBar',
  selectedMainRoute = 'sideBar/selectedMainRoute',
  selectedSubRoute = 'sideBar/selectedSubRoute',
}

export enum ProductCategoryGetterEnum {
  categoryList = 'productCategory/categoryList',
  saleQuantityOverviewData = 'productCategory/saleQuantityOverviewData',
  saleAmountOverviewData = 'productCategory/saleAmountOverviewData',
}

export enum ProductGetterEnum {
  productList = 'product/productList',
}

export enum FilterByGetterEnum {
  filterByList = 'filterBy/filterByList',
}
