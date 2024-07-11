<template>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
    integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
    crossorigin="anonymous" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <button id="modal-button" @click="modalOpen"><i class="fas fa-user fa-2x"></i></button>

    <div class="modal-wrap" v-show="modalCheck" @click="modalOpen">
    <div class="modal-container" @click.stop="">
        
        <img id="profile">
        <div v-if="!isLoggedIn" class="modal-wrap" v-show="modalCheck" @click="modalOpen">
        <div class="modal-container" @click.stop="">
            <!-- 로그인 폼 -->
            <img id="profile">
            <div class="input_container">
            <div>
                <input type="text" v-model="loginId" id="login-id-input" placeholder="ID" />
            </div>
            <br/>
            <div>
                <input type="password" v-model="loginPassword" id="login-password-input" placeholder="PASSWORD" />
            </div>
            </div>
            <div class="modal-btn">
            <button id="login-button" @click="login">login</button>
            <button id="register-button" @click="modalOpen">register</button>
            </div>
        </div>
        </div>
            <!-- 로그인된 경우 마이페이지 내용 표시 -->
        <div v-else>
            <p>마이페이지 내용이 여기에 표시됩니다.</p>
            <!-- 로그아웃 버튼 등 마이페이지 관련 내용 -->
        </div>
    </div>
</div>
    <div id="main">
    <div id="center">
        <img id="logo">
        <form id="search">
            <input type="text" id="home-search-input" placeholder="       장소를 입력하세요">
            <button id="home-search-button"><i class="fas fa-search fa-lg"></i></button>
        </form>
    </div>
    </div>
    <div id="map"></div>
</template>



<script>
import axios from 'axios'; // axios 임포트

export default {
  data() {
    return {
      modalCheck: false,
      loginId: '', // 로그인 ID
      loginPassword: '', // 로그인 비밀번호
      isLoggedIn: false, // 로그인 상태
    };
  },
  methods: {
    modalOpen() {
      this.modalCheck = !this.modalCheck;
    },
    login() {
      const loginData = {
        username: this.loginId,
        password: this.loginPassword,
      };
      axios.post('http://localhost:8000/user/api/token/', loginData)
        .then(response => {
        console.log(response.data.access);
        localStorage.setItem('userToken', response.data.access); // 토큰 저장
        this.isLoggedIn = true; // 로그인 상태 업데이트
        this.modalCheck = false; // 로그인 성공 후 모달 닫기
        })
        .catch(error => {
          console.error("Login error:", error);
        });
    },
    checkLoginStatus() {
      // 로컬 스토리지에서 토큰 확인
      const token = localStorage.getItem('userToken');
      this.isLoggedIn = !!token; // 토큰 유무에 따라 로그인 상태 설정
    },
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
@import "../assets/css/home.css";


</style>
