<template>
  <div class="cart-empty">
    <div class="cart-empty__body">
      <h1 class="cart-empty__title">Корзина пустая</h1>
      <span @click="goToStore()" class="cart-empty__subtitle"
        >ПЕРЕЙТИ В МАГАЗИН</span
      >
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    goToStore() {
      this.$router.push({ name: "store" })
    },
  },
}
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
    cursor: pointer;
    @include text-large;
    color: #998e78;
    transition: color 0.5s ease;
  }
  &__subtitle:hover {
    color: #000;
  }
}
</style>
