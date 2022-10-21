import type { CommonMaster } from "./Master";

export interface SaleOverviewType {
  labels: Array<String>,
  datasets: Array<CategorySaleQuantityType | CategorySaleAmountType>, 
}

export interface CategorySaleQuantityType {
  id: number,
  name: string,
  quantity: Array<number>,
}

export interface CategorySaleAmountType {
  id: number,
  name: string,
  amount: Array<number>,
}

export interface CategorySaleAmountType {
  id: number,
  name: string,
  amount: Array<number>,
}

export interface NewCategoryType {
  id: number | null,
  name: string,
}

