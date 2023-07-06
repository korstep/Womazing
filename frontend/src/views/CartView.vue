<template>
  <CartItems v-if="getCart.length" />
  <CartEmpty v-else />
</template>
<script>
import { mapGetters, mapMutations } from "vuex"
import CartItems from "@/components/CartItems"
import CartEmpty from "@/components/CartEmpty"
export default {
  components: { CartItems, CartEmpty },
  computed: {
    ...mapGetters(["getCart"]),
  },
  methods: {
    ...mapMutations(["setTotal"]),
  },
  watch: {
    getCart: {
      handler() {
        console.log("here")
        this.setTotal()
      },
      deep: true,
    },
  },
}
</script>
<style lang="scss"></style>
