import axios from 'axios'

const API_BASE = 'http://localhost:8000/api'

export const getFlights = async (params) => {
  return axios.get(`${API_BASE}/flights/`, { params })
}
