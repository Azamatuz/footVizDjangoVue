<template>
    <div
        class="d-flex justify-content-start flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <a href="#home-team">
          <h1 class="h2">{{ homeTeam.name }}</h1>
        </a>
        <h1 class="h2 m-2">vs</h1>
        <a href="#away-team">
          <h1 class="h2">{{ awayTeam.name }}</h1>
        </a>
    </div>

    <div class="row">
      <div class="col-12">
        <h1 class="h2">Teams comparison</h1>
      </div>
      <div class="col-12 col-md-6" v-for="(team, index) in statsData" :key="index">
        <RadarChart v-bind:playerStats="Object.values(team)" />
      </div>
    </div>
    <div class="row" id="home-team">
      <div class="col-12">
        <h2 class="text-start">{{ homeTeam.name }}</h2>
        <StatsTable v-bind:playerStats="homeTeamPlayers"/>
      </div>
      <div class="col-6" v-for="(player, index) in homeTeamPlayers" :key="index">
        <RadarChart v-bind:playerStats="Object.values(player)" />
      </div>
    </div>
    <div class="row" id="away-team">
      <div class="col-12">
        <h2 class="text-start">{{ awayTeam.name }}</h2>
        <StatsTable v-bind:playerStats="awayTeamPlayers" />
      </div>
      <div class="col-6" v-for="(player, index) in awayTeamPlayers" :key="index">
        <RadarChart v-bind:playerStats="Object.values(player)" />
      </div>
    </div>

</template>

<script>
import axios from 'axios';
// components
import RadarChart from './RadarChart.vue'
import StatsTable from './StatsTable.vue'

export default {
  name: 'StatsList',
  props: {
    gameId: Number,
    defaultId: Number,
  },
  components: {
    RadarChart,
    StatsTable,
  },
  data() {
    return {
        statsData: [],
        teamsStats: [],
        teamsStatsValues: [],
        homeTeam: '',
        homeTeamStats: '',
        homeTeamPlayers: [],
        awayTeam: '',
        awayTeamPlayers: [],
        awayTeamStats: '',
    };
  },
  mounted() {

  },
  methods: {
    setTeamsStats(){
      // combine this.homeTeam.name and this.teamsStats[0] into this.homeTeamStats: { name: 'this.homeTeam.name', stats: [this.teamsStats[0]] }
      this.homeTeamStats = { name: this.homeTeam.name, stats: [this.teamsStats[0]] };
      this.awayTeamStats = { name: this.awayTeam.name, stats: [this.teamsStats[1]] };
      this.statsData.push(this.homeTeamStats)
      this.statsData.push(this.awayTeamStats);

    },
    getValues() {
      // extract values from teamsStats to teamsStatsValues
      for (let i = 0; i < this.teamsStats.length; i++) {
        this.teamsStatsValues.push(Object.values(this.teamsStats[i]));
      }
    },
    normalizeData() {
      const minMaxNormalization = (value, max) => (value) / (max);
      const attributes = Object.keys(this.teamsStats[0]);
      const attributeValues = this.teamsStats.map(obj => attributes.map(attr => Number(obj[attr])));
      const maxValues = attributeValues.reduce((max, curr) => curr.map((value, index) => Math.max(value, max[index])), Array(attributes.length).fill(Number.NEGATIVE_INFINITY));

      for (let i = 0; i < this.teamsStats.length; i++) {
        for (const attr of attributes) {
          this.teamsStats[i][attr] = parseFloat(minMaxNormalization(Number(this.teamsStats[i][attr]), maxValues[attributes.indexOf(attr)])).toFixed(2);
        }
      }
    },

    getGameData(gameId) {
      axios.get('http://localhost:8000/api/games/' + gameId)
        .then(response => {
          this.teamsStats = response.data.teams_stats.stats;
          this.homeTeam = response.data.home_team;
          this.homeTeamPlayers = response.data.home_team.players;
          this.awayTeam = response.data.away_team;
          this.awayTeamPlayers = response.data.away_team.players;
          this.normalizeData();
          this.getValues();
          this.setTeamsStats()
        })
        .catch(error => {
          console.log('error', error);
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

  },
}
</script>
<style scoped>

</style>