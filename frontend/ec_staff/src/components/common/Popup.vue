<script lang="ts">
import { defineComponent, ref } from 'vue'
import AddButton from './buttons/AddButton.vue'

export default defineComponent({
  props: {
    isAdded: {
      required: false,
      default: false,
      type: Boolean,
    },
    title: {
      required: true,
      type: String,
    }
  },
  emits: ['add'],
  setup() {
    const isPopup = ref(false)

    const openPopUp = () => isPopup.value = true
    const closePopUp = () => isPopup.value = false

    return {
      isPopup,
      openPopUp,
      closePopUp,
    };
  },
  components: { AddButton }
})
</script>

<template>
  <div :class="isPopup ? 'popup-wrapper' : ''">
    <div v-click-outside="closePopUp">
      <div v-show="isPopup" class="main">
        <div class="title">{{ title }}</div>
        <div class="fields">
          <slot></slot>
        </div>
        <div :class="isAdded ? 'btn is-added' : 'btn'" @click="$emit('add')">Add</div>
      </div>
      <AddButton @click="openPopUp" v-show="!isPopup"/>
    </div>
  </div>
  
</template>

<style lang="scss" scoped>
.popup-wrapper {
  display: flex;
  width: 100%;
  height: 100vh;
  flex-grow: 2; 
  align-items: center;
  justify-content: center;
  background: var(--c-popup-transparent);
  z-index: 100;
  position: fixed;
  top: 0;
  left: 0;
}
.popup-closed {
  width: 0px;
}
.main {
  background: var(--c-white);
  border-radius: var(--b-r-normal);
  padding: var(--s-large) var(--s-extra-large);
  display: flex;
  flex-direction: column;
  gap: var(--s-large);
}
.title {
  font-size: var(--f-s-header-3);
  font-weight: var(--f-w-extra-bold);
  text-align: center;
  text-transform: capitalize;
}
.btn {
  cursor: pointer;
  background: var(--c-highlight);
  color: var(--c-white);
  border-radius: var(--b-r-normal);
  text-align: center;
  font-size: var(--f-s-header-4);
  font-weight: var(--f-w-semi-bold);
  padding: var(--s-regular) 0;
  text-transform: uppercase;
  &.is-added {
    pointer-events: none;
    opacity: 0.5;
  }
}
.fields {
  display: flex;
  flex-direction: column;
}
</style>
