
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Games</h3>
    <ul v-for="game in games" :key="game.id">
      <li>
        {{ game.date }}
        {{ game.home_team }} vs {{ game.away_team }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GameList',
  props: {
    msg: String
  },
  data() {
    return {
      games: [],
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