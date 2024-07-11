<template>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
    integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
    crossorigin="anonymous" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
    <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
    <div class="modal-favorite-container" @click="preventClose">

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
        <button id="favorits-button" @click="openFavModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
        <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
        </svg></button>
        <div class="modal-favorits-wrap" v-show="thirdModalOpen" @click="closeFavModals">
        <div class="modal-favorits-container" @click="preventClose">
        <div>
          <!-- listData가 있을 경우 listData를 띄우기 -->
          <div v-if="listData && listData.length > 0">
            <ul>
              <li v-for="(place, index) in listData" :key="index">
                <h3 v-if="!place.editMode">{{ place.mypin_name }}</h3>
                <!-- 수정 모드일 때 입력 필드 표시 -->
                <input v-else v-model="place.newMypinName" placeholder="새로운 이름 입력">
                
                <!-- 수정 모드 토글 버튼 -->
                <button @click="place.editMode = !place.editMode">
                  {{ place.editMode ? '취소' : '수정' }}
                </button>
                
                <!-- 수정 완료 버튼 -->
                <button v-if="place.editMode" @click="updateMypinName(place.mypin_id, place.newMypinName)">수정 완료</button>
                
                <!-- 삭제 버튼 -->
                <button @click="deletePlace(place.mypin_id)">삭제</button>
                
                <p>장소 이름: {{ place.place_name }}</p>
                <p>주소: {{ place.address }}</p>
                <p>카테고리: {{ place.category }}</p>
                <p>영업 상태: <span :class="{ 'open': place.isopen, 'closed': !place.isopen }">{{ place.isopen ? '영업 중' : '휴무' }}</span></p>
                <p>리스트 이름: {{ place.list_name }}</p>
              </li>
            </ul>
          </div>
          <!-- listData가 없고 favoriteData만 있을 경우 favoriteData를 띄우기 -->
          <div v-else-if="favoriteData && favoriteData.list && favoriteData.list.length > 0">
            <ul>
              <li v-for="favorite in favoriteData.list" :key="favorite.id">
                <!-- 리스트 상세 표시 -->
                <button @click="handleFavoriteClick(favorite.id)" v-if="!favorite.editMode">{{ favorite.name }}</button>

                <!-- 수정 모드일 때 입력 필드 표시 -->
                <input v-else v-model="favorite.newName" placeholder="새로운 이름 입력">
                
                <!-- 수정 모드 토글 버튼 -->
                <button @click="favorite.editMode = !favorite.editMode">
                  {{ favorite.editMode ? '취소' : '수정' }}
                </button>
                
                <!-- 수정 완료 버튼 -->
                <button v-if="favorite.editMode" @click="updateFavoriteName(favorite.id, favorite.newName)">수정 완료</button>
                
                <!-- 삭제 버튼 -->
                <button @click="deleteFavorite(favorite.id)">삭제</button>
              </li>
            </ul>
          </div>
          <!-- 둘 다 없을 경우 메시지 표시 -->
          <div v-else>
            <p>장소 정보가 없습니다.</p>
          </div>
        </div>
        <div class="modal-btn"></div>
        
        </div>
        </div>
        </div>

        <div class="modal-btn">
        <button id="history-button" @click="openHisModal"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
        <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
        <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
        <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
        </svg></button>
        <div class="modal-history-wrap" v-show="fourthModalOpen" @click="closeHisModals">
        <div class="modal-history-container" @click="preventClose">
            <div class="modal-btn"></div>
        
        </div>
        </div>
        </div>
        
    </div>
    </div>


    <div id="main">
    <div id="search-center">
        <img id="search-logo">
        <form id="search">
          <input type="text" id="search-input" placeholder="       장소를 입력하세요">
            <button id="search-button"><i class="fas fa-search fa-lg"></i></button>
        </form>
    </div>
    </div>
    <button id="modal-button" @click="openModal"><i class="fas fa-user fa-2x"></i></button>
    <div class="modal-wrap" v-show="modalOpen" @click="closeModal">
    <div class="modal-container" @click="preventClose">
        
        <img id="profile">
        <div v-if="!isLoggedIn" class="modal-wrap" v-show="modalOpen" @click="modalOpen">
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
    <div id="search-map"></div>

    <!-- listData를 화면에 표시 -->
 
</template>



<script>
import axios from 'axios';

export default {
    data() {
  return {
    favoriteModalOpen: false,
    secondModalOpen: false,
    thirdModalOpen: false,
    fourthModalOpen: false,
    modalOpen: false,
    isLoggedIn: false, // 로그인 상태
    listData: null,  // 리스트 상세 데이터
    favoriteData: null, // 즐겨찾기 데이터 
  };
},
methods: {
  openFavoriteModal() {
    this.favoriteModalOpen = true;
    this.closeModalsExcept('favoriteModalOpen');
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
    this.closeModalsExcept('fourthModalOpen');
  },
  openModal() {
    this.modalOpen = true;
    this.closeModalsExcept('modalOpen');
  },
  closeFavoriteModals() {
    this.favoriteModalOpen = false;
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
    this.favoriteModalOpen = true;
    this.modalOpen = false;
  },
  preventClose(event) {
    event.stopPropagation();
  },
  closeModalsExcept(exceptModal) {
    if (exceptModal !== 'favoriteModalOpen') {
    this.favoriteModalOpen = true;
  }
  if (exceptModal !== 'secondModalOpen') {
    this.secondModalOpen = false;
  }
  if (exceptModal !== 'thirdModalOpen') {
    this.thirdModalOpen = false;
  }
  if (exceptModal !== 'fourthModalOpen') {
    this.fourthModalOpen = false;
  }
  if (exceptModal !== 'modalOpen') {
    this.modalOpen = false;
  }
  },

  // 로그인 요청
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
        this.modalOpen = false; // 로그인 성공 후 모달 닫기
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
    axios.get(`http://localhost:8000/favorites`, {
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
  addMarker(latitude, longitude) {
    console.log('addMarker')
    var marker = new naver.maps.Marker({
    position: new naver.maps.LatLng(latitude, longitude),
    map: this.map
  });
    // 마커의 위치를 LatLngBounds 객체에 추가
    this.bounds.extend(marker.getPosition());
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
    axios.get(`http://localhost:8000/favorites/list/${id}/`, {
      headers: {
        'Authorization': `Bearer ${userToken}`
      }
    })
    .then(response => {
      this.listData = response.data.MyPin;
      console.log(this.listData)
      this.listData.forEach(place => {
          console.log(place.latitude, place.longitude);
          this.addMarker(place.latitude, place.longitude);
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
    
  // 각 리스트 삭제 요청
  deleteFavorite(id) {
    console.log(`Deleting list data for ID: ${id}`);
    const userToken = localStorage.getItem('userToken');
    console.log(userToken);
    axios.delete(`http://localhost:8000/favorites/list/delete/${id}/`, {
      headers: {
        'Authorization': `Bearer ${userToken}`
      }
    })
    .then(response => {
      console.log('Response status:', response.status);
    })
    .catch(error => {
      console.error("There was an error fetching the place data!", error);
    });
    },

  // 각 리스트 수정 요청
  updateFavoriteName(id, newName) {
    console.log(`Updating favorite ${id} with new name ${newName}`);
    const userToken = localStorage.getItem('userToken');
    console.log(userToken);
    axios.put(`http://localhost:8000/favorites/list/update/${id}/`, {
      name: newName // 수정할 리스트 이름을 요청 본문에 포함
    }, {
      headers: {
        'Authorization': `Bearer ${userToken}`
      }
    })
    .then(response => {
      console.log('Response status:', response.status);
    })
    .catch(error => {
      console.error("There was an error fetching the place data!", error);
    });
    },
  
  // 마이핀 이름 수정 요청
  updateMypinName(id, newMypinName) {
    console.log(`Updating mypin_name for place ${id} with new name ${newMypinName}`);
    const userToken = localStorage.getItem('userToken');
    axios.put(`http://localhost:8000/favorites/mypin/update/${id}/`, {
      name: newMypinName
    }, {
      headers: {
        'Authorization': `Bearer ${userToken}`
      }
    })
    .then(response => {
      console.log('Response status:', response.status);
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
    axios.delete(`http://localhost:8000/favorites/mypin/delete/${id}/`, {
      headers: {
        'Authorization': `Bearer ${userToken}`
      }
    })
    .then(response => {
      console.log('Response status:', response.status);
      // 성공적으로 삭제되었을 때의 로직
    })
    .catch(error => {
      console.error("There was an error deleting the place!", error);
    });
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
        zoom: 10
      });
      // 모든 마커를 포함할 수 있는 LatLngBounds 객체 생성
      this.bounds = new naver.maps.LatLngBounds();
    };

    // this.checkLoginStatus(); // 컴포넌트가 마운트될 때 로그인 상태 확인
    this.fetchFavoriteData();  // 컴포넌트가 마운트될 때 즐겨찾기 데이터 요청
    
  }
};
</script>



<style>
@import "../assets/css/search.css";


</style>