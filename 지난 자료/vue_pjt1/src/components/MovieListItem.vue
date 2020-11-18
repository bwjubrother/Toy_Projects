<template>
  <div class="col-lg-3">
    <div class="card" style="width: 18rem height: 30rem">
      <img :src="movie.poster_url" class="max-width: 100%" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <MovieListItemModal :movie="movie"/>
      </div>
    </div> 
  </div>
</template>

<script>
import MovieListItemModal from '@/components/MovieListItemModal.vue'


export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal
  },
  props: {
    movie: {
      type: Object
    }
  },
}
</script>

<style>
img {
  height: 400px;
}


</style>