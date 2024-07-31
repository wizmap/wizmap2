<template>
      <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
      <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
      <div class="modal-favorite-container" @click="preventClose">

        <router-link to="/"><img id="search-logo"></router-link>

        <hr class="hr-3"> 
  
        <div class="modal-btn">
          <router-link to="/searchresult" id="modal-search-button"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
        </svg></router-link>
        </div>

        <hr class="hr-3">
  
          <div class="modal-btn">
          <router-link to="/Nav" id="nav-button" ><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-send-fill" viewBox="0 0 16 16">
          <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471z"/>
          </svg></router-link>
          <div class="modal-nav-wrap" v-show="secondModalOpen" >
          <div class="modal-quikslot-container" @click="preventClose">
          <div id = "quik-buttons">
          </div>
          </div>
          </div>
          </div>

          <hr class="hr-3">
  
          <div class="modal-btn">
          <router-link to="/favorites" id="favorits-button" @click="openFavModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
          <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
          </svg></router-link>
          </div>

          <hr class="hr-3">
  
          <div class="modal-btn">
          <button id="history-button" @click="openHisModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
          <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
          <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
          <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
          </svg></button>
          <div class="modal-history-wrap" v-show="fourthModalOpen" @click="closeHisModals">
          <div class="modal-history-container" @click="preventClose">
              <ul class="list-group list-group-flush scrollable">
                  <li class="list-group-item" v-for="history in histories" :key="history.id">
                      <span id="name" @click="navigateToSearchResult(history)">
                        {{ history.search }}
                      </span>
                      <br>
                      <span id="address">
                          {{ history.place ? `${history.place.address.address}` : '' }}
                      </span>
                      <span>
                        <button id="history-delete-button" @click="deleteHistory(history.id)">삭제</button>
                      </span>
                  </li>
              </ul>
              <nav nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center" v-if="histories.length > 0">
                  <li class="page-item">
                  <button class="page-link" @click="prevPage" :disabled="page === 1">Prev</button>
                  </li>
                  <li class="page-item">
                  <button v-for="pageNumber in pageNumbersToShow" :key="pageNumber" class="page-link" @click="fetchHistory(pageNumber)" :disabled="pageNumber === page">
                    {{ pageNumber }}
                  </button>
                  </li>
                  <li class="page-item">
                  <button class="page-link" @click="nextPage" :disabled="page === pagination.total_pages">Next</button>
                  </li>
                </ul>
              </nav>
          </div>
          </div>
          </div>

          <hr class="hr-3">
          
      </div>
      </div>
  
  
      <div id="main">
      <div id="search-center">
          <router-link to="/"><img id="search-logo"></router-link>
          <form id="search"  @submit.prevent="navigateToSearchResult({ search: searchTerm })">
            <input type="text" v-model="searchTerm" id="search-input" placeholder="       장소를 입력하세요" @focus="showHistory" @blur="hideHistory">
              <router-link to ="/searchresult" id="search-button" @click="search"><i class="fas fa-search fa-lg"></i></router-link>
          </form>
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
      placeData: null,
      searchTerm: '',
      searchResults: [],
      map: null, // 지도 객체를 저장할 변수 추가
      mapInitialized: false, // 지도 초기화 상태를 저장할 변수 추가
      markers: [], // 마커 객체를 저장할 배열 추가
      histories: [], // 검색 기록을 저장할 배열
      selectedPlace: null, // 선택된 장소의 상세 정보를 저장할 변수 추가
      pagination: {
      total_pages: 1 // 총 페이지 수 초기화
    },
      page: 1,
    };
  },
  created() {
      this.openHisModal();
    },
  computed: {
  pageNumbersToShow() {
    let pages = [];
    const totalPages = this.pagination.total_pages || 1;

    if (totalPages <= 3) {
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
    } else if (this.page === 1) {
      pages = [1, 2, 3];
    } else if (this.page === totalPages) {
      pages = [totalPages - 2, totalPages - 1, totalPages];
    } else {
      pages = [this.page - 1, this.page, this.page + 1];
    }
    return pages;
  }
},
  methods: {
    openFavoriteModal() {
      this.favoriteModalOpen = true;
      this.closeModalsExcept('favoriteModalOpen');
    },
    openHisModal() {
      this.fourthModalOpen = true;
      this.fetchHistory(); // 검색 기록 불러오기
      this.closeModalsExcept('fourthModalOpen');
    },
    closeFavoriteModals() {
      this.favoriteModalOpen = false;
    },
    closeHisModals() {
      this.favoriteModalOpen = true;
      this.fourthModalOpen = false;
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
    search() {
    this.$router.push({ name: 'SearchResult', query: { searchTerm: this.searchTerm } }); //SearchResult로 searchTerm 전달
    },
    async fetchHistory(page = 1) {
      const userToken = localStorage.getItem('userToken');
      try {
        const response = await fetch(`http://15.165.119.226:8000/history/?page=${page}`, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${userToken}`,
            'Content-Type': 'application/json'
          }
        });
        if (response.ok) {
          const data = await response.json();
          this.histories = data.results; // 검색 기록을 데이터에 저장
          this.pagination = data;
          this.pagination.total_pages = Math.ceil(data.count / 10);
          this.page = page; // 현재 페이지 업데이트
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
          const response = await fetch('http://15.165.119.226:8000/search/', {
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
        const response = await fetch(`http://15.165.119.226:8000/search/pin/${id}/`, {
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
      navigateToSearchResult(history) {
        if (history.place) {
          // 장소 ID를 쿼리 파라미터로 전달
          this.$router.push({ name: 'SearchResult', query: { placeId: history.place.id } });
        } else {
          // 검색어를 쿼리 파라미터로 전달
          this.$router.push({ name: 'SearchResult', query: { searchTerm: history.search } });
        }
      },
      async deleteHistory(id) {
        const userToken = localStorage.getItem('userToken');
        try {
          const response = await fetch(`http://15.165.119.226:8000/history/delete/${id}`, {
            method: 'DELETE',
            headers: {
              'Authorization': `Bearer ${userToken}`,
              'Content-Type': 'application/json'
            }
          });
           if (response.ok) {
          await this.fetchHistory(this.page);  // 현재 페이지 다시 로드
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
      },
    prevPage() {
      if (this.page > 1) {
        this.fetchHistory(this.page - 1);
      }
    },
    nextPage() {
      if (this.page < this.pagination.total_pages) {
        this.fetchHistory(this.page + 1);
      }
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
        let center = new window.naver.maps.LatLng(35.8858646, 128.5828924); // 기본 중심 좌표
        const storedCenter = localStorage.getItem('mapCenter');
        if (storedCenter) {
          const { lat, lng } = JSON.parse(storedCenter);
          center = new window.naver.maps.LatLng(lat, lng);
        }
        this.map = new window.naver.maps.Map("search-map", {
          center: center,
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