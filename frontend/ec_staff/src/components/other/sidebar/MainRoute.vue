<script lang="ts">
import { SideBarDispatchEnum } from '@/enum/Dispatch'
import { SideBarGetterEnum } from '@/enum/Getter'
import { computed, defineComponent, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import SubRoute from './SubRoute.vue'
import type { SubRouteType } from '@/interfaces/Route'

export default defineComponent({
  props: {
    mainRouteObj: {
      required: true,
      type: Object,
    },
  },
  setup(props) {
    const store = useStore()
    const router = useRouter()
    const isSelected = computed(() => props.mainRouteObj.title === store.getters[SideBarGetterEnum.selectedMainRoute])
    const isOpenChildrenList = ref(isSelected.value)

    const toggleChildren = () => isOpenChildrenList.value = !isOpenChildrenList.value
    const selectRoute = ( subRoute: SubRouteType ) => {
      router.push(subRoute.route)
    }

    return {
      isOpenChildrenList,
      isSelected,
      toggleChildren,
      selectRoute,
    }
  },
  components: { SubRoute }
})
</script>

<template>
  <div class="main-route-wrapper">
    <div :class="isSelected ? 'main-route selected' : 'main-route'" @click="toggleChildren">
      <span class="material-symbols-outlined icon">{{ mainRouteObj.icon }}</span>
      <div>{{ mainRouteObj.title }}</div>
      <span class="material-symbols-outlined collapse" v-if="isOpenChildrenList">expand_more</span>
      <span class="material-symbols-outlined collapse" v-else>expand_less</span>
    </div>
    <div class="sub-route" v-if="isOpenChildrenList">
      <SubRoute
        v-for="child in mainRouteObj.children" 
        :key="child.title" 
        :title="child.title"
        :mainRouteObj="mainRouteObj"
        @click="selectRoute(child)"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main-route {
  cursor: pointer;
  text-transform: capitalize;
  align-items: center;
  display: flex;
  font-size: var(--f-s-semi-small);
  font-weight: var(--f-w-medium);
  padding: var(--s-medium);
  border-radius: var(--b-r-normal);
  min-width: 200px;

  &.selected {
    background: var(--c-white);
    margin-bottom: var(--s-regular);
  }
}
.material-symbols-outlined {
  font-size: var(--f-s-regular);
  &.icon {
    margin-right: var(--s-regular);
  }
  &.collapse {
    display: flex;
    flex-grow: 2;
    font-size: var(--f-s-semi-small);
    justify-content: flex-end;
  }
}
</style>
