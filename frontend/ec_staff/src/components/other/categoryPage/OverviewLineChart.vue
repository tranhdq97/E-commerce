<script lang="ts">
import { defineComponent, ref } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, Legend, LinearScale, Title, Tooltip, LineElement, PointElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

export default defineComponent({
  props: {
    title: {
      required: true,
      type: String,
    },
  },
  setup() {
    const sortBy = ref('current year')
    const chartOptions = {
      responsive: true
    }
    const chartData = {
      labels: ['January', 'February', 'March', 'January', 'February', 'March', 'January', 'February', 'March', 'January', 'February', 'March' ],
      datasets: [ 
        { 
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [40, 21, 12, 12 ],
        },
        { 
          label: 'Data Two',
          backgroundColor: '#f22342',
          data: [100, 221, 112, 12 ],
        } 
      ],
    }

    return {
      sortBy,
      chartOptions,
      chartData,
    }
  },
  components: { Line, }
})
</script>

<template>
  <div class="chart-wrapper">
    <div class="header">
      <div class="title">{{ title }}</div>
      <div class="sort-by">
        <div class="sort-title">sort by:</div>
        <div class="sort-element">
          {{ sortBy }}
          <span class="material-symbols-outlined">expand_more</span>
        </div>
      </div>
    </div>
    <Line
      :chart-options="chartOptions"
      :chart-data="chartData"
      chart-id="line-chart"
      dataset-id-key="label"
      :plugins="() => []"
      css-classes="line-chart"
      :style="() => {}"
      :height="300"
      :width="700"
    />
  </div>
</template>

<style lang="scss" scoped>
.chart-wrapper {
  display: flex;
  flex-direction: column;
  background: var(--c-white);
  height: 400px;
  border-radius: var(--b-r-normal);
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
    .sort-element {
      display: flex;
      margin-left: var(--s-small);
      text-transform: capitalize;
      font-size: var(--f-s-semi-regular);
      font-weight: var(--f-w-medium);
    }
    .sort-title {
      text-transform: uppercase;
      font-weight: var(--f-w-semi-bold);
      color: var(--c-primary);
    }
  }
}
.line-chart {
  padding: var(--s-medium);
}
</style>
