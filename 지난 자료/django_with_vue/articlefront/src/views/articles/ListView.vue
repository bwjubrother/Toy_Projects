<template>
  <div>
    <h1>article list</h1>
    <li v-for="article in articles" :key="article.id">{{ article.title }}</li>
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ListView',
  data() {
    return {
      articles: null,
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      axios.get(`${BACK_URL}/articles/`)
        .then(response => {
          this.articles = response.data
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
