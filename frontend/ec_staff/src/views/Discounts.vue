<script lang="ts">
import { SideBarDispatchEnum } from '@/enum/Dispatch'
import { RouterEnum } from '@/enum/Router'
import { SideBarEnum } from '@/enum/SideBar'
import { defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  setup() {
    const store = useStore()
    store.dispatch(SideBarDispatchEnum.selectRoute, {
      mainRoute: SideBarEnum.products,
      subRoute: RouterEnum.discountsName,
    })
  },
})
</script>


<template>
  <div class="page">
    <h1>This is an discounts page</h1>
  </div>
</template>

<style>
</style>
