<script lang="ts">
import { ItemListDispatchEnum } from '@/enum/Dispatch';
import { ItemListGetterEnum } from '@/enum/Getter';
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex';

export default defineComponent({
  props: {
    factor: {
      required: true,
      type: Object,
    },
  },
  emits: [],
  setup(props) {
    const store = useStore()
    const isCurrentFactor = computed(() => store.getters[ItemListGetterEnum.orderFactor] === props.factor)
    const isDesc = computed(() => store.getters[ItemListGetterEnum.isDesc])

    const orderItemList = () => {
      store.dispatch(ItemListDispatchEnum.orderItemList, props.factor)
    }

    return {
      isDesc,
      isCurrentFactor,
      orderItemList,
    }    
  },
})
</script>
<template>
  <div class="order-wrapper" @click="orderItemList">
      <span class="material-symbols-outlined">{{ factor.icon }}</span>
    <div class="name">{{ factor.name }}</div>
    <div class="is-search" v-if="isCurrentFactor && !factor.isAllMode">
      <span class="material-symbols-outlined" v-if="isDesc">south</span>
      <span class="material-symbols-outlined" v-else>north</span>
    </div>
  </div>
  
</template>
<style lang="scss" scoped>
.order-wrapper {
  display: flex;
  align-items: center;
  cursor: pointer;
  span {
    font-size: var(--f-s-header-3);
    margin-right: var(--s-small);
  }
  .name {
    font-size: var(--f-s-regular);
    font-weight: var(--f-w-semi-bold);
  }
}
.is-search {
  display: flex;
  span {
    font-size: var(--f-s-semi-small);
  }
}
</style>