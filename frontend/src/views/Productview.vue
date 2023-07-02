<template>
  <ProductDetail />
  <ProductsSimilar />
</template>
<script>
import ProductDetail from "@/components/ProductDetail.vue"
import ProductsSimilar from "@/components/ProductsSimilar.vue"
import { mapActions } from "vuex"
export default {
  components: { ProductDetail, ProductsSimilar },
  data() {
    return {}
  },
  mounted: async function () {
    await this.createProductDetail(this.getContext)
  },
  computed: {
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
      handler: function (newParams, oldParams) {
        const newProductSlug = newParams.productSlug
        const newColorSlug = newParams.colorSlug
        const oldProductSlug = oldParams.productSlug
        const oldColorSlug = oldParams.colorSlug

        if (
          newProductSlug !== oldProductSlug ||
          newColorSlug !== oldColorSlug
        ) {
          this.createProductDetail(this.getContext)
        }
      },
      deep: true,
    },
  },
}
</script>
<style lang="scss"></style>
