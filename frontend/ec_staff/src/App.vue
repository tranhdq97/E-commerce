<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    HEADER
  </header>
  <RouterView />
  <footer>FOOTER</footer>
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
