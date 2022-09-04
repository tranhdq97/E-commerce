<template>
  <aside
    :class="`${is_expanded ? 'is-expanded' : ''}`"
    @mouseenter="openSideBar"
    @mouseleave="closeSideBar"
  >
    <div class="responsive section-separate" @dblclick="login">
      <router-link to="/" class="button">
        <img class="logo" src="../assets/smoke-logo.svg" alt="Vue logo" />
        <span class="text logo-text">Vape</span>
      </router-link>
    </div>
    <div class="responsive section-separate">
      <router-link to="/login" class="button" v-if="!isAuthenticated">
        <span class="material-icons">login</span>
        <span class="text">Login</span>
      </router-link>
      <div class="login-wrapper" v-else>
        <div class="button">
          <img
            class="logo avatar"
            src="../assets/background.jpeg"
            alt="Avatar"
          />
          <span class="text username">Dong Quoc Tranh </span>
        </div>
        <div class="button" @click="logout">
          <span class="material-icons logout-icon">logout</span>
        </div>
      </div>
    </div>
    <div class="responsive">
      <router-link class="button" to="/">
        <span class="material-icons">home</span>
        <span class="text">Home</span>
      </router-link>
      <router-link class="button" to="/about">
        <span class="material-icons">visibility</span>
        <span class="text">About</span>
      </router-link>
      <router-link class="button" to="/team">
        <span class="material-icons">group</span>
        <span class="text">Team</span>
      </router-link>
      <router-link class="button" to="/contact">
        <span class="material-icons">email</span>
        <span class="text">Contact</span>
      </router-link>
    </div>

    <div class="flex"></div>

    <div class="responsive">
      <router-link class="button" to="/settings">
        <span class="material-icons">settings</span>
        <span class="text">Settings</span>
      </router-link>
    </div>
  </aside>
</template>

<script>
import { ref, computed } from "vue";

import router from "../router";
import store from "../store";

export default {
  setup() {
    const is_expanded = ref(localStorage.is_expanded);
    const is_login = ref(localStorage.is_login);

    // eslint-disable-next-line no-unused-vars
    const isLoggedIn = computed(() => store.getters.isAuthenticated);

    function openSideBar() {
      is_expanded.value = true;
    }
    function closeSideBar() {
      is_expanded.value = false;
    }
    function login() {
      is_login.value = true;
    }
    function logout() {
      is_login.value = false;
      router.push("/");
    }

    return {
      is_expanded,
      is_login,
      openSideBar,
      closeSideBar,
      login,
      logout,
    };
  },
};
</script>

<style scoped lang="scss">
aside {
  display: flex;
  flex-direction: column;
  width: calc(2rem + 2rem);
  min-height: 100vh;
  padding: 1rem;
  padding-top: 0;
  background-color: var(--dark);
  color: var(--light);
  transition: 0.3s ease-out;

  .flex {
    flex: 1 1 0;
  }
  .logo {
    width: 3rem;
    height: 3rem;
    transform: translateX(-0.5rem);
    &.avatar {
      border-radius: 50%;
      border: 2px solid var(--light);
    }
  }
  .login-wrapper {
    display: flex;
    justify-content: space-between;
  }
  .button .text {
    opacity: 0;
  }
  .responsive {
    margin: 0 -1rem;
    .button {
      display: flex;
      align-items: center;
      text-decoration: none;
      padding: 0.5rem 1rem;
      transition: 0.2s ease-out;
      .material-icons {
        font-size: 2rem;
        color: var(--light);
        transition: 0.2s ease-out;
        &.logout-icon {
          margin-right: 0;
          opacity: 0;
        }
      }
      .text {
        color: var(--light);
        width: calc(var(--sidebar-width) - 9rem);
        text-align: left;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        transition: 0.5s ease-out;
        &.logo-text {
          color: var(--light);
          text-transform: uppercase;
          font-size: 1.25rem;
        }
      }
      &:hover,
      &.router-link-exact-active {
        background-color: var(--dark-alt);
        .material-icons,
        .text {
          color: var(--primary);
        }
      }
      &.router-link-exact-active {
        border-right: 5px solid var(--primary);
      }
    }
    &.section-separate {
      border-bottom: 2px solid var(--dark-alt);
      .button.router-link-exact-active {
        border-right: none;
        background-color: var(--dark);
      }
    }
  }
  &.is-expanded {
    width: var(--sidebar-width);

    .button .text {
      opacity: 1;
    }
    .button {
      .material-icons {
        margin-right: 1rem;

        &.logout-icon {
          opacity: 1;
          transition: 0.5s ease-out;
        }
      }
    }
  }

  @media (max-width: 768px) {
    position: fixed;
    z-index: 99;
  }
}
</style>
