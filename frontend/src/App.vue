<script setup>
import GameList from './components/GameList.vue';
import NavBar from './components/NavBar.vue'
import StatsList from './components/StatsList.vue'

</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
    <GameList />
    <StatsList />
  </main>
</template>

<style scoped>

</style>