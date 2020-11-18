<template>
  <div>
    <div class="details">
      <h4 v-html="video.snippet.title"></h4>
    </div>
    <div class="embed-responsive embed-responsive-16by9">
      <iframe class="embed-responsive-item" type="text/html" :src="videoUrl" frameborder="0"></iframe>
    </div>


  </div>
</template>

<script>
export default {
    name: 'VideoItemDetail',
    props: {
      video: {
        type: Object
      }
    },
    computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
    }
}
</script>

<style scoped>

</style>