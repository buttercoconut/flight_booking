<template>
  <div class="flight-search-form">
    <h2>Search Flights</h2>
    <form @submit.prevent="searchFlights">
      <div>
        <label for="origin">Origin:</label>
        <input id="origin" v-model="origin" required />
      </div>
      <div>
        <label for="destination">Destination:</label>
        <input id="destination" v-model="destination" required />
      </div>
      <div>
        <label for="date">Date:</label>
        <input id="date" type="date" v-model="date" required />
      </div>
      <button type="submit">Search</button>
    </form>
    <ul v-if="flights.length">
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.airline }} - {{ flight.flightNumber }} - {{ flight.departureTime }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getFlights } from '../api/flight'

const origin = ref('')
const destination = ref('')
const date = ref('')
const flights = ref([])

const searchFlights = async () => {
  const result = await getFlights({ origin: origin.value, destination: destination.value, date: date.value })
  flights.value = result.data
}
</script>

<style scoped>
.flight-search-form {
  max-width: 600px;
  margin: 0 auto;
}
.flight-search-form form > div {
  margin-bottom: 10px;
}
</style>
