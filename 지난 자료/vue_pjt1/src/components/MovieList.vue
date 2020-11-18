<template>
  <ul class="row">
    <MovieListItem
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />
  </ul>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
    name: 'MovieList',
    components: {
      MovieListItem
    },
    props: {
      movies: {
        type: Array
      }
    },    
}
</script>

<style>

</style>