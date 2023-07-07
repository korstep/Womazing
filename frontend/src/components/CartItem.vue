<template>
  <div v-if="item" class="cart-item">
    <div class="container">
      <div class="cart-item__body">
        <div class="product">
          <img
            @click="removeProductHandler()"
            class="cart-item__cross"
            src="@/assets/media/icons/cross.svg"
            alt=""
          />
          <img
            class="cart-item__image"
            :src="getImageUrl(this.item.image)"
            alt=""
          />
          <div class="cart-item__name-color-size">
            <span class="cart-item__name">{{ item.name }}</span>
            <span class="cart-item__color">Цвет: {{ item.color }}</span>
            <span class="cart-item__size">Размер: {{ item.size }}</span>
          </div>
        </div>
        <div class="prices">
          <span class="cart-item__price">${{ item.price }}</span>
        </div>
        <div class="amount">
          <img
            @click="reduceQuantityHandler()"
            class="cart-item__reduce"
            :class="{
              'cart-item__reduce_disabled': this.item.quantity === 1,
            }"
            src="@/assets/media/icons/reduce.svg"
            alt="-"
          />
          <span class="cart-item__quantity">{{ item.quantity }}</span>

          <img
            @click="increaseQuantityHandler()"
            class="cart-item__increase"
            :class="{
              'cart-item__reduce_disabled': this.item.quantity === item.supply,
            }"
            src="@/assets/media/icons/increase.svg"
            alt="+"
          />
        </div>
        <div class="total">${{ computeTotalPrice }}</div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapMutations } from "vuex"
export default {
  data() {
    return {}
  },
  props: {
    item: { type: Object, requered: false },
  },
  mounted() {},
  computed: {
    ...mapGetters(["getBackendBaseUrl", "getBackendUrl"]),
    computeTotalPrice() {
      return this.item.price * this.item.quantity
    },
    getProductContext() {
      return {
        productSlug: this.item.productSlug,
        colorSlug: this.item.colorSlug,
        size: this.item.size,
      }
    },
  },
  methods: {
    ...mapMutations(["increaseQuantity", "reduceQuantity", "removeProduct"]),
    removeProductHandler() {
      if (this.$store.getters.isItemInCart(this.getProductContext)) {
        this.removeProduct(this.getProductContext)
      }
    },

    reduceQuantityHandler() {
      if (this.item.quantity === 1) {
        return
      }
      this.reduceQuantity(this.getProductContext)
    },
    increaseQuantityHandler() {
      if (this.item.quantity >= this.item.supply) {
        return
      }
      this.increaseQuantity(this.getProductContext)
    },
    getImageUrl(imagePath) {
      return `${this.getBackendBaseUrl}${imagePath}`
    },
  },
  watch: {},
}
</script>
<style lang="scss">
.cart-item {
  &__body {
    display: flex;
    max-height: 180px;
  }
  .product {
    padding-right: 20px;
    display: flex;
    align-items: center;
    column-gap: 30px;
  }
  &__cross {
    cursor: pointer;
  }
  &__image {
    width: 125px;
    height: 100%;
    object-fit: cover;
  }
  &__name-color-size {
    display: flex;
    flex-direction: column;
    align-items: start;
    row-gap: 10px;
  }
  &__name {
    @include text;
  }
  &__size {
    @include text-small;
    color: #9c9c9c;
  }
  &__color {
    @include text-small;
    color: #9c9c9c;
  }
  .prices {
    display: flex;
    flex-direction: column;
    justify-content: center;
    row-gap: 10px;
  }
  &__price {
    @include text;
  }
  .amount {
    display: flex;
    align-items: center;
    column-gap: 15px;
  }
  &__increase {
    width: 20px;
    background-color: rgba(156, 156, 156, 0.15);
    border-radius: 30px;
    cursor: pointer;
  }
  &__increase_disabled {
    cursor: default;
    opacity: 0.5;
  }
  &__quantity {
    @include text-large;
  }
  &__reduce {
    width: 20px;
    background-color: rgba(156, 156, 156, 0.15);
    border-radius: 30px;
    cursor: pointer;
  }
  &__reduce_disabled {
    opacity: 0.5;
    cursor: default;
  }
  .total {
    display: flex;
    align-items: center;
  }
}
</style>
