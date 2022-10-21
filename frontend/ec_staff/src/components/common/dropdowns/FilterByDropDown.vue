<script lang="ts">
import type { CommonMaster } from '@/interfaces/Master';
import { computed, defineComponent, ref, watch } from 'vue';


export default defineComponent({
  props: {
    dropDownList: {
      required: true,
      type: Array,
      default: [],
    } 
  },
  emits: ['selectFilterBy',],
  setup(props, { emit }) {
    const isExpanded = ref(false)
    const selectedOption = ref<CommonMaster | null>(null)
    watch(() => selectedOption.value, (newValue) => {
      emit('selectFilterBy', newValue)
    })
    selectedOption.value = props.dropDownList.filter((item) => item.id === 1)[0]
    const options = computed(() => {
      return props.dropDownList.filter((item) => item.id !== selectedOption.value.id).sort(
        (a, b) => a.id < b.id ? -1: 1
      )
    })
    const toggleDropDown = () => isExpanded.value = !isExpanded.value
  
    const select = (option: CommonMaster) => {
      selectedOption.value = option
      isExpanded.value = false
    }

    return {
      isExpanded,
      options,
      selectedOption,
      toggleDropDown,
      select,
    }
  }
  
})
</script>

<template>
  <div class="dropdown-wrapper">
    <div class="selected" @click="toggleDropDown">
      {{ selectedOption.name }}
      <span class="material-symbols-outlined" v-if="isExpanded" >expand_more</span>
      <span class="material-symbols-outlined" v-else>expand_less</span>
    </div>
    <div class="options" v-if="isExpanded">
      <div v-for="option in options" :key="option.name" class="option" @click="select(option)">
        {{ option.name }}
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.dropdown-wrapper {
  display: flex;
  flex-direction: column;
  text-transform: capitalize;
  font-size: var(--f-s-semi-regular);
  font-weight: var(--f-w-medium);
  .selected {
    cursor: pointer;
    align-items: center;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    padding: 0 var(--s-regular);
  }
  .options {
    display: flex;
    margin-top: 25px;
    padding: 0 var(--s-regular) var(--s-small) var(--s-regular);
    position: absolute;
    display: flex;
    flex-direction: column;
    z-index: 99;
    background: var(--c-transparent);
    color: var(--c-white);
    .option {
      cursor: pointer;
      display: flex;
      white-space: nowrap;
      &:hover {
        transform: translateX(var(--s-regular));
        transition: ease-in 0.5s;
      }
    }
  }
}
</style>