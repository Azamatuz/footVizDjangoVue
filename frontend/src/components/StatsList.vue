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
      <div class="col-12">
        <BarChart v-bind:homeTeamStats="homeTeamStats" v-bind:awayTeamStats="awayTeamStats" />
      </div>
    </div>
    <div class="row" id="home-team">
      <div class="col-12">
        <h2 class="text-start">{{ homeTeam.name }}</h2>
        <StatsTable v-bind:playerStats="homeTeamPlayers"/>
      </div>
      <div class="col-6" v-for="(player, index) in homeTeamPlayers" :key="index">
        <RadarChart v-bind:playerStats="Object.values(player)" v-bind:homeTeam="true"/>
      </div>
    </div>
    <div class="row" id="away-team">
      <div class="col-12">
        <h2 class="text-start">{{ awayTeam.name }}</h2>
        <StatsTable v-bind:playerStats="awayTeamPlayers" />
      </div>
      <div class="col-6" v-for="(player, index) in awayTeamPlayers" :key="index">
        <RadarChart v-bind:playerStats="Object.values(player)" v-bind:homeTeam="false"/>
      </div>
    </div>

</template>

<script>
import axios from 'axios';
// components
import RadarChart from './RadarChart.vue'
import StatsTable from './StatsTable.vue'
import BarChart from './VerticalBar.vue'
import { Bar } from 'vue-chartjs';

export default {
  name: 'StatsList',
  props: {
    gameId: Number,
    defaultId: Number,
  },
  components: {
    RadarChart,
    StatsTable,
    BarChart,
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
    normalizeData() {
      const attributes = ["shots", "sca", "touches", "passes", "carries", "tackled", "interceptions", "blocks"];
      const attributeValues = this.teamsStats.map(obj => attributes.map(attr => Number(obj.stats[0][attr])));
      const maxValues = attributeValues.reduce((max, curr) => curr.map((value, index) => Math.max(value, max[index])), Array(attributes.length).fill(Number.NEGATIVE_INFINITY));

      for (let i = 0; i < this.teamsStats.length; i++) {
        for (const attr of attributes) {
          const value = parseFloat(this.teamsStats[i].stats[0][attr]);
          this.teamsStats[i].stats[0][attr] = parseFloat(value / maxValues[attributes.indexOf(attr)]).toFixed(2);
        }
      }
    },
    // make this.homeTeamStats and this.awayTeamStats in this.teamsStats
    combineTeamsData() {
      this.teamsStats = [{name: this.homeTeamStats.team_name, stats: this.homeTeamStats.stats}];
      this.teamsStats.push({name: this.awayTeamStats.team_name, stats: this.awayTeamStats.stats});
      //this.normalizeData();
    },
    getGameData(gameId) {
      axios.get('http://localhost:8000/api/games/' + gameId)
        .then(response => {
          this.homeTeam = response.data.home_team;
          this.homeTeamStats = response.data.home_team_stats;
          this.homeTeamPlayers = response.data.home_team.players;
          this.awayTeam = response.data.away_team;
          this.awayTeamStats = response.data.away_team_stats;
          this.awayTeamPlayers = response.data.away_team.players;
          this.combineTeamsData();
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