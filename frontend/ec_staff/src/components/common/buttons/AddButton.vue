<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
  },
})
</script>

<template>
  <div class="button-wrapper">
    <span class="material-symbols-outlined">add</span>
  </div>
</template>

<style lang="scss" scoped>
.button-wrapper {
  cursor: pointer;
  background: rgba(255,255,255, 0.4);
  display: flex;
  padding: var(--s-regular);
  border-radius: var(--b-r-normal);
  z-index: 98;
  position: fixed;
  right: var(--s-large);
  bottom: var(--s-large);
  &:hover {
    background: var(--c-white);
  }
}
</style>
