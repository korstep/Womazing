<template>
  <section class="cart">
    <div class="container">
      <div class="cart__body">
        <div class="cart__columns">
          <h4 class="product">Товар</h4>
          <h4 class="prices">Цена</h4>
          <h4 class="amount">Количество</h4>
          <h4 class="total">Всего</h4>
        </div>
        <div class="cart__items">
          <CartItem
            v-for="(item, index) in getCart"
            :key="index"
            :item="item"
          />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import { mapGetters } from "vuex"
import CartItem from "./CartItem.vue"
export default {
  components: {
    CartItem,
  },
  computed: {
    ...mapGetters(["getCart"]),
  },
}
</script>
<style lang="scss">
.cart {
  &__items {
    width: 100%;
    display: flex;
    flex-direction: column;
    row-gap: 25px;
  }
  &__columns {
    @include heading-h4;
    display: flex;
    padding-bottom: 25px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 50px;
  }
  .product {
    width: 47%;
  }
  .prices {
    width: 20%;
  }
  .amount {
    width: 23%;
  }
  .total {
    width: 10%;
  }
}
</style>
