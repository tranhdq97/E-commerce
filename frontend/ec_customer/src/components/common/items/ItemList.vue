<script lang="ts">
import { ItemListGetterEnum } from '@/enum/Getter';
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex';
import Item from './Item.vue'

export default defineComponent({
  setup() {
    const store = useStore()
    const itemList = computed(() => store.getters[ItemListGetterEnum.itemList])

    return {
      itemList,
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
    />
    <div class="last-item"></div>
  </div>
</template>

<style lang="scss" scoped>
.item-list-wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: var(--s-large);
}
.last-item {
  flex-grow: 1;
}

</style>
