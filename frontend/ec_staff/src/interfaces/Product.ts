export interface Product {
  id: number | null,
  name: string,
  purchasePrice: number,
  price: number,
  desc: string,
  categoryId: number,
  photoId: null | number,
  quantity: null | number,
}

export interface ProductQuantity {
  id: number,
  quantity: number,
}
