<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartGetterEnum } from '@/enum/Getter'
import { CartStateEnum } from "@/enum/State"
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  setup() {
    const store = useStore()
    const numberOfUniqueItems = computed(() => store.getters[CartGetterEnum.numberOfUniqueItems])
    const currency = computed(() => store.getters[CartGetterEnum.currency])
    const itemList = computed(() => store.getters[CartGetterEnum.itemList])

    const toggleCart = () => {
      store.dispatch(CartDispatchEnum.toggleCart)
    }

    return {
      currency,
      itemList,
      numberOfUniqueItems,
      toggleCart,
    }
  },
})
</script>

<template>
  <div class="wrapper" @click="toggleCart">
    <div class="icon">
      <span class="material-symbols-outlined">shopping_cart</span>
    </div>
    <div class="number">{{ numberOfUniqueItems }}</div>
    </div>
</template>

<style lang="scss" scoped>
.wrapper {
  cursor: pointer;
  display: flex;
}
.icon {
  cursor: pointer;
  display:flex;
  align-items:center;
}
.number {
  color: var(--c-primary);
  font-weight: var(--f-w-semi-bold);
  margin-left: -5px;
  margin-top: 20px;
  background: yellow;
  padding: 0px 1px;
  text-align: center;
  border-radius: var(--b-r-small);
}
</style>
