<template>
  <section class="cart-empty">
    <div class="cart-empty__body">
      <h1 class="cart-empty__title">Корзина пустая</h1>
      <router-link :to="{name: 'store'}" class="cart-empty__subtitle"
        >ПЕРЕЙТИ В МАГАЗИН</router-link
      >
    </div>
  </section>
</template>
<script>
export default {}
</script>
<style lang="scss">
.cart-empty {
  display: flex;
  flex: 1;
  &__body {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    row-gap: 50px;
  }
  &__title {
    @include heading-h1;
  }
  &__subtitle {
    @include text-large;
    cursor: pointer;
    color: #998e78;
    transition: color 0.5s ease;
  }
  &__subtitle:hover {
    color: #000;
  }
}
</style>
