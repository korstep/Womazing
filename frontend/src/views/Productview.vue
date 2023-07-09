<template>
  <ProductDetail />
  <ProductsSimilar />
</template>
<script>
import ProductDetail from "@/components/ProductDetail.vue"
import ProductsSimilar from "@/components/ProductsSimilar.vue"
import { mapActions, mapGetters } from "vuex"
export default {
  components: { ProductDetail, ProductsSimilar },
  data() {
    return {}
  },
  mounted: async function () {
    await this.createProductDetail(this.getContext)
  },
  computed: {
    ...mapGetters(["getProductDetail"]),
    getColorSlug() {
      return this.$route.params.colorSlug
    },
    getProductSlug() {
      return this.$route.params.productSlug
    },
    getContext() {
      return {
        productSlug: `${this.getProductSlug}`,
        colorSlug: `${this.getColorSlug}`,
      }
    },
  },
  methods: {
    ...mapActions(["createProductDetail"]),
  },
  watch: {
    "$route.params": {
      handler: async function (newParams, oldParams) {
        const newProductSlug = newParams.productSlug
        const newColorSlug = newParams.colorSlug
        const oldProductSlug = oldParams.productSlug
        const oldColorSlug = oldParams.colorSlug

        if (
          newProductSlug &&
          newColorSlug &&
          (newProductSlug !== oldProductSlug || newColorSlug !== oldColorSlug)
        ) {
          await this.createProductDetail(this.getContext)
        }
      },
      deep: true,
    },
  },
}
</script>
<style lang="scss"></style>
