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
            <br />
            <div>
              <input type="password" v-model="loginPassword" id="login-password-input" placeholder="PASSWORD" />
            </div>
          </div>
          <div class="home-modal-btn">
            <button id="login-button" @click="login">login</button>
            <button id="register-button" @click="showRegisterForm">register</button>
          </div>
        </div>
      </div>
      <!-- 로그인된 경우 마이페이지 내용 표시 -->
      <div v-else class="mypage_container">
        <p>{{loginId}}님</p>
        <!-- 로그아웃 버튼 추가 -->
        <button id="logout-button" @click="logout">로그아웃</button>
        <button id="delete-account-button" @click="confirmDeleteAccount">회원탈퇴</button>
        <button id="mypage-button" @click="showMyPageModal">마이페이지</button> <!-- 여기를 수정 -->
      </div>
    </div>
  </div>

   <!-- 비밀번호 확인 모달 -->
   <div class="modal-wrap" v-show="passwordConfirmModalVisible" @click="closePasswordConfirmModal">
      <div class="modal-container" @click.stop="">
        <h2>비밀번호 확인</h2>
        <input type="password" v-model="passwordToConfirm" placeholder="비밀번호 입력" />
        <div class="modal-btn">
          <button @click="confirmPassword">확인</button>
          <button @click="closePasswordConfirmModal">취소</button>
        </div>
      </div>
    </div>

  <!-- Registration Form Modal -->
  <div class="modal-wrap" v-show="registerFormVisible" @click="closeRegisterForm">
    <div class="modal-container" @click.stop="">
      <h2>Register</h2>
      <div class="input_container">
        <div>
          <input type="text" v-model="registerId" id="register-id-input" placeholder="ID" />
        </div>
        <br />
        <div>
          <input type="password" v-model="registerPassword" id="register-password-input" placeholder="PASSWORD" />
        </div>
        <br />
        <div>
          <input type="email" v-model="registerEmail" id="register-email-input" placeholder="Email" />
        </div>
        <br />
        <div>
          <input type="text" v-model="registerPhone" id="register-phone-input" placeholder="Phone" />
        </div>
        <br />
        <div>
          <label class="gender-option">
            <input type="radio" v-model="registerGender" value="true" />
            남성
          </label>
          <label class="gender-option">
            <input type="radio" v-model="registerGender" value="false" />
            여성
          </label>
        </div>
        <br />
        <div>
          <input type="date" v-model="registerBirth" id="register-birth-input" placeholder="Birthdate" />
        </div>
      </div>
      <div class="modal-btn">
        <button id="register-submit-button" @click="register">Register</button>
        <button id="register-cancel-button" @click="closeRegisterForm">Cancel</button>
      </div>
    </div>
  </div>

  <!-- MyPage Modal -->
  <div class="modal-wrap" v-show="myPageModalVisible" @click="closeMyPageModal">
    <div class="modal-container" @click.stop="">
      <h2>My Page</h2>
      <div class="input_container">
          <!-- 비밀번호 변경 폼 -->
          <div>
            <input type="password" v-model="currentPassword" placeholder="현재 비밀번호" />
          </div>
          <br />
          <div>
            <input type="password" v-model="newPassword" placeholder="새 비밀번호" />
          </div>
          <br />
          <div>
            <input type="password" v-model="confirmNewPassword" placeholder="새 비밀번호 확인" />
          </div>
        </div>
        <div class="modal-btn">
          <button @click="changePassword">비밀번호 변경</button>
        </div>
       

        <!-- 이메일 변경 폼 -->
        <div class="input_container">
          <div>
            <input type="email" v-model="newEmail" placeholder="새 이메일" />
          </div>
          <div class="modal-btn">
            <button @click="changeEmail">이메일 변경</button>
          </div>
        </div>

         <!-- 휴대폰 번호 변경 폼 -->
        <div class="input_container">
          <div>
            <input type="text" v-model="newPhone" placeholder="새 휴대폰 번호" />
          </div>
          <div class="modal-btn">
            <button @click="changePhone">휴대폰 번호 변경</button>
          </div>
        </div>

        <div class="modal-btn">
          <button @click="closeMyPageModal">닫기</button>
        </div>
      </div>
    </div>

  <!-- 로그인 실패 모달 -->
  <div class="modal-wrap" v-if="loginFailed" @click="closeLoginFailedModal">
    <div class="modal-container" @click.stop="">
      <h2>로그인 실패</h2>
      <p>아이디 또는 비밀번호가 일치하지 않습니다.</p>
      <div class="modal-btn">
        <button @click="closeLoginFailedModal">확인</button>
      </div>
    </div>
  </div>
  <!-- 회원탈퇴 확인 모달 -->
  <div class="modal-wrap" v-if="confirmDeleteVisible" @click="closeConfirmDeleteModal">
    <div class="modal-container" @click.stop="">
      <h2>회원탈퇴 확인</h2>
      <p>정말로 회원 탈퇴하시겠습니까?</p>
      <div class="modal-btn">
        <button @click="deleteAccount">확인</button>
        <button @click="closeConfirmDeleteModal">취소</button>
      </div>
    </div>
  </div>

</template>

<style>
.gender-option input[type="radio"] {
  transform: scale(0.8); /* 라디오 버튼의 크기를 줄입니다. */
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      modalCheck: false,
      loginId: '', // 로그인 ID
      loginPassword: '', // 로그인 비밀번호
      isLoggedIn: false, // 로그인 상태
      registerFormVisible: false, // Registration form visibility
      myPageModalVisible: false, // MyPage 모달 창 표시 여부
      registerId: '', // Registration ID
      registerPassword: '', // Registration Password
      registerEmail: '', // Registration Email
      registerPhone: '', // Registration Phone
      registerGender: "true", // Registration Gender
      registerBirth: '', // Registration Birthdate
      passwordConfirmModalVisible: false, // 비밀번호 변경 확인 모달 표시 여부
      loginFailed: false, // 로그인 실패 여부
      confirmDeleteVisible: false, // 회원탈퇴 확인 모달 표시 여부
      currentPassword: '', // 현재 비밀번호
      newPassword: '', // 새로운 비밀번호
      confirmNewPassword: '', // 새로운 비밀번호 확인
      newEmail: '',
      newPhone: '',
    };
  },
  methods: {
    modalOpen() {
      this.modalCheck = !this.modalCheck;
    },
    showRegisterForm() {
      this.registerFormVisible = true;
    },
    closeRegisterForm() {
      this.registerFormVisible = false;
    },
    showPasswordConfirmModal() {
    this.passwordConfirmModalVisible = true; // 비밀번호 확인 모달을 보이게 설정
    },
    closePasswordConfirmModal() {
    this.passwordConfirmModalVisible = false; // 비밀번호 확인 모달을 숨김
    },
    showMyPageModal() {
      // 비밀번호 확인 모달을 열도록 변경
      this.showPasswordConfirmModal();
    },
    closeMyPageModal() {
      this.myPageModalVisible = false;
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
          this.loginFailed = false; // 로그인 성공 시 실패 상태를 false로 변경
        })
        .catch(error => {
          console.error("Login error:", error);
          this.loginFailed = true; // 로그인 실패 시 실패 상태를 true로 변경
        });
    },
    register() {
      const registerData = {
        username: this.registerId,
        password: this.registerPassword,
        email: this.registerEmail,
        phone: this.registerPhone,
        gender: this.registerGender,
        birth: this.registerBirth,
      };
      axios.post('http://localhost:8000/user/register/', registerData)
        .then(response => {
          console.log("Registration successful:", response.data);
          this.registerFormVisible = false; // Registration form 닫기
        })
        .catch(error => {
          console.error("Registration error:", error);
        });
    },
    checkLoginStatus() {
      // 로컬 스토리지에서 토큰 확인
      const token = localStorage.getItem('userToken');
      this.isLoggedIn = !!token; // 토큰 유무에 따라 로그인 상태 설정
    },
    logout() {
      localStorage.removeItem('userToken'); // 토큰 삭제
      this.isLoggedIn = false; // 로그인 상태 업데이트
      this.modalCheck = false; // 로그아웃 후 모달 닫기

      if (this.$route.name === 'home') {
        this.$router.push({ name: 'home' }); // Home.vue로 이동
      } else {
        this.$router.push({ name: 'SearchResult' }); // SearchResult.vue로 이동
      }
    },
    closeLoginFailedModal() {
      this.loginFailed = false;
    },
    changePassword() {
      if (this.newPassword !== this.confirmNewPassword) {
        alert("새 비밀번호가 일치하지 않습니다.");
        return;
      }
      
      const passwordData = {
        old_password: this.currentPassword,
        new_password: this.newPassword
      };
      
      axios.post('http://localhost:8000/user/change-password/', passwordData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(response => {
        alert("비밀번호가 성공적으로 변경되었습니다.");
        this.currentPassword = '';
        this.newPassword = '';
        this.confirmNewPassword = '';
      })
      .catch(error => {
        console.error("Password change error:", error);
        alert("비밀번호 변경 중 오류가 발생했습니다.");
      });
    },
    changeEmail() {
      const emailData = {
        email: this.newEmail
      };
      
      axios.post('http://localhost:8000/user/change-email/', emailData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(response => {
        alert("이메일이 성공적으로 변경되었습니다.");
        this.newEmail = '';
      })
      .catch(error => {
        console.error("Email change error:", error);
        alert("이메일 변경 중 오류가 발생했습니다.");
      });
    },
    changePhone() {
      const phoneData = {
        phone: this.newPhone
      };
      
      axios.post('http://localhost:8000/user/change-phone/', phoneData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(response => {
        alert("휴대폰 번호가 성공적으로 변경되었습니다.");
        this.newPhone = '';
      })
      .catch(error => {
        console.error("Phone change error:", error);
        alert("휴대폰 번호 변경 중 오류가 발생했습니다.");
      });
    },
    confirmPassword() {
      // 비밀번호 확인 API 엔드포인트
      axios.post('http://localhost:8000/user/check-password/', {
        password: this.passwordToConfirm
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(response => {
        // 비밀번호가 확인되면 비밀번호 확인 모달을 닫고 마이페이지 모달을 열기
        this.closePasswordConfirmModal();
        this.myPageModalVisible = true;
      })
      .catch(error => {
        console.error("Password confirmation error:", error);
        alert("비밀번호 확인 중 오류가 발생했습니다.");
      });
    },
    confirmDeleteAccount() {
      this.confirmDeleteVisible = true; // 확인 모달 표시
    },
    closeConfirmDeleteModal() {
      this.confirmDeleteVisible = false; // 확인 모달 닫기
    }
  },
  mounted() {
    this.checkLoginStatus(); // 컴포넌트가 마운트될 때 로그인 상태 확인
  }
};
</script>
  
  <style>
  @import "../assets/css/home.css";
  
  </style>