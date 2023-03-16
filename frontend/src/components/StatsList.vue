<template>
    <div
        class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Dashboard / {{ gameId }}</h1>
        <div class="btn-toolbar mb-2 mb-md-0">
            <div class="btn-group me-2">
                <button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
                <button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
            </div>
            <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
                <span data-feather="calendar" class="align-text-bottom"></span>
                This week
            </button>
        </div>
    </div>
    <div class="row justify-content-end">
        <div class="col-12">
            <h2 class="m-3">{{ homeTeam.name }}</h2>
            <div class="table-responsive my-3">
                <table class="table table-striped table-sm">
                    <thead>
                        <tr>
                            <th>Player</th>
                            <th style="max-width: 20px;">Number</th>
                            <th>Goals</th>
                            <th>Assists</th>
                            <th>Passes</th>
                            <th>Blocks</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="index in homeTeamPlayers.length" :key="index">
                            <td>{{ homeTeamPlayers[index-1].name }}</td>
                            <td>{{ homeTeamPlayers[index-1].number }}</td>
                            <td>{{ homeTeamPlayers[index-1].stats.assists }}</td>
                            <td>{{ homeTeamPlayers[index-1].stats.goals }}</td>
                            <td>{{ homeTeamPlayers[index-1].stats.passes }}</td>
                            <td>{{ homeTeamPlayers[index-1].stats.blocks }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div row v-for="index in homeTeamPlayers.length" :key="index">
            <div class="col-3">
                <RadarChart v-bind:playerStats="Object.values(homeTeamPlayers[index-1].stats)"/>
            </div>
    </div>
    </div>
    <div class="row justify-content-end">
        <div class="col-12">
            <h2 class="m-3">{{ awayTeam.name }}</h2>
            <StatsTable v-bind:playerStats="awayTeamPlayers"/>
        </div>
        <div class="row" v-for="index in awayTeamPlayers.length" :key="index">
            <div class="col-3">
                <RadarChart v-bind:playerStats="Object.values(awayTeamPlayers[index-1].stats)"/>
            </div>
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
  },
  components: {
    RadarChart,
    StatsTable,
  },
  data() {
    return {
        statsData: [],
        homeTeam: '',
        homeTeamPlayers: '',
        awayTeam: '',
        awayTeamPlayers: '',
        gameDefaultId: 1,

    };
  },
  mounted() {
    this.getGameData(this.gameDefaultId);
  },
  methods: {
    getGameData(gameId) {
      axios.get('http://localhost:8000/api/games/' + gameId)
        .then(response => {
          console.log('away',response.data.away_team.players);
          this.homeTeam = response.data.home_team;
          this.homeTeamPlayers = response.data.home_team.players;
          this.awayTeam = response.data.away_team;
          this.awayTeamPlayers = response.data.away_team.players;
          console.log(this.awayTeamPlayers.length);
        })
        .catch(error => {
          console.log('error', error);
        });
    },
  },
  watch: {
    gameId: function (newGameId) {
      this.getGameData(newGameId);
    },
  },
}
</script>
<style scoped>

</style>