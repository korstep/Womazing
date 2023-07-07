<template>
  <div class="total">
    <div class="container">
      <div class="total__body">
        <div class="total__total">
          <span>Итого:</span>
          <span>${{ getTotal }}</span>
        </div>
        <button class="total__button">Оформить заказ</button>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex"

export default {
  computed: {
    ...mapGetters(["getTotal"]),
  },
}
</script>
<style lang="scss">
.total {
  &__body {
    display: flex;
    justify-content: end;
    column-gap: 15px;
  }
  &__total {
    @include heading-h3;
    padding-right: 30px;
    padding-left: 30px;
    background: #f1eadc;
    display: flex;
    align-items: center;
    column-gap: 70px;
  }
  &__button {
    @include button-filled;
  }
}
</style>
