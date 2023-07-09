<template>
  <TheModal v-if="getShowCallback"> <ModalCallback /></TheModal>
  <div class="wrapper">
    <the-header />
    <router-view />
    <the-footer />
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex"
import TheHeader from "@/components/TheHeader.vue"
import TheFooter from "@/components/TheFooter.vue"
import TheModal from "@/components/TheModal.vue"
import ModalCallback from "@/components/ModalCallback.vue"

export default {
  name: "App",
  components: {
    TheHeader,
    TheFooter,
    TheModal,
    ModalCallback,
  },
  computed: {
    ...mapGetters(["getCategories", "getCart", "getShowCallback"]),
  },
  created: async function () {
    await this.createCategories()
    this.createCartMethod()
  },

  methods: {
    ...mapActions(["createCategories"]),
    ...mapMutations(["createCart", "setTotal"]),
    createCartMethod() {
      if (localStorage.getItem("cart")) {
        const cartData = JSON.parse(localStorage.getItem("cart"))
        this.createCart(cartData)
      } else {
        localStorage.setItem("cart", JSON.stringify(this.getCart))
      }
    },
  },
  watch: {
    getCart: {
      handler(newCartData) {
        localStorage.setItem("cart", JSON.stringify(newCartData))
        this.setTotal()
      },
      deep: true,
    },
  },
}
</script>

<style lang="scss"></style>
