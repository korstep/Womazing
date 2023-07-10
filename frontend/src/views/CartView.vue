<template>
  <template v-if="!getCart.length">
    <CartEmpty />
  </template>
  <template v-if="getCart.length">
    <CartItems />
    <CartCoupon />
    <CartTotal />
  </template>
</template>
<script>
import { mapGetters } from "vuex"
import CartItems from "@/components/CartItems"
import CartEmpty from "@/components/CartEmpty"
import CartTotal from "@/components/CartTotal.vue"
import CartCoupon from "@/components/CartCoupon.vue"
export default {
  components: { CartItems, CartEmpty, CartTotal, CartCoupon },
  created() {},
  computed: {
    ...mapGetters(["getCart", "getCoupon"]),
  },
  watch: {},
}
</script>
<style lang="scss"></style>
