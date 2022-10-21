<script lang="ts">
import type { CommonMaster } from '@/interfaces/Master'
import { computed, defineComponent, ref } from 'vue'

export default defineComponent({
  props: {
    itemList: { required: false, type: Array, default: [], },
    title: { required: true, type: String, },
    placeHolder: { required: false, type: String, },
    isClickable: { required: false, type: Boolean, default: false},
    field: { required: true, type: Object, },
    isDisabled: { required: false, default: false, type: Boolean },
  },
  emits: ['updateField', 'selectRecommendation',],
  setup(props, {emit}) {
    const isOpenRecommendations = ref(false)
    const recommendationList = computed(() => props.itemList.filter((item) => {
      return item.name.toLowerCase().search(props.field.name.toLowerCase()) !== -1 ? true : false
    }))

    const toggleOpenRecommendations = () => {
      if (recommendationList.value.length > 0 && props.field.name.length > 0) {
        isOpenRecommendations.value = true
      } else {
        isOpenRecommendations.value = false
      }
    }
    const onChange = (item: CommonMaster) => {
      toggleOpenRecommendations()
      props.field.name.length === 0 || (props.field.name.length > 0 && item.id) ? emit('updateField', { ...item, id: null }) : null
    }
    const closeRecommendations = () => isOpenRecommendations.value = false
    const selectRecommendation = (item: CommonMaster) => {
      emit('updateField', item)
      emit('selectRecommendation', item)
      isOpenRecommendations.value = false
    }
    return {
      recommendationList,
      isOpenRecommendations,
      onChange,
      closeRecommendations,
      selectRecommendation,
    }
  },
})
</script>

<template>
  <div class="wrapper">
    <div :class="isDisabled ? 'title is-disabled' : 'title'">{{ title }}</div>
    <input
      :class="field.isAdded ? 'is-added' : isDisabled ? 'is-disabled' : ''"
      type="text"
      :placeholder="placeHolder" 
      :value="field.name"
      @input="(e) => $emit('updateField', { ...field, name: e.target.value })"
      @keyup="onChange(field)"
    />
    <div
      class="recommendations"
      v-show="isOpenRecommendations"
      v-click-outside="closeRecommendations"
    >
      <div class="items">
        <div
          class="item exclude"
          v-for="item in recommendationList"
          :key="item.id"
          @click="isClickable ? selectRecommendation(item) : null"
        >
        {{ item.name }}
        </div>
      </div>
      <div class="item similar">
        There are {{ recommendationList.length }} similar one...
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: var(--s-medium);
  min-width: 250px;
}
.title {
  text-transform: capitalize;
  font-size: var(--f-s-semi-regular);
  font-weight: var(--f-w-semi-bold);
  margin-bottom: var(--s-small);
  color: var(--c-primary);
  &.is-disabled {
    color: var(--c-grey);
  }
}
input {
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
  padding: var(--s-medium);
  border-radius: var(--b-r-small);
  background: var(--c-enter-transparent);
  text-transform: capitalize;
  &.is-disabled {
    pointer-events: none;
  }
}
.recommendations {
  display: flex;
  flex-direction: column;
  z-index: 98;
  position: fixed;
  margin-top: 71px;
  min-width: 250px;
  max-height: 200px;
  cursor: pointer;
  .items {
    overflow: auto;
    &::-webkit-scrollbar {
      background: var(--c-enter-transparent);
      width: 3px;
    }
    &::-webkit-scrollbar-thumb {
      background: var(--c-primary);
    }
  }
}
.item {
  display: flex;
  background: var(--c-white-transparent);
  border-bottom: 1px solid var(--b-c-regular);
  padding: 2px var(--s-medium);
  font-size: var(--f-s-small);
  font-weight: var(--f-w-medium);
  color: var(--c-light-regular);
  &.exclude {
    text-transform: capitalize;
  }

  &.similar {
    display: flex;
    justify-content: center;
    border-bottom-left-radius: var(--b-r-small);
    border-bottom-right-radius: var(--b-r-small);
  }
}
.is-added {
  background: var(--c-remarkable);
  transition: ease-out var(--t-o-add);
}
</style>
