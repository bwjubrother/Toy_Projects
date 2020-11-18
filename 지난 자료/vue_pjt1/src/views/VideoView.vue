<template>
  <div class="container">
    <h1>영화 예고편 검색</h1>
    <VideoSearch @input-change="onInputChange"/>
    <VideoItem :videos="videos" @video-select="onVideoSelect"/>
  </div>
</template>

<script>
import VideoSearch from '@/components/VideoSearch'
import VideoItem from '@/components/VideoItem'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
    name: 'VideoView',
    data() {
      return {
        videos: [],
        selectedVideo: null
      }
    },
    components: {
      VideoSearch,
      VideoItem
    },
    methods: {
      onVideoSelect(video) {
        this.selectedVideo = video
      },
      onInputChange(inputValue) {
        axios.get(API_URL, {
          params: {
            key: API_KEY,
            part: 'snippet',
            type: 'video',
            q: inputValue + 'trailer'
          }
        })
        .then(response => {
          this.videos = response.data.items
        })
        .catch(error => { console.log(error) })
      }
    }
    
}
</script>

<style>

</style>