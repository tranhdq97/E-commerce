<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String
    },
    slogan: {
      required: true,
      type: String
    },
    submitError: {
      required: false,
      type: String
    }
  },
  setup() {
    
  },
})
</script>

<template>
  <div class="wrapper">
    <div class="photo">
      <img src="src/assets/images/auth_background.svg" alt='Photo' />
    </div>
    <div class="form">
      <div class="title">{{ title }}</div>
      <div class="slogan-and-error">
        <div class="slogan">{{ slogan }}</div>
        <div class="submit-error" v-if="submitError">{{ submitError }}</div>  
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  justify-content: space-between;
}
.photo {
  padding-right: 20px;
  justify-items: center;
  img {
    width: 100%;
    height: 99vh;
    min-width: 500px;
  }
}
.form {
  padding:0 85px;
  border-left: 4px solid rgba($color: #000000, $alpha: 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 500px;
}
.title {
  text-align: center;
  font-size: var(--f-s-header-1);
  font-weight: var(--f-w-black);
  color: var(--c-secondary);
  margin-bottom: var(--s-large);
}
.slogan-and-error {
  margin-bottom: var(--s-large);
  .slogan {
    text-align: center;
    font-size: var(--f-s-header-4);
    font-weight: var(--f-w-black);
    color: var(--c-grey);
    margin-bottom: var(--s-regular);
  }
  .submit-error {
    text-align: center;
    font-size: var(--f-s-semi-regular);
    font-weight: var(--f-w-extra-bold);
    color: var(--c-error);
  }
}
</style>