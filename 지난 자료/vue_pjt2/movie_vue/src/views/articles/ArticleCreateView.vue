<template>
    <div class="createform container">
        <h1 class="title">커뮤니티</h1>
        <form>
            <div class="form-group">
                 <label for="title">Title</label>
                 <input v-model="articleData.title" class="form-control" id="title" type="text" />
                <small id="emailHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요.</small>
            </div>
            <div class="form-group">
                <label for="content">Content</label>
                <textarea v-model="articleData.content" class="form-control" id="content" cols="30" rows="10"></textarea>
            </div>
            <input value="작성하기" id="createArticleButton" @click="createArticle" class="btn btn-primary">
        </form>
    </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: "CreateView",
  data() {
    return {
      articleData: {
        title: null,
        content: null,
      }
    };
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // article 생성은 Header: Token / Body: { title: , content: }
      axios.post(SERVER_URL + 'articles/create/', this.articleData, config)
        .then(res => { 
          console.log(res.data) 
          this.$router.push('/articles')
        })
        .catch(err => console.log(err.response.data))
    },
    // checkLoggedIn() {
    //   if (!this.$cookies.isKey('auth-token')) {
    //     this.$router.push({ name: 'Login' })
    //   } 
    // }
  },

  // created() {
  //   this.checkLoggedIn()
  // },
};
</script>

<style scoped>
.createform {
    text-align: left;
    width: 50vh;
}
.title {
    text-align: center;
    font: bold;
}

</style>
