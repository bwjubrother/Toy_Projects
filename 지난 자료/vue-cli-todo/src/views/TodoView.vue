<template>
  <div>
    <!-- TodoInput emit 5. 하위 컴포넌트의 create-todo 이벤트 감지 -->
    <TodoInput @create-todo="createTodo"/>
    <!-- prop 2. 하위 컴포넌트로 전달 데이터 바인딩 (오른쪽 todos가 하위 컴포트가 받는 이름) -->
    <!-- TodoList emit 2. 하위 컴포넌트의 checked 이벤트 감지-->
    <TodoList :todos="todos" @checked="updateTodo"/>
  </div>
</template>

<script>
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'TodoView',
  components: {
    TodoInput,
    TodoList
  },
  // prop 1. todos data 작성
  data() {
    return {
      todos: [
        {
          id: 1,
          content: 'Vue',
          isCompleted: true
        },
        {
          id: 2,
          content: 'Django',
          isCompleted: false
        },
        {
          id: 3,
          content: 'Python',
          isCompleted: false
        },
      ]
    }
  },
  methods: {
    // TodoList emit 3. 하위 컴포넌트(TodoList)의 이벤트(checked)를 감지하면 실행할 메서드
    updateTodo(todo) {
      todo.isCompleted = !todo.isCompleted
    },
    // TodoInput emit 6. 하위 컴포넌트(TodoInput)의 이벤트(create-todo)를 감지하면 실행할 메서드
    createTodo(todo) {
      this.todos.push(todo)
    }
  }
}
</script>

<style>

</style>
