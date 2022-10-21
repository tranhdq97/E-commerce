<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import Auth from '@/components/layouts/Auth.vue'
import AuthForm from '@/components/layouts/AuthForm.vue'
import SubmitButton from '@/components/common/buttons/SubmitButton.vue'
import EnterField from '@/components/common/fields/EnterField.vue'
import { AuthEnum } from '@/enum/Auth'
import { RouterEnum } from '@/enum/Router'
import { AuthDispatchEnum } from '@/enum/Dispatch'

export default defineComponent({
  components: { Auth, AuthForm, SubmitButton, EnterField },
  setup() {
    const store = useStore()
    const router = useRouter()
    const slogan = ref("Don't be hater, be a Vaper")
    const submitError = ref("")
    const emailError = ref("")
    const passwordError = ref("")
    const email = ref("")
    const password = ref("")
    const rememberMe = ref<Boolean>(false)

    watch([email, password], ([newEmail, newPassword]) => {
      emailError.value = '',
      passwordError.value = ''
      submitError.value = ''
    })

    async function login(){
      try {
        await store.dispatch(AuthDispatchEnum.login, {
          email: email.value,
          password: password.value,
          rememberMe: rememberMe.value
        })
        router.push(RouterEnum.home)
      } catch (e) {
        const errorDetail = e.response.data.detail
        if (typeof(errorDetail) == "string") {
          submitError.value = errorDetail
        } else {
          emailError.value = errorDetail.hasOwnProperty(AuthEnum.email) ? errorDetail.email[0] : ""
          passwordError.value = errorDetail.hasOwnProperty(AuthEnum.password) ? errorDetail.password[0] : ""
        }
      }
    }
    function clickGoogle() {
      console.log("Login by google account")
    }
    async function clickFacebook() {
      console.log("Login by facebook account")
      await store.dispatch(AuthDispatchEnum.refreshToken)
    }

    return { 
      slogan, 
      submitError, 
      emailError,
      passwordError,
      email,
      password,
      rememberMe,
      login,
      clickGoogle,
      clickFacebook,
    }
  },
})
</script>

<template>
  <main>
    <Auth title="Sign In" :slogan="slogan" :submitError="submitError">
      <AuthForm
        :emailError="emailError" 
        :passwordError="passwordError" 
        :email="email"
        :password="password"
        @updateEmail="(data) => email = data"
        @updatePassword="(data) => password = data"
        @keyup.enter="login"
      >
        <div class="remember-forget">
          <div class="remember-me">
            <input type="checkbox" id="remember-me" v-model="rememberMe" />
            <label for="remember-me">Remember me</label>
          </div>
          <div class="forget-password">
            <router-link class="link" to="/forgot-password">Forgot password</router-link>
          </div>
        </div>
        <SubmitButton name="Log In" @click="login"/>
        <div class="centered">-- or login with --</div>
        <div class="centered">
          <div class="google-icon" @click="clickGoogle">
            <img src="@/assets/icons/google.svg" alt="Google" />
          </div>
          <div @click="clickFacebook">
            <img src="@/assets/icons/facebook.svg" alt="Facebook" />
          </div>
        </div>
        <div class="register-link">
          <router-link class="link" to="/register">Sign Up</router-link>
        </div>
      </AuthForm>
    </Auth>
  </main>
</template>

<style lang="scss" scoped>
.remember-forget{
  margin-bottom: var(--s-medium);
  color: var(--c-grey);
  font-weight: var(--f-w-regular);
  display: flex;
  flex-direction: row;
  
  .remember-me {
    input {
      margin-right: var(--s-regular);
    }
    margin-right: var(--s-large);
  }
}
.centered {
  margin-bottom: var(--s-medium);
}
.register-link, .centered{
  display: flex;
  justify-content: center;
}
.link, .centered {
  color: var(--c-grey);
}
.google-icon {
  margin-right: var(--s-regular);
}
</style>
