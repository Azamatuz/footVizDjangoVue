
<template>

  <nav class="col-md-2 d-none d-md-block bg-light sidebar">
    <div class="sidebar-sticky">
      <!-- v-for game in games in <ul><li>-->
        <ul class="nav flex-column" v-for="month in monthsList" :key="month.id">
          <h6 class=" align-items-center px-3 mt-4 mb-1 text-muted"
            @click="selectMonth(month.id)">
            <span>{{ month.name }}</span>
          </h6>
          <li class="nav-item" v-for="game in sortedGames" :key="game.id">
            <a v-if="game.date.slice(5,7) == (month.id) && currentMonth == month.id"
              class="nav-link active" @click="selectGame(game.id)">
              <span data-feather="home">{{ game.date }}</span>
              <br>
              <span class="">{{ game.home_team.name }} vs {{ game.away_team.name }}</span>
            </a>
          </li>
        </ul>
      <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
        <span>Saved reports</span>
        <a class="d-flex align-items-center text-muted" href="#">
          <span data-feather="plus-circle"></span>
        </a>
      </h6>
      <ul class="nav flex-column mb-2">
        <li class="nav-item">
          <a class="nav-link" href="#">
            <span data-feather="file-text"></span>
            Current month
          </a>
        </li>
      </ul>
    </div>
  </nav>

</template>

<script>
// TODO: Add a button to toggle the sidebar
// TODO: Group games by date
// TODO: Toggle between games
import axios from 'axios';

export default {
  name: 'GameList',
  props: {
    msg: String,

  },
  data() {
    return {
      games: [],
      selectedGameId: null, // pass selectedGameId to statsList.vue
      monthsList : [ // month list of names and ids
      {
        id: '01',
        name: 'January'
      }, {
        id: '02',
        name: 'February'
      }, {
        id: '03',
        name: 'March'
      }, {
        id: '04',
        name: 'April'
      }, {
        id: '05',
        name: 'May'
      }, {
        id: '06',
        name: 'June'
      }, {
        id: '07',
        name: 'July'
      }, {
        id: '08',
        name: 'August'
      }, {
        id: '09',
        name: 'September'
      }, {
        id: '10',
        name: 'October'
      }, {
        id: '11',
        name: 'November'
      }, {
        id: '12',
        name: 'December'
      }
      ],
      currentMonth: new Date().getMonth() + 1
    };

  },
  mounted() {
    axios.get('http://localhost:8000/api/games/')
      .then(response => {
        console.log(response);
        this.games = response.data;
        console.log(this.games);
      })
      .catch(error => {
        console.log('error', error);
      });
  },
  methods: {
    selectGame(gameId) {
      this.selectedGameId = gameId;
      this.$emit('game-selected', gameId);
    },
    selectMonth(monthId) {
      this.currentMonth = monthId;
    }
  },
  computed: {
    // Sort games by date
    sortedGames() {
      return this.games.sort((a, b) => {
        return new Date(a.date) - new Date(b.date);
      });
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>