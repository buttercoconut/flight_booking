<template>
  <div class="booking">
    <h2>예약 상세</h2>
    <div v-if="booking">
      <p>항공편: {{ booking.flight.airline }} {{ booking.flight.flight_number }}</p>
      <p>출발지: {{ booking.flight.origin }}</p>
      <p>도착지: {{ booking.flight.destination }}</p>
      <p>날짜: {{ booking.flight.date }}</p>
      <p>승객 수: {{ booking.passengers }}</p>
      <router-link :to="{ path: '/payment/' + booking.id }" class="btn">결제하기</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getBooking } from '../api/api'

const booking = ref(null)
const props = defineProps({ id: { type: String, required: true } })

onMounted(async () => {
  const { data } = await getBooking(props.id)
  booking.value = data.data
})
</script>
