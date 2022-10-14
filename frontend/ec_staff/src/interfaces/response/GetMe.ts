export interface GetMe {
  data : {
    id: number,
    email: string,
    info: {
      id: number,
      first_name: string,
      last_name: string,
      dob: string,
      phone_number: string,
      photo: string,
    },
    created_at: string,
    updated_at: string,
  }
}