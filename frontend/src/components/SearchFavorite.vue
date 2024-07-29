<template>
  <button id="modal-favorite-button" @click="openFavoriteModal"><i class="fas fa-list fa-2x"></i></button>
  <div class="modal-favorite-wrap" v-show="favoriteModalOpen" @click="closeFavoriteModals">
    <div class="modal-favorite-container" @click="preventClose">

      <router-link to="/"><img id="search-logo"></router-link>

      <hr class="hr-3"> 

      <div class="modal-btn">
        <router-link to="/searchresult" id="modal-search-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
          </svg>
        </router-link>
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
        <button id="favorits-button" @click="openFavModal">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16">
            <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
          </svg>
        </button>
        <!--즐겨찾기 리스트 목록 표시-->
        <div class="modal-favorits-wrap" v-show="thirdModalOpen" @click="closeFavModals">
          <div class="modal-favorits-container" @click="preventClose">
            <div class ="up-box">
              <div id="quick-buttons">
                <div v-for="index in [0, 1, 2]" :key="index" class="quick-modal-btn">
                  <button v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.some(item => item.type === index)" @click="handleUpBoxObjectClick">
                    <!-- 작은 네모 버튼 -->
                    <button class="small-square-button" @click="showNameInputModal(favoriteData.quicktype.find(item => item.type === index)?.id)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-square" viewBox="0 0 16 16">
                        <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
                      </svg>
                    </button>
                    <!-- 하트 모양 SVG -->
                    <button @click="handleButtonClick(index)">
                      <!-- 아이콘 변경 -->
                      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi" :class="getIconClass(index)" viewBox="0 0 16 16">
                        <path :d="getIconPath(favoriteData.quicktype.find(item => item.type === index)?.icon-1)"></path>
                      </svg>
                    </button>
                    <p v-if="favoriteData && favoriteData.quicktype">
                      {{ favoriteData.quicktype.find(item => item.type === index)?.name || `Type ${index} 이름 없음` }}
                    </p>
                    <!-- 작은 빨간 x 버튼 -->
                    <span class="close-btn" @click.stop="removeItem(favoriteData.quicktype.find(item => item.type === index)?.id)">×</span>
                  </button>
                  <button v-else id="first-quick" @click="showQuickSlotModal(index)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
                      <path d="..."></path>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
            <div  class="down-box1"  v-if="!isQuickButtonsClicked">
            
             <div class="modal-btn">
              <!-- 리스트 추가하기 버튼 -->
              <div class="modal-btn">
                <button id="add-list-button" @click="showListModal" class="add-list-button">
                  <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
                    <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
                  </svg>
                     새 리스트
                </button>
              </div>
              <div id="favorite-results" v-if="favoriteData && favoriteData.list">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item" v-for="favorite in favoriteData.list" :key="favorite.id">
                    <button @click="openFavoriteDetailModal(favorite)" v-if="!favorite.editMode"> 
                      <p id="name">{{ favorite.name }}</p>
                      <p id="memo">{{ favorite.memo }}</p>
                    </button>
                    <!-- 수정 모드일 때 입력 필드 표시 -->
                    <div v-else>
                      <label for="list-name-{{ favorite.id }}">이름:</label>
                      <input :value="favorite.editMode && favorite.newName === undefined ? (favorite.newName = favorite.name) : favorite.newName" @input="favorite.newName = $event.target.value">
                      <label for="list-private-{{ favorite.id }}">비공개:</label>
                      <input type="checkbox" :id="'list-private-' + favorite.id" v-model="favorite.newIsPrivate" :checked="favorite.private">
                      <label for="list-memo-{{ favorite.id }}">메모:</label>
                      <input :value="favorite.editMode && favorite.newMemo === undefined ? (favorite.newMemo = favorite.memo) : favorite.newMemo" @input="favorite.newMemo = $event.target.value">
                    </div>

                    <!-- 수정 모드 토글 버튼 -->
                    <button @click="favorite.editMode = !favorite.editMode">
                      {{ favorite.editMode ? '취소' : '수정' }}
                    </button>
                    <!-- 수정 완료 버튼 -->
                    <button v-if="favorite.editMode" @click="() => { console.log('newName:', favorite.newName, 'name:', favorite.name, 'newMemo:', favorite.newMemo); updateFavoriteName(favorite.id, favorite.newName, favorite.newIsPrivate, favorite.newMemo); }">수정 완료</button>
                    <!-- 삭제 버튼 -->
                    <button @click="deleteFavorite(favorite.id)">삭제</button>
                     <!-- 즐겨찾기 리스트 디테일 표시 -->
                      <div class="modal-btn">
                        <div class="modal-favorits-detail-wrap" v-show="thirdDetailModalOpen" @click="closeFavoriteDetailModals">
                          <div class="modal-favorits-detail-container" @click="preventClose">
                              <div id="place-details" v-if="listData">
                                <ul>
                                  <li v-for="(place, index) in listData" :key="index">
                                    <div v-if="!place.editMode">
                                      <p id="name-details" v-if="!place.editMode">{{ place.place_name }}</p>
                                      <p id="category">{{ place.category }}</p>
                                      <p id="address-details">주소: {{ place.address }}</p>
                                      <p id="isopen">영업 상태: <span :class="{ 'open': place.isopen, 'closed': !place.isopen }">{{ place.isopen ? '영업 중' : '휴무' }}</span></p>
                                    </div>
                                    <!-- 수정 모드일 때 입력 필드 표시 -->
                                    <input v-else v-model="place.newMypinName" placeholder="새로운 이름 입력">
                                    
                                    <!-- 수정 모드 토글 버튼 -->
                                    <button @click="place.editMode = !place.editMode">
                                      {{ place.editMode ? '취소' : '수정' }}
                                    </button>
                                    <!-- 수정 완료 버튼 -->
                                    <button v-if="place.editMode" @click="updateMypinName(place.mypin_id, place.newMypinName)">수정완료</button>
                                    
                                    <!-- 삭제 버튼 -->
                                    <button @click="deletePlace(place.mypin_id)">삭제</button>
                                  </li>
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
            
            
              <!-- 공개 리스트 표시 -->
              <div class="public-list-header">
                <h3>공개 리스트</h3>
                <button @click="showPublicFavorites = !showPublicFavorites" class="toggle-button">
                  <i :class="showPublicFavorites ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                </button>
              </div>
              <!-- 공개 리스트 표시 -->
              <div id="public-favorite-results" v-if="showPublicFavorites && favoriteData && favoriteData.public_list">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item" v-for="favorite in favoriteData.public_list" :key="favorite.id">
                    <button @click="openFavoriteDetailModal(favorite)" v-if="!favorite.editMode"> 
                      <p id="name">{{ favorite.name }}</p>
                      <p id="memo">{{ favorite.memo }}</p>
                      <p id="username"> made by. {{ favorite.username }}</p>
                      <button @click="likeFavorite(favorite.id); favorite.likes++" v-if="!favorite.liked">
                        <i class="far fa-thumbs-up"></i> 
                      </button>
                      <button @click="unlikeFavorite(favorite.id); favorite.likes--" v-else>
                        <i class="fas fa-thumbs-up" style="color: blue;"></i>
                      </button>
                      <p id="like_count">{{ favorite.likes }}</p>
                    </button>
                        <!-- 즐겨찾기 리스트 디테일 표시 -->
                        <div class="modal-btn">
                          <div class="modal-favorits-detail-wrap" v-show="thirdDetailModalOpen" @click="closeFavoriteDetailModals">
                            <div class="modal-favorits-detail-container" @click="preventClose">
                              <div id="place-details" v-if="listData">
                                <ul>
                                  <li v-for="(place, index) in listData" :key="index">
                                    <div>
                                      <p id="name-details">{{ place.place_name }}</p>
                                      <p id="category">{{ place.category }}</p>
                                      <p id="address-details">주소: {{ place.address }}</p>
                                      <p id="isopen">영업 상태: <span :class="{ 'open': place.isopen, 'closed': !place.isopen }">{{ place.isopen ? '영업 중' : '휴무' }}</span></p>
                                    </div>
                                  </li>
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

            <div class="down-box2" v-if="isQuickButtonsClicked">
              <div v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.length > 0">
                <div>
                  <div v-if="displayQuickData && quickData">
                    <!-- 기존 퀵 데이터 표시 -->
                    <p>{{ quickData.quick_name }}</p>
                    <p>{{ quickData.place_name }}</p>
                    <p>{{ quickData.address }}</p>
                    <p>{{ quickData.category }}</p>
                    <p>{{ quickData.isopen }}</p>
                  </div>
                  <div v-else-if="displayNewLocation">
                    <!-- 새 위치 데이터 표시 -->
                    <p>주소: {{ newAddress }}</p>
                  </div>
                  <div v-else>
                  
                  </div>
                </div>
              </div>
            </div>

            </div>
          </div>
        </div>
     

        <!-- 리스트 추가 모달 -->
        <div class="list-add-modal" v-show="addListModalOpen" @click="closeAddListModal">
          <div class="modal-container" @click.stop="preventClose">
            <h3>리스트 추가하기</h3>
            <div>
              <label for="list-name">리스트 이름:</label>
              <input type="text" id="list-name" v-model="newListName" placeholder="리스트 이름 입력">
            </div>
            <div>
              <label for="list-private">비공개:</label>
              <input type="checkbox" id="list-private" v-model="isListPrivate">
            </div>
            <div class="modal-btn">
              <button @click="addList">추가</button>
              <button @click="closeAddListModal">취소</button>
            </div>
          </div>
        </div>

        <!-- 마이핀 추가 모달 -->
        <div class="mypin-add-modal" v-show="AddMyPinModalOpen" @click="closeAddMyPinModal">
          <div class="modal-container" v-if="favoriteData" @click.stop="preventClose">
            <h3>리스트를 선택하세요</h3>
            <select v-model="selectedListId">
              <option v-for="list in favoriteData.list" :key="list.id" :value="list.id">{{ list.name }}</option>
            </select>
            <div>
              <label for="mypin-name">마이핀의 이름을 입력하세요:</label>
              <input type="text" v-model="mypinName" id="mypin-name" />
            </div>
            <div class="modal-btn">
              <button @click="saveMypin(selectedListId)">저장</button>
              <button @click="closeAddMyPinModal">취소</button>
            </div>
          </div>
        </div>

        <!-- 퀵슬롯 추가 모달 -->
        <div class="quick-add-modal" v-show="isQuickSlotModalOpen" @click="closeQuickSlotModal">
          <div class="modal-container" @click.stop="preventClose">
            <h3>퀵슬롯 추가하기</h3>
            <div>
              <label for="quickslot-name">퀵슬롯의 이름을 입력하세요:</label>
              <input type="text" id="quickslot-name" v-model="quickSlotName" placeholder="퀵슬롯 이름 입력">
            </div>
            <div class="modal-btn">
              <button @click="saveQuickSlot(quickSlotName, quickSlotType)">추가</button>
              <button @click="closeQuickSlotModal">취소</button>
            </div>
          </div>
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
      isQuickButtonsClicked: false,
      showPublicFavorites:false,  // 공개 리스트 표시 토글
      addListModalOpen:false,   // 새 리스트 추가 모달
      isQuickSlotModalOpen: false, // 퀵슬롯 추가 모달
      quickSlotName:'',   //새 퀵슬롯 이름 
      quickSlotType:null, // 새 퀵슬롯 타입
      AddMyPinModalOpen: false,  // 마이핀 추가 모달
      selectedListId: null,   // 마이핀 추가 시 선택된 리스트
      mypinName: '',    // 마이핀 추가 이름
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
      openFavModal() {
        this.thirdModalOpen = true;
        this.closeModalsExcept('thirdModalOpen');
        this.isQuickButtonsClicked = false;
      },
      // 즐겨찾기 리스트 디테일
      openFavoriteDetailModal(result) {
        console.log(result)
        this.fetchlistData(result.id)//id값으로 장소데이터 불러오기
        this.thirdDetailModalOpen = true;
        this.closeModalsExcept('thirdDetailModalOpen');
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
      closeFavModals() {
        this.favoriteModalOpen = true;
        this.thirdModalOpen = false;
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
        axios.post('http://localhost:8000/user/api/token/', loginData)
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
      axios.get(`http://localhost:8000/favorites`, {
        headers: {
            // Bearer 스키마를 사용하여 토큰을 전송
            'Authorization': `Bearer ${userToken}`
          }
      })  // PinPlaceAPIView에서 데이터 가져오기
        .then(response => {
          this.favoriteData = response.data;
          // 사용자의 ListLike 데이터 요청
          return axios.get(`http://localhost:8000/favorites/like`, {
            headers: {
              'Authorization': `Bearer ${userToken}`
            }
          });
        })
        .then(likeResponse => {
          if (likeResponse.data.length === 0) {
            this.favoriteData.public_list.forEach(favorite => {
              favorite.liked = false; // 데이터가 없으면 모든 liked 속성을 false로 설정
            });
          } else {
            const likedListIds = likeResponse.data.map(like => like.list); // 사용자의 liked 리스트 ID 배열
            console.log(likedListIds, likeResponse.data);
            // public_list의 각 항목에 liked 속성 추가
            this.favoriteData.public_list.forEach(favorite => {
              favorite.liked = likedListIds.includes(favorite.id); // ID가 포함되면 true, 아니면 false
            });
          }
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
      axios.get(`http://localhost:8000/favorites/list/${id}/`, {
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
      this.addListModalOpen = true; // 모달 열기
    },
    closeAddListModal() {
      this.addListModalOpen = false; // 모달 닫기
    },
    // 리스트 추가 요청 
    async addList() {
      const userToken = localStorage.getItem('userToken');
      try {
        const response = await axios.post('http://localhost:8000/favorites/list/create/', {
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
        this.closeAddListModal();
      } catch (error) {
        console.error('Error adding list:', error);
      }
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

      axios.put(`http://localhost:8000/favorites/list/update/${id}/`, {
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
      axios.put(`http://localhost:8000/favorites/mypin/update/${id}/`, {
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
      axios.delete(`http://localhost:8000/favorites/mypin/delete/${id}/`, {
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
    showAddMyPinModal(latitude, longitude) {
      // 리스트 데이터를 가져와서 모달에 표시
      
      if (this.favoriteData && this.favoriteData.list && this.favoriteData.list.length > 0) {
        this.AddMyPinModalOpen = true; // 모달 열기
        this.newLatitude = latitude; // 위도 저장
        this.newLongitude = longitude; // 경도 저장
      } else {
        console.error('No favorite lists found');
      }
      
    },
    // 마이핀 추가 리스트 선택 모달 닫기
    closeAddMyPinModal() {
      this.AddMyPinModalOpen = false; // 모달 닫기
      this.selectedListId = null; // 선택된 리스트 초기화
      this.mypinName = ''; // 마이핀 이름 초기화
    },
  
    // 마이핀 저장 메서드
    saveMypin(listId) {
      const userToken = localStorage.getItem('userToken');
      // console.log(address, latitude, longitude)
      axios.post(`http://localhost:8000/favorites/mypin/create/${listId}/`, {
        address: this.newAddress, // 주소 문자열을 전송
        latitude: Number(this.newLatitude.toFixed(6)),
        longitude: Number(this.newLongitude.toFixed(6)),
        list: listId,
        name: this.mypinName,
        menu: null, // 필요에 따라 추가
        phone: null, // 필요에 따라 추가
        memo: "마이핀 추가", // 필요에 따라 추가
        category: '기타', // 필요에 따라 추가
        new_place: true,
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
    this.quickSlotType = type; // 퀵슬롯 타입 저장
    this.isQuickSlotModalOpen = true; // 모달 열기
  },
  closeQuickSlotModal() {
      this.isQuickSlotModalOpen = false; // 모달 닫기
      this.quickSlotName = ''; // 입력 필드 초기화
    },

  // 퀵슬롯 추가 요청 메서드
  saveQuickSlot(name,type) {
    const userToken = localStorage.getItem('userToken');
    console.log(this.newLatitude,this.newLongitude,this.newAddress)
    axios.post(`http://localhost:8000/favorites/quick/create/`, {
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
      this.closeQuickSlotModal(); // 모달 닫기
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
    axios.delete(`http://localhost:8000/favorites/quick/delete/${id}/`, {
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
  axios.put(`http://localhost:8000/favorites/quick/update/${id}/`, {
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
    axios.get(`http://localhost:8000/favorites/quick/${id}/`, {
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
  handleUpBoxObjectClick() {
      this.isQuickButtonsClicked = true;
    },
  // 리스트 좋아요 메서드
  likeFavorite(listId) {
    // liked 상태를 즉시 업데이트
    const favorite = this.favoriteData.public_list.find(fav => fav.id === listId);
    if (favorite) {
      favorite.liked = true; // 좋아요 상태로 변경
    }

    const userToken = localStorage.getItem('userToken');
    console.log(listId);
    axios.post(`http://localhost:8000/favorites/list/like/`, {
      list: listId
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
      // 에러 발생 시 원래 상태로 되돌리기
      if (favorite) {
        favorite.liked = false; // 좋아요 취소
      }
    });
  },

    // 리스트 좋아요 취소 메서드
  unlikeFavorite(listId) {
    // liked 상태를 즉시 업데이트
    const favorite = this.favoriteData.public_list.find(fav => fav.id === listId);
    if (favorite) {
      favorite.liked = false; // 좋아요 취소 상태로 변경
    }

    const userToken = localStorage.getItem('userToken');
    console.log(listId);
    axios.delete(`http://localhost:8000/favorites/list/unlike/${listId}/`, {
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
      // 에러 발생 시 원래 상태로 되돌리기
      if (favorite) {
        favorite.liked = true; // 좋아요 상태로 되돌리기
      }
    });
  },

},
  mounted() {
    // 네이버 지도 API 로드
    const script = document.createElement("script");
    script.src = "https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=" + process.env.VUE_APP_MAPURL+ "&ncpClientSecret=" + process.env.VUE_APP_MAPKEY+ "&submodules=geocoder";  // geocoder 서브모듈 추가
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
      // 지도 클릭 이벤트 추가 : 우클릭
      naver. maps.Event.addListener(this.map, 'rightclick', this.handleMapClick.bind(this));
    };

    //this.checkLoginStatus(); // 컴포넌트가 마운트될 때 로그인 상태 확인
    this.fetchFavoriteData();  // 컴포넌트가 마운트될 때 즐겨찾기 데이터 요청
    window.addQuickSlot = this.showQuickSlotModal.bind(this);  // 퀵슬롯 추가 요청
    window.addMyPin = this.showAddMyPinModal.bind(this);  // 마이핀 추가 요청
  }
};
  </script>
  
  
  <style>
  @import "../assets/css/search.css";
  
  
  </style>
