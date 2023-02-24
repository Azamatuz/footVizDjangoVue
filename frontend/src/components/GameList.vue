
<template>
  <div class="hello">
    <div class="container-fluid">
      <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <!-- v-for game in games in <ul><li>-->
              <ul class="nav flex-column">
                <li class="nav-item" v-for="game in games" :key="game.id">
                  <a class="nav-link active" href="#">
                    <span data-feather="home">{{ game.date }}</span>
                    <br>
                    <span class="">{{ game.home_team }} vs {{ game.away_team }}</span>
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
      </div>
    </div>

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