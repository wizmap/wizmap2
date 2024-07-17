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

              <div class="modal-btn">
    
    <button v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.some(item => item.type === 0)"@click="handleButtonClick(0)">
      <!-- 작은 네모 버튼 -->
      <button class="small-square-button" @click="showNameInputModal(favoriteData.quicktype.find(item => item.type === 0)?.id)">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-square" viewBox="0 0 16 16">
          <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
        </svg>
      </button>
      <!-- 하트 모양 SVG -->
      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.912 3.452-2.923 5.365-5.096 6.286-6.912.955-1.884.838-3.362.314-4.385C13.486.878 10.4.281 8.717 2.01L8 2.748zm0 0c-.319-.319-.636-.637-.717-.737-.08.1-.398.418-.717.737z"/>
      </svg>
      <p v-if="favoriteData && favoriteData.quicktype">
      {{ favoriteData.quicktype.find(item => item.type === 0)?.name || 'Type 0 이름 없음' }}
    </p>
      <!-- 작은 빨간 x 버튼 -->
    <span class="close-btn" @click.stop="removeItem(favoriteData.quicktype.find(item => item.type === 0)?.id)">×</span>
    </button>
    <button v-else id="first-quik" @click="showQuickSlotModal(0)"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
            <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
            </svg></button></div>
             <!-- type이 1인 경우 하트 모양 버튼, 아닌 경우 기존 버튼 -->
  <div class="modal-btn">
    <button v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.some(item => item.type === 1)"@click="handleButtonClick(1)">
      <!-- 작은 네모 버튼 -->
      <button class="small-square-button" @click="showNameInputModal(favoriteData.quicktype.find(item => item.type === 1)?.id)">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-square" viewBox="0 0 16 16">
          <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
        </svg>
      </button>
      <!-- 하트 모양 SVG -->
      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.912 3.452-2.923 5.365-5.096 6.286-6.912.955-1.884.838-3.362.314-4.385C13.486.878 10.4.281 8.717 2.01L8 2.748zm0 0c-.319-.319-.636-.637-.717-.737-.08.1-.398.418-.717.737z"/>
      </svg>
      <p v-if="favoriteData && favoriteData.quicktype">
      {{ favoriteData.quicktype.find(item => item.type === 1)?.name || 'Type 1 이름 없음' }}
    </p>
      <!-- 작은 빨간 x 버튼 -->
    <span class="close-btn" @click.stop="removeItem(favoriteData.quicktype.find(item => item.type === 1)?.id)">×</span>
    </button>
    <button v-else id="second-quik" @click="showQuickSlotModal(1)"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
            <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
            </svg></button></div>
            <!-- type이 2인 경우 하트 모양 버튼, 아닌 경우 기존 버튼 -->
  <div class="modal-btn">
    <button v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.some(item => item.type === 2)"@click="handleButtonClick(2)">
      <!-- 작은 네모 버튼 -->
      <button class="small-square-button" @click="showNameInputModal(favoriteData.quicktype.find(item => item.type === 2)?.id)">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-square" viewBox="0 0 16 16">
          <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12z"/>
        </svg>
      </button>
      <!-- 하트 모양 SVG -->
      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.912 3.452-2.923 5.365-5.096 6.286-6.912.955-1.884.838-3.362.314-4.385C13.486.878 10.4.281 8.717 2.01L8 2.748zm0 0c-.319-.319-.636-.637-.717-.737-.08.1-.398.418-.717.737z"/>
      </svg>
      <p v-if="favoriteData && favoriteData.quicktype">
      {{ favoriteData.quicktype.find(item => item.type === 2)?.name || 'Type 2 이름 없음' }}
    </p>
      <!-- 작은 빨간 x 버튼 -->
    <span class="close-btn" @click.stop="removeItem(favoriteData.quicktype.find(item => item.type === 2)?.id)">×</span>
    </button>
    <button v-else id="third-quik"  @click="showQuickSlotModal(2)"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-square-dotted" viewBox="0 0 16 16">
            <path d="M2.5 0q-.25 0-.487.048l.194.98A1.5 1.5 0 0 1 2.5 1h.458V0zm2.292 0h-.917v1h.917zm1.833 0h-.917v1h.917zm1.833 0h-.916v1h.916zm1.834 0h-.917v1h.917zm1.833 0h-.917v1h.917zM13.5 0h-.458v1h.458q.151 0 .293.029l.194-.981A2.5 2.5 0 0 0 13.5 0m2.079 1.11a2.5 2.5 0 0 0-.69-.689l-.556.831q.248.167.415.415l.83-.556zM1.11.421a2.5 2.5 0 0 0-.689.69l.831.556c.11-.164.251-.305.415-.415zM16 2.5q0-.25-.048-.487l-.98.194q.027.141.028.293v.458h1zM.048 2.013A2.5 2.5 0 0 0 0 2.5v.458h1V2.5q0-.151.029-.293zM0 3.875v.917h1v-.917zm16 .917v-.917h-1v.917zM0 5.708v.917h1v-.917zm16 .917v-.917h-1v.917zM0 7.542v.916h1v-.916zm15 .916h1v-.916h-1zM0 9.375v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .916v.917h1v-.917zm16 .917v-.917h-1v.917zm-16 .917v.458q0 .25.048.487l.98-.194A1.5 1.5 0 0 1 1 13.5v-.458zm16 .458v-.458h-1v.458q0 .151-.029.293l.981.194Q16 13.75 16 13.5M.421 14.89c.183.272.417.506.69.689l.556-.831a1.5 1.5 0 0 1-.415-.415zm14.469.689c.272-.183.506-.417.689-.69l-.831-.556c-.11.164-.251.305-.415.415l.556.83zm-12.877.373Q2.25 16 2.5 16h.458v-1H2.5q-.151 0-.293-.029zM13.5 16q.25 0 .487-.048l-.194-.98A1.5 1.5 0 0 1 13.5 15h-.458v1zm-9.625 0h.917v-1h-.917zm1.833 0h.917v-1h-.917zm1.834-1v1h.916v-1zm1.833 1h.917v-1h-.917zm1.833 0h.917v-1h-.917zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3z"/>
            </svg></button> 
          </div>
        </div>

        
        <div v-if="favoriteData && favoriteData.quicktype && favoriteData.quicktype.length > 0">
          <div>
  <div v-if="displayQuickData">
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
    <p>데이터가 없습니다.</p>
  </div>
  

</div>
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
      favoriteModalOpen: true,
      firstModalOpen: false,
      firstDetailModalOpen: false,
      secondModalOpen: false,
      thirdModalOpen: false,
      fourthModalOpen: false,
      modalOpen: false,
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
      axios.post(`http://localhost:8000/favorites/mypin/create/${listId}/`, {
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

  
  updateQuickData(id, updatedData) {
  axios.put(`http://localhost:8000/favorites/quick/update/${id}/`, updatedData, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('userToken')}`,
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    console.log('Quick data updated:', response.data);
    this.isEditModalOpen = false; // 수정 모달 닫기
    // 성공적으로 수정 후의 로직 (예: 데이터 갱신)
  })
  .catch(error => {
    console.error('Error updating quick data:', error);
  });
},
deleteQuickData(quickId) {
  axios.delete(`http://localhost:8000/favorites/quick/delete/${quickId}/`, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('userToken')}`
    }
  })
  .then(() => {
    console.log('Quick data deleted successfully');
    // 여기에 성공적으로 삭제 후의 로직을 추가하세요.
  })
  .catch(error => {
    console.error('Error deleting quick data:', error);
  });
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
      <button id="save-name">저장</button>
    </div>
  `

  const modal = document.createElement('div');
  modal.innerHTML = quickSlotHtml;
  document.body.appendChild(modal);

  document.getElementById('save-name').addEventListener('click', () => {
    this.updateQuickSlotName(id);
    document.body.removeChild(modal); // 모달 제거
  });
  },
  updateQuickSlotName(id) {
  const newName = document.getElementById('quickslot-name').value;
  const userToken = localStorage.getItem('userToken');
  axios.put(`http://localhost:8000/favorites/quick/update/${id}/`, {
    name: newName
  }, {
    headers: {
      'Authorization': `Bearer ${userToken}`,
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    console.log('QuickSlot updated:', response.data);
    // 서버 응답이 성공적이면, 로컬 데이터를 업데이트합니다.
    this.updateLocalQuickSlotName(id, newName);
    this.$nextTick(() => {
      console.log("DOM 업데이트 후 실행되는 코드");
    });
  })
  .catch(error => {
    console.error('Error updating QuickSlot:', error);
  });
},
updateLocalQuickSlotName(id, newName) {
  const quickSlot = this.favoriteData.quicktype.find(item => item.id === id);
  if (quickSlot) {
    quickSlot.name = newName;
    // 강제로 컴포넌트를 업데이트하려면 아래 코드를 사용할 수 있습니다.
    this.$forceUpdate();
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
  showNewLocation() {
  this.displayQuickData = false;
  this.displayNewLocation = true;
  this.newQuickSlotName = ''; // 입력 필드 초기화
  this.$nextTick(() => {
    this.$forceUpdate();
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
    window.addMyPin = this.showListSelectionModal.bind(this);  // 마이핀 추가 요청
  }
};
  </script>
  
  
  <style>
  @import "../assets/css/search.css";
  
  
  </style>
