import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000,
})

export const searchFlights = (params) => apiClient.get('/flights/search', { params })
export const createBooking = (data) => apiClient.post('/bookings', data)
export const getBooking = (id) => apiClient.get(`/bookings/${id}`)
export const processPayment = (bookingId, paymentData) => apiClient.post(`/payments/${bookingId}`, paymentData)
