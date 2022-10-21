<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, Legend, LinearScale, Title, Tooltip, LineElement, PointElement, Chart } from 'chart.js'
import { useStore } from 'vuex'
import { FilterByDispatchEnum } from '@/enum/Dispatch'
import { FilterByGetterEnum } from '@/enum/Getter'
import FilterByDropDown from '@/components/common/dropdowns/FilterByDropDown.vue'

ChartJS.register(Title, Tooltip, LineElement, PointElement, CategoryScale, LinearScale)

export default defineComponent({
  props: {
    titles: {
      required: true,
      type: Array<String>,
    },
    chartData: {
      required: false,
      type: Object,
      default: {
        labels: [],
        datasets: [],
      }
    }
  },
  emits: ['filterChart', 'updateChartType'],
  setup(props, { emit }) {
    const store = useStore()
    store.dispatch(FilterByDispatchEnum.getFilterByList)
    const filterByList = computed(() => store.getters[FilterByGetterEnum.filterByList])
    const titleIndex = ref(0)
    
    const handleChangeChartType = () => {
      titleIndex.value < props.titles.length - 1 ? titleIndex.value += 1 : titleIndex.value = 0
      emit('updateChartType', titleIndex.value)
    }

    return {
      titleIndex,
      filterByList,
      // chartOptions,
      handleChangeChartType
    }
  },
  components: { Line, FilterByDropDown }
})
</script>

<template>
  <div class="chart-wrapper">
    <div class="header">
      <div class="title-wrapper">
        <div class="title">{{ titles[titleIndex] }}</div>
        <span class="material-symbols-rounded" @click="handleChangeChartType" v-if="titles.length > 1">eject</span>
      </div>
      <div class="sort-by">
        <div class="sort-title">sort by:</div>
        <FilterByDropDown :dropDownList="filterByList" @selectFilterBy="(option) => $emit('filterChart', option)"/>
      </div>
    </div>
    <Line
      :chart-data="chartData"
      chart-id="line"
      css-classes="line-chart"
    />
  </div>
</template>

<style lang="scss" scoped>
.chart-wrapper {
  display: flex;
  flex-direction: column;
  background: var(--c-white);
  height: 400px;
  width: 100%;
  border-radius: var(--b-r-normal);
  box-shadow: 3px 3px 5px var(--c-grey);
  flex-grow: 2;
  overflow-x: none;
}
.header {
  display: flex;
  padding: var(--s-medium);
  justify-content: space-between;
  border-bottom: var(--b-s-small) solid var(--b-c-regular);
  .title {
    text-transform: capitalize;
    font-size: var(--f-s-header-4);
    font-weight: var(--f-w-regular);
  }
  .sort-by {
    display: flex;
    align-items: center;
    .sort-title {
      text-transform: uppercase;
      font-weight: var(--f-w-semi-bold);
      color: var(--c-primary);
    }
  }
}
.line-chart {
  display: flex;
  padding: var(--s-medium);
  height: 330px;
  width: 99%;
}
.title-wrapper {
  display: flex;
  align-items: center;
  gap: var(--s-regular);
  .material-symbols-rounded {
    transform: rotate(0.25turn);
  }
}
</style>
