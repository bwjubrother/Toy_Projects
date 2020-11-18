<template>
  <div id="app">
    <div id="nav">
      <router-link to="/articles">목록으로</router-link> |
      <span v-if="isLogin">
        <router-link to="/accounts/logout" @click.native="logout">Logout</router-link> |
      </span>
      <span v-else>
        <router-link to="/accounts/signup">Signup</router-link> | 
        <router-link to="/accounts/login">Login</router-link>
      </span>
      <div v-if="isLogin">
        <router-link to="/articles/create"><button class="btn btn-success">글쓰기</button></router-link>
      </div>
    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup"/>
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isLogin: false,
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.isLogin = true
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLogin = true
    },
    login(loginData) {
      axios.post(`${BACK_URL}/rest-auth/login/`, loginData)
      .then(response => {
        // console.log(response)
        this.setCookie(response.data.key)  
        this.$router.push('/')
      })
      .catch(error => { console.log(error.response.data) })
    },
    logout() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${BACK_URL}/rest-auth/logout/`, null, requestHeader)
      .then(() => {
        this.$cookies.remove('auth-token')
        this.isLogin = false
        this.$router.push('/')
      })
    },
    signup(signupData) {
      axios.post(`${BACK_URL}/rest-auth/signup/`, signupData)
      .then(response => {
        this.setCookie(response.data.key)
        this.$router.push('/')
      })
      .catch(error => { console.log(error) })
    },
    // createArticle(articleData) {
    //   axios.post(`${BACK_URL}/articles/create/`, articleData)
    //   .then(
    //     this.$router.push('/')
    //   )
    //   .catch(error => { console.log(error) })
    // }
    
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
