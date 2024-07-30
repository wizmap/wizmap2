<template>
  <button id="modal-button" @click="modalOpen"><i class="fas fa-user fa-2x"></i></button>

  <div class="modal-wrap" v-show="modalCheck" @click="modalOpen">
    <div class="right-modal-container" @click.stop="">
      <div v-if="!isLoggedIn" class="modal-wrap" v-show="modalCheck" @click="modalOpen">
        <div class="right-modal-container" @click.stop="">
          <!-- 로그인 폼 -->
          <div class="signin-wrapper">
            <div class="form-wrapper">
              <p class="login-modal-title">Login WIZMAP</p>
                <input type="text" v-model="loginId" class="form-field" placeholder="ID" />
                <input type="password" v-model="loginPassword" class="form-field" placeholder="PASSWORD" />
                <button class="button primary" @click="login">login</button>
                <button class="button secondary" @click="showRegisterForm">register</button>
                <p>
                  Forgot your 
                  <a id="mobile"><b>id</b></a> 
                  or  
                  <a id="desk"><b>password?</b></a>
                </p>
            </div>
          </div>
        </div>
      </div>
      <!-- 로그인된 경우 마이페이지 내용 표시 -->
      <div v-else class="mypage_container">
        <div class="form-wrapper">
          <svg xmlns="http://www.w3.org/2000/svg" width="150" height="150" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
          <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
          <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
          </svg>
        <p class="login-modal-title">{{loginId}}님</p>
        <!-- 로그아웃 버튼 추가 -->
        <button class="button primary" @click="showMyPageModal">마이페이지</button> <!-- 여기를 수정 -->
        <button class="button secondary" @click="logout">로그아웃</button>
        <p>
          Are you sure 
          <a id="withdrawal" @click="confirmDeleteAccount"><b>Withdrawal</b></a> 
          ?  
        </p>
        </div>
      </div>
    </div>
  </div>


   <!-- 비밀번호 확인 모달 -->
  <div class="modal-wrap" v-show="passwordConfirmModalVisible" @click="closePasswordConfirmModal">
    <div class="password-confirm-container" @click.stop="">
      <div class="signup-wrapper">
        <div class="form-wrapper">
            <p class="login-modal-title">Confirm Password</p>
            <input type="password" v-model="passwordToConfirm" class="form-field" placeholder="비밀번호 입력" />
            <div class="modal-btn">
              <button class="button primary" @click="confirmPassword">확인</button>
              <button class="button secondary" @click="closePasswordConfirmModal">취소</button>
            </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Registration Form Modal -->
  <div class="modal-wrap" v-show="registerFormVisible" @click="closeRegisterForm">
    <div class="right-modal-container" @click.stop="">
      <div class="signup-wrapper">
        <div class="form-wrapper">
          <p class="login-modal-title">Welcome to WIZMAP</p>
              <input type="text" v-model="registerId" class="form-field" placeholder="ID" />
              <input type="password" v-model="registerPassword" class="form-field" placeholder="PASSWORD" />
              <input type="email" v-model="registerEmail" class="form-field" placeholder="Email" />
              <input type="text" v-model="registerPhone" class="form-field" placeholder="Phone" />
              <select class="form-select form-field" aria-label="Default select example">
                <option selected>Gender</option>
                <option><input v-model="registerGender">남성</input></option>
                <option><input v-model="registerGender">여성</input></option>
              </select>
              <input type="date" v-model="registerBirth" class="form-field" placeholder="Birthdate" />
            <button class="button primary" @click="register">Register</button>
            <button class="button secondary" @click="closeRegisterForm">Cancel</button>
          </div>
        </div>
    </div>
  </div>

  <!-- MyPage Modal -->
  <div class="modal-wrap" v-show="myPageModalVisible" @click="closeMyPageModal">
    <div class="right-modal-container" @click.stop="">
      <div class="signup-wrapper">
        <div class="form-wrapper">
          <p class="login-modal-title">My Page</p>
          <br></br>
            <!-- 비밀번호 변경 폼 -->
            <h4>비밀변호 변경</h4>
              <input type="password" v-model="currentPassword" class="form-field" placeholder="현재 비밀번호" />
              <input type="password" v-model="newPassword" class="form-field" placeholder="새 비밀번호" />
              <input type="password" v-model="confirmNewPassword" class="form-field" placeholder="새 비밀번호 확인" />
              <button class="button primary" @click="changePassword">비밀번호 변경</button>

          <!-- 이메일 변경 폼 -->
            <h4>이메일 변경</h4>
              <input type="email" v-model="newEmail" class="form-field" placeholder="새 이메일" />
              <button class="button primary" @click="changeEmail">이메일 변경</button>
        
          <!-- 휴대폰 번호 변경 폼 -->
            <h4>휴대폰 번호 변경</h4>
              <input type="text" v-model="newPhone" class="form-field" placeholder="새 휴대폰 번호" />
              <button class="button primary" @click="changePhone">휴대폰 번호 변경</button>
              <p>
                <br></br>
                변경이 완료되었다면 닫기를 눌러주세요.
                <br></br>
              </p>
            <button class="button secondary" @click="closeMyPageModal">닫기</button>
          </div>
      </div>
    </div>
  </div>

  <!-- 로그인 실패 모달 -->
  <div class="modal-wrap" v-if="loginFailed" @click="closeLoginFailedModal">
    <div class="right-modal-container" @click.stop="">
      <div class="form-wrapper">
        <p class="login-modal-title">Login Failed</p>
        <br></br>
        <p>아이디 또는 비밀번호가 일치하지 않습니다.</p>
        <br></br>
        <button class="button primary" @click="closeLoginFailedModal">확인</button>
      </div>
    </div>
  </div>

  <!-- 회원탈퇴 확인 모달 -->
  <div class="modal-wrap" v-if="confirmDeleteVisible" @click="closeConfirmDeleteModal">
    <div class="right-modal-container" @click.stop="">
      <div class="form-wrapper">
        <p class="login-modal-title">Confirm Withdrawal</p>
        <p>정말로 회원 탈퇴하시겠습니까?</p>
        <br></br>
          <button class="button secondary" @click="deleteAccount">확인</button>
          <button class="button primary" @click="closeConfirmDeleteModal">취소</button>
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
  axios.post('http://15.165.119.226/user/api/token/', loginData)
    .then(response => {
      console.log(response.data.access);
      localStorage.setItem('userToken', response.data.access); // 토큰 저장
      localStorage.setItem('loginId', this.loginId); // loginId 저장
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
      axios.post('http://15.165.119.226/user/register/', registerData)
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
      
      axios.post('http://15.165.119.226/user/change-password/', passwordData, {
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
      
      axios.post('http://15.165.119.226/user/change-email/', emailData, {
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
      
      axios.post('http://15.165.119.226/user/change-phone/', phoneData, {
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
      axios.post('http://15.165.119.226/user/check-password/', {
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
    },
    setLoginId() {
    // 로컬 스토리지에서 loginId 확인
    const loginId = localStorage.getItem('loginId');
    this.loginId = loginId || ''; // loginId 유무에 따라 loginId 설정
  },
  },
  mounted() {
    this.checkLoginStatus();
    this.setLoginId();
  }
};
</script>
  
  <style>
  @import "../assets/css/home.css";
  
  </style>