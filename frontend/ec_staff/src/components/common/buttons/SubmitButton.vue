<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    name: {
      required: true,
      type: String
    }
  },
})
</script>

<template>
  <div class="button">{{ name }}</div>
</template>

<style lang="scss" scoped>
.button {
  background: var(--c-primaryHighlight);
  color: var(--c-white);
  font-size: var(--f-s-header-3);
  font-weight: var(--f-w-extra-bold);
  padding: 10px;
  text-align: center;
  border-radius: var(--b-r-normal);
  margin-bottom: var(--s-large);
  &:hover {
    cursor: pointer;
    background: var(--c-primaryHighlight-lighter);
  }
  &:active {
    background: var(--c-primaryHighlight);
  }
}
</style>
