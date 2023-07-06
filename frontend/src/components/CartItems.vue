<template>
  <div class="cart">
    <div class="container">
      <div class="cart__body">
        <div class="cart__columns">
          <div class="product">Товар</div>
          <div class="prices">Цена</div>
          <div class="amount">Количество</div>
          <div class="total">Всего</div>
        </div>
        <CartItem
          v-for="(item, index) in getCart"
          :key="index"
          :productSlug="item.productSlug"
          :colorSlug="item.colorSlug"
          :size="item.size"
          :quantity="item.quantity"
        />
      </div>
    </div>
  </div>
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
