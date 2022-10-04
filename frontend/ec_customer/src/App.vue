<script setup lang="ts">
import { computed } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'
import Header from './components/other/Header.vue';
import { RouterEnum } from './enum/Router';
import SideBar from './components/other/SideBar.vue';

const router = useRouter()
const currentRouteName = computed(() => router.currentRoute.value.name)

</script>

<template>
  <div class="app-wrapper">
    <div class="main-wrapper">
      <Header
        v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
      ></Header>
      <RouterView />
      <footer
        v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
      >FOOTER</footer>
    </div>
    <SideBar />
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
  display: flex;
  flex-direction: column;
}
.app-wrapper {
  display: flex;
  flex-direction: row;
}
</style>
