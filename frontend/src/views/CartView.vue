<template>
  <CartItems v-if="getCart.length" />
  <CartEmpty v-else />
</template>
<script>
import { mapGetters } from "vuex"
import CartItems from "@/components/CartItems"
import CartEmpty from "@/components/CartEmpty"
export default {
  components: { CartItems, CartEmpty },
  computed: {
    ...mapGetters(["getCart"]),
  },
  methods: {},
}
</script>
<style lang="scss"></style>
