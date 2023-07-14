<template>
  <main class="main">
    <BreadCrumbs />
    <router-view></router-view>
  </main>
</template>
<script>
import BreadCrumbs from "@/components/BreadCrumbs.vue"
export default {
  components: {
    BreadCrumbs,
  },
}
</script>
<style lang="scss">
.main {
  flex: 1 1 auto;
  padding-top: 95px;
  padding-bottom: 130px;
  display: flex;
  flex-direction: column;
  row-gap: 130px;
}
</style>
