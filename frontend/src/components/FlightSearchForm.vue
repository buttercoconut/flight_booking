<template>
  <div class="flight-search">
    <h2>항공편 검색</h2>
    <form @submit.prevent="searchFlights">
      <label>
        출발지:
        <input v-model="search.from" required />
      </label>
      <label>
        도착지:
        <input v-model="search.to" required />
      </label>
      <label>
        날짜:
        <input type="date" v-model="search.date" required />
      </label>
      <label>
        승객 수:
        <input type="number" v-model.number="search.passengers" min="1" required />
      </label>
      <button type="submit">검색</button>
    </form>
    <ul v-if="flights.length">
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.airline }} {{ flight.flight_number }} - {{ flight.departure_time }} → {{ flight.arrival_time }}
        <button @click="selectFlight(flight)">선택</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { searchFlightsApi } from '../api/flight.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const search = ref({ from: '', to: '', date: '', passengers: 1 })
const flights = ref([])

const searchFlights = async () => {
  const res = await searchFlightsApi(search.value)
  flights.value = res.data
}

const selectFlight = (flight) => {
  router.push({ name: 'Booking', query: { flightId: flight.id } })
}
</script>

<style scoped>
.flight-search { max-width: 600px; margin: auto; }
label { display: block; margin: 0.5rem 0; }
</style>
