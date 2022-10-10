<script lang="ts">
import { computed, defineComponent } from 'vue'

export default defineComponent({
  props: {
    numberStars: {
      required: true,
      type: Number,
    },
    numberVotes: {
      required: true,
      type: Number,
    }
  },
  setup(props) {
    const roundedStars = computed(() => {
      const stars = Math.round(props.numberStars)
      return stars < 0 ? 0 : ( stars > 5 ? 5 : stars )
    })
    return { roundedStars }
  },
})
</script>

<template>
  <div class="star-wrapper">
    <div v-for="i in roundedStars" :key="i" class="stars">
      <span class="material-icons">grade</span>
    </div>
    <div v-for="i in 5 - roundedStars" :key="i" class="stars"  >
      <span class="material-icons">star_outline</span>
    </div>
    <div class="number-votes">({{ numberVotes }})</div>
  </div>
  
</template>

<style lang="scss" scoped>
.star-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: var(--s-small) 0;
}
.number-votes {
  color: var(--c-grey);
  font-size: var(--f-s-semi-small);
  margin-left: var(--s-small);
}
.stars {
  display: flex;
}
span {
  font-size: var(--f-s-semi-regular);
  color: var(--c-yellow);
}
</style>