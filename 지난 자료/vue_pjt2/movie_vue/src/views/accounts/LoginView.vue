<template>
  <div>
    <div class="container">
        <h1 class="title">로그인</h1>
        <form>
            <div class="form-group">
                 <label for="title">아이디</label>
                 <input v-model="loginData.username" class="form-control" id="title" type="text" />
                <small class="form-text text-muted">아이디를 작성해주세요.</small>
            </div>
            <div class="form-group">
                <label for="password">비밀번호</label>
                <input v-model="loginData.password" class="form-control" id="password" type="password"/>
                <small class="form-text text-muted">비밀번호를 작성해주세요.</small>
            </div>
            <button @click="login" class="btn btn-primary">확인</button>
        </form>
      </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.$router.push('/')
    }
  },
  methods: {
    login() {
      this.$emit('submit-login-data', this.loginData)
    }
  }
}
</script>

<style scoped>
.container {
    text-align: left;
    width: 50vh;
}
.title {
    text-align: center;
    font: bold;
}
</style>