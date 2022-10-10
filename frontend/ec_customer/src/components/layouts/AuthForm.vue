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
    },
    email: {
      required: true,
      type: String,
    },
    password: {
      required: true,
      type: String
    }
  },
  emits: ['updateEmail', 'updatePassword'],
  setup() {
    const isPasswordShowed = ref<boolean>(false)

    function togglePasswordDisplay() {
      isPasswordShowed.value = !isPasswordShowed.value
    }

    return {
      isPasswordShowed,
      togglePasswordDisplay,
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
      :error="emailError"
      :content="email"
      @updateContent="(data) => $emit('updateEmail', data)"
      />
    <EnterField
      title="password"
      inputType="password"
      :isPasswordShowed="isPasswordShowed"
      placeHolder="Enter your password"
      :error="passwordError"
      :content="password"
      @updateContent="(data) => $emit('updatePassword', data)"
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
.material-symbols-outlined {
  font-size: 20px;
}
</style>
