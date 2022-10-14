<script lang="ts">
import { SideBarDispatchEnum } from '@/enum/Dispatch'
import { SideBarGetterEnum } from '@/enum/Getter'
import { RouterEnum } from '@/enum/Router'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import { SideBarEnum } from '@/enum/SideBar'
import MainRoute from './sidebar/MainRoute.vue'

export default defineComponent({
  setup() {
    const store = useStore();
    const isOpenSideBar = computed(() => store.getters[SideBarGetterEnum.isOpenSideBar]);
    const mainRouteObj = {
      title: SideBarEnum.products,
      icon: SideBarEnum.productsIcon,
      children: [
        { title: RouterEnum.categoriesName, route: RouterEnum.categories },
        { title: RouterEnum.productsName, route: RouterEnum.products },
        { title: RouterEnum.discountsName, route: RouterEnum.discounts },
      ]
    }

    const closeSideBar = () => {
      store.dispatch(SideBarDispatchEnum.closeSideBar);
    }

    return {
      mainRouteObj,
      isOpenSideBar,
      closeSideBar,
    };
  },
  components: { MainRoute }
})
</script>

<template>
  <div class="side-bar-wrapper" v-if="isOpenSideBar">
    <div class="side-bar">
      <MainRoute :mainRouteObj="mainRouteObj" />
      <MainRoute :mainRouteObj="{title: 'dashboard', icon: 'category', children: [{ title: 'xx', route: '/'}]}" />
    </div>
    <div class="transparent" @click="closeSideBar"></div>
  </div>
</template>

<style lang="scss" scoped>
.side-bar-wrapper {
  display: flex;
  flex-direction: row;
  height: 100vh;
  width: 100%;
  z-index: 100;
  position: fixed;
}
.side-bar {
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  padding: var(--s-medium);
  background: var(--c-background);
}
.transparent {
  display: flex;
  flex-grow: 1;
  background: var(--c-popup-transparent);
}
</style>