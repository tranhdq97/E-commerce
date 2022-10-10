<script lang="ts">
import { defineComponent, ref } from 'vue'
import { RouterEnum } from '@/enum/Router';
import HeaderUserIcon from './HeaderUserIcon.vue';
import HeaderShoppingCartIcon from './HeaderShoppingCartIcon.vue';
import SearchSection from './SearchSection.vue';
import HeaderNavigator from '@/components/common/navigators/HeaderNavigator.vue';

export default defineComponent({
  emits: ['openBar', 'closeBar'],
  setup() {
    const router = RouterEnum
    const isSearching = ref(false)

    const openBar = () => isSearching.value = true
    const closeBar = () => isSearching.value = false

    return { 
      router,
      isSearching,
      openBar,
      closeBar,
    }
  },
  components: { HeaderNavigator, HeaderUserIcon, HeaderShoppingCartIcon, SearchSection }
})
</script>

<template>
  <header>
    <router-link class="logo" :to="router.home">
      Vape Bros
    </router-link>
    <div class="navigation-wrapper">
      <div class="navigation" v-if="!isSearching">
        <HeaderNavigator title="Home" :to="router.home" iconName="home"/>
        <HeaderNavigator title="Products" :to="router.products" iconName="category">
          <div class="dropdown">
            <span class="material-symbols-outlined">expand_more</span>
          </div>
        </HeaderNavigator>
        <HeaderNavigator title="About" :to="router.about" iconName="info"/>
        <HeaderNavigator title="Contact" :to="router.contact" iconName="contacts"/>
      </div>
      <SearchSection  @closeBar="closeBar" @openBar="openBar"/>
    </div>
    <div class="user-section">
      <HeaderUserIcon />
      <HeaderShoppingCartIcon />
    </div>
  </header>
</template>

<style lang="scss" scoped>
header {
  background: rgb(0, 0, 0, 0.4);
  z-index: 98;
  width: 100%;
  position: fixed;
  display: flex;
  justify-content: space-between;
  padding: var(--s-regular) var(--s-large)
}
.navigation, .navigation-wrapper {
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
  white-space: nowrap;
}
.user-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--s-large);
  color: var(--c-white);
}
</style>
