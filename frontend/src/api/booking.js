import axios from 'axios'

const API_BASE = '/api/booking'

export const createBookingApi = async (data) => {
  return axios.post(`${API_BASE}/create`, data)
}
