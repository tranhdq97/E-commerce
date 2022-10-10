<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    iconName: {
      required: true,
      type: String
    },
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
  <router-link class="wrapper" :to="to">
    <div class="nav-icon">
      <span class="material-icons">{{ iconName }}</span>
    </div>
    <div>{{ title }}</div>
  </router-link>
</template>

<style lang="scss" scoped>
.wrapper {
  cursor: pointer;
  display: flex;
  align-items: center;
  color: var(--c-semi-grey);
  text-decoration: none;
  text-transform: capitalize;
  font-weight: var(--f-w-medium);
  font-size: var(--f-s-header-4);
  &:hover {
    color: var(--c-white);
  }
  .nav-icon {
    display: flex;
    margin-right: var(--s-small);
  }
}
.router-link-exact-active {
  color: var(--c-white);
}
</style>
