<script lang="ts">
  import { defineComponent, ref } from 'vue'
  import EnterField from '../components/common/fields/EnterField.vue'
  
  export default defineComponent({
    components: {
      EnterField
    },
    setup() {
      const isPasswordShowed = ref<boolean>(false)
      
      function togglePasswordDisplay() {
        isPasswordShowed.value = !isPasswordShowed.value
        console.log('CLICK', isPasswordShowed.value)
      }
      
      return { isPasswordShowed, togglePasswordDisplay }
    }
  })
</script>

<template>
  <main>
    <EnterField title="email" inputType="text" placeHoder="Enter your email" error="Your supplied email is not in right form."/>
    <EnterField title="password" inputType="password" :isPasswordShowed="isPasswordShowed" placeHoder="Enter your password" error="Password must contain 8-255 letters, includes at least 1 upper letter, 1 digit.">
      <div @click="togglePasswordDisplay" class="password-display">
        <span class="material-symbols-outlined" v-if="isPasswordShowed">visibility_off</span>
        <span class="material-symbols-outlined" v-else>visibility</span>
      </div>
    </EnterField>
  </main>
</template>

<style lang="scss" scoped>
.password-display {
  display: flex;
  align-items: center;
  padding-right: 10px;
}
</style>
  