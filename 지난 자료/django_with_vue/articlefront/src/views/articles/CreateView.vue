<template>
  <div>
    <h1>create</h1>
    title : <input type="text" v-model="articleData.title"><br>
    content : <input type="text" v-model="articleData.content"><br>
    <button @click="createArticle">create</button>
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
			articleData: {
        title: null,
        content: null,
			}
    }
  },
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      return this.$router.push('/login')
    }
  },
  methods: {
    createArticle() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${BACK_URL}/articles/create/`, this.articleData, requestHeaders)
        .then(() => {
          this.$router.push('/articles/')
        })
        .catch(errors => {
          console.log(errors.response.data)
        })
    }
  },
}
</script>

<style>

</style>
