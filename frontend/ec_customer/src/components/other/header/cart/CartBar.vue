<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import ItemList from './ItemList.vue'

export default defineComponent({
  setup() {
    const store = useStore();
    const isOpenCart = computed(() => store.getters[CartGetterEnum.isOpenCart]);
    const itemList = computed(() => store.getters[CartGetterEnum.itemList])
    const closeCart = () => {
      store.dispatch(CartDispatchEnum.closeCart);
    };
    return {
      itemList,
      isOpenCart,
      closeCart,
    };
  },
  components: { ItemList }
})
</script>

<template>
  <div
    class="cart-wrapper"
    v-if="isOpenCart"
  >
    <div class="title">Your Cart</div>
    <ItemList :itemList="itemList" />
    <div class="total" >Total: </div>
  </div>
  
</template>

<style lang="scss" scoped>
.title {
  width: 350px;
  display: flex;
  justify-content: center;
  padding: var(--s-large);
  border-bottom: 3px solid var(--c-grey);
  font-size: var(--f-s-header-3);
  font-weight: var(--f-w-extra-bold);
}
.cart-wrapper {
  margin-top: 52px;
  position: fixed;
  right: 0;
  height: 100vh;
  background: var(--c-transparent);
}
</style>
