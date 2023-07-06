<template>
  <div class="wrapper">
    <the-header />
    <main class="main">
      <bread-crumbs v-if="shouldShowComponent" />
      <router-view />
    </main>
    <the-footer />
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex"

import TheHeader from "@/components/TheHeader.vue"
import TheFooter from "@/components/TheFooter.vue"
import BreadCrumbs from "@/components/BreadCrumbs.vue"

export default {
  name: "App",
  components: {
    TheHeader,
    TheFooter,
    BreadCrumbs,
  },
  computed: {
    ...mapGetters(["getCategories", "getCart"]),
    shouldShowComponent() {
      return this.$route.name !== "home" && this.$route.name !== "not-found"
    },
  },
  created: async function () {
    await this.createCategories()
    await this.createCartMethod()
  },

  methods: {
    ...mapActions(["createCategories"]),
    ...mapMutations(["createCart"]),
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
      },
      deep: true,
    },
  },
}
</script>

<style lang="scss"></style>
