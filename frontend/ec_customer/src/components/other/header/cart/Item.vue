<script lang="ts">
import { ItemListDispatchEnum } from '@/enum/Dispatch'
import { ItemListGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  props: {
    item: {
      required: true,
      type: Object,
    }
  },
  setup(props) {
    const store = useStore()
    const currency = computed(() => store.getters[ItemListGetterEnum.currency])
    
    const increaseQuantity  = () => {
      store.dispatch(ItemListDispatchEnum.increaseQuantity, props.item)
    }
    const decreaseQuantity = () => {
      store.dispatch(ItemListDispatchEnum.decreaseQuantity, props.item)
    }
    const resetQuantity = () => {
      store.dispatch(ItemListDispatchEnum.resetQuantity, props.item)
    }
    const removeItem = () => {
      store.dispatch(ItemListDispatchEnum.removeFromCart, props.item)
    }
    
    return {
      currency,
      increaseQuantity,
      decreaseQuantity,
      resetQuantity,
      removeItem,
    }
  },
})
</script>

<template>
  <div class="item-wrapper">
    <img :src="item.photo" />
    <div class="purchase-info">
      <div class="title">{{ item.name }}</div>
      <div class="quantity">
        <div class="button">
          <span class="material-symbols-outlined btn" @click="removeItem">delete_forever</span>
          <span class="material-symbols-outlined btn" @click="resetQuantity">autorenew</span>
        </div>
        <div class="quantity-manipulation">
          <div class="btn" @click="decreaseQuantity">-</div>
          <div>{{ item.orderQuantity }}</div>
          <div class="btn" @click="increaseQuantity">+</div>
        </div>
      </div>
      <div class="money-wrapper">
        <span class="material-symbols-outlined">payments</span>
        <div class="money">{{ item.orderQuantity * item.unitPrice }}</div>
        <div class="currency">{{ currency }}</div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.item-wrapper {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: var(--s-medium);
  border-bottom: var(--b-s-small) solid var(--c-grey);
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);

  &:hover {
    background-color: rgb(255, 255, 255, 0.1);
  }
}
img {
  cursor: pointer;
  width: 90px;
  height: 90px;
  border-radius: var(--b-r-small);
  margin-right: var(--s-medium);
}
.title {
  display: flex;
  justify-content: stretch;
  overflow-wrap: break-word;
}
.material-symbols-outlined {
  &.btn {
    border-radius: var(--b-r-small);
    border: var(--b-s-small) solid var(--c-grey);
    padding: var(--s-small);
    margin-right: var(--s-small);
  }
}
.purchase-info {
  display: flex;
  flex-grow: 2;
  flex-direction: column;
  gap: var(--s-small);
}
.quantity {
  display: flex;
  justify-content: space-between;
}
.quantity-manipulation {
  display: flex;
  gap: var(--s-medium);
  align-items: center;
  border-radius: var(--b-r-small);
  border: var(--b-s-small) solid white;
  padding: 0 var(--s-medium);
  .btn {
    cursor: pointer;
  }
}
.money-wrapper {
  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: stretch;
  .material-symbols-outlined {
    cursor: default;
  }
  .money {
    margin-right: var(--s-small);
    text-align: right;
    flex-grow: 1;
  }
}
</style>