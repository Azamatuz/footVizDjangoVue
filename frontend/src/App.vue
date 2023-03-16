<template>
  <NavBar />
  <div class="container-fluid">
    <div class="row">
      <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
        <GameList @game-selected="selectGame" />
      </nav>
      <main class="bg-white col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <StatsList v-bind:gameId="gameId" />
      </main>
    </div>
  </div>
</template>

<script>
import GameList from './components/GameList.vue';
import NavBar from './components/NavBar.vue'
import StatsList from './components/StatsList.vue'

export default {
  name: 'App',
  components: {
    GameList,
    NavBar,
    StatsList,
  },
  data() {
    return {
      gameId: null,
    };
  },
  methods: {
    selectGame(gameId) {
      console.log('selectGame', gameId);
      this.gameId = gameId;
    },

    }
};

</script>

<style scoped>

</style>