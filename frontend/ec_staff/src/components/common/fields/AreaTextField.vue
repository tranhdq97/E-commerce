<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: { required: true, type: String, },
    placeHolder: { required: false, type: String, },
    field: { required: true, type: Object, },
    type: { required: false, default: 'text', type: String},
    row: { required: false, default: '4', type: String },
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
    <textarea
      :rows="row"
      :type="type"
      :placeholder="placeHolder" 
      :value="field.name"
      @input="(e) => $emit('updateField', { ...field, name: e.target.value })"
    ></textarea>
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
textarea {
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
  padding: var(--s-medium);
  border-radius: var(--b-r-small);
  background: var(--c-enter-transparent);
  border: none;
  outline: none;
}
</style>
