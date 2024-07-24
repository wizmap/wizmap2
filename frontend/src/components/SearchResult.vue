<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
      <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
      <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
      <div class="modal-favorite-container" @click="preventClose">
  
        <div class="modal-btn">
          <button id="modal-search-button" @click="openSearchModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
        </svg></button>

          <div class="modal-search-wrap" v-show="firstModalOpen" @click="closeSearchModals">
          <div class="modal-search-container" @click="preventClose">
              <div class="modal-btn">
                <div id="search-results">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item" v-for="result in searchResults" :key="result.place.id">
                    <button @click="openSearchDetailModal(result)">
                      <p id="name">{{ result.place.name }}</p>
                    <p id="category">{{ result.place.category }}</p>
                    <p id="address">{{ result.place.address.address }}</p>
                    <p id="isopen">영업 상태: <span :class="{ 'open': result.place.isopen, 'closed': !result.place.isopen }">{{ result.place.isopen ? '영업 중' : '휴무' }}</span></p>
                    </button>
                      <div class="modal-btn">
                        <div class="modal-search-detail-wrap" v-show="firstDetailModalOpen" @click="closeSearchDetailModals">
                          <div class="modal-search-detail-container" @click="preventClose">
                              <div id="place-details" v-if="selectedPlace">
                                <p id="name-details">{{ selectedPlace.place.name }}</p>
                                <p id="category">{{ selectedPlace.place.category }}</p>
                                <p id="address-details">주소: {{ selectedPlace.place.address.address }}</p>
                                <p>위도: {{ selectedPlace.place.address.latitude }}</p>
                                <p>경도: {{ selectedPlace.place.address.longitude }}</p>
                                <p>메뉴: {{ selectedPlace.place.menu }}</p>
                                <p>전화번호: {{ selectedPlace.place.phone }}</p>
                                <p>메모: {{ selectedPlace.place.memo }}</p>
                                <p id="isopen">영업 상태: <span :class="{ 'open': selectedPlace.place.isopen, 'closed': !selectedPlace.place.isopen }">{{ selectedPlace.place.isopen ? '영업 중' : '휴무' }}</span></p>
                                <ul>
                                  <li v-for="hour in selectedPlace.business_hours" :key="hour.id">{{ hour.day }}: {{ hour.open }} - {{ hour.close }}</li>
                                </ul>
                              </div>
                              <div v-else>
                              <p>장소 정보가 없습니다.</p>
                            </div>
                          </div>
                        </div>
                      </div>
                  </li>
                </ul>
              </div>
              </div>
          
          </div>
          </div>
          </div>
  
          <div class="modal-btn">
          <router-link to="/favorites" id="quikslot-button" @click.prevent="checkLoginAndNavigate('Favorites')" @click="openQuikModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-send-fill" viewBox="0 0 16 16">
          <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471z"/>
          </svg></router-link>
          </div>
  
          <div class="modal-btn">
          <router-link to="/favorites" id="favorits-button" @click="openFavModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
          <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
          </svg></router-link>
          </div>
  
          <div class="modal-btn">
          <router-link to="/history" id="history-button" @click.prevent="checkLoginAndNavigate('SearchHistory')" @click="openHisModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
          <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
          <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
          <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
          </svg></router-link>
          </div>
          
      </div>
      </div>
  
      <div id="main">
      <div id="search-center">
          <router-link to="/"><img id="search-logo"></router-link>
          <form id="search" @submit.prevent="onSearch">
            <input type="text" v-model="searchTerm" id="search-input" placeholder="장소를 입력하세요" @input="fetchSuggestions" @focus="showSuggestions" @blur="hideSuggestions" />
            <button id="search-button"><i class="fas fa-search fa-lg"></i></button>
          </form>
          <ul v-if="showAutocomplete && suggestions.length" class="autocomplete-list">
            <li v-for="(suggestion, index) in suggestions" :key="index" @mousedown.prevent="selectSuggestion(suggestion)">
              {{ suggestion }}
            </li>
          </ul>
      </div>
      </div>
      <div id="search-map"></div>
      <!-- 로그인 필요 알림창 -->
      <div v-if="showAlert" class="alert-overlay">
      <div class="alert-box">
        <p>{{ alertMessage }}</p>
        <button @click="closeAlert">확인</button>
      </div>
    </div>
  
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
      data() {
    return {
      favoriteModalOpen: false,
      firstModalOpen: false,
      firstDetailModalOpen: false,
      secondModalOpen: false,
      thirdModalOpen: false,
      fourthModalOpen: false,
      modalOpen: false,
      placeData: null,
      searchTerm: '',
      searchResults: [],
      showAlert: false, // 알림창 표시 여부
      alertMessage: '', // 알림창 메시지
      map: null, // 지도 객체를 저장할 변수 추가
      mapInitialized: false, // 지도 초기화 상태를 저장할 변수 추가
      markers: [], // 마커 객체를 저장할 배열 추가
      histories: [], // 검색 기록을 저장할 배열
      selectedPlace: null, // 선택된 장소의 상세 정보를 저장할 변수 추가
      placeId: null,
      suggestions: [],
      showAutocomplete: false,
    };
  },
  created() {
    this.openSearchModal();
    this.checkInitialSearch(); //SearchResult.vue 실행과 동시에 실행되도록 함
  },
  // SearchHistory.vue에서 가져온 searchTerm에 대한 검색결과 뿌려줌
  watch: {
  '$route.query.searchTerm': {
    immediate: true,
    handler(newQuery) {
      this.searchTerm = newQuery;
      if (this.searchTerm) {
        this.fetchSearchResults();
      } else {
        console.error("Search term is null or empty");
      }
    }
  }
},
  methods: {
    openFavoriteModal() {
      this.favoriteModalOpen = true;
      this.closeModalsExcept('favoriteModalOpen');
    },
    openSearchModal() {
      this.firstModalOpen = true;
      this.closeModalsExcept('firstModalOpen');
    },
    openSearchDetailModal(result) {
      this.fetchPlaceDetails(result.place.id)//id값으로 장소데이터 불러오기
      this.firstDetailModalOpen = true;
      this.closeModalsExcept('firstDetailModalOpen');
    },
    openQuikModal() {
      this.secondModalOpen = true;
      this.closeModalsExcept('secondModalOpen');
    },
    openFavModal() {
      this.thirdModalOpen = true;
      this.closeModalsExcept('thirdModalOpen');
    },
    openHisModal() {
      this.fourthModalOpen = true;
      this.fetchHistory(); // 검색 기록 불러오기
      this.closeModalsExcept('fourthModalOpen');
    },
    openModal() {
      this.modalOpen = true;
      this.closeModalsExcept('modalOpen');
    },
    closeFavoriteModals() {
      this.favoriteModalOpen = false;
    },
    closeSearchDetailModals() {
      this.favoriteModalOpen = true;
      this.firstModalOpen = true;
      this.firstDetailModalOpen = false;
    },
    closeSearchModals() {
      this.favoriteModalOpen = true;
      this.firstModalOpen = false;
    },
    closeQuikModals() {
      this.favoriteModalOpen = true;
      this.secondModalOpen = false;
    },
    closeFavModals() {
      this.favoriteModalOpen = true;
      this.thirdModalOpen = false;
    },
    closeHisModals() {
      this.favoriteModalOpen = true;
      this.fourthModalOpen = false;
    },
    closeModal() {
      this.modalOpen = false;
    },
    preventClose(event) {
      event.stopPropagation();
    },
    closeModalsExcept(exceptModal) {
    if (exceptModal !== 'favoriteModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.favoriteModalOpen == 'true') {
          this.favoriteModalOpen = true;
        }
      }
      else {
      this.favoriteModalOpen = true;
      }
    }
    if (exceptModal !== 'firstModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.firstModalOpen == 'true') {
          this.firstModalOpen = true;
        }
      }
      else {
      this.firstModalOpen = false;
      }
    }
    if (exceptModal !== 'firstDetailModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.firstDetailModalOpen == 'true') {
          this.firstDetailModalOpen = true;
        }
      }
      else {
      this.firstDetailModalOpen = false;
      }
    }
    if (exceptModal !== 'secondModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.secondModalOpen == 'true') {
          this.secondModalOpen = true;
        }
      }
      else {
      this.secondModalOpen = false;
      }
    }
    if (exceptModal !== 'thirdModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.thirdModalOpen == 'true') {
          this.thirdModalOpen = true;
        }
      }
      else {
      this.thirdModalOpen = false;
      }
    }
    if (exceptModal !== 'fourthModalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'modalOpen') {
        if (this.fourthModalOpen == 'true') {
          this.fourthModalOpen = true;
        }
      }
      else {
      this.fourthModalOpen = false;
      }
    }
    if (exceptModal !== 'modalOpen') {
      if (exceptModal == 'firstModalOpen') {
        this.firstModalOpen = true;
      }
      if (exceptModal == 'firstDetailModalOpen') {
        this.firstModalOpen = true;
      }
      this.modalOpen = false;
    }
    },
    checkLoginAndNavigate(routeName) {
    const isLoggedIn = localStorage.getItem('userToken');
    if (!isLoggedIn) {
      this.alertMessage = '로그인이 필요합니다.';
      this.showAlert = true;
    } else {
      this.$router.push({ name: routeName });
    }
    },
    closeAlert() {
      this.showAlert = false;
    },
    async fetchHistory() {
    const userToken = localStorage.getItem('userToken');
    try {
      const response = await fetch('http://localhost:8000/history/', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${userToken}`,
          'Content-Type': 'application/json'
        }
      });
      if (response.ok) {
        const data = await response.json();
        this.histories = data.histories; // 검색 기록을 데이터에 저장
      } else {
        throw new Error('Failed to fetch history');
      }
    } catch (error) {
      console.error("There was an error fetching the history!", error);
    }
  },

  async fetchSearchResults() {
      if (!this.searchTerm) {
        console.error("Search term is null or empty");
        return;
      }
      try {
        const userToken = localStorage.getItem('userToken');
        const headers = {
          'Content-Type': 'application/json',
        };
        if (userToken) {
          headers['Authorization'] = `Bearer ${userToken}`;
        }
        const response = await fetch('http://localhost:8000/searchengine/', {
          method: 'POST',
          headers,
          body: JSON.stringify({ search: this.searchTerm })
        });
        this.searchResults = await response.json();

        // 기존 마커 제거
        this.markers.forEach(marker => marker.setMap(null));
        this.markers = [];

        // 검색 결과의 첫 번째 장소의 위도와 경도로 지도 중심 변경
        if (this.searchResults.length > 0) {
          const firstResult = this.searchResults[0].place;
          const newCenter = new window.naver.maps.LatLng(firstResult.address.latitude, firstResult.address.longitude);
          if (this.mapInitialized) {
            this.map.setCenter(newCenter);

            // 검색 결과의 위치에 마커 추가
            this.searchResults.forEach(result => {
              const position = new window.naver.maps.LatLng(result.place.address.latitude, result.place.address.longitude);
              const marker = new window.naver.maps.Marker({
                position,
                map: this.map,
                title: result.place.name
              });
              marker.addListener('click', () => {
                this.fetchPlaceDetails(result.place.id);
                this.openSearchDetailModal(result);

              });
              this.markers.push(marker);
            });
          } else {
            console.error('Map is not initialized');
          }
        }
        // 새로운 검색이 수행되면 장소 세부 정보 숨기기
        this.selectedPlace = null;
      } catch (error) {
        console.error("There was an error fetching the search results!", error);
      }
    },
    fetchSuggestions() {
      if (this.searchTerm.length > 1) {
        axios.get(`http://localhost:8000/searchengine/`, {
          params: { query: this.searchTerm }
        })
        .then(response => {
          this.suggestions = response.data;
        })
        .catch(error => {
          console.error(error);
        });
      } else {
        this.suggestions = [];
      }
    },
    showSuggestions() {
      this.showAutocomplete = true;
    },
    hideSuggestions() {
      setTimeout(() => {
        this.showAutocomplete = false;
      }, 200);
    },
    selectSuggestion(suggestion) {
      this.searchTerm = suggestion;
      this.showAutocomplete = false;
      this.onSearch();
    },
    async fetchPlaceDetails(id) {
      try {
        const userToken = localStorage.getItem('userToken');
        const headers = {
          'Content-Type': 'application/json',
        };
        if (userToken) {
          headers['Authorization'] = `Bearer ${userToken}`;
        }
        const response = await fetch(`http://localhost:8000/search/pin/${id}/`, {
          method: 'GET',
          headers,
        });
        if (response.ok) {
          this.selectedPlace = await response.json();
          this.searchTerm = this.selectedPlace.place.name;
        } else {
          const errorText = await response.text();
          console.error('Failed to fetch place details:', errorText);
          throw new Error('Failed to fetch place details');
        }
      } catch (error) {
        console.error("There was an error fetching the place details!", error);
      }
    },
    onSearch() {
      if (this.mapInitialized) {
        this.fetchSearchResults();
      } else {
        console.error('Map is not initialized yet');
      }
    },
    checkInitialSearch() {
      if (this.mapInitialized) {
        if (this.$route.query.searchTerm) {
          this.searchTerm = this.$route.query.searchTerm;
          this.onSearch();
        } else if (this.$route.query.placeId) {
          this.placeId = this.$route.query.placeId;
          this.fetchPlaceDetails(this.placeId);
        }
      }
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
      script.src = "https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=" + process.env.VUE_APP_MAPURL;
      script.async = true;
      script.defer = true;
      document.head.appendChild(script);
      script.onload = () => {
        // 네이버 지도 생성
        this.map = new window.naver.maps.Map("search-map", {
          center: new window.naver.maps.LatLng(37.5670135, 126.9783740),
          zoom: 12
        });
        this.mapInitialized = true; // 지도 초기화 상태 업데이트

        this.checkInitialSearch(); // 지도 초기화 후 초기 검색 조건 확인 및 실행
      };
    }
  };
  </script>



  <style>
  @import "../assets/css/search.css";


  </style>