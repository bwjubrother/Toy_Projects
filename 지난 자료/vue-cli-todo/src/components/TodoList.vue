<template>
  <div>
    <h1>TodoList</h1>
    <ul class="todo-list">
      <!-- prop 4. props 데이터 사용 -->
      <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.isCompleted }">
        <!-- TodoInput emit 1. 하위 컴포넌트에서 체크박스 클릭 시 checked 이벤트를 부모 컴포넌트에 알려줌 -->
        <input type="checkbox" @click="$emit('checked', todo)" :checked="todo.isCompleted">
        {{ todo.content }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  // prop 3. props 데이터 정의 + 검증
  props: {
    todos: {
      type: Array,
      required: true
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}

.todo-list {
  display: inline-block;
  list-style-type: none;
  text-align: left;
  padding: 0;
}
</style>
