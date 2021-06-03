<template>
  <div class="app">

    <!-- Modal -->
    <div class="black-bg" v-if="modalOn==true">
      <div class="white-bg">
        <h4>상세페이지</h4>
        <p>세부내용</p>
        <button @click="modalOn = false">닫기</button>
      </div>
    </div>

    <!-- Home -->
    <div class="menu">
      <a v-for="(menu, i) in menus" :key="i">{{ menu }}</a>
    </div>
    <div class="items" v-for="room in room_data" :key="room.id">
      <img :src="room.image" alt="" @click="modalOn = true">
      <h4 @click="modalOn = true">{{ room.title }}</h4>
      <p>{{ room.price }} 만원</p>
      <p>{{ room.content }}</p>
      <button @click="numUp(room.id)">허위매물신고</button> <span>신고수: {{ nums[room.id] }}</span>
    </div>
    
  </div>
</template>

<script>
import room_data from './assets/data/room_data.js';

export default {
  name: 'App',
  data() {
    return {
      menus: ['Home', "Shop", 'About'],
      // products: ['역삼동원룸', '천호동원룸', '마포구원룸'],
      // prices: [60, 70, 80],
      nums: [0, 0, 0, 0, 0, 0],
      modalOn: false,
      room_data: room_data,
    }
  },
  methods: {
    numUp(i) {
      this.nums[i] += 1;
    },
  },
  components: {
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu {
  background: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}

.menu a {
  color: white;
  padding: 10px;
}

.items {
  margin: 10px 0px;
}

.items > img {
  width: 512px;
}

.items > img,
.items > h4 {
  cursor: pointer;
}



.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
  display: flex;
  justify-content: center;
}

.white-bg {
  width: 50%;
  height: 15%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}

</style>
