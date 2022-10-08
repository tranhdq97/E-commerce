<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartGetterEnum } from '@/enum/Getter'
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex'
import CartBar from './cart/CartBar.vue'

export default defineComponent({
    setup() {
        const store = useStore();
        const numberOfUniqueItems = computed(() => store.getters[CartGetterEnum.numberOfUniqueItems]);
        const currency = computed(() => store.getters[CartGetterEnum.currency]);
        const itemList = computed(() => store.getters[CartGetterEnum.itemList]);
        const isOpenCart = computed(() => store.getters[CartGetterEnum.isOpenCart]);
        const toggleCart = () => {
            store.dispatch(CartDispatchEnum.toggleCart);
        };
        return {
            currency,
            itemList,
            isOpenCart,
            numberOfUniqueItems,
            toggleCart,
        };
    },
    components: { CartBar }
})
</script>

<template>
  <div class="wrapper">
    <div
      :class="isOpenCart ? 'icon isOpenCart' : 'icon'"
      @click="toggleCart"  
    >
      <span class="material-symbols-outlined">shopping_cart</span>
    </div>
    <div class="number">{{ numberOfUniqueItems }}</div>
    <CartBar />
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
}
.icon {
  cursor: pointer;
  display:flex;
  align-items:center;
  padding: var(--b-r-small);
  border-radius: var(--b-r-small);
}
.isOpenCart {
  background: var(--c-primary);
  transition: ease-in 0.4s;
}
.number {
  color: var(--c-primary);
  font-weight: var(--f-w-semi-bold);
  margin-left: -5px;
  margin-top: 20px;
  background: var(--c-remarkable);
  position: absolute;
  padding: 0px 1px;
  text-align: center;
  border-radius: var(--b-r-small);
}
</style>
