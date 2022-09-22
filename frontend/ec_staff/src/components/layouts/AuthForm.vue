<script lang="ts">
import { defineComponent, ref } from 'vue'
import EnterField from '../common/fields/EnterField.vue';
import SubmitButton from '../common/buttons/SubmitButton.vue';

export default defineComponent({
  components: {
    EnterField,
    SubmitButton,
  },
  props: {
    emailError: {
      required: false,
      type: String
    },
    passwordError: {
      required: false,
      type: String
    }
  },
  setup() {
    const isPasswordShowed = ref<boolean>(false)

    function togglePasswordDisplay() {
      isPasswordShowed.value = !isPasswordShowed.value
    }

    return {
      isPasswordShowed,
      togglePasswordDisplay 
    }
  },
})
</script>

<template>
  <div>
    <EnterField 
      title="Email" 
      inputType="text" 
      placeHolder="Enter your email" 
      :error="emailError" />
    <EnterField
      title="password"
      inputType="password"
      :isPasswordShowed="isPasswordShowed"
      placeHolder="Enter your password"
      :error="passwordError"
    >
      <div @click="togglePasswordDisplay" class="password-display">
        <span class="material-symbols-outlined" v-if="isPasswordShowed">visibility_off</span>
        <span class="material-symbols-outlined" v-else>visibility</span>
      </div>
    </EnterField>
    <slot></slot>
  </div>
  
</template>

<style lang="scss" scoped>
.password-display {
  display: flex;
  cursor: pointer;
}
</style>
