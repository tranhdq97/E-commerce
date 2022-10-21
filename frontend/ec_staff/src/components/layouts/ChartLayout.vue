<script lang="ts">
import { SortByEnum } from '@/enum/SortBy';
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String,
    },
    sortBy: {
      required: false,
      default: SortByEnum.thisMonth,
      // type
    }
  },
  setup() {
  },
})
</script>

<template>
  <div class="chart-wrapper">
    <div class="header">
      <div class="title">{{ title }}</div>
      <div class="sort-by">
        <div class="sort-title">sort by:</div>
        <div class="sort-element">
          {{ sortBy }}
          <span class="material-symbols-outlined">expand_more</span>
        </div>
      </div>
    </div>
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
.chart-wrapper {
  display: flex;
  flex-direction: column;
  background: var(--c-white);
  height: 400px;
  border-radius: var(--b-r-normal);
}
.header {
  display: flex;
  padding: var(--s-medium);
  justify-content: space-between;
  border-bottom: var(--b-s-small) solid var(--b-c-regular);
  .title {
    text-transform: capitalize;
    font-size: var(--f-s-header-4);
    font-weight: var(--f-w-regular);
  }
  .sort-by {
    display: flex;
    align-items: center;
    .sort-element {
      display: flex;
      margin-left: var(--s-small);
      text-transform: capitalize;
      font-size: var(--f-s-semi-regular);
      font-weight: var(--f-w-medium);
    }
    .sort-title {
      text-transform: uppercase;
      font-weight: var(--f-w-semi-bold);
      color: var(--c-primary);
    }
  }
}
</style>
