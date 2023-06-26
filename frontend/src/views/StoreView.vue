<template>
  <ProductCategories />
  <ProductsCatalog />
</template>
<script>
import ProductCategories from "@/components/ProductsCategories.vue"
import ProductsCatalog from "@/components/ProductsCatalog.vue"
import { mapActions, mapGetters } from "vuex"
export default {
  components: { ProductCategories, ProductsCatalog },
  computed: {
    ...mapGetters(["getCatalog"]),
  },
  mounted: async function () {
    console.log("hello")
    if (!this.getCatalog) {
      await this.createCatalog()
    }
  },
  methods: {
    ...mapActions(["createCatalog"]),
  },
}
</script>
<style lang="scss"></style>
