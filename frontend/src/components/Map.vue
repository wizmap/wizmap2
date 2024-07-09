<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
  
    <div id="map"></div>
  </template>
  
  <script>
  export default {
      data() {
          return {
              modalCheck: false,
          }
      },
      methods: {
          modalOpen() {
              this.modalCheck = !this.modalCheck
          }
      },
    mounted() {
      // 네이버 지도 API 로드
      const script = document.createElement("script");
      script.src = "https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=" + process.env.VUE_APP_MAPURL
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
  @import "../assets/css/main.css";
  
  
  </style>