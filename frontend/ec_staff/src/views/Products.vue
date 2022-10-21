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
import DisplayField from '../components/common/fields/DisplayField.vue'
import type { Product } from '@/interfaces/Product'


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
    const product = ref({ id: null as number | null ,name: '', isAdded: false })
    const purchasePrice = ref({ name: null as number | null })
    const quantity = ref({ name: 1 as number })
    const price = ref({ name: null as number | null })
    const desc = ref({ name: null as string | null })
    const photo = ref({ id: null as number | null, file: '', isAdded: false })
    const isQuantityIncreased = ref(true)
    const currentProduct = computed(() => 
      productList.value.filter((item: Product) => product.value.id ? item.id === product.value.id : false)[0]
    )

    const refreshValues = () => {
      category.value = { id: null, name: '' }
      purchasePrice.value = { name: null }
      price.value = { name: null }
      desc.value = { name: null }
      photo.value = { id: null, file: '', isAdded: false }
    }

    async function addNewProduct() {
      try {
        if (product.value.id) {
          await store.dispatch(ProductDispatchEnum.updateQuantity, { id: product.value.id, quantity: quantity.value.name })
          product.value.isAdded = true
          refreshValues()
        } else {
          const resp = await store.dispatch(ProductDispatchEnum.addNewProduct, {
            name: product.value.name,
            purchase_price: purchasePrice.value.name,
            price: price.value.name,
            desc: desc.value.name,
            category_id: category.value.id,
            photo_id: photo.value.id,
          })
          product.value.id = resp.data.id
        }
      } catch (e: any) {
        alert(e.response.data.message)
      } 
    }
    async function selectCategory(selectedCategory: CommonMaster) {
      await store.dispatch(ProductDispatchEnum.selectCategory, selectedCategory)
    }
    const toggleQuantityAddingMode = () => isQuantityIncreased.value = !isQuantityIncreased.value

    watch(() => product.value.isAdded, (newValue: boolean) => {
      if (newValue) {
        setTimeout(function() {
          product.value = { id: null, name: '', isAdded: false }
        }, 2000)
      }
    });

    return {
      isQuantityIncreased,
      category,
      product,
      categoryList,
      productList,
      purchasePrice,
      price,
      quantity,
      desc,
      photo,
      currentProduct,
      addNewProduct,
      selectCategory,
      toggleQuantityAddingMode,
    }
  },
  components: { Popup, EnterSearchField, TextField, AreaTextField, PhotoUploadField, DisplayField }
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
            :isClickable="true"
            :field="product"
            :itemList="productList"
            @updateField="(field) => product = field"
            :isDisabled="!category.id"
          />
          <TextField
            v-if="!product.id"
            title="Purchase price"
            placeHolder="Enter purchase price"
            type="number"
            :field="purchasePrice"
            @updateField="(field) => purchasePrice = field"
            :isDisabled="!category.id"
          />
          <TextField
            v-if="!product.id"
            title="Sale Price"
            type="number"
            placeHolder="Enter price"
            :field="price"
            @updateField="(field) => price = field"
            :isDisabled="!category.id"
          />
          <div v-if="product.id" class="quantity-wrapper">
            <DisplayField title="Available quantity" :content="currentProduct.quantity"/>
            <TextField
              title="Quantity"
              type="number"
              placeHolder="Enter product quantity"
              :field="quantity"
              @updateField="(field) => quantity = field"
              :isDisabled="!product.id"
            />
          </div>
        </div>
        <div class="right-side" v-if="!product.id">
          <AreaTextField
            v-if="!product.id"
            title="Description"
            placeHolder="Describe you product"
            :field="desc"
            @updateField="(field) => desc = field"
            :isDisabled="!category.id"
          />
          <PhotoUploadField
            v-if="!product.id"
            title="Product photo"
            placeHolder="Describe you product"
            :field="photo"
            @updateField="(field) => photo = field"
            :isDisabled="!category.id"
          />
        </div>
      </div>
    </Popup>
  </div>
</template>

<style lang="scss" scoped>
.fields-wrapper {
  display: flex;
  flex-direction: column;
}
.info-wrapper {
  display: flex;
}
.right-side {
  margin-left: var(--s-large);
}
.quantity-wrapper {
  display: flex;
  flex-direction: column;
}
.quantity-adding-mode {
  cursor: pointer;
  display: flex;
  align-items: center;
  margin-left: var(--s-small);
  justify-content: center;
  background: var(--c-secondaryHighlight);
  border-radius: var(--b-r-small);
  padding: var(--s-regular);
  span {
    color: var(--c-white);
    pointer-events: none;
  }
  &.increase {
    background: var(--c-remarkable);
  }
}
</style>
