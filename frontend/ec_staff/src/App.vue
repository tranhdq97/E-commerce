<script setup lang="ts">
import { computed } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'
import Header from './components/other/header/Header.vue';
import { RouterEnum } from './enum/Router';
import SideBar from './components/other/SideBar.vue';
import { useStore } from 'vuex';
import { AuthDispatchEnum } from './enum/Dispatch';

const router = useRouter()
const store = useStore()
const currentRouteName = computed(() => router.currentRoute.value.name)
store.dispatch(AuthDispatchEnum.getMe)

</script>

<template>
  <SideBar />
  <div class="main-wrapper">
    <Header
      v-if="![RouterEnum.registerName, RouterEnum.loginName].includes(currentRouteName)"
    ></Header>
    <RouterView class="router-view" />
    <footer
      v-if="![RouterEnum.registerName, RouterEnum.loginName].includes(currentRouteName)"
    ></footer>
  </div>
</template>

<style lang="scss" scoped>
.main-wrapper {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.router-view {
  display: flex;
  flex-grow: 2;
  padding: var(--s-medium);
  scroll-behavior: auto;
  background: var(--c-background);
  &::-webkit-scrollbar {
    background: none;
  }
}
</style>
