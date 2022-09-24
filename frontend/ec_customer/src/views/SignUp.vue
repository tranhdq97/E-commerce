<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { useStore } from 'vuex'
import Auth from '@/components/layouts/Auth.vue'
import AuthForm from '@/components/layouts/AuthForm.vue'
import SubmitButton from '@/components/common/buttons/SubmitButton.vue'
import EnterField from '../components/common/fields/EnterField.vue'
import { useRouter } from 'vue-router'
import { AuthDispatchEnum } from '@/interfaces/enum/Dispatch'
import { RouterEnum } from '@/interfaces/enum/Router'
import { AuthEnum } from '@/interfaces/enum/Auth'

export default defineComponent({
  components: {
  Auth,
  AuthForm,
  SubmitButton,
  EnterField
  },
  setup() {
    const store = useStore()
    const router = useRouter()
    const slogan = ref("Live long and vape strong")
    const submitError = ref("")
    const emailError = ref("")
    const passwordError = ref("")
    const lastNameError = ref("")
    const email = ref("")
    const password = ref("")
    const lastName = ref("")

    watch([email, password, lastName], ([newEmail, newPassword, newLastName]) => {
      emailError.value = '',
      passwordError.value = ''
      submitError.value = ''
      lastNameError.value = ''
    })

    async function register(){
      try {
        await store.dispatch(AuthDispatchEnum.register, {
          email: email.value,
          password: password.value,
          info: {
            last_name: lastName.value
          }
        })
        router.push(RouterEnum.login)
      } catch (e) {
        const errorDetail = e.response.data.detail
        if (typeof(errorDetail) == "string") {
          submitError.value = errorDetail
        } else {
          emailError.value = errorDetail.hasOwnProperty(AuthEnum.email) ? errorDetail.email[0] : ""
          passwordError.value = errorDetail.hasOwnProperty(AuthEnum.password) ? errorDetail.password[0] : ""
          lastNameError.value = errorDetail.hasOwnProperty(AuthEnum.info) ? errorDetail.info.last_name[0] : ""
        }
      }
    }

    return { 
      slogan, 
      submitError, 
      emailError,
      passwordError,
      lastNameError,
      email,
      password,
      lastName,

      register,
    }
  }
})
</script>

<template>
  <main>
    <Auth title="Sign Up" :slogan="slogan" :submitError="submitError">
      <AuthForm
        :emailError="emailError" 
        :passwordError="passwordError" 
        :email="email"
        :password="password"
        @updateEmail="(data) => email = data"
        @updatePassword="(data) => password = data"
      >
        <EnterField
          title="Last Name"
          inputType="text"
          placeHolder="Enter your last name"
          :error="lastNameError"
          :content="lastName"
          @updateContent="(data) => lastName = data"
        /> 
        <SubmitButton name="Register" @click="register" />
        <div class="login-link">
          <router-link class="link" to="/login">Sign In</router-link>
        </div>
      </AuthForm>
    </Auth>
  </main>
</template>

<style lang="scss" scoped>
.login-link {
  display: flex;
  justify-content: center;
  .link {
    color: var(--c-grey);
  }
}
</style>
