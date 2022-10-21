<script lang="ts">
import { ProductCategoryGetterEnum } from '@/enum/Getter';
import { computed, defineComponent, ref, watch } from 'vue';
import { useStore } from 'vuex';


export default defineComponent({
  props: {
    title: {
      required: true, 
      type: String,
    }
  },
  setup() {
    const store = useStore()
    const categoryTempList = computed(() => store.getters[ProductCategoryGetterEnum.categoryList])
    const categoryList = ref([ ...categoryTempList.value ])
    const isToEnd = ref(true)

    const moveItemToEnd = () => categoryList.value.push(categoryList.value.shift())
    const toggleToEndFlag = () => isToEnd.value = !isToEnd.value

    watch(categoryTempList.value, () => {
      categoryList.value = [ ...categoryTempList.value ]
    })
    watch(isToEnd, () => {
      if (isToEnd.value) {
        setTimeout(() => {
          moveItemToEnd()
          toggleToEndFlag()
        }, 3000)
      } else { toggleToEndFlag() }
    })
    isToEnd.value = false

    return {
      categoryList,
    }
  }
})
</script>

<template>
  <div class="wrapper">
    <div class="header">{{ title }}</div>
    <div class="category-list">
      <div
        v-for="(category, index) in categoryList" 
        :key="category.id" 
        :class="index === 0 ? 'main to-end' : 'main'"
      >
        <div class="name">{{ category.name }}</div>
        <span :style="{backgroundColor: category.color}">
          {{ category.numChildren }}
        </span>
    </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.wrapper {
  height: 400px;
  background: var(--c-white);
  display: flex;
  flex-direction: column;
  border-radius: var(--b-r-normal);
  padding-bottom: var(--s-regular);
  box-shadow: 3px 3px 5px var(--c-grey);
}
.header {
  display: flex;
  padding: var(--s-medium);
  border-bottom: var(--b-s-small) solid var(--b-c-regular);
  text-transform: capitalize;
  font-size: var(--f-s-header-4);
  font-weight: var(--f-w-regular);
  justify-content: center;
}
.to-end {
  animation-name: to-end;
  animation-duration: 3s;
}
.main {
  padding: var(--s-small);
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-transform: capitalize;
  white-space: nowrap;
  gap: var(--s-medium);
  span {
    border-radius: var(--b-r-semi-large);
    padding: 3px var(--s-medium);
    color: var(--c-white);
    font-weight: var(--f-w-semi-bold);
  }
  .name {
    overflow: hidden;
    padding-left: var(--s-small);
  }
}
.category-list {
  padding: var(--s-small) var(--s-medium);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  &::-webkit-scrollbar-thumb {
    background: none;
  }
  &:hover::-webkit-scrollbar-thumb {
    background: var(--c-highlight);
  }
}

@keyframes to-end {
  50% {
    width: 100%;
  }
  100% {
    width: 0;
    gap: 0;
  }
}
</style>
