<script lang="ts">
import { defineComponent, ref } from 'vue'
import HeaderNavigator from '../common/navigators/HeaderNavigator.vue'
import { RouterEnum } from '@/interfaces/enum/Router';
import HeaderUserIcon from './HeaderUserIcon.vue';
import HeaderShoppingCartIcon from './HeaderShoppingCartIcon.vue';

export default defineComponent({
  setup() {
    const router = RouterEnum

    return { router }
  },
  components: { HeaderNavigator, HeaderUserIcon, HeaderShoppingCartIcon }
})
</script>

<template>
  <header>
    <router-link class="logo" :to="router.home">
      Vape Bros
    </router-link>
    <div class="navigation">
      <HeaderNavigator title="Home" :to="router.home" />
      <HeaderNavigator title="Products" :to="router.products">
        <div class="dropdown">
          <span class="material-symbols-outlined">expand_more</span>
        </div>
      </HeaderNavigator>
      <HeaderNavigator title="About" :to="router.about" />
      <HeaderNavigator title="Contact" :to="router.contact" />
    </div>
    <div class="user-section">
      <HeaderUserIcon />
      <HeaderShoppingCartIcon />
    </div>
  </header>
</template>

<style lang="scss" scoped>
header {
  background: transparent;
  z-index: 100;
  width: 100%;
  position: fixed;
  display: flex;
  justify-content: space-between;
  padding: var(--s-regular) var(--s-large)
}
.navigation {
  display: flex;
  justify-content: space-between;
  gap: var(--s-large);
}
.dropdown {
  display: flex;
  align-items: center;
}
.logo {
  font-family: 'Chela One', cursive;
  color: var(--c-white);
  font-size: var(--f-s-header-2);
  font-weight: var(--f-w-semi-bold);
  text-decoration: none;
  padding-left: 50px;
}
.user-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--s-medium);
  color: var(--c-white);
}
</style>
