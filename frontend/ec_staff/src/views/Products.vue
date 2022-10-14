<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
import Popup from '@/components/common/Popup.vue'
import EnterSearchField from '@/components/common/fields/EnterSearchField.vue'
import { useStore } from 'vuex'
import { ProductCategoryGetterEnum, ProductGetterEnum } from '@/enum/Getter'
import { RouterEnum } from '@/enum/Router'
import { ProductCategoryDispatchEnum, ProductDispatchEnum, SideBarDispatchEnum } from '@/enum/Dispatch'
import { SideBarEnum } from '@/enum/SideBar'
import type { CommonMaster } from '@/interfaces/Master'
import TextField from '../components/common/fields/TextField.vue'
import AreaTextField from '../components/common/fields/AreaTextField.vue'
import PhotoUploadField from '../components/common/fields/PhotoUploadField.vue'


export default defineComponent({
  setup() {
    const store = useStore()
    store.dispatch(SideBarDispatchEnum.selectRoute, {
      mainRoute: SideBarEnum.products,
      subRoute: RouterEnum.productsName,
    })
    store.dispatch(ProductCategoryDispatchEnum.getCategoryList)
    const categoryList = computed(() => store.getters[ProductCategoryGetterEnum.categoryList])
    const productList = computed(() => store.getters[ProductGetterEnum.productList])
    const category = ref({ id: null as number | null, name: '' })
    const product = ref({ name: '', isAdded: false })
    const purchasePrice = ref({ name: null as number | null })
    const price = ref({ name: null as number | null })
    const desc = ref({ name: null as string | null })
    const photo = ref({ id: null as number | null, file: '', isAdded: false })

    const refreshValues = () => {
      category.value = { id: null, name: '' }
      purchasePrice.value = { name: null }
      price.value = { name: null }
      desc.value = { name: null }
      photo.value = { id: null, file: '', isAdded: false }
    }

    async function addNewProduct() {
      try {
        await store.dispatch(ProductDispatchEnum.addNewProduct, {
          name: product.value.name,
          purchase_price: purchasePrice.value.name,
          price: price.value.name,
          desc: desc.value.name,
          category_id: category.value.id,
          photo_id: photo.value.id,
        })
        product.value.isAdded = true
        refreshValues()
      } catch (e) {
        alert(e.response.data.message)
      } 
    }
    async function selectCategory(selectedCategory: CommonMaster) {
      await store.dispatch(ProductDispatchEnum.selectCategory, selectedCategory)
    }

    watch(() => product.value.isAdded, (newValue: boolean) => {
      if (newValue) {
        setTimeout(function() {
          product.value = { name: '', isAdded: false }
        }, 2000)
      }
    });

    return {
      category,
      product,
      categoryList,
      productList,
      purchasePrice,
      price,
      desc,
      photo,
      addNewProduct,
      selectCategory,
    }
  },
  components: { Popup, EnterSearchField, TextField, AreaTextField, PhotoUploadField }
})
</script>


<template>
  <div class="page">
    <Popup @add="addNewProduct" :isAdded="product.isAdded" title="Add product" >
      <div class="info-wrapper">
        <div class="fields-wrapper">
          <EnterSearchField 
            title='Category'
            placeHolder="Enter category"
            :isClickable="true"
            :field="category"
            :itemList="categoryList"
            @updateField="(field) => category = field"
            @selectRecommendation="selectCategory"
          />
          <EnterSearchField
            title="Product name"
            placeHolder="Enter product"
            :field="product"
            :itemList="productList"
            @updateField="(field) => product = field"
          />
          <TextField
            title="Purchase price"
            placeHolder="Enter purchase price"
            type="number"
            :field="purchasePrice"
            @updateField="(field) => purchasePrice = field"
          />
          <TextField
            title="Sale Price"
            type="number"
            placeHolder="Enter price"
            :field="price"
            @updateField="(field) => price = field"
          />
          <AreaTextField
            title="Description"
            placeHolder="Describe you product"
            :field="desc"
            @updateField="(field) => desc = field"
          />
        </div>
        <PhotoUploadField 
          title="Product photo"
          placeHolder="Describe you product"
          :field="photo"
          @updateField="(field) => photo = field"/>
      </div>
    </Popup>
  </div>
</template>

<style>
.fields-wrapper {
  display: flex;
  flex-direction: column;
}
.info-wrapper {
  display: flex;
  gap: var(--s-large);
}
</style>
