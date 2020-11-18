<template>
  <div>
    <h1>login</h1>
    username : <input type="text" v-model="loginData.username"><br>
    password : <input type="password" v-model="loginData.password"><br>
    <button @click="login">login</button>
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
      return this.$router.push('/')
    } 
  },
  methods: {
    login() {
      this.$emit('submit-login-data', this.loginData)
    }
  },
}
</script>

<style>

</style>
