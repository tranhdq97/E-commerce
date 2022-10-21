<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: { required: true, type: String, },
    content: { required: true, type: String, },
  },
  emits: ['updateField',],
  setup() {
    return {
    }
  },
})
</script>

<template>
  <div class="wrapper">
    <div class="title">{{ title }}</div>
    <div class="field-value">{{ content }}</div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: var(--s-medium);
  min-width: 250px;
}
.title {
  text-transform: capitalize;
  font-size: var(--f-s-semi-regular);
  font-weight: var(--f-w-semi-bold);
  margin-bottom: var(--s-small);
}
.field-value {
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
  padding: var(--s-medium);
  border-radius: var(--b-r-small);
  background: var(--c-enter-transparent);
  text-transform: capitalize;
}
</style>
