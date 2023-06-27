<template>
  <ProductDetail />
</template>
<script>
import ProductDetail from "@/components/ProductDetail.vue"
import { mapActions } from "vuex"
export default {
  components: { ProductDetail },
  mounted: function () {
    this.createProductDetail(this.getContext)
  },
  computed: {
    getContext() {
      return {
        productSlug: `${this.$route.params.productSlug}`,
        colorSlug: `${this.$route.params.colorSlug}`,
      }
    },
  },
  methods: {
    ...mapActions(["createProductDetail"]),
  },
}
</script>
<style lang="scss"></style>
