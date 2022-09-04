<template>
  <div class="page">
    <label>Home</label>
    <div>This is home page</div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "HomePage",
});
</script>

<style scoped lang="scss">
.page {
  background-color: var(--dark);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>
