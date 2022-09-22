<script setup lang="ts">
import { computed, defineComponent } from '@vue/runtime-core'
import { RouterView, useRouter } from 'vue-router'

const router = useRouter()
const currentRouteName = computed(() => router.currentRoute.value.name)
</script>

<template>
  <header
    v-if="currentRouteName !== 'register' && currentRouteName !== 'login'"
  ></header>
  <RouterView />
  <footer
    v-if="currentRouteName !== 'register' && currentRouteName !== 'login'"
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
