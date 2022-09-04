<script lang="ts">
import { computed, defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String
    },
    placeHoder: {
      required: false,
      type: String
    },
    inputType: {
      required: true,
      type: String
    },
    error: {
      required: false,
      type: String
    },
    isPasswordShowed: {
      required: false,
      type: Boolean
    }
  },
})
</script>

<template>
  <div class="wrapper">
    <div class="title">{{ title }}</div>
    <div class="entry-wrapper">
      <input :type="isPasswordShowed?'text':inputType" :placeholder="placeHoder">
      <slot></slot>
    </div>
    <div class="warning" v-if="error">* {{ error }}</div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  background: lightcyan;
  padding: 1rem;
  display: flex;
  flex-direction: column;

}
.title {
  text-transform: capitalize;
  color: var(--c-primary);
  font-size: var(--f-s-header-4);
  font-weight: var(--f-w-black);
  padding:10px 0;
}
.entry-wrapper {
  background: var(--c-lightgrey);
  border-radius: var(--b-r-normal);
  display: flex;
  flex-direction: row;
  height: 50px;
  input {
    width: 100%;
    padding-left: 10px;
  }
}
.warning {
  color: var(--c-error);
  font-size: var(--f-s-small);
  font-weight: var(--f-w-medium);
}
</style>
