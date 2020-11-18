<template>
  <div>
    <!-- TodoInput emit 2. v-model 작성 -->
    <!-- TodoInput emit 3. 입력 후 상위 컴포넌트로 보낼 이벤트를 발생시킬 메서드(createTodo) 작성 -->
    <input type="text" v-model="todo" @keypress.enter="createTodo">
    <button @click="createTodo">작성</button>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  // TodoInput emit 1. data 작성
  data() {
    return {
      todo: ''
    }
  },
  // TodoInput emit 4. emit 이벤트를 만드는 메서드
  methods: {
    createTodo() {
      if (this.todo.trim()) {
        this.$emit('create-todo', {
          id: Date.now(),
          content: this.todo,
          isCompleted: false
        })
        this.todo = ''
      }
    }
  }
}
</script>

<style>

</style>
