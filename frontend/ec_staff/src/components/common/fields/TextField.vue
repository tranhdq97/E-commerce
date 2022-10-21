<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: { required: true, type: String, },
    placeHolder: { required: false, type: String, },
    field: { required: true, type: Object, },
    type: { required: false, default: 'text', type: String},
    isDisabled: { required: false, default: false, type: Boolean },
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
    <div :class="isDisabled ? 'title is-disabled' : 'title'">{{ title }}</div>
    <input
      :class="isDisabled ? 'is-disabled' : ''"
      :type="type"
      :placeholder="placeHolder" 
      :value="field.name"
      @input="(e) => $emit('updateField', { ...field, name: e.target.value })"
    />
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
  &.is-disabled {
    color: var(--c-grey);
  }
}
input {
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
  padding: var(--s-medium);
  border-radius: var(--b-r-small);
  background: var(--c-enter-transparent);
  text-transform: capitalize;
  &.is-disabled {
    pointer-events: none;
  }
}
.input-wrapper {
  display: flex;
  align-items: center;
}
</style>
