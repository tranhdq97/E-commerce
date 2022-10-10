<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String
    },
    placeHolder: {
      required: false,
      type: String
    },
    inputType: {
      required: true,
      type: String
    },
    content: {
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
    },
  },
  emits: ['updateContent']
})
</script>

<template>
  <div class="wrapper">
    <div class="title">{{ title }}</div>
    <div class="entry-wrapper">
      <input
        :type="isPasswordShowed?'text':inputType" 
        :placeholder="placeHolder"
        :value="content"
        @input="$emit('updateContent', $event.target.value)"
      />
      <slot></slot>
    </div>
    <div class="warning" v-if="error">* {{ error }}</div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  min-width: 300px;
  margin-bottom: var(--s-medium);
}
.title {
  text-transform: capitalize;
  color: var(--c-primary);
  font-size: var(--f-s-header-4);
  font-weight: var(--f-w-black);
  padding-bottom: var(--s-regular);
}
.entry-wrapper {
  background: var(--c-lightgrey);
  border-radius: var(--b-r-normal);
  display: flex;
  flex-direction: row;
  padding: var(--s-medium) var(--s-regular);
  input {
    width: 100%;
    padding:0 var(--s-regular);
  }
}
.warning {
  color: var(--c-error);
  font-size: var(--f-s-small);
  font-weight: var(--f-w-medium);
}
</style>
