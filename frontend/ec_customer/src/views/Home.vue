<script lang="ts">
import { CartDispatchEnum } from '@/enum/Dispatch'
import { CartGetterEnum } from '@/enum/Getter'
import type { ItemType } from '@/interfaces/Cart'
import { defineComponent, ref } from 'vue'
import { useStore } from 'vuex'
import Item from '../components/common/items/Item.vue'

export default defineComponent({
  setup() {
    const store = useStore();
    const item = {
      id: 1,
      name: "Fruitylicious markisa",
      quantity: 1,
      photo: "http://127.0.0.1:8003/media/1/2022/10/01/3c0cca8a2610ea88f1d398037c16cb90..jpg",
      unitPrice: 1500,
      isAdded: false,
      numStars: 4.3,
      currency: 'VND',
      numberVotes: 1223,
      numberOrders: 12000,
    };
    const item2 = { ...item }
    item2.numStars = 1.2
    item2.id = 2
    const itemList = ref([item, item2])

    const addItemToCart = (item: ItemType) => {
      item.isAdded = true
      store.dispatch(CartDispatchEnum.addItemToCart, item);
    };
    const removeItemFromCart = (item: ItemType) => {
      item.isAdded = false
      store.dispatch(CartDispatchEnum.removeItemFromCart, item);
    };
    return {
      item,
      itemList,
      addItemToCart,
      removeItemFromCart,
    };
  },
  components: { Item }
})
</script>

<template>
  <main>
    <div class="test">
    </div>
    <div class="item-list">
      <Item 
        v-for="item in itemList" 
        :key="item.id" 
        array_index=1
        :item="item"
        @addToCart="addItemToCart(item)"
        @removeFromCart="removeItemFromCart(item)"
      />
    </div>
  </main>
</template>

<style scoped>
main {
}
.test {
  background: linear-gradient(0deg, rgba(108,99,255,1) 0%, rgba(141,134,255,1) 30%, rgba(147,140,255,1) 50%, rgba(138,131,255,1) 70%, rgba(108,99,255,1) 100%);
  height: 40vh;
}
.item-list {
  padding: 10px 30px 10px 30px;
  display: flex;
  gap: var(--s-large);
}

</style>