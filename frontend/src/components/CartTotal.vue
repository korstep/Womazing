<template>
  <section class="total">
    <div class="container">
      <div class="total__body">
        <h3 class="total__total">
          <span>Итого:</span>
          <span>${{ getTotal }}</span>
        </h3>
        <button class="total__button">Оформить заказ</button>
      </div>
    </div>
  </section>
</template>
<script>
import { mapGetters, mapMutations } from "vuex"

export default {
  computed: {
    ...mapGetters(["getTotal"]),
  },
  methods: {
    ...mapMutations(["setTotal"]),
  },
  watch: {
    getCart: {
      handler() {
        this.setTotal()
      },
      deep: true,
    },
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
