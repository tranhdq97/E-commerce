<script lang="ts">
import { defineComponent } from 'vue'
import Star from './Star.vue'

export default defineComponent({
  props: {
    item: {
      required: true,
      type: Object,
    }
  },
  emits: ['addToCart', 'removeFromCart'],
  setup() {
  },
  components: { Star }
})
</script>

<template>
  <div class="wrapper">
    <div class="photo">
      <img :src="item.photo" alt="photo" />
    </div>
    <div class="info-wrapper">
      <div class="name">{{ item.name }}</div>
      <div class="product-info">
        <div class="product-detail">
          <Star :numberStars="item.numStars" :numberVotes="item.numberVotes"/>
          <div class="info-text">Price: {{ item.unitPrice }} {{ item.currency }}</div>
          <div class="info-text">No.Orders: {{ item.numberOrders }}</div>
        </div>
        <div class="add-remove">
          <span
            v-if="item.isAdded" 
            class="material-icons remove"
            @click="$emit('removeFromCart')"
          >
            library_add_check
          </span>
          <span
            v-else
            class="material-icons add"
            @click="$emit('addToCart')"
          >
            library_add
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
  width: 280px;
  border-radius: var(--b-r-semi-large);
  border: var(--b-s-regular) solid var(--b-c-regular);
}
.info-wrapper {
  padding-bottom: var(--s-regular);
  .name {
    text-align: center;
    font-size: var(--f-s-header-4);
    font-weight: var(--f-w-extra-bold);
    text-transform: capitalize;
    color: var(--c-primary);
    border-bottom: var(--b-s-small) solid var(--b-c-regular);
    border-top: var(--b-s-small) solid var(--b-c-regular);
  }
}
.add-remove {
  margin-right: var(--s-medium);
  display: flex;
  span {
    cursor: pointer;
    display: flex;
    font-size: var(--f-s-header-1);
    align-items: center;
    &.add {
      color: var(--c-secondary);
    }
    &.remove {
      color: var(--c-remarkable);
    }
  }
}
.product-info {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}
.photo {
  width: inherit;
  height: 280px;
  align-items: center;
  justify-content: center;
  img {
    border-top-left-radius: var(--b-r-semi-large);
    border-top-right-radius: var(--b-r-semi-large);
    width: 276px;
    height: 279px;
  }
}
.info-text {
  color: var(--c-secondary);
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-semi-bold);
}
.product-detail {
  margin-left: var(--s-regular);
}
</style>