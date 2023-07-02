<template>
  <div class="catalog">
    <div class="container">
      <div v-if="getCatalog" class="catalog__body">
        <section v-if="getCatalog" class="products">
          <product-cart
            v-for="(product, index) in getCatalog"
            :key="index"
            :name="product.name"
            :price="product.price"
            :productSlug="product.productSlug"
            :colorSlug="product.colorSlug"
            :oldPrice="product.oldPrice"
            :imagePath="product.image"
          />
        </section>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex"
import ProductCart from "./ProductCart.vue"
export default {
  components: {
    ProductCart,
  },
  data() {
    return {}
  },
  mounted: async function () {
    await this.manageCatalog()
  },
  computed: {
    ...mapGetters(["getCatalog"]),
  },

  methods: {
    ...mapActions(["createCatalogCategory", "createCatalog"]),
    async manageCatalog() {
      if (this.$route.name == "store") {
        await this.createCatalog()
      } else {
        await this.createCatalogCategory({
          category: this.$route.params.category,
          sortBy: "",
        })
      }
    },
  },
  watch: {
    "$route.params.category": async function () {
      this.manageCatalog()
    },
  },
}
</script>
<style lang="scss">
.products {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  row-gap: 30px;
  column-gap: 30px;
  margin-bottom: 65px;
}
.product-cart {
  width: calc(33.33% - 20px);
}
</style>
