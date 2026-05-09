<template>
  <div class="payment">
    <h2>결제 페이지</h2>
    <form @submit.prevent="onPay">
      <label>카드 번호: <input v-model="form.cardNumber" required /></label>
      <label>유효기간: <input v-model="form.expiry" required /></label>
      <label>CVC: <input v-model="form.cvc" required /></label>
      <button type="submit">결제하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { processPayment } from '../api/api'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({ bookingId: { type: String, required: true } })
const form = ref({ cardNumber: '', expiry: '', cvc: '' })

const onPay = async () => {
  await processPayment(props.bookingId, form.value)
  router.push('/')
}
</script>
