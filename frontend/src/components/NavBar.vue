<template>
   <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
     <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#">FBViz</a>
     <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse"
       data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
       <span class="navbar-toggler-icon"></span>
     </button>
     <div class="navbar-nav">
       <div class="nav-item text-nowrap">
         <a class="nav-link px-3" @click="redirectLogin">Add data</a>
       </div>
     </div>
   </header>
  </template>

  <script>
  export default {
    name: 'NavBar',
    props: {
    },
    methods: {
      redirectLogin() {
        window.location.href = 'http://127.0.0.1:8000/users/login/';
      }
  }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>