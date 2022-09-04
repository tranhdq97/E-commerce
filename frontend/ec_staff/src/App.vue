<script setup lang="ts">
import { computed } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'
import { RouterEnum } from './interfaces/enum/Router';

const router = useRouter()
const currentRouteName = computed(() => router.currentRoute.value.name)
</script>

<template>
  <header
    v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
  ></header>
  <RouterView />
  <footer
    v-if="currentRouteName !== RouterEnum.registerName && currentRouteName !== RouterEnum.loginName"
  >FOOTER</footer>
</template>

<style lang="scss" scoped>
  header {
    background: transparent;
    border: 1px solid lightcoral;
    z-index: 100;
    width: 100%;
    position: fixed;
    text-align: center;
  }
  footer {
    background: lightgreen;
    padding: 3rem;
    text-align: center;
    border: 1px solid lightsalmon;
  }
</style>
