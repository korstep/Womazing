<template>
  <main class="main">
    <router-view></router-view>
  </main>
</template>
<script>
export default {}
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
