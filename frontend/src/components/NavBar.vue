<template>
    <div class="row">
      <div class="col-12 p-0">
        <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
          <a class="navbar-brand col-sm-3 col-md-2 m-0" href="#">FTBViz</a>
          <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
          <ul class="navbar-nav px-3">
            <li class="nav-item text-nowrap">
              <a class="nav-link" href="#">Sign out</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </template>

  <script>
  export default {
    name: 'NavBar',
    props: {

    }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .container-fluid {
    padding: 0;
  }
</style>