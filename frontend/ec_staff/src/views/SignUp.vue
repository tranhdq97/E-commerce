<script lang="ts">
  import { defineComponent, ref } from 'vue'
  import Auth from '@/components/layouts/Auth.vue'
  import AuthForm from '@/components/layouts/AuthForm.vue'
  import SubmitButton from '@/components/common/buttons/SubmitButton.vue'

  export default defineComponent({
    components: {
      Auth,
      AuthForm,
      SubmitButton,
    },
    setup() {
      const slogan = ref("Live long and vape strong")
      const submitError = ref("Submit Error")
      const emailError = ref("Email Error")
      const passwordError = ref("Password Error")

      return { slogan, submitError, emailError, passwordError }
    }
  })
</script>

<template>
  <main>
    <Auth title="Sign Up" :slogan="slogan" :submitError="submitError">
      <AuthForm :emailError="emailError" :password-error="passwordError">
        <SubmitButton name="Register" />
        <div class="login-btn">
          <router-link class="btn" to="/login">Sign In</router-link>
        </div>
      </AuthForm>
    </Auth>
  </main>
</template>

<style lang="scss" scoped>
.login-btn {
  display: flex;
  justify-content: center;
  .btn {
    color: var(--c-grey);
  }
}
</style>
