<template>
  <v-app>
    <v-main>
        <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { RouterView } from 'vue-router';
import SearchResult from './components/SearchResult.vue';
import Home from './components/Home.vue';
import SearchHistory from './components/SearchHistory.vue';



export default {
  name: 'App',

  components: {
    SearchResult,
    Home,
    SearchHistory,
  },

  data: () => ({
    //
  }),
}
</script>
