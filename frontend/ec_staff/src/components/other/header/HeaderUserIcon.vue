<script lang="ts">
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { RouterEnum } from '@/enum/Router';
import { AuthGetterEnum } from '@/enum/Getter';
import { computed, defineComponent, ref } from 'vue'
import { AuthDispatchEnum } from '@/enum/Dispatch';

export default defineComponent({
  setup() {
    const store = useStore()
    const router = useRouter()
    const routerEnum = RouterEnum
    const isAuthenticated = store.getters[AuthGetterEnum.isAuthenticated]
    const isExpanded = ref(false)
    const photo = computed(() => {
      if (store.getters[AuthGetterEnum.stateUser] && store.getters[AuthGetterEnum.stateUser].photo) {
        return store.getters[AuthGetterEnum.stateUser].photo
      } else {
        return null
      }
    })
    const lang = ref('en')

    const toLogin = () => router.push(routerEnum.login)
    const closeBar = () => isExpanded.value = false
    const toggleBar = () => isExpanded.value = !isExpanded.value
    const logout = () => {
      store.dispatch(AuthDispatchEnum.logout)
      router.push(routerEnum.login)
    }

    return {
      isAuthenticated,
      routerEnum,
      router,
      photo,
      lang,
      toLogin,
      logout,
      isExpanded,
      closeBar,
      toggleBar,
    }
  },
})
</script>

<template>
  <div @click="toggleBar">
    <div class="wrapper">
      <div v-if="isAuthenticated" class="photo">
        <img :src="photo" v-if="photo"/>
        <div v-else class="default_photo">
          <span class="material-symbols-outlined" >person</span>
        </div>
      </div>
      <span @click="toLogin" v-else class="material-symbols-outlined" >person</span>
    </div>
    <div class="expand-mode" v-show="isExpanded" @mouseleave="closeBar">
      <div class="item" @click="router.push(routerEnum.home)">
        <span class="material-symbols-outlined">account_circle</span>
        <div class="title">Profile</div>
      </div>
      <div class="item" @click="router.push(routerEnum.home)">
        <span class="material-symbols-outlined">language</span>
        <div class="title">
          Language: {{ lang.toUpperCase() }}
        </div>
      </div>
      <div class="item" @click="router.push(routerEnum.home)">
        <span class="material-symbols-outlined">settings</span>
        <div class="title">Settings</div>
      </div>
      <div class="item" @click="logout">
        <span class="material-symbols-outlined">logout</span>
        <div class="title">Logout</div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  cursor: pointer;
  display: flex;
}
.photo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items:center;
}
img {
  cursor: pointer;
  width: 100%;
  height: 100%;
  border-radius: var(--b-r-small);
  border: 2px solid var(--c-lightgrey);
  background: var(--c-white);
}
.default_photo {
  display: flex;
  justify-content: center;
  color: var(--c-grey);
  width: 100%;
  height: 100%;
  border-radius: var(--b-r-small);
  background: var(--c-lightgrey);
  align-items: center;
  span {
    font-size: 28px;
  }
}
.expand-mode {
  margin: var(--s-medium) 0;
  padding: var(--s-small) 0;
  background: rgba(0, 0, 0, 0.8);
  z-index: 99;
  position: fixed;
  display: flex;
  flex-direction: column;
  gap: var(--s-small);
  right: 0;
  .item {
    cursor: pointer;
    padding: var(--s-small) var(--s-regular);
    display: flex;
    justify-content: left;
    align-items: center;
    font-size: var(--f-s-semi-small);
    font-weight: var(--f-w-medium);
    span {
      height:100%;
      margin-right: var(--s-small);
    }
    .title {
      color: var(--c-white);
      text-decoration: none;
      white-space: nowrap;
    }
    &:hover {
      background: rgba(50, 50, 50, 0.8)
    }
  }
}
</style>