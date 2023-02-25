<template>
    <div class="row justify-content-end">
        <div class="col-10">
            <h2 class="m-3">{{ homeTeam.name }}</h2>
    <div v-for="index in homeTeamPlayers.length" :key="index"  class="table-responsive my-3">
        <table  class="table table-striped table-sm">
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
                <tr>
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
    </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'StatsList',
  props: {

  },
  data() {
    return {
        statsData: [],
        homeTeam: '',
        homeTeamPlayers: '',
        awayTeam: '',
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/games/1/')
      .then(response => {
        console.log(response.data.home_team.players);
        this.homeTeam = response.data.home_team;
        this.homeTeamPlayers = response.data.home_team.players;
        this.awayTeam = response.data.away_team;

        console.log(this.homeTeam);
      })
      .catch(error => {
        console.log('error', error);
      });
  },
}
</script>
<style scoped>
    .stats-table {
        margin: 40px 185px 0;
        width: 85%;
    }
</style>