<template>
  <div class="app">
    <SideBar />
    <main>
      <router-view />
      <Footer></Footer>
    </main>
  </div>
</template>

<script setup>
import Footer from "./components/Footer.vue";
import SideBar from "./components/SideBar.vue";
</script>

<style>
.app {
  display: flex;
}

main {
  flex: 1 1 0;
  overflow-y: scroll;
  height: 100vh;
}
</style>
