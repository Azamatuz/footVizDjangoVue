<template>
    <div
        class="d-flex justify-content-start flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <a href="#home-team">
          <h1 class="h2">{{ homeTeam }}</h1>
        </a>
        <h1 class="h2 m-2">vs</h1>
        <a href="#away-team">
          <h1 class="h2">{{ awayTeam }}</h1>
        </a>
    </div>

    <div class="row">
      <div class="col-12">
        <h1 class="h2">Teams comparison</h1>
      </div>
      <div class="col-12">
        <BarChart v-bind:homeTeamStats="homeTeamData" v-bind:awayTeamStats="awayTeamData" />
      </div>
    </div>

    <div class="row mt-5" id="home-team">
      <div class="col-12">
        <h2 class="text-start">{{ homeTeam }}</h2>
      </div>
      <div class="col-12 col-md-10 text-start">
          <h4>Players' normalized performance </h4>
      </div>
      <TabNav v-bind:PlayersSumData="homePlayersSum" v-bind:PlayersData="homePlayersData" v-bind:homeTeam=true v-bind:tabId="'Home'" />
    </div>

    <div class="row" id="away-team">
      <div class="col-12">
        <h2 class="text-start">{{ awayTeam }}</h2>
      </div>
      <div class="col-12 col-md-10 text-start">
          <h4>Players' normalized performance </h4>
      </div>
      <TabNav v-bind:PlayersSumData="awayPlayersSum" v-bind:PlayersData="awayPlayersData" v-bind:homeTeam=false v-bind:tabId="'Away'" />
    </div>

</template>

<script>
import axios from 'axios';
// components
import BarChart from './VerticalBar.vue'
import TabNav from './TabNav.vue'

export default {
  name: 'StatsList',
  props: {
    gameId: Number,
    defaultId: Number,
  },
  components: {
    BarChart,
    TabNav,
  },
  data() {
    return {
        statsData: [],
        playerStatsSum:[],
        homeTeam: '',
        homeTeamStats: '',
        awayTeam: '',
        awayTeamStats: '',
    };
  },
  mounted() {
    this.getGameData(this.gameId);
  },
  methods: {
    getGameData(gameId) {
      axios.get('http://localhost:8000/api/game-stats/game_id=' + gameId)
        .then(response => {
          this.statsData = response.data;
        })
        .catch(error => {
          console.log('StatsList error', error);
      });
      axios.get('http://localhost:8000/api/player-stats-sum/game_id=' + gameId)
        .then(response => {
          this.playerStatsSum = response.data;
        })
        .catch(error => {
          console.log('StatsList error', error);
      });
      axios.get('http://localhost:8000/api/games/' + gameId)
        .then(response => {
          this.homeTeam = response.data.home_team;
          this.awayTeam = response.data.away_team;
        })
        .catch(error => {
          console.log('StatsList error', error);
        });
    },
  },
  watch: {
    defaultId: function (newDefaultId) {
      this.getGameData(newDefaultId);
    },
    gameId: function (newGameId) {
      this.getGameData(newGameId);
      this.statsData = [];
    },
  },
  computed: {
    homePlayersData() {
      return this.statsData.filter(
        player => player.player_name !== "Team" && player.player_team === this.homeTeam
      );
    },
    homePlayersSum() {
      return this.playerStatsSum.filter(
        player => player.player_name !== "Team" && player.player_team === this.homeTeam
      );
    },
    awayPlayersData() {
      return this.statsData.filter(
        player => player.player_name !== "Team" && player.player_team === this.awayTeam
      );
    },
    awayPlayersSum() {
      return this.playerStatsSum.filter(
        player => player.player_name !== "Team" && player.player_team === this.awayTeam
      );
    },
    homeTeamData() {
      return this.statsData.filter(
        player => player.player_name === "Team" && player.player_team === this.homeTeam
      );
    },
    awayTeamData() {
      return this.statsData.filter(
        player => player.player_name === "Team" && player.player_team === this.awayTeam
      );
    },
  },
}
</script>
<style scoped>

</style>