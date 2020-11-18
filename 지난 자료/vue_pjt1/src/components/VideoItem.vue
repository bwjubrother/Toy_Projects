<template>
  <ul class="list-group">
    <VideoItemDetail 
    v-for="video in videos"
    :key="video.etag"
    :video="video"
    @video-select="onVideoSelect"
    />
  </ul>
</template>

<script>
import VideoItemDetail from '@/components/VideoItemDetail.vue'

export default {
  name: 'VideoItem',
  components: {
      VideoItemDetail
  },
  props: {
      videos: {
          type: Array
      }
  },

}
</script>

<style>

</style>