<template>
  <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
  <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
    <div class="modal-favorite-container" @click="preventClose">

      <router-link to="/"><img id="search-logo"></router-link>

      <hr class="hr-3">

      <div class="modal-btn">
        <router-link to="/searchresult" id="modal-search-button" @click="openSearchModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
          </svg>
        </router-link>
      </div>

      <hr class="hr-3">

      <div class="modal-btn" >
        <button id="nav-button" @click="openNavModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-send-fill" viewBox="0 0 16 16">
            <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471z"/>
          </svg>
        </button>

        <div class="modal-nav-wrap" v-show="secondModalOpen" @click="closeNavModals">
          <div class="modal-nav-container" @click="preventClose">
            
            <div id="directions-panel" style="width: 100%; height: 200px; overflow: auto;"></div>
            <div id="current-coords"></div>
            <div id="current-coords"></div>
  <div id="start-coords"></div>
  <div id="end-coords"></div>
  <button @click="setStartPoint">시작점 지정</button>
  <button @click="setEndPoint">도착점 지정</button>
  <button @click="handleDirectionClick(startCoords, endCoords)">길찾기</button>
  
          </div>
        </div>
      </div>

      <hr class="hr-3">

      <div class="modal-btn">
          <router-link to="/favorites" id="favorits-button"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
          <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
          </svg></router-link>
      </div>

      <hr class="hr-3">
          
      <div class="modal-btn">
        <router-link to="/history" id="history-button" @click="openHisModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
            <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
            <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
            <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
          </svg>
        </router-link>
        <div class="modal-history-wrap" v-show="fourthModalOpen" @click="closeHisModals">
          <div class="modal-history-container" @click="preventClose">
            <div class="modal-btn"></div>
          </div>
        </div>
      </div>

      <hr class="hr-3">

      </div>
  
  </div>
      <div id="main">
      <div id="search-center">
        <router-link to="/"><img id="search-logo"></router-link>
          <form id="search" @submit.prevent="navigateToSearchResult({ search: searchTerm })">
            <input type="text" v-model="searchTerm" id="search-input" placeholder="       장소를 입력하세요">
              <router-link to="/searchresult" id="search-button" @click="search"><i class="fas fa-search fa-lg"></i></router-link>
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
      thirdDetailModalOpen: false, // 즐겨찾기 리스트 디테일
      fourthModalOpen: false,
      modalOpen: false,
      searchTerm: '', //검색어
      isLoggedIn: false, // 로그인 상태
      listData: null,  // 리스트 상세 데이터
      favoriteData: null, // 즐겨찾기 데이터 
      currentMarker: null, // 현재 마커
      newLatitude: null,  // 새 마커의 위도
      newLongitude: null, // 새 마커의 경도 
      newAddress: null, // 새 마커의 주소
      quickData:null,
      newQuickSlotName: '',
      isEditModalOpen: false,
      editingQuickData: null,
      newListName: '', // 새로운 리스트 이름
      isListPrivate: false, // 리스트 공개 여부
      newListMemo: '',  // 새로운 리스트 메모
      currentCoords: null,
      startCoords: null,
      endCoords: null,
      startMarker: null,
    endMarker: null,
    polyline: null,
    };
  },
  created() {
      this.openFavModal();
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
      openNavModal() {
        this.secondModalOpen = true;
        this.closeModalsExcept('secondModalOpen');
      },
      openFavModal() {
        this.thirdModalOpen = true;
        this.closeModalsExcept('thirdModalOpen');
      },
      // 즐겨찾기 리스트 디테일
      openFavoriteDetailModal(result) {
        console.log(result)
        this.fetchlistData(result.id)//id값으로 장소데이터 불러오기
        this.thirdDetailModalOpen = true;
        this.closeModalsExcept('thirdDetailModalOpen');
      },
      openHisModal() {
        this.fourthModalOpen = true;
        this.closeModalsExcept('fourthModalOpen');
      },
      openModal() {
        this.modalOpen = true;
        this.closeModalsExcept('modalOpen');
      },
      closeFavoriteModals() {
        this.favoriteModalOpen = false;
      },
      // 즐겨찾기 리스트 디테일
      closeFavoriteDetailModals() {
        this.favoriteModalOpen = true;
        this.thirdModalOpen = true;
        this.thirdDetailModalOpen = false;
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
      closeNavModals() {
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
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
      if (exceptModal !== 'thirdDetailModalOpen') {
        if (exceptModal == 'firstModalOpen') {
          this.firstModalOpen = true;
        }
        if (exceptModal == 'firstDetailModalOpen') {
          this.firstModalOpen = true;
        }
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'modalOpen') {
          if (this.firstDetailModalOpen == 'true') {
            this.firstDetailModalOpen = true;
          }
        }
        else {
        this.thirdDetailModalOpen = false;
        }
      }
      if (exceptModal !== 'fourthModalOpen') {
        if (exceptModal == 'firstModalOpen') {
          this.firstModalOpen = true;
        }
        if (exceptModal == 'firstDetailModalOpen') {
          this.firstModalOpen = true;
        }
        if (exceptModal == 'thirdModalOpen') {
          this.thirdModalOpen = true;
        }
        if (exceptModal == 'thirdDetailModalOpen') {
          this.thirdModalOpen = true;
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
      // 검색어를 searchresult로 전달
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
      },
  
    // 로그인 요청
    login() {
        const loginData = {
          username: this.loginId,
          password: this.loginPassword,
        };
        axios.post('http://15.165.119.226/user/api/token/', loginData)
          .then(response => {
          console.log(response.data.access);
          localStorage.setItem('userToken', response.data.access); // 토큰 저장
          this.isLoggedIn = true; // 로그인 상태 업데이트
          this.modalOpen = false; // 로그인 성공 후 모달 닫기
          window.location.reload();
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
  
    // 즐겨찾기 기본 화면 (리스트, 퀵슬롯) 요청
    fetchFavoriteData(id) {
      console.log(`Fetching list data for ID: ${id}`);
      const userToken = localStorage.getItem('userToken');
      console.log(userToken)
      axios.get(`http://15.165.119.226/favorites`, {
        headers: {
            // Bearer 스키마를 사용하여 토큰을 전송
            'Authorization': `Bearer ${userToken}`
          }
      })  // PinPlaceAPIView에서 데이터 가져오기
        .then(response => {
          this.favoriteData = response.data;
          console.log('Response data:', response.data);  // 응답 데이터 로그 추가
        })
        .catch(error => {
          console.error("There was an error fetching the list data!", error);
        });
    },
  
    // 마커를 추가하는 메서드
    addMarker(latitude, longitude, placeInfo) {
      console.log('addMarker');
      var marker = new naver.maps.Marker({
        position: new naver.maps.LatLng(latitude, longitude),
        map: this.map
      });
  
      // 마커의 위치를 LatLngBounds 객체에 추가
      this.bounds.extend(marker.getPosition());
  
      // 정보창 내용 설정
      var contentString = [
        '<div class="iw_inner">',
        `   <h3>${placeInfo.mypin_name}</h3>`,
        `   <p>장소 이름: ${placeInfo.place_name}<br />`,
        `   주소: ${placeInfo.address}<br />`,
        `   카테고리: ${placeInfo.category}<br />`,
        `   영업 상태: ${placeInfo.isopen ? '영업 중' : '휴무'}<br />`,
        `   리스트 이름: ${placeInfo.list_name}</p>`,
        '</div>'
      ].join('');
  
      var infowindow = new naver.maps.InfoWindow({
        content: contentString
      });
  
      // 마커 클릭 이벤트 추가
      naver.maps.Event.addListener(marker, "click", function(e) {
        if (infowindow.getMap()) {
          infowindow.close();
        } else {
          infowindow.open(this.map, marker);
        }
      }.bind(this));
    },
    
    // 모든 마커가 추가된 후 지도의 중심을 재설정하는 메서드
    adjustMapCenter() {
      this.map.fitBounds(this.bounds); // 지도의 중심과 줌 레벨을 조정
    },
  
    // 각 리스트 상세 정보 요청
    fetchlistData(id) {
      console.log(`Fetching place data for ID: ${id}`);
      const userToken = localStorage.getItem('userToken');
      console.log(userToken);
      axios.get(`http://15.165.119.226/favorites/list/${id}/`, {
        headers: {
          'Authorization': `Bearer ${userToken}`
        }
      })
      .then(response => {
        this.listData = response.data.MyPin;
        console.log(this.listData)
        this.listData.forEach(place => {
            console.log(place.latitude, place.longitude, place);
            this.addMarker(place.latitude, place.longitude, place);
        });
        this.adjustMapCenter(); // 지도의 중심을 마커들의 중심으로 조정
        console.log('Response data:', response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the place data!", error);
      });
      },
  
      // 리스트 목록에서 하나의 리스트 클릭하면 해당 리스트의 상세 정보 요청
      handleFavoriteClick(id) {
        // 여기에서 fetchlistData 함수를 호출하고, favorite.id를 인자로 전달합니다.
        this.fetchlistData(id);
      },

    // 리스트 추가 모달
    showListModal() {
      const listAddHtml = `
        <div>
          <h3>리스트 추가하기</h3>
          <div>
            <label for="list-name">리스트 이름:</label>
            <input type="text" id="list-name" placeholder="리스트 이름 입력">
          </div>
          <div>
            <label for="list-private">비공개:</label>
            <input type="checkbox" id="list-private">
          </div>
          <div>
            <label for="list-memo">메모: </label>
            <input type="text" id="list-memo" placeholder="리스트에 대한 설명을 적어주세요.">
          </div>
          <button id="add-list">추가</button>
          <button id="cancel-add-list">취소</button>
        </div>
      `;

      const modal = document.createElement('div');
      modal.innerHTML = listAddHtml;
      document.body.appendChild(modal);

      document.getElementById('add-list').addEventListener('click', () => {
        this.newListName = document.getElementById('list-name').value;
        this.isListPrivate = document.getElementById('list-private').checked;
        this.newListMemo = document.getElementById('list-memo').value;
        this.addList();
        document.body.removeChild(modal); // 모달 제거
      });

      document.getElementById('cancel-add-list').addEventListener('click', () => {
        document.body.removeChild(modal); // 모달 제거
      });
    },
    // 리스트 추가 요청 
    async addList() {
      const userToken = localStorage.getItem('userToken');
      try {
        const response = await axios.post('http://15.165.119.226/favorites/list/create/', {
          name: this.newListName,
          private: this.isListPrivate,
          memo: this.newListMemo,
        }, {
          headers: {
            'Authorization': `Bearer ${userToken}`,
            'Content-Type': 'application/json'
          }
        });
        console.log('List added:', response.data);
        // 리스트 추가 후 데이터 갱신
        this.fetchFavoriteData();
      } catch (error) {
        console.error('Error adding list:', error);
      }
    },
      
    // 각 리스트 삭제 요청
    deleteFavorite(id) {
      console.log(`Deleting list data for ID: ${id}`);
      const userToken = localStorage.getItem('userToken');
      console.log(userToken);
      axios.delete(`http://15.165.119.226/favorites/list/delete/${id}/`, {
        headers: {
          'Authorization': `Bearer ${userToken}`
        }
      })
      .then(response => {
        console.log('Response status:', response.status);
        // 페이지 리로드
        window.location.reload();
      })
      .catch(error => {
        console.error("There was an error fetching the place data!", error);
      });
      },
  
    // 각 리스트 수정 요청
    updateFavoriteName(id, newName, newIsPrivate, newMemo) {
      console.log(`Updating favorite ${id} with new name ${newName}`);
      const userToken = localStorage.getItem('userToken');
      console.log(userToken);
      console.log(newName, newIsPrivate);
      if (newIsPrivate == null) {
        newIsPrivate = false;
      }

      axios.put(`http://15.165.119.226/favorites/list/update/${id}/`, {
        name: newName, // 수정할 리스트 이름을 요청 본문에 포함
        private: newIsPrivate,
        memo:newMemo,
      }, {
        headers: {
          'Authorization': `Bearer ${userToken}`
        }
      })
      .then(response => {
        console.log('Response status:', response.status);
        // 페이지 리로드
        window.location.reload();
      })
      .catch(error => {
        console.error("There was an error fetching the place data!", error);
      });
      },
    
    // 마이핀 이름 수정 요청
    updateMypinName(id, newMypinName) {
      console.log(`Updating mypin_name for place ${id} with new name ${newMypinName}`);
      const userToken = localStorage.getItem('userToken');
      axios.put(`http://15.165.119.226/favorites/mypin/update/${id}/`, {
        name: newMypinName
      }, {
        headers: {
          'Authorization': `Bearer ${userToken}`
        }
      })
      .then(response => {
        console.log('Response status:', response.status);
        // 페이지 리로드
        window.location.reload();
      })
      .catch(error => {
        console.error("There was an error updating the mypin_name!", error);
      });
    },
  
    //마이핀 삭제 요청
    deletePlace(id) {
      // 서버에 삭제 요청 보내기
      console.log(`Deleting place ${id}`);
      const userToken = localStorage.getItem('userToken');
      axios.delete(`http://15.165.119.226/favorites/mypin/delete/${id}/`, {
        headers: {
          'Authorization': `Bearer ${userToken}`
        }
      })
      .then(response => {
        console.log('Response status:', response.status);
        // 성공적으로 삭제되었을 때의 로직
        // 페이지 리로드
        window.location.reload();
      })
      .catch(error => {
        console.error("There was an error deleting the place!", error);
      });
    },
    
    // 새로운 장소를 클릭했을 때 마커를 추가하는 메서드
    addNewMarker(latitude, longitude) {
      console.log('addNewMarker');
  
      // 기존 마커 있으면 제거 
      if (this.currentMarker) {
        this.currentMarker.setMap(null);
      }
  
      var marker = new naver.maps.Marker({
        position: new naver.maps.LatLng(latitude, longitude),
        map: this.map
      });
  
      //현재 마커 저장
      this.currentMarker = marker;
  
      console.log(this.currentMarker);
  
      // 정보창 내용 설정
      var infowindow = new naver.maps.InfoWindow();
  
      // 클릭한 위치의 주소를 가져와서 정보창 내용 업데이트 (퀵슬롯 추가 / 마이핀 추가 선택)
      this.getAddressFromCoords(latitude, longitude, (address) => {
        var contentString = [
          '<div class="iw_inner">',
          `   <h3>새 장소</h3>`,
          `   <p>장소 이름: 클릭한 장소<br />`,
          `   주소: ${address}<br />`,
          `   카테고리: 알 수 없음<br />`,
          `   영업 상태: 영업 중<br />`,
          `   리스트 이름: 기본 리스트</p>`,
          `   <button onclick="window.addQuickSlot(${latitude}, ${longitude}, '${address}')">퀵슬롯 추가</button>`,
          `   <button onclick="window.addMyPin(${latitude}, ${longitude}, '${address}')">마이핀 추가</button>`,
          '</div>'
        ].join('');
  
        infowindow.setContent(contentString);
  
        // 새 주소, 위도, 경도 저장 
        this.newAddress = address;
        this.newLatitude = latitude;
        this.newLongitude = longitude;  
  
        console.log(this.newAddress, this.newLatitude, this.newLongitude);
      });
  
      // 마커 클릭 이벤트 추가
      naver.maps.Event.addListener(marker, "click", function(e) {
        if (infowindow.getMap()) {
          infowindow.close();
        } else {
          infowindow.open(this.map, marker);
        }
      }.bind(this));
  
    },
  
    // 좌표를 주소로 변환하는 메서드
    getAddressFromCoords(latitude, longitude, callback) {
      const latlng = new naver.maps.LatLng(latitude, longitude);
      naver.maps.Service.reverseGeocode({
        coords: latlng,
        orders: [
          naver.maps.Service.OrderType.ADDR,
          naver.maps.Service.OrderType.ROAD_ADDR
        ].join(',')
      }, function(status, response) {
        if (status === naver.maps.Service.Status.ERROR) {
          console.error('Reverse geocoding failed:', status);
          callback('알 수 없음');
          return;
        }
  
        setTimeout(() => {
          const items = response.v2.addresses;
          let address;
          console.log('Response:', response.v2.addresses); // 응답 데이터 출력
          console.log('Items:', items); // items 변수 출력
          if (items && items.length > 0) {
            const address = items[0].roadAddress || items[0].jibunAddress;
            callback(address);
          } else {
            console.error('No addresses found');
            console.log('Response:', response.v2.address); // 응답 데이터 출력
            const items = response.v2.address;
            console.log(items);
            address = items.roadAddress || items.jibunAddress;
            console.log(address)
            callback(address);
          }
        }, 200); // 100ms 지연 추가
        
      });
    },
  
    // 마이핀 리스트 선택 모달을 표시하는 메서드
    showListSelectionModal(latitude, longitude) {
      // 리스트 데이터를 가져와서 모달에 표시
      if (this.favoriteData && this.favoriteData.list && this.favoriteData.list.length > 0) {
        const listOptions = this.favoriteData.list.map(list => `<option value="${list.id}">${list.name}</option>`).join('');
        const listSelectHtml = `
          <div>
            <label for="list-select">리스트를 선택하세요:</label>
            <select id="list-select">${listOptions}</select>
          </div>
          <div>
            <label for="mypin-name">마이핀의 이름을 입력하세요:</label>
            <input type="text" id="mypin-name" />
          </div>
          <button id="save-mypin">저장</button>
        `;
  

        const modal = document.createElement('div');
        modal.innerHTML = listSelectHtml;
        document.body.appendChild(modal);
  
        document.getElementById('save-mypin').addEventListener('click', () => {
          const listId = document.getElementById('list-select').value;
          const name = document.getElementById('mypin-name').value;
          this.getAddressFromCoords(latitude, longitude, (address) => {
            this.saveMypin(Number(latitude.toFixed(6)), Number(longitude.toFixed(6)), address, listId, name);
            document.body.removeChild(modal); // 모달 제거
          });
        });
      } else {
        console.error('No favorite lists found');
      }
    },
  
    // 마이핀 저장 메서드
    saveMypin(latitude, longitude, address, listId, name) {
      const userToken = localStorage.getItem('userToken');
      console.log(address, latitude, longitude)
      axios.post(`http://15.165.119.226/favorites/mypin/create/${listId}/`, {
        address: address, // 주소 문자열을 전송
        latitude: latitude,
        longitude: longitude,
        list: listId,
        name: name,
        menu: null, // 필요에 따라 추가
        phone: null, // 필요에 따라 추가
        memo: "마이핀 추가", // 필요에 따라 추가
        category: '기타' // 필요에 따라 추가
      }, {
        headers: {
          'Authorization': `Bearer ${userToken}`,
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        console.log('Mypin saved:', response.data);
        // 페이지 리로드
        window.location.reload();
      })
      .catch(error => {
        console.error('Error saving mypin:', error);
      });
    },
    showQuickSlotModal(type) {
    
    const quickSlotHtml = `
      <div>
        <label for="quickslot-name">퀵슬롯의 이름을 입력하세요:</label>
        <input type="text" id="quickslot-name" />
      </div>
      <button id="save-quickslot">저장</button>
    `;
      
    const modal = document.createElement('div');
    modal.innerHTML = quickSlotHtml;
    document.body.appendChild(modal);

    document.getElementById('save-quickslot').addEventListener('click', () => {
      const name = document.getElementById('quickslot-name').value;
      this.saveQuickSlot(name,type);
      document.body.removeChild(modal); // 모달 제거
    });
  },


  // 퀵슬롯 추가 요청 메서드
  saveQuickSlot(name,type) {
    const userToken = localStorage.getItem('userToken');
    console.log(this.newLatitude,this.newLongitude,this.newAddress)
    axios.post(`http://15.165.119.226/favorites/quick/create/`, {
      address: this.newAddress, // 주소 문자열을 전송
      latitude: Number(this.newLatitude.toFixed(6)),
      longitude: Number(this.newLongitude.toFixed(6)),
      name: name,
      menu: null, // 필요에 따라 추가
      phone: null, // 필요에 따라 추가
      memo: "퀵슬롯 추가", // 필요에 따라 추가
      category: '기타', // 필요에 따라 추가
      type:type
    }, {
      headers: {
        'Authorization': `Bearer ${userToken}`,
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      console.log('QuickSlot saved:', response.data);
    })
    .catch(error => {
      console.error('Error saving quickslot:', error);
    });
  },

  // 지도 클릭 이벤트 처리 메서드
  handleMapClick(e) {
    const latitude = e.coord.lat();
    const longitude = e.coord.lng();
    console.log(`Map clicked at: ${latitude}, ${longitude}`);

    // 클릭한 위치에 새로운 마커 추가
    this.addNewMarker(latitude, longitude);
  },
openEditModal(quickData) {
    this.editingQuickData = {...quickData}; // 현재 퀵 데이터를 복사하여 저장
    this.isEditModalOpen = true; // 수정 모달 열기
  },
  removeItem(id) {
    axios.delete(`http://15.165.119.226/favorites/quick/delete/${id}/`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('userToken')}`
      }
    })
    .then(response => {
      console.log('Item deleted successfully:', response);
      // 성공적으로 삭제 후 UI 업데이트 또는 알림
      this.updateUIAfterDeletion(id);
    })
    .catch(error => {
      console.error('Error deleting item:', error);
      // 에러 처리 로직
    });
  },
  updateUIAfterDeletion(deletedId) {
    // 삭제된 아이템을 UI에서 제거
    this.favoriteData.quicktype = this.favoriteData.quicktype.filter(item => item.id !== deletedId);
  },
  showNameInputModal(id) {
  const quickSlotHtml = `
  <div>
    <label for="quickslot-name">퀵슬롯의 이름을 입력하세요:</label>
    <input type="text" id="quickslot-name" />
    <div>
      <button class="icon-button" data-icon="1">
    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d='M8 3.293l-6 6V15h12v-5.707l-6-6zm0-1.414l6.707 6.707-.707.707H13v4h-2v-3H5v3H3v-4H1.414l-.707-.707L8 1.879z'/>
    </svg>
  </button>
  <button class="icon-button" data-icon="2">
    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.912 3.452-2.923 5.365-5.096 6.286-6.912.955-1.884.838-3.362.314-4.385C13.486.878 10.4.281 8.717 2.01L8 2.748zm0 0c-.319-.319-.636-.637-.717-.737-.08.1-.398.418-.717.737z"/>
    </svg>
  </button>
  <button class="icon-button" data-icon="3">
    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-building" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M6.5 7.5v-1h3v1h-3zm0 2v-1h3v1h-3zm0 2v-1h3v1h-3zm-2-4v-1h1v1h-1zm0 2v-1h1v1h-1zm0 2v-1h1v1h-1z"/>
      <path d='M15.5 1h-15C.223 1 0 1.224 0 1.5v13c0 .276.223.5.5.5H1v-1h1v1h12v-1h1v1h.5c.277 0 .5-.224.5-.5v-13c0-.276-.223-.5-.5-.5zM1 2h14v10H1V2zm1 11h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5V6H2v1zm6 0h5V6H8v1zm-6-2h5V4H2v1zm6 0h5V4H8v1z'/>
    </svg>
  </button>
    </div>
    <input type="hidden" id="quickslot-icon" />
    <button id="save-name">저장</button>
  </div>
  `;

  const modal = document.createElement('div');
  modal.innerHTML = quickSlotHtml;
  document.body.appendChild(modal);

  // 아이콘 버튼에 이벤트 리스너 추가
  document.querySelectorAll('.icon-button').forEach(button => {
    button.addEventListener('click', function() {
      const iconValue = this.getAttribute('data-icon');
      document.getElementById('quickslot-icon').value = iconValue; // 선택된 아이콘 값을 숨겨진 입력 필드에 저장
    });
  });

  document.getElementById('save-name').addEventListener('click', () => {
    const newName = document.getElementById('quickslot-name').value;
    const newIcon = document.getElementById('quickslot-icon').value;
    this.updateQuickSlotName(id, newName, newIcon);
    document.body.removeChild(modal); // 모달 제거
  });
},
  updateQuickSlotName(id) {
  const newName = document.getElementById('quickslot-name').value;
  const newIcon = document.getElementById('quickslot-icon').value; // 아이콘 값 가져오기
  const userToken = localStorage.getItem('userToken');
  axios.put(`http://15.165.119.226/favorites/quick/update/${id}/`, {
    name: newName,
    icon: newIcon // 아이콘 데이터도 전송
  }, {
    headers: {
      'Authorization': `Bearer ${userToken}`,
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    console.log('QuickSlot updated:', response.data);
    // 서버 응답이 성공적이면, 로컬 데이터를 업데이트합니다.
    this.updateLocalQuickSlotNameAndIcon(id, newName, newIcon); // 이름과 아이콘 업데이트 함수 호출
    this.$nextTick(() => {
      console.log("DOM 업데이트 후 실행되는 코드");
    });
  })
  .catch(error => {
    console.error('Error updating QuickSlot:', error);
  });
},

updateLocalQuickSlotNameAndIcon(id, newName, newIcon) {
  const quickSlot = this.favoriteData.quicktype.find(item => item.id === id);
  if (quickSlot) {
    quickSlot.name = newName;
    quickSlot.icon = newIcon; // 아이콘 데이터도 업데이트
    this.$forceUpdate(); // 강제로 컴포넌트를 업데이트
  }
},
  handleButtonClick(type) {
    const item = this.favoriteData.quicktype.find(item => item.type === type);
    if (item) {
      this.fetchQuickViewData(item.id);
      this.displayQuickData = true;
      this.displayNewLocation = false;
      this.$nextTick(() => {
        // DOM 업데이트 후 실행할 코드
      });
    }
  },
  fetchQuickViewData(id) {
    const userToken = localStorage.getItem('userToken');
    axios.get(`http://15.165.119.226/favorites/quick/${id}/`, {
  headers: {
    'Authorization': `Bearer ${userToken}`
  }
})
      .then(response => {
        this.quickData = response.data; // 데이터 업데이트
        this.$forceUpdate(); // 강제로 컴포넌트를 업데이트
      })
      .catch(error => {
        console.error("There was an error fetching the QuickView data!", error);
      });
  },
  getIconClass(index) {
    const icon = this.favoriteData.quicktype.find(item => item.type === index)?.icon;
    switch (icon) {
      case 1: return 'bi-house-fill';
      case 2: return 'bi-heart-fill';
      case 3: return 'bi-building';
      default: return ''; // 기본값 혹은 에러 처리
    }
  },
  getIconPath(index) {
    const icon = this.favoriteData.quicktype.find(item => item.type === index)?.icon;
    switch (icon) {
      case 1:
        return 'M8 3.293l-6 6V15h12v-5.707l-6-6zm0-1.414l6.707 6.707-.707.707H13v4h-2v-3H5v3H3v-4H1.414l-.707-.707L8 1.879z'; // 집 모양 SVG path
      case 2:
        return 'M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.912 3.452-2.923 5.365-5.096 6.286-6.912.955-1.884.838-3.362.314-4.385C13.486.878 10.4.281 8.717 2.01L8 2.748zm0 0c-.319-.319-.636-.637-.717-.737-.08.1-.398.418-.717.737z'; // 하트 모양 SVG path
      case 3:
        return 'M15.5 1h-15C.223 1 0 1.224 0 1.5v13c0 .276.223.5.5.5H1v-1h1v1h12v-1h1v1h.5c.277 0 .5-.224.5-.5v-13c0-.276-.223-.5-.5-.5zM1 2h14v10H1V2zm1 11h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5v-1H2v1zm6 0h5v-1H8v1zm-6-2h5V6H2v1zm6 0h5V6H8v1zm-6-2h5V4H2v1zm6 0h5V4H8v1z'; // 건물 모양 SVG path
      default:
        return ''; // 기본값 혹은 에러 처리
    }
  },
  async handleDirectionClick(startCoords, endCoords) {
  // 이전 경로 제거
  if (this.polyline) {
    this.polyline.setMap(null);
  }

  const url = 'http://localhost:8000/searchengine/api/map-direction/';
  const params = {
    start: `${startCoords.lng},${startCoords.lat}`,
    goal: `${endCoords.lng},${endCoords.lat}`,
    option: 'traoptimal'
  };

  try {
    const response = await axios.get(url, { params });

    if (response.data.route.traoptimal) {
      const route = response.data.route.traoptimal[0].path;
      const path = route.map(coord => new naver.maps.LatLng(coord[1], coord[0]));

      // 경로 생성
      this.polyline = new naver.maps.Polyline({
        map: this.map,
        path: path,
        strokeColor: '#5347AA',
        strokeWeight: 5
      });

      this.map.setCenter(path[0]);
    } else {
      console.error('Traoptimal data is undefined');
    }
  } catch (error) {
    console.error('Directions request failed due to ', error);
  }
},
setStartPoint() {
    // 이전 시작점 마커 제거
    if (this.startMarker) {
      this.startMarker.setMap(null);
    }

    this.startCoords = this.currentCoords;
    document.getElementById('start-coords').innerText = `시작점: 위도 ${this.startCoords.lat}, 경도 ${this.startCoords.lng}`;

    // 빨간색 마커 생성
    this.startMarker = new naver.maps.Marker({
      position: new naver.maps.LatLng(this.startCoords.lat, this.startCoords.lng),
      map: this.map,
      icon: {
        content: '<svg width="20" height="20" viewBox="0 0 20 20" fill="red"><path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 10 20 10 20C10 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM10 15C8.34 15 7 13.66 7 12C7 10.34 8.34 9 10 9C11.66 9 13 10.34 13 12C13 13.66 11.66 15 10 15Z"></path></svg>',
        anchor: new naver.maps.Point(10, 10),
      },
      
    });
  },
  setEndPoint() {
    // 이전 도착점 마커 제거
    if (this.endMarker) {
      this.endMarker.setMap(null);
    }

    this.endCoords = this.currentCoords;
    document.getElementById('end-coords').innerText = `도착점: 위도 ${this.endCoords.lat}, 경도 ${this.endCoords.lng}`;

    // 파란색 마커 생성
    this.endMarker = new naver.maps.Marker({
      position: new naver.maps.LatLng(this.endCoords.lat, this.endCoords.lng),
      map: this.map,
      icon: {
        content: '<svg width="20" height="20" viewBox="0 0 20 20" fill="blue"><path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 10 20 10 20C10 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM10 15C8.34 15 7 13.66 7 12C7 10.34 8.34 9 10 9C11.66 9 13 10.34 13 12C13 13.66 11.66 15 10 15Z"></path></svg>',
        anchor: new naver.maps.Point(10, 10),
      },
    });
  },
  handleMapClick(e) {
    const latlng = e.coord;
    this.currentCoords = { lat: latlng._lat, lng: latlng._lng };
    document.getElementById('current-coords').innerText = `위도: ${latlng._lat}, 경도: ${latlng._lng}`;
  },

},
mounted() {
  const script = document.createElement("script");
  script.src = "https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=" + process.env.VUE_APP_MAPURL+ "&ncpClientSecret=" + process.env.VUE_APP_MAPKEY+ "&submodules=geocoder,directions"; // directions 서브모듈 추가
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
    this.bounds = new naver.maps.LatLngBounds();
    naver.maps.Event.addListener(this.map, 'rightclick', this.handleMapClick.bind(this));
  };

  this.fetchFavoriteData();
  window.addQuickSlot = this.showQuickSlotModal.bind(this);
  window.addMyPin = this.showListSelectionModal.bind(this);
}
};
  </script>
  
  
  <style>
  @import "../assets/css/search.css";
  
  
  </style>