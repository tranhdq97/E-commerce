<template>
  <div class="page">
    <div>
      <div>
        <img class="avatar" :src="user.info ? user.info.avatar: require('../assets/avatar-placeholder.png')" alt="Avatar" />
      </div>
      <div :class="!isEdited? 'editable': ''">
        <div class="tag">
          <label>Email:</label>
          <input type="text" v-model="info.email" placeholder="Email" />
        </div>
        <div class="tag">
          <label>First name:</label>
          <input type="text" v-model="info.info.first_name" placeholder="First name" />
        </div>
        <div class="tag">
          <label>Last name:</label>
          <input type="text" v-model="info.info.last_name" placeholder="Last name" />
        </div>
        <!-- <div class="tag">
          <label>Sex:</label>
          <input type="text" v-model="info.info.sex" placeholder="Sex" />
        </div> -->
        <div class="tag">
          <label>Date of birth:</label>
          <input type="date" v-model="info.info.dob" placeholder="Date of birth" />
        </div>
        <div class="tag">
          <label>Phone number:</label>
          <input type="text" v-model="info.info.phone_number" placeholder="Phone number" />
        </div>
        <div class="tag">
          <label>Postal code:</label>
          <input type="text" v-model="info.info.postal_code" placeholder="Postal code" />
        </div>
        <div class="tag">
          <label>Created at:</label>
          <input type="text" disabled v-model="info.info.created_at" placeholder="Created at" />
        </div>
        <div class="tag">
          <label>Updated at:</label>
          <input type="text" disabled v-model="info.info.updated_at" placeholder="Updated at" />
        </div>
      </div>
      <div class="button" @click="toggleEditMode">EDIT</div>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { computed, ref } from "vue";

export default ({
  name: "ProfilePage",
  setup(){
    const store = useStore();
    const user = computed(() => store.getters["auth/stateUser"]);
    console.log("SETUP ", user.value);
    const isEdited = ref(false);
    const info = {
      email: user.value.email,
      info: {
        first_name: user.value.info ? user.value.info.first_name : "",
        last_name: user.value.info ? user.value.info.last_name : "",
        dob: user.value.info ? user.value.info.dob : "",
        phone_number: user.value.info ? user.value.info.phone_number : "",
        postal_code: user.value.info ? user.value.info.postal_code : "",
        created_at: user.value.info ? user.value.info.created_at : "",
        updated_at: user.value.info ? user.value.info.updated_at : "",
      }
    }
    const emailEditor = ref({})

    function toggleEditMode() {
      isEdited.value = !isEdited.value;
    }
    return {
      user,
      info,
      emailEditor,
      isEdited,
      toggleEditMode,
    } 
  },
})
</script>

<style lang="scss" scoped>
.page {
  margin: 1rem;
}
.button {
  background-color: grey;
}
.avatar {
  width: 10rem;
  height: 10rem;
}
.editable {
pointer-events: none;
}
.tag {
  display: flex;
  label {
    margin-right: 2rem;
  }
}
</style>
