<template>
  <v-app>
    <v-main>
      <IndexMap/>
    </v-main>
  </v-app>
</template>

<script>
import IndexMap from './components/IndexMap.vue'


export default {
  name: 'App',

  components: {
    IndexMap,
  },

  data: () => ({
    //
  }),
}
</script>
