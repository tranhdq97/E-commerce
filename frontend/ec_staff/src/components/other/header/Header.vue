<script lang="ts">
import { SideBarDispatchEnum } from '@/enum/Dispatch';
import { SideBarGetterEnum } from '@/enum/Getter';
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex';
import HeaderUserIcon from './HeaderUserIcon.vue';

export default defineComponent({
  setup() {
    const store = useStore()
    const mainRoute = computed(() => store.getters[SideBarGetterEnum.selectedMainRoute])
    const subRoute = computed(() => store.getters[SideBarGetterEnum.selectedSubRoute])
    const numNotifications = ref(0)
    
    const toggleSideBar = () => {
      store.dispatch(SideBarDispatchEnum.toggleSideBar)
    }

    return {
      mainRoute, 
      subRoute,
      numNotifications,
      toggleSideBar,
    }
  },
  components: { HeaderUserIcon }
})
</script>

<template>
  <header>
    <div class="left-side">
      <span class="material-symbols-outlined" @click="toggleSideBar">menu</span>
      <div class="main-route">{{ mainRoute }}<span>/</span></div>
      <div class="sub-route">{{ subRoute }}</div>
    </div>
    <div class="right-side">
      <div class="bell">
        <span class="material-icons">notifications</span>
        <div class="notification">{{ numNotifications }}</div>
      </div>
      <HeaderUserIcon />
    </div>
  </header>
</template>

<style lang="scss" scoped>
header {
  background: var(--c-white);
  width: 100%;
  display: flex;
  flex-grow: 0;
  justify-content: space-between;
  padding: var(--s-regular) var(--s-medium);
}
.left-side, .right-side {
  display: flex;
  align-items: center;
}
.left-side {
  font-size: var(--f-s-semi-regular);
  text-transform: capitalize;
  span {
    margin-right: var(--s-medium);
  }
  .main-route {
    color: var(--c-light-regular);
    span {
      margin: 0 var(--s-small);
    }
  }
  .sub-route {
    font-weight: var(--f-w-semi-bold);
  }
}
.right-side {
  .bell {
    cursor: pointer;
    .notification {
      background: var(--c-secondaryHighlight);
      color: var(--c-white);
      text-align: center;
      border-radius: var(--b-r-small);
      font-size: var(--f-s-small);
      margin-top: -40px;
      margin-left: 15px;
    }
    margin-right: var(--s-medium);
  }
}
</style>
