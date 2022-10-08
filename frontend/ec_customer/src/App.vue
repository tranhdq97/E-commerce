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
    >FOOTER</footer>
  </div>
</template>

<style lang="scss" scoped>
footer {
  background: lightgreen;
  padding: 3rem;
  text-align: center;
  border: 1px solid lightsalmon;
}
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
