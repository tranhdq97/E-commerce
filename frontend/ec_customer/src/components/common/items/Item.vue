<script lang="ts">
import { ItemListDispatchEnum } from '@/enum/Dispatch'
import { ItemListGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import Star from './Star.vue'

export default defineComponent({
  props: {
    item: {
      required: true,
      type: Object,
    }
  },
  setup(props) {
    const store = useStore()
    const isRunOutQuantity = computed(() => props.item.quantity === 0)
    const currency = computed(() => store.getters[ItemListGetterEnum.currency])

    const addToCart = () => {
      store.dispatch(ItemListDispatchEnum.addToCart, props.item)
    }
    const removeFromCart = () => {
      store.dispatch(ItemListDispatchEnum.removeFromCart, props.item)
    }
    
    return {
      currency,
      isRunOutQuantity,
      addToCart,
      removeFromCart,
    }
  },
  components: { Star }
})
</script>

<template>
  <div class="wrapper">
    <img :src="item.photo" alt="photo" />
    <div class="info-wrapper">
      <div class="name">{{ item.name }}</div>
      <div class="product-info">
        <div class="product-detail">
          <Star :numberStars="item.numStars" :numberVotes="item.numVotes"/>
          <div class="info-text">Quantity: <span>{{ item.quantity }}</span></div>
          <div class="info-text">Price: <span>{{ item.unitPrice }} {{ currency }}</span></div>
          <div class="info-text">No.Orders: <span>{{ item.numOrders }}</span></div>
        </div>
        <div class="add-remove">
          <span
            v-if="!isRunOutQuantity && item.isAdded"
            class="material-icons remove"
            @click="removeFromCart"
          >
            library_add_check
          </span>
          <span
            v-if="!isRunOutQuantity && !item.isAdded"
            class="material-icons add"
            @click="addToCart"
          >
            library_add
          </span>
          <span
            class="material-icons run-out"
            v-if="isRunOutQuantity"
          >
            remove_shopping_cart
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  width: 220px;
  border-radius: var(--b-r-semi-large);
  border: var(--b-s-regular) solid var(--b-c-regular);
}
.info-wrapper {
  .name {
    text-align: center;
    font-size: var(--f-s-semi-regular);
    font-weight: var(--f-w-extra-bold);
    text-transform: capitalize;
    color: var(--c-primary);
    border-bottom: var(--b-s-small) solid var(--b-c-regular);
    border-top: var(--b-s-small) solid var(--b-c-regular);
  }
}
.add-remove {
  padding: 0 var(--s-medium);
  display: flex;
  border-left: var(--b-s-small) solid var(--b-c-regular);
  span {
    cursor: pointer;
    display: flex;
    font-size: var(--f-s-header-2);
    align-items: center;
    &.add {
      color: var(--c-secondary);
    }
    &.remove {
      color: var(--c-remarkable);
    }
    &.run-out {
      color: var(--c-grey);
      cursor: default;
    }
  }
}
.product-info {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}
img {
  border-top-left-radius: var(--b-r-semi-large);
  border-top-right-radius: var(--b-r-semi-large);
  width: 214px;
  height: 214px;
}
.info-text {
  display: flex;
  color: var(--c-secondary);
  font-size: var(--f-s-small);
  font-weight: var(--f-w-semi-bold);
  span {
    flex-grow: 1;
    text-align: right;
  }
}
.product-detail {
  margin:0 0 var(--s-small) var(--s-regular);
}
</style>