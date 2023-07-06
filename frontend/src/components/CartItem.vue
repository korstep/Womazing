<template>
  <div class="cart-item">
    <div class="container">
      <div v-if="item" class="cart-item__body">
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
          <div class="cart-item__name-size">
            <span class="cart-item__name">{{ item.name }}</span>
            <span class="cart-item__size">{{ item.size }}</span>
          </div>
        </div>
        <div class="prices">
          <span class="cart-item__price">${{ item.price }}</span>
        </div>
        <div class="amount">
          <img
            @click="reduceQuantityHandler()"
            class="cart-item__reduce"
            :class="{ 'cart-item__reduce_disabled': this.quantity === 1 }"
            src="@/assets/media/icons/reduce.svg"
            alt="-"
          />
          <span class="cart-item__quantity">{{ quantity }}</span>

          <img
            @click="increaseQuantityHandler()"
            class="cart-item__increase"
            :class="{
              'cart-item__reduce_disabled': this.quantity === item.supply,
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
import axios from "axios"
export default {
  data() {
    return {
      item: null,
    }
  },
  props: {
    productSlug: { type: String, requered: true },
    colorSlug: { type: String, requered: true },
    size: { type: String, requered: true },
    quantity: { type: Number, requered: true },
  },
  mounted: function () {
    this.getCartItem(this.productSlug, this.colorSlug, this.size).then(
      (item) => (this.item = item)
    )
  },
  computed: {
    ...mapGetters(["getBackendBaseUrl"]),
    ...mapGetters(["getBackendUrl"]),
    computeTotalPrice() {
      return this.item.price * this.quantity
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
      this.removeProduct(this.getProductContext)
    },

    reduceQuantityHandler() {
      if (this.quantity === 1) {
        return
      }
      this.reduceQuantity(this.getProductContext)
    },
    increaseQuantityHandler() {
      if (this.quantity >= this.item.supply) {
        return
      }
      this.increaseQuantity(this.getProductContext)
    },
    // async getSupply(productSlug, colorSlug, size) {
    //   const response = axios
    //     .get(
    //       `${
    //         this.getBackendUrl
    //       }v1/products/${productSlug}/${colorSlug}/${size.toUpperCase()}/supply/`
    //     )
    //     .then((response) => response.data)
    //   return response
    // },
    async getCartItem(productSlug, colorSlug, size) {
      const response = axios
        .get(
          `${
            this.getBackendUrl
          }v1/products/${productSlug}/${colorSlug}/${size.toUpperCase()}/`
        )
        .then((response) => response.data)
      return response
    },
    getImageUrl(imagePath) {
      return `${this.getBackendBaseUrl}${imagePath}`
    },
  },
}
</script>
<style lang="scss">
.cart-item {
  &__body {
    display: flex;
    max-height: 180px;
  }
  .product {
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
  &__name-size {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 10px;
  }
  &__name {
    @include text;
  }
  &__size {
    @include text-small;
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
