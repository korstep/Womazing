<template>
  <section class="coupon">
    <div class="container">
      <form class="coupon__form" @submit.prevent="applyCouponHandler">
        <div class="coupon__group">
          <input
            @input="this.error = ''"
            class="coupon__input"
            v-model="couponCode"
            type="text"
            placeholder="Введите код купона"
            :disabled="isApply"
            :class="{ coupon__input_error: error }"
          />
          <span v-if="error" class="coupon__error">{{ error }}</span>
        </div>
        <div
          @click="resetCouponHandler()"
          v-if="isApply"
          class="coupon__cancel"
        >
          <img
            class="coupon__cross"
            src="@/assets/media/icons/cross.svg"
            alt="X"
          />
        </div>
        <button v-else class="coupon__button" type="submit">
          Применить купон
        </button>
      </form>
    </div>
  </section>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex"

export default {
  data() {
    return {
      couponCode: "",
      error: "",
      isApply: false,
    }
  },
  created() {
    this.createCoupon()
    if (this.getCoupon) {
      this.couponCode = this.getCoupon.code
      this.isApply = true
    }
  },
  computed: {
    ...mapGetters(["getCoupon"]),
  },
  methods: {
    ...mapActions(["applyCoupon"]),
    ...mapMutations(["resetCoupon", "setTotal", "setCoupon"]),
    resetCouponHandler() {
      this.resetCoupon()
      this.couponCode = ""
      this.isApply = false
    },
    async applyCouponHandler() {
      const result = await this.validateCoupon()
      if (result) {
        this.isApply = true
      }
    },
    async validateCoupon() {
      if (this.couponCode.length) {
        const result = await this.applyCoupon(this.couponCode)
        if (!result) {
          return true
        }
        this.error = result
      }
      return false
    },
    createCoupon() {
      if (localStorage.getItem("coupon")) {
        const couponData = JSON.parse(localStorage.getItem("coupon"))
        this.setCoupon(couponData)
      }
    },
  },
  watch: {
    getCoupon: {
      handler(NewCoupon) {
        localStorage.setItem("coupon", JSON.stringify(NewCoupon))
        this.setTotal()
      },
      deep: true,
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
  // &__input_error {
  //   border: 1px solid #570000;
  // }
  &__error {
    @include text-small;
    color: #570000;
  }
  &__button {
    @include button-outlined;
  }
  &__group {
    display: flex;
    flex-direction: column;
    row-gap: 5px;
  }
  &__cancel {
    @include button-outlined;
    padding: 22px;
    cursor: pointer;
  }
  &__cross {
    height: 100%;
  }
}
</style>
