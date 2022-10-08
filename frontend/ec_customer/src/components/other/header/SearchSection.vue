<script lang="ts">
import { defineComponent, ref } from 'vue'
export default defineComponent({
  setup(props, { emit }) {
    const isBarShowed = ref(false)

    const closeBar = () => { 
      isBarShowed.value = false
      emit('closeBar')
    }
    const openBar = () => {
      isBarShowed.value = true
      emit('openBar')
    }
    const search = () => {
      console.log("Searching")
    }
    const openOrSearch = () => {
      if (isBarShowed.value) {
        search()
      } else {
        openBar()
      }
    }
    return {
      isBarShowed,
      closeBar,
      openBar,
      search,
      openOrSearch,
    }    
  },
})
</script>

<template>
  <div
    :class="isBarShowed?'wrapper searching':'wrapper'" 
    @click="this.$refs.searchArea.focus()"
    v-click-outside="closeBar"
  >
    <input
      ref="searchArea"
      type="text"
      placeholder="Search your product here"
      @keyup.enter="search"
      v-if="isBarShowed"
    />
    <div class="search-icon" @click="openOrSearch">
      <span class="material-symbols-outlined">search</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  border-radius: var(--b-r-normal);
  gap: var(--s-medium);
  transition: ease-out 1s;
  color: var(--c-semi-grey);
  font-size: var(--f-s-semi-regular);
  font-weight: var(--f-w-semi-bold);
  input {
    color: var(--c-white);
    &::placeholder {
      color: var(--c-semi-grey) ;
    }
  }
  &.searching {
    background: rgba(255, 255, 255, 0.2);
    min-width: 50%;
    padding: 0 var(--s-medium) 0 var(--s-large);
    transition: ease-in 1s;
    color: var(--c-white);
  }
}
.search-icon {
  display: flex;
  align-items: center;
  cursor: pointer;
}

</style>