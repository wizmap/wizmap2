<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
    integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
    crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <v-app>
    <v-main>
        <Login></Login>
        <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { RouterView } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import SearchResult from './components/SearchResult.vue';
import SearchHistory from './components/SearchHistory.vue';
import SearchFavorite from './components/SearchFavorite.vue';




export default {
  name: 'App',

  components: {
    SearchResult,
    Home,
    Login,
    SearchHistory,
    SearchFavorite,
  },

  data: () => ({
    //
  }),
}
</script>
