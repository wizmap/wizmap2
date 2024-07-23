<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

  <div id="main">
      <div id="center">
        <img id="logo">
        <form id="search" @submit.prevent="navigateToSearchResult({ search: searchTerm })">
          <input type="text" v-model="searchTerm" id="home-search-input" placeholder=" 장소를 입력하세요">
          <router-link to="/searchresult" id="home-search-button" @click="search"><i class="fas fa-search fa-lg"></i></router-link>
        </form>
      </div>
    </div>

  <div id="map"></div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchTerm: ''
    };
  },
  methods: {
    search() {
      this.$router.push({ name: 'SearchResult', query: { searchTerm: this.searchTerm } });
    },
    navigateToSearchResult(history) {
        if (history.place) {
          // 장소 ID를 쿼리 파라미터로 전달
          this.$router.push({ name: 'SearchResult', query: { placeId: history.place.id } });
        } else {
          // 검색어를 쿼리 파라미터로 전달
          this.$router.push({ name: 'SearchResult', query: { searchTerm: history.search } });
        }
      }
  },
  mounted() {
    // 네이버 지도 API 로드
    const script = document.createElement("script");
    script.src = "https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=" + process.env.VUE_APP_MAPURL;
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);

    script.onload = () => {
      // 네이버 지도 생성
      new window.naver.maps.Map("map", {
        center: new window.naver.maps.LatLng(37.5670135, 126.9783740),
        zoom: 10
      });
    };
  }
};
</script>

<style>
@import "../assets/css/home.css";

</style>