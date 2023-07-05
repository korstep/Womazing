<template>
  <div class="cart-item">
    <div class="container">
      <div class="cart-item__body">
        <div class="cart-item__product">
          <img
            class="cart-item__cross"
            src="@/assets/media/icons/cross.svg"
            alt=""
          />
          <img :src="getImageUrl(this.image)" alt="" />
          <span class="cart-item__name">{{ name }}</span>
        </div>
        <div class="cart-item__prices">
          <span class="cart-item__price">{{ price }}</span>
        </div>
        <div class="cart-item__amount">
          <img
            class="cart-item__increase"
            src="@/assets/media/icons/increase.svg"
            alt="+"
          />
          <span class="cart-item__quantity">{{ quantity }}</span>
          <img
            class="cart-item__reduce"
            src="@/assets/media/icons/reduce.svg"
            alt="-"
          />
        </div>
        <div class="cart-item__total">{{}}</div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex"

export default {
  props: {
    image: { type: String, required: true },
    name: { type: String, required: true },
    size: { type: String, required: true },
    price: { type: Number, required: true },
    quantity: { type: Number, required: true },
  },
  computed: {
    ...mapGetters(["getBackendBaseUrl"]),
    computeTotalPrice() {
      return this.price * this.quantity
    },
  },
  methods: {
    getImageUrl(imagePath) {
      return `${this.getBackendBaseUrl}${imagePath}`
    },
  },
}
</script>
<style lang="scss"></style>
