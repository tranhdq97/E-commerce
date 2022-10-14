import axios from 'axios'

const authAxios = axios.create({
  baseURL: import.meta.env.BASE_URL,
  timeout: 5000,
  headers: {},
})

export default authAxios
