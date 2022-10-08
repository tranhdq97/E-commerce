<script lang="ts">
import { CartGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import Item from './Item.vue'

export default defineComponent({
  props: {
    itemList: {
      required: true,
      type: Array
    }
  },
  setup() {
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
}

</style>