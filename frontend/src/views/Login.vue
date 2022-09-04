<template>
  <div class="page">
    <div class="login-bg">
      <div class="title">Login</div>
      <div class="button show-error" v-if="showError">
        <p>Username or Password is incorrect</p>
      </div>
      <div>
        <div class="entry-wrapper">
          <div class="entry-label">Email</div>
          <div class="entry">
            <span class="material-icons">email</span>
            <input v-model="email" type="email" placeholder="Type your email" />
          </div>
        </div>
        <div class="entry-wrapper pwd">
          <div class="entry-label">Password</div>
          <div class="pwd-wrapper">
            <div class="entry">
              <span class="material-icons">lock</span>
              <input
                v-model="password"
                :type="isPwdShowed ? 'text' : 'password'"
                placeholder="Type your password"
              />
            </div>
            <div class="button">
              <span class="material-icons" @click="togglePwd">visibility</span>
            </div>
          </div>
        </div>
        <div class="button forgot-pwd">
          <router-link to="/forgot-pwd">Forgot password?</router-link>
        </div>
        <div class="button login-btn" @click="submit">Login</div>
        <div class="button">
          <router-link to="/signup">SignUp</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  name: "LoginPage",
  setup() {
    const store = useStore();
    // eslint-disable-next-line no-unused-vars
    const router = useRouter();
    const email = ref("");
    const password = ref("");
    const isPwdShowed = ref(false);
    const showError = ref(false);

    async function submit() {
      const user = new FormData();
      user.email = email.value;
      user.password = password.value;
      user.provider = "staff";
      store.dispatch("logIn", user);
    }

    function togglePwd() {
      isPwdShowed.value = !isPwdShowed.value;
      console.log(isPwdShowed.value);
    }

    return {
      email,
      password,
      isPwdShowed,
      showError,
      submit,
      togglePwd,
    };
  },
};
</script>

<style scoped lang="scss">
form {
  cursor: default;
}
a {
  color: var(--light);
}
.page {
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--light);
  height: 100vh;

  .login-bg {
    background-color: var(--dark-alt);
    width: 24rem;
    border-radius: 10px;
    box-shadow: 10px 10px 10px var(--light);
    padding: 3rem;
  }
  .button {
    text-align: center;
    &.login-btn {
      background-color: var(--secondary);
      border-radius: 1.5rem;
      font-size: 1.25rem;
      padding: 0.5rem 0;
      text-shadow: 1px 0.5px grey;
      text-transform: uppercase;
      margin-bottom: 2rem;

      &:active {
        background: var(--secondary-light);
      }
    }
    &.forgot-pwd {
      text-align: right;
      margin-bottom: 2rem;
    }
    &.show-error {
      color: red;
      margin-bottom: 1rem;
    }
  }
  .title {
    color: var(--secondary);
    text-shadow: 2px 1px 1px white;
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 2rem;
  }
  .entry-wrapper {
    display: flex;
    flex-direction: column;
    margin-bottom: 2rem;
    border-bottom: 1px solid var(--light);
    font-size: 1rem;

    &.pwd {
      margin-bottom: 1rem;
    }
    .pwd-wrapper {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .entry {
      display: flex;
      align-items: center;
      .material-icons {
        margin: 0.5rem;
      }
      input {
        border: none;
        font-size: 0.9rem;
        padding: 0.3rem;
        width: 100%;
        &::placeholder {
          color: var(--dark);
        }
      }
    }
  }
}
</style>
