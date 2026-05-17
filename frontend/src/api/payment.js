import axios from 'axios'

const API_BASE = '/api/payment'

export const processPaymentApi = async (data) => {
  return axios.post(`${API_BASE}/process`, data)
}
