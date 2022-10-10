<script setup lang="ts">
import { computed } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'
import Header from './components/other/header/Header.vue';
import { RouterEnum } from './enum/Router';

const router = useRouter()
const currentRouteName = computed(() => router.currentRoute.value.name)

</script>

<template>
  <div class="main-wrapper">
    <Header
      v-if="![RouterEnum.registerName, RouterEnum.loginName].includes(currentRouteName)"
    ></Header>
    <RouterView />
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
  overflow-y: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
}
</style>
