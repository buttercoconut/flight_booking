<template>
  <div class="booking-form">
    <h2>예약 정보 입력</h2>
    <form @submit.prevent="submitBooking">
      <label>
        승객 이름:
        <input v-model="booking.name" required />
      </label>
      <label>
        연락처:
        <input v-model="booking.phone" required />
      </label>
      <label>
        이메일:
        <input type="email" v-model="booking.email" required />
      </label>
      <button type="submit">결제 페이지로 이동</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { createBookingApi } from '../api/booking.js'

const router = useRouter()
const route = useRoute()
const booking = ref({ name: '', phone: '', email: '' })

const submitBooking = async () => {
  const flightId = route.query.flightId
  const res = await createBookingApi({ flightId, ...booking.value })
  const bookingId = res.data.bookingId
  router.push({ name: 'Payment', query: { bookingId } })
}
</script>

<style scoped>
.booking-form { max-width: 600px; margin: auto; }
label { display: block; margin: 0.5rem 0; }
</style>
