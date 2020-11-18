<template>
  <div>
    <div class="container">
      <h1 class="title">로그인</h1>
      <form>
          <div class="form-group">
                <label for="title">아이디</label>
                <input v-model="signupData.username" class="form-control" id="title" type="text" />
              <small class="form-text text-muted">아이디를 작성해주세요.</small>
          </div>
          <div class="form-group">
              <label for="password">비밀번호</label>
              <input v-model="signupData.password1" class="form-control" id="password" type="password"/>
              <small class="form-text text-muted">비밀번호를 작성해주세요.</small>
          </div>
          <div class="form-group">
              <label for="password">비밀번호 확인</label>
              <input v-model="signupData.password2" class="form-control" id="password" type="password"/>
              <small class="form-text text-muted">비밀번호를 다시 한번 입력해주세요.</small>
          </div>
          <button @click="signup" class="btn btn-primary">확인</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      signupData: {
          username: null,
          password1: null,
          password2: null,
      }
    }
  },
  methods: {
    signup() {
      this.$emit('submit-signup-data', this.signupData)
    }
  }
}
</script>

<style>
.container {
    text-align: left;
    width: 50vh;
}
.title {
    text-align: center;
    font: bold;
}
</style>