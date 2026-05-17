<template>
  <div class="payment-form">
    <h2>결제 정보 입력</h2>
    <form @submit.prevent="submitPayment">
      <label>
        카드 번호:
        <input v-model="payment.cardNumber" required />
      </label>
      <label>
        유효기간 (MM/YY):
        <input v-model="payment.expiry" required />
      </label>
      <label>
        CVC:
        <input v-model="payment.cvc" required />
      </label>
      <button type="submit">결제 완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { processPaymentApi } from '../api/payment.js'

const router = useRouter()
const route = useRoute()
const payment = ref({ cardNumber: '', expiry: '', cvc: '' })

const submitPayment = async () => {
  const bookingId = route.query.bookingId
  await processPaymentApi({ bookingId, ...payment.value })
  router.push({ name: 'Home', query: { success: true } })
}
</script>

<style scoped>
.payment-form { max-width: 600px; margin: auto; }
label { display: block; margin: 0.5rem 0; }
</style>
