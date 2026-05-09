<template>
  <div class="flight-search">
    <h2>항공편 검색</h2>
    <form @submit.prevent="onSearch">
      <label>출발지: <input v-model="form.origin" required /></label>
      <label>도착지: <input v-model="form.destination" required /></label>
      <label>날짜: <input type="date" v-model="form.date" required /></label>
      <label>승객 수: <input type="number" v-model.number="form.passengers" min="1" required /></label>
      <button type="submit">검색</button>
    </form>
    <ul v-if="flights.length">
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.airline }} {{ flight.flight_number }} - {{ flight.origin }} → {{ flight.destination }}
        <router-link :to="{ path: '/booking/' + flight.id }">예약하기</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { searchFlights } from '../api/api'

const form = ref({ origin: '', destination: '', date: '', passengers: 1 })
const flights = ref([])

const onSearch = async () => {
  const { data } = await searchFlights(form.value)
  flights.value = data.data
}
</script>
