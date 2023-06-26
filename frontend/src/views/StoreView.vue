<template>
  <ProductCategories />
  <ProductsSorting />
  <ProductsCatalog v-if="getCategories" />
</template>
<script>
import ProductCategories from "@/components/ProductsCategories.vue"
import ProductsCatalog from "@/components/ProductsCatalog.vue"
import ProductsSorting from "@/components/ProductsSorting.vue"
import { mapGetters } from "vuex"
export default {
  components: { ProductCategories, ProductsCatalog, ProductsSorting },
  computed: {
    ...mapGetters(["getCategories"]),
  },
  methods: {},
}
</script>
<style lang="scss"></style>
