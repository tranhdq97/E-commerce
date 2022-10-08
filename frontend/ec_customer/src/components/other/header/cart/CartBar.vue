<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartGetterEnum, ItemListGetterEnum } from '@/enum/Getter'
import type { ItemType } from '@/interfaces/Cart'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import ItemList from './ItemList.vue'

export default defineComponent({
  setup() {
    const store = useStore();
    const isOpenCart = computed(() => store.getters[CartGetterEnum.isOpenCart]);
    const currency = computed(() => store.getters[ItemListGetterEnum.currency])
    const total = computed(() => store.getters[ItemListGetterEnum.addedItemList].reduce(
        (sum: number, item: ItemType) => sum + item.orderQuantity * item.unitPrice, 0  
      )
    )

    const closeCart = () => {
      store.dispatch(CartDispatchEnum.closeCart);
    };
    return {
      isOpenCart,
      closeCart,
      total,
      currency,
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
    <ItemList />
    <div class="total-wrapper" >
      <div class="total">
        <div>Total:</div>
        <div>{{ total }} {{ currency }}</div>
      </div>
      <div class="checkout">
        Checkout
      </div>
    </div>
  </div>
  
</template>

<style lang="scss" scoped>
.title {
  display: flex;
  justify-content: center;
  padding: var(--s-small);
  border-bottom: var(--b-s-regular) solid var(--c-grey);
  font-size: var(--f-s-header-3);
  font-weight: var(--f-w-extra-bold);
  flex-grow: 0;
  background: var(--c-transparent);
}
.total-wrapper {
  display: flex;
  flex-direction: column;
  flex-grow: 0;
  background: var(--c-transparent);
  padding: var(--s-small) var(--s-medium) var(--s-medium) var(--s-medium);
  border-top: var(--b-s-regular) solid var(--c-grey);
  gap: var(--s-small);
  .total {
    display: flex;
    justify-content: space-between;
  }
  .checkout {
    cursor: pointer;
    background: var(--c-primaryHighlight);
    border-radius: var(--b-r-normal);
    padding: var(--s-small);
    text-align: center;
    font-size: var(--f-s-header-3);
    font-weight: var(--f-w-semi-bold);
  }
}
.cart-wrapper {
  display: flex;
  flex-direction: column;
  margin-top: 71px;
  padding-bottom: 71px;
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  min-width: 350px;
  max-width: 400px;
}
</style>
