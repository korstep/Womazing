<template>
  <template v-if="getCategories">
    <ProductCategories />
    <ProductsSorting />
    <ProductsCatalog />
    <router-view></router-view>
  </template>
</template>
<script>
import ProductCategories from "@/components/ProductsCategories.vue"
import ProductsCatalog from "@/components/ProductsCatalog.vue"
import ProductsSorting from "@/components/ProductsSorting.vue"
import { mapGetters } from "vuex"
export default {
  components: { ProductCategories, ProductsCatalog, ProductsSorting },
  created() {},
  computed: {
    ...mapGetters(["getCategories"]),
  },
  methods: {},
  watch: {},
}
</script>
<style lang="scss"></style>
