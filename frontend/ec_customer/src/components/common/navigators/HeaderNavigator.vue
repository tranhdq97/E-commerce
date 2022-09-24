<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String,
    },
    to: {
      required: true,
      type: String,
    },
  },
})
</script>

<template>
  <div class="wrapper">
    <router-link class="default-link" :to="to">{{ title }}</router-link>
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  align-items: center;
  color: var(--c-semi-grey);
  .default-link {
    color: var(--c-semi-grey);
    text-decoration: none;
    text-transform: capitalize;
    font-weight: var(--f-w-medium);
    font-size: var(--f-s-header-4);
  }
  &:hover {
    color: var(--c-white);
    .default-link {
      color: var(--c-white);
    }
  }
  .router-link-exact-active {
    color: var(--c-white);
  }
}
</style>
