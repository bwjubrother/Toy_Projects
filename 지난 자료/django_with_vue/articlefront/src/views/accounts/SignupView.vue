<template>
  <div>
    <h1>Signup</h1>
    username : <input type="text" v-model="signupData.username"><br>
    password1 : <input type="password" v-model="signupData.password1"><br>
    password2 : <input type="password" v-model="signupData.password2"><br>
    <button @click="signup">signup</button>
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
        password2: null
      }
    }
  },
  methods: {
    signup() {
      this.$emit('submit-signup-data', this.signupData)
    }
  },
}
</script>

<style>

</style>
