
import { createRouter, createWebHistory } from 'vue-router'
import FlightSearchView from './views/FlightSearchView.vue'
import BookingView from './views/BookingView.vue'
import PaymentView from './views/PaymentView.vue'

const routes = [
  { path: '/', component: FlightSearchView },
  { path: '/booking/:id', component: BookingView, props: true },
  { path: '/payment/:bookingId', component: PaymentView, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
