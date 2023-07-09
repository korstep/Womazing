<template>
  <div class="coupon">
    <div class="container">
      <form class="coupon__form" @submit.prevent="applyCoupon">
        <div class="coupon__group">
          <input
            class="coupon__input"
            v-model="couponCode"
            type="text"
            placeholder="Введите код купона"
            :class="{ coupon__input_error: isError }"
          />
          <!-- <span class="coupon__error"></span> -->
        </div>
        <button class="coupon__button" type="submit">Применить купон</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      couponCode: "",
      isError: false,
    }
  },
  methods: {
    applyCoupon() {
      if (this.validateCoupon()) {
        console.log("Применение купона:", this.couponCode)

        this.couponCode = ""
        this.isError = false
      } else {
        this.isError = true
      }
    },
    validateCoupon() {
      return true
    },
  },
}
</script>

<style lang="scss">
.coupon {
  &__form {
    display: flex;
    justify-content: start;
    column-gap: 15px;
  }
  &__input {
    min-height: 100%;
    border-bottom: 1px solid #000;
  }
  &__input_error {
    border: 1px solid #570000;
  }
  &__button {
    @include button-outlined;
  }
}
</style>
