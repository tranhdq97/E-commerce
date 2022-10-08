<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch';
import type { ItemType } from '@/interfaces/Cart';
import { defineComponent } from 'vue'
import { useStore } from 'vuex';
import Item from './Item.vue'

export default defineComponent({
  emits: ['addToCart', 'removeFromCart'],
  props: {
    itemList: {
      required: true,
      type: Array
    }
  },
  setup() {
    const store = useStore()

    const addItemToCart = (item: ItemType) => {
      item.isAdded = true
      store.dispatch(CartDispatchEnum.addItemToCart, item);
    };
    const removeItemFromCart = (item: ItemType) => {
      item.isAdded = false
      store.dispatch(CartDispatchEnum.removeItemFromCart, item);
    };

    return {
      addItemToCart,
      removeItemFromCart,
    }
  },
  components: { Item }
})
</script>

<template>
  <div class="item-list-wrapper">
    <Item 
      v-for="item in itemList" 
      :key="item.id" 
      :item="item"
      @addToCart="addItemToCart(item)"
      @removeFromCart="removeItemFromCart(item)"
    />
  </div>
</template>

<style lang="scss" scoped>

</style>
