<script lang="ts">
import { CartGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  setup() {
    const store = useStore()

    const isOpenCart = computed(() => store.getters[CartGetterEnum.isOpenCart])

    return {
      isOpenCart,
    }    
  },
})
</script>

<template>
  <aside v-if="isOpenCart">
    adasdadsfas
  </aside>
  
</template>

<style lang="scss" scoped>

aside {
  z-index: 101;
  position: fixed;
  margin-top: 70px;
  background: rgb(0, 0, 0, 0.3);
  display: flex;
  height: 100vh;
  right: 0;
}
</style>
