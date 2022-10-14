<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
import Popup from '../components/common/Popup.vue'
import EnterSearchField from '../components/common/fields/EnterSearchField.vue'
import { useStore } from 'vuex'
import { ProductCategoryGetterEnum } from '@/enum/Getter'
import { RouterEnum } from '@/enum/Router'
import { ProductCategoryDispatchEnum, SideBarDispatchEnum } from '@/enum/Dispatch'
import { SideBarEnum } from '@/enum/SideBar'
import OverviewLineChart from '../components/other/categoryPage/OverviewLineChart.vue'

export default defineComponent({
  setup() {
    const store = useStore()
    store.dispatch(SideBarDispatchEnum.selectRoute, {
      mainRoute: SideBarEnum.products,
      subRoute: RouterEnum.categoriesName,
    })
    store.dispatch(ProductCategoryDispatchEnum.getCategoryList)
    const category = ref({ name: '', isAdded: false })
    const categoryList = computed(() => {
      return store.getters[ProductCategoryGetterEnum.categoryList]
    })

    async function addNewCategory() {
      try {
        await store.dispatch(ProductCategoryDispatchEnum.addNewCategory, {
          name: category.value.name.toLowerCase(),
        })
        category.value.isAdded = true
      } catch (e) {
        console.log('addNewCategory Error: ', e)
      } 
    }

    watch(() => category.value.isAdded, (newValue: boolean) => {
      if (newValue) {
        setTimeout(function() {
          category.value = { name: '', isAdded: false }
        }, 2000)
      }
    });

    return {
      category,
      categoryList,
      addNewCategory,
    }
  },
  components: { Popup, EnterSearchField, OverviewLineChart }
})
</script>


<template>
  <div class="page">
    <Popup @add="addNewCategory" :isAdded="category.isAdded" title="Add category">
      <EnterSearchField
        title="Category name"
        placeHolder="Enter category"
        :isClickable="false"
        :field="category"
        :itemList="categoryList"
        @updateField="(field) => category = field"
      />
    </Popup>
    <OverviewLineChart title="Category overview" />
  </div>
</template>

<style>
</style>
