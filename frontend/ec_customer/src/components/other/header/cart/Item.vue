<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartMutationEnum } from '@/enum/Mutation'
import { defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  props: {
    item: {
      required: true,
      type: Object
    }
  },
  setup(props ) {
    const store = useStore()

    const increaseQuantity  = () => {
      store.commit(CartMutationEnum.increaseItemQuantity, props.item)
    }
    const decreaseQuantity = () => {
      store.commit(CartMutationEnum.decreaseItemQuantity, props.item)
    }
    const resetQuantity = () => {

    }
    const removeItem = () => {
      
    }
    
    return {
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
      <div>
        <div class="title">{{ item.name }}</div>
      </div>
      
      <div class="quantity">
        <div class="button">
          <span class="material-symbols-outlined">delete_forever</span>
          <span class="material-symbols-outlined">autorenew</span>
        </div>
        <div class="quantity-manipulation">
          <div class="btn" @click="decreaseQuantity">-</div>
          <div>{{ item.orderQuantity }}</div>
          <div class="btn" @click="increaseQuantity">+</div>
        </div>
      </div>
      <div class="money-wrapper">
        <span class="material-symbols-outlined">money</span>
        <div class="money">{{ item.orderQuantity * item.unitPrice }}</div>
        <div class="currency">{{ item.currency }}</div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.item-wrapper {
  display: flex;
  flex-direction: row;
  padding: var(--s-medium);
  border-bottom: 1px solid var(--c-grey);
}
img {
  width: 80px;
  height: 80px;
  border-radius: var(--b-r-small);
  margin-right: var(--s-medium);
}
.title {
  display: flex;
  width: 100%;
  overflow-wrap: break-word;
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
}
.material-symbols-outlined {
  border-radius: var(--b-r-small);
  border: 1px solid white;
  padding: var(--s-small);
  margin-right: var(--s-small);
}
.purchase-info {
  width: 220px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.quantity {
  width: 100%;
  display: flex;
}
.quantity-manipulation {
  display: flex;
  gap: var(--s-medium);
  align-items: center;
  border-radius: var(--b-r-small);
  border: 1px solid white;
  padding: 0 var(--s-medium);
}
.btn {
  cursor: pointer;
}
.money-wrapper {
  display: flex;
  flex-direction: row;
  align-content: center;
}

</style>