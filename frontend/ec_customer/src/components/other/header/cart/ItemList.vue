<script lang="ts">
import { ItemListGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import Item from './Item.vue'

export default defineComponent({
  setup() {
    const store = useStore()
    const itemList = computed(() => store.getters[ItemListGetterEnum.addedItemList])

    return {
      itemList,
    }
  },
  components: { Item }
})
</script>

<template>
  <div class="item-list">
    <Item 
      v-for="item in itemList"
      :key="item.id"
      :item=item
    />
  </div>
</template>

<style lang="scss" scoped>
.item-list {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  overflow-y: auto;
  background: var(--c-transparent);
  &::-webkit-scrollbar {
    width: 5px;
    border-right: var(--b-s-small) solid var(--c-primaryHighlight);
  }
  &::-webkit-scrollbar-thumb {
    background: var(--c-primaryHighlight);
    border-top-left-radius: var(--b-s-small);
    border-bottom-left-radius: var(--b-s-small);
  }
}

</style>