<script lang="ts">
import { defineComponent, ref } from 'vue'
import ItemList from '@/components/common/items/ItemList.vue'
import OrderFactor from '@/components/other/OrderFactor.vue'
import type { OrderFactorType } from '@/interfaces/OrderFactorType'
import { orderFactorIconEnum, orderFactorNameEnum, orderFactorPropertyEnum } from '@/enum/OrderMapping'


export default defineComponent({
  setup() {
    const orderFactors = ref<OrderFactorType[]>([
      {
        name: orderFactorNameEnum.all,
        icon: orderFactorIconEnum.all,
        isAllMode: true,
        property: null
      },
      {
        name: orderFactorNameEnum.name,
        icon: orderFactorIconEnum.name,
        isAllMode: false,
        property: orderFactorPropertyEnum.name
      },
      {
        name: orderFactorNameEnum.price,
        icon: orderFactorIconEnum.price,
        isAllMode: false,
        property: orderFactorPropertyEnum.price
      },
      {
        name: orderFactorNameEnum.numOrders,
        icon: orderFactorIconEnum.numOrders,
        isAllMode: false,
        property: orderFactorPropertyEnum.numOrders
      },
      {
        name: orderFactorNameEnum.numStars,
        icon: orderFactorIconEnum.numStars,
        isAllMode: false,
        property: orderFactorPropertyEnum.numStars
      },
      {
        name: orderFactorNameEnum.numVotes,
        icon: orderFactorIconEnum.numVotes,
        isAllMode: false,
        property: orderFactorPropertyEnum.numVotes
      },
      {
        name: orderFactorNameEnum.quantity,
        icon: orderFactorIconEnum.quantity,
        isAllMode: false,
        property: orderFactorPropertyEnum.quantity
      },
      {
        name: orderFactorNameEnum.category,
        icon: orderFactorIconEnum.category,
        isAllMode: false,
        property: orderFactorPropertyEnum.category
      },
    ])

    const isFixedOrderBar = ref(false)
    const bannerHeight = 500
    const headerHeight = 71
    const scrolling = (e) => {
      // 500: height of banner
      // 71: height of header
      isFixedOrderBar.value = e.target.scrollTop > bannerHeight - headerHeight ? true : false
    }
    
    return {
      isFixedOrderBar,
      orderFactors,
      scrolling,
    }
  },
  components: { ItemList, OrderFactor }
})
</script>

<template>
  <main @scroll="scrolling">
    <div class="banner-wrapper">
      <div class="banner">Banner SECTION</div>
    </div>
    <div :class="isFixedOrderBar ? 'order fixed' : 'order'">
      <OrderFactor v-for="orderFactor in orderFactors" :key="orderFactor.name" :factor="orderFactor" />
    </div>
    <div class="item-list">
      <ItemList />
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
}
.banner-wrapper {
  display: flex;
  background: linear-gradient(0deg, rgba(108,99,255,1) 0%, rgba(141,134,255,1) 30%, rgba(147,140,255,1) 50%, rgba(138,131,255,1) 70%, rgba(108,99,255,1) 100%);
  .banner {
    display: flex;
    align-items: center;
    height: var(--bannerHeight);
  }
}
.item-list {
  padding: var(--s-large);
  display: flex;
}
.order {
  justify-content: space-between;
  display: flex;
  padding: var(--s-medium);
  border-bottom: var(--b-s-regular) solid var(--c-grey);
  &.fixed {
    position: fixed;
    background: var(--c-white);
    padding-top: calc(var(--headerHeight) + var(--s-medium));
    z-index: 97;
    width: 100%;
    transition: var(--t-regular);
  }
}

</style>