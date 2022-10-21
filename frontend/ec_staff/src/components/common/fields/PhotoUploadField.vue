<script lang="ts">
import { FileManagementDispatchEnum } from '@/enum/Dispatch'
import { defineComponent, ref, watch } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  props: {
    title: { required: true, type: String, },
    field: { required: true, type: Object, },
    isDisabled: { required: false, default: false, type: Boolean },
  },
  emits: ['updateField',],
  setup(props, { emit }) {
    const store = useStore()
    const image = ref('')

    async function chooseImage(e) {
      image.value = e.target.files[0]
      const formData = new FormData()
      formData.append('file', image.value)
      formData.append('type_id', '1')
      const resp = await store.dispatch(FileManagementDispatchEnum.uploadFile, formData)
      emit('updateField', { ...props.field, id: resp.id, file: resp.file, isAdded: true })
    }

    watch(() => props.field.file, (newValue: string) => {
      newValue ? null : image.value = ''
    })

    return {
      chooseImage,
    }
  },
})
</script>

<template>
  <div class="wrapper">
    <div :class="isDisabled ? 'title is-disabled' : 'title'">{{ title }}</div>
    <div>
      <input
        :class="isDisabled ? 'is-disabled' : ''"
        @change="chooseImage" 
        type='file' 
        class="frame"/>
      <img :src="field.file" v-if="field.isAdded" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: var(--s-medium);
  width: 250px;
}
.title {
  text-transform: capitalize;
  font-size: var(--f-s-semi-regular);
  font-weight: var(--f-w-semi-bold);
  margin-bottom: var(--s-small);
  &.is-disabled {
    color: var(--c-grey);
  }
}
.frame {
  width: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
  &::-webkit-file-upload-button {
    cursor: pointer;
    outline: none;
    border: none;
    padding: var(--s-regular);
    background: var(--c-highlight);
    color: var(--c-white);
  }
  &.is-disabled {
    &::-webkit-file-upload-button {
      background: var(--c-grey);
    }
  }
}
img {
  margin-top: var(--s-regular);
  width: 250px;
  height: 250px;
}
input {
  &.is-disabled {
    pointer-events: none;
  }
}
</style>
