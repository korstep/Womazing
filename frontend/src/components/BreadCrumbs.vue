<template>
  <div class="crumbs">
    <div class="container">
      <div class="crumbs__body">
        <span class="crumbs__curr">Магазин</span>
        <div class="crumbs__path">Главная - Магазин</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss">
.crumbs {
  margin-top: 190px;
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 25px;
  }
  &__curr {
    @include heading-h1;
  }
  &__path {
    @include text;
  }
}
</style>
