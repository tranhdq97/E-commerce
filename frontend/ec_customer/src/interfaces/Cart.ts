export interface ItemType {
  id: number,
  name: string,
  quantity: number,
  orderQuantity: number,
  photo: string,
  unitPrice: number,
  isAdded: boolean
  numStars: number,
  numVotes: number | null,
  numOrders: null | number,
  category: {
    id: number, 
    name: string,
  }
}
