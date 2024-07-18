<template>
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
