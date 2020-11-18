<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" :data-target="'#movie-'+movie.id">
      영화 정보 상세보기
    </button>

    <!-- Modal -->
    <div class="modal fade" :id="'movie-'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <hr>
          <div>
          <img :src="movie.backdrop_url" class="img-fluid" alt="movieimg">
          <hr>
          </div>
           <h4><span class="badge badge-success">{{ movie.user_rating }}</span></h4>
          <div class="modal-body">
            {{ movie.overview }}
          </div>
          <hr>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItemModal',
  props: {
    movie: {
      type: Object
    }
  }
}
</script>

<style>

</style>