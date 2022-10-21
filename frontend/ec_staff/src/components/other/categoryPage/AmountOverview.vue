<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
import { useStore } from 'vuex'
import { FilterByGetterEnum, ProductCategoryGetterEnum } from '@/enum/Getter'
import { ProductCategoryDispatchEnum } from '@/enum/Dispatch'
import type { CommonMaster } from '@/interfaces/Master'
import CommonLineChart from './CommonLineChart.vue'


export default defineComponent({
  setup() {
    const store = useStore()
    const filterBy = ref(store.getters[FilterByGetterEnum.filterByList].filter((item) => item.id === 1)[0])
    const titles = ["Amount overview", "Quantity overview"]
    const titleIndex = ref(0)
    const categoryList = computed(() => store.getters[ProductCategoryGetterEnum.categoryList])
    const chartData = computed(() => 
      titleIndex.value ===  0 ?
        store.getters[ProductCategoryGetterEnum.saleAmountOverviewData] :
        store.getters[ProductCategoryGetterEnum.saleQuantityOverviewData]
    )

    const updateOverview = () => {
      titleIndex.value === 0 ? 
      store.dispatch(ProductCategoryDispatchEnum.updateSaleAmountOverview, filterBy.value) :
      store.dispatch(ProductCategoryDispatchEnum.updateSaleQuantityOverview, filterBy.value)
    }

    const filterChart = (option: CommonMaster) => {
      filterBy.value = option
      updateOverview()
    }

    watch(titleIndex, () => updateOverview())
    watch(categoryList.value, () => updateOverview())

    setInterval(() => updateOverview(), 30000)

    return {
      titleIndex,
      titles,
      chartData,
      filterChart,
    }
  },
  components: { CommonLineChart, }
})
</script>

<template>
  <CommonLineChart 
    :chartData="chartData" 
    :titles=titles 
    @filterChart="(option) => filterChart(option)"
    @updateChartType="(index) => titleIndex = index"
  />
</template>
