<template>
    <div>
        <h1>게시판</h1>
        <table class="table container">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">제목</th>
                <th scope="col">작성자</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="article in articles" :key="article.id">
                <th scope="row">{{ article.id }}</th>
                <td>{{ article.title }}</td>
                <td>{{ article.user.username }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://127.0.0.1:8000/";

export default {
  name: "ListView",
  data() {
    return {
      articles: []
    };
  },
  created() {
    this.fetchArticles()
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + "articles/")
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
  }
  
};
</script>

<style>
.table {
    width: 100vh;
}

</style>
