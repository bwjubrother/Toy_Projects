<template>
  <div>
    <input type="text" @keypress.enter="onInput">
    <button @click="onInput">검색</button>
  </div>
</template>

<script>

export default {
    name: 'VideoSearch',
    methods: {
      onInput(event) {
        this.$emit('input-change', event.target.value)
      }
    }
}
</script>

<style>

</style>