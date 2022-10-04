export interface ItemType {
  array_index: null | number,
  id: number,
  name: string,
  quantity: number,
  photo: null | string,
  unitPrice: number,
  isAdded: boolean
}


// array_index: { required: true, type: Number },
      // id: { required: true, type: String },
      // name: { required: true, type: String },
      // quantity: { required: true, type: Number },
      // photo: { required: true, type: String },
      // unitPrice: { required: true, type: Number },
      // isAdded: { required: true, type: Boolean },
      // numStars: { required: false, type: Number, default: 0, },
      // numberVotes: { required: false, type: Number, default: 160, },
      // currency: { required: true, type: String, },
      // numberOrders: { required: false, type: Number, default: 0, }