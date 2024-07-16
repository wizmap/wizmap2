<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
      <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
      <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
      <div class="modal-favorite-container" @click="preventClose">
  
        <div class="modal-btn">
          <router-link to="/searchresult" id="modal-search-button" @click="openSearchModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
        </svg></router-link>
        </div>
  
          <div class="modal-btn">
          <button id="quikslot-button" @click="openQuikModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-send-fill" viewBox="0 0 16 16">
          <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471z"/>
          </svg></button>
          <div class="modal-quikslot-wrap" v-show="secondModalOpen" @click="closeQuikModals">
          <div class="modal-quikslot-container" @click="preventClose">
          <div id = "quik-buttons">
              <div class="modal-btn"><button id="first-quik"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
              <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
              </svg></button></div>
              <div class="modal-btn"><button id="second-quik"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
              <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
              </svg></button></div>
              <div class="modal-btn"><button id="third-quik"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
              <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
              </svg></button></div>
          </div>
          </div>
          </div>
          </div>
  
          <div class="modal-btn">
          <router-link to="/favorites" id="favorits-button" @click="openFavModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
          <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
          </svg></router-link>
          </div>
  
          <div class="modal-btn">
          <button id="history-button" @click="openHisModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
          <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
          <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
          <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
          </svg></button>
          <div class="modal-history-wrap" v-show="fourthModalOpen" @click="closeHisModals">
          <div class="modal-history-container" @click="preventClose">
              <ul class="list-group list-group-flush">
                  <li class="list-group-item" v-for="history in histories" :key="history.id">
                      <span id="history-name-details" @click="() => { 
                          if (history.place) {
                              fetchPlaceDetails(history.place.id); 
                          } else {
                              setSearchTerm(history.search);
                          }
                      }">
                          {{ history.search }}
                      </span>
                      <br>
                      <span id="address-details">
                          {{ history.place ? `${history.place.address.address}` : '' }}
                      </span>
                      <button id="history-delete-button" @click="deleteHistory(history.id)">삭제</button>
                  </li>
              </ul>
          </div>
          </div>
          </div>
          
      </div>
      </div>
  
  
      <div id="main">
      <div id="search-center">
          <img id="search-logo">
          <form id="search"  @submit.prevent="onSearch">
            <input type="text" v-model="searchTerm" id="search-input" placeholder="       장소를 입력하세요" @focus="showHistory" @blur="hideHistory">
              <router-link to="/searchresult" id="search-button"><i class="fas fa-search fa-lg"></i></router-link>
          </form>
      </div>
      </div>
      <button id="modal-button" @click="openModal"><i class="fas fa-user fa-2x"></i></button>
      <div class="modal-wrap" v-show="modalOpen" @click="closeModal">
      <div class="modal-container" @click="preventClose">
          
          <img id="profile">
          <div class="input_container">
          <div>
              <input type="text" id="login-id-input" placeholder="ID" />
          </div>
          <br/>
          <div>
              <input type="text" id="login-password-input" placeholder="PASSWORD" />
          </div>
          </div>
          
          <div class="modal-btn">
          <button id="register-button" @click="modalOpen">register</button>
          </div>
      </div>
      </div>
      <div id="search-map"></div>
  
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
      data() {
    return {
      favoriteModalOpen: true,
      firstModalOpen: false,
      firstDetailModalOpen: false,
      secondModalOpen: false,
      thirdModalOpen: false,
      fourthModalOpen: false,
      modalOpen: false,
      isLoggedIn: false, // 로그인 상태 여부
      loginId: '', // 로그인한 사용자의 ID
      placeData: null,
      searchTerm: '',
      searchResults: [],
      map: null, // 지도 객체를 저장할 변수 추가
      mapInitialized: false, // 지도 초기화 상태를 저장할 변수 추가
      markers: [], // 마커 객체를 저장할 배열 추가
      histories: [], // 검색 기록을 저장할 배열
      selectedPlace: null, // 선택된 장소의 상세 정보를 저장할 변수 추가
    };
  },
  created() {
      this.openHisModal();
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
   async fetchSearchResults(query) {
        try {
          //localStorage.removeItem('userToken'); //사용자 토큰 삭제
          const userToken = localStorage.getItem('userToken'); // 사용자 토큰 가져오기
          const headers = {
            'Content-Type': 'application/json',
          };
          if (userToken) {
            headers['Authorization'] = `Bearer ${userToken}`; // 헤더에 토큰 추가
          }
          const response = await fetch('http://localhost:8000/search/', {
            method: 'POST',
            headers,
            body: JSON.stringify({ search_term: query })
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
      async fetchPlaceDetails(id) {
       try {
        console.log(`Fetching details for place ID: ${id}`); // 추가된 로그
        const userToken = localStorage.getItem('userToken'); // 사용자 토큰 가져오기
        const headers = {
          'Content-Type': 'application/json',
        };
        if (userToken) {
          headers['Authorization'] = `Bearer ${userToken}`; // 헤더에 토큰 추가
        }
        const response = await fetch(`http://localhost:8000/search/pin/${id}/`, {
          method: 'GET',
          headers,
        });
        if (response.ok) {
          this.selectedPlace = await response.json();
          console.log('Place details fetched successfully:', this.selectedPlace); // 추가된 로그

          // 장소 이름 검색어로 설정
          this.searchTerm = this.selectedPlace.place.name;    
          // 검색 결과 배열 비우기
          this.searchResults = [];

        } else {
          const errorText = await response.text();
          console.error('Failed to fetch place details:', errorText); // 추가된 로그
          throw new Error('Failed to fetch place details');
        }
      } catch (error) {
        console.error("There was an error fetching the place details!", error);
      }
    },
      onSearch() {
        if (this.mapInitialized) {
          this.fetchSearchResults(this.searchTerm);
        } else {
          console.error('Map is not initialized yet');
        }
      },
      setSearchTerm(term) {
        this.searchTerm = term;
        this.onSearch();
      },
      async deleteHistory(id) {
        const userToken = localStorage.getItem('userToken');
        try {
          const response = await fetch(`http://localhost:8000/history/delete/${id}`, {
            method: 'DELETE',
            headers: {
              'Authorization': `Bearer ${userToken}`,
              'Content-Type': 'application/json'
            }
          });
          if (response.ok) {
            this.histories = this.histories.filter(history => history.id !== id);
          } else {
            throw new Error('Failed to delete history');
          }
        } catch (error) {
          console.error("There was an error deleting the history!", error);
        }
      },
      showHistory() {
        this.historyVisible = true;
        this.fetchHistory();
      },
      hideHistory() {
        this.historyVisible = false;
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
        this.map = new window.naver.maps.Map("search-map", {
          center: new window.naver.maps.LatLng(37.5670135, 126.9783740),
          zoom: 12
        });
        this.mapInitialized = true; // 지도 초기화 상태 업데이트
      };
    }
  };
  </script>
  
  
  
  <style>
  @import "../assets/css/search.css";
  
  
  </style>