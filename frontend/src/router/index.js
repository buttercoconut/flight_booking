import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Booking from '../views/Booking.vue'
import Payment from '../views/Payment.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/booking', name: 'Booking', component: Booking },
  { path: '/payment', name: 'Payment', component: Payment },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
