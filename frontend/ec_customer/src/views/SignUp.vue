<template>
  <div class="register">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="email">Email:</label>
          <input type="text" name="email" v-model="email" />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" name="password" v-model="password" />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
    <p v-if="showError" id="error">Username already exists</p>
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
      try {
        const user = new FormData();
        user.email = email.value;
        user.password = password.value;
        const resp = await store.dispatch("auth/register", user);
        console.log("RES: ", resp);
        router.push('/login');
      } catch (e) {
        alert(e.response.data.message);
      }
    }

    function togglePwd() {
      isPwdShowed.value = !isPwdShowed.value;
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
