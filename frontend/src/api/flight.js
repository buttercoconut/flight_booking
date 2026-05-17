import axios from 'axios'

const API_BASE = '/api/flight'

export const searchFlightsApi = async (params) => {
  return axios.get(`${API_BASE}/search`, { params })
}
