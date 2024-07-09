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



export default {
  name: 'App',

  components: {
    SearchResult,
    Home,
  },

  data: () => ({
    //
  }),
}
</script>
