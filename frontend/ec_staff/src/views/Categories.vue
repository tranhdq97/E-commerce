<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
import Popup from '@/components/common/Popup.vue'
import EnterSearchField from '@/components/common/fields/EnterSearchField.vue'
import { useStore } from 'vuex'
import { ProductCategoryGetterEnum } from '@/enum/Getter'
import { RouterEnum } from '@/enum/Router'
import { ProductCategoryDispatchEnum, SideBarDispatchEnum } from '@/enum/Dispatch'
import { SideBarEnum } from '@/enum/SideBar'
import AmountOverview from '@/components/other/categoryPage/AmountOverview.vue'
import CategoryList from '@/components/other/categoryPage/CategoryList.vue'


export default defineComponent({
  setup() {
    const store = useStore()
    store.dispatch(SideBarDispatchEnum.selectRoute, {
      mainRoute: SideBarEnum.products,
      subRoute: RouterEnum.categoriesName,
    })
    const category = ref({ name: '', isAdded: false })
    const categoryList = computed(() => store.getters[ProductCategoryGetterEnum.categoryList])
    store.dispatch(ProductCategoryDispatchEnum.getCategoryList)

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
  components: { Popup, EnterSearchField, AmountOverview, CategoryList }
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
    <div class="first-row">
      <CategoryList title="Category list"/>
      <AmountOverview />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.page {
  display: flex;
  flex-flow: row wrap;
  flex-direction: column;
}
.first-row {
  display: flex;
  width: 100%;
  gap: var(--s-large);
}
</style>
