<template>
  <div class="container">
    <h1>나만의 무비 컬렉션</h1>
    <div>
      <button v-if="clicked === 0" @click="getMovieData" class="btn btn-primary">영화 가져오기</button>
    </div>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

// const API_URL = process.env.VUE_APP_MOVIE_API_URL

export default {
    name: 'MovieView',
    data() {
      return {
        movies: [],
        clicked: 0
      }
    },
    components: {
      MovieList
    },
    methods: {
      getMovieData: function() {
        const URL = 'http://www.json-generator.com/api/json/get/ceNyuXZmwi?indent=2'
        axios.get(URL)
        .then(response => {
          this.movies = response.data
          this.clicked = 1
        })
      }
    }
}
</script>

<style>

</style>