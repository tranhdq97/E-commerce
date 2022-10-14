<script lang="ts">
import { SideBarGetterEnum } from '@/enum/Getter'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  props: {
    title: {
      required: true, 
      type: String,
    },
    mainRouteObj: {
      required: true,
      type: Object,
    }
  },
  setup(props) {
    const store = useStore()
    const isSelected = computed(() => 
      store.getters[SideBarGetterEnum.selectedMainRoute] === props.mainRouteObj.title && 
      store.getters[SideBarGetterEnum.selectedSubRoute] === props.title
    )

    return {
      isSelected,
    }    
  },
})
</script>

<template>
  <div class="sub-route-wrapper">
    <div :class="isSelected ? 'selected' : ''"><span></span>{{ title }}</div>
  </div>
</template>

<style lang="scss" scoped>
.sub-route-wrapper {
  display: flex;
  cursor: pointer;
  margin-bottom: var(--s-small);
  div {
    display: flex;
    text-transform: capitalize;
    align-items: center;
    font-size: var(--f-s-small);
    font-weight: var(--f-w-regular);

    span {
      width: 4px;
      height: 4px;
      border-radius: 2px;
      background: var(--c-regular);
      margin-left: var(--s-medium);
      margin-right: var(--s-regular);
    }
  }
  .selected {
    color: var(--c-highlight);
    span {
      background-color: var(--c-highlight);
    }
  }
}

</style>
