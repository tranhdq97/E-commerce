<script setup lang="ts">
import { computed } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'
import { RouterEnum } from './interfaces/enum/Router';
import Header from './components/other/Header.vue';

const router = useRouter()
const currentRouteName = computed(() => router.currentRoute.value.name)
</script>

<template>
  <Header
    v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
  ></Header>
  <RouterView />
  <footer
    v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
  >FOOTER</footer>
</template>

<style lang="scss" scoped>
  footer {
    background: lightgreen;
    padding: 3rem;
    text-align: center;
    border: 1px solid lightsalmon;
  }
</style>
