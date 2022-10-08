<script lang="ts">
import { defineComponent, ref } from 'vue'
import Item from '../components/common/items/Item.vue'
import ItemList from '../components/common/items/ItemList.vue'

export default defineComponent({
  setup() {
    const item = {
      id: 1,
      name: "Fruitylici asdasd",
      quantity: 10,
      photo: "http://127.0.0.1:8003/media/1/2022/10/01/3c0cca8a2610ea88f1d398037c16cb90..jpg",
      unitPrice: 1500,
      isAdded: false,
      numStars: 4.3,
      orderQuantity: 0,
      currency: 'VND',
      numberVotes: 1223,
      numberOrders: 12000,
    };
    const item2 = { ...item }
    item2.numStars = 1.2
    item2.id = 2
    const itemList = ref([item, item2])

    return {
      itemList,
    };
  },
  components: { ItemList }
})
</script>

<template>
  <main>
    <div class="test">
    </div>
    <div class="item-list">
      <ItemList :itemList="itemList"/>
    </div>
  </main>
</template>

<style scoped>
.test {
  background: linear-gradient(0deg, rgba(108,99,255,1) 0%, rgba(141,134,255,1) 30%, rgba(147,140,255,1) 50%, rgba(138,131,255,1) 70%, rgba(108,99,255,1) 100%);
  height: 80vh;
}
.item-list {
  padding: 10px 30px 10px 30px;
  display: flex;
  gap: var(--s-large);
}

</style>