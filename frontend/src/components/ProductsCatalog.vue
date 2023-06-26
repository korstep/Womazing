<template>
  <div class="catalog">
    <div class="container">
      <div v-if="catalog" class="catalog__body">
        <section v-if="catalog" class="products">
          <product-cart
            v-for="(product, index) in catalog"
            :key="index"
            :name="product.name"
            :price="product.price"
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
    if (!this.getCatalog) {
      if (this.$route.name == "store") {
        await this.createCatalog()
        console.log("nema")
      } else if (this.$route.name == "category") {
        await this.createCatalogCategory({
          category: this.$route.params.category,
          sortBy: "",
        })
      }
    }
  },
  computed: {
    ...mapGetters(["getCatalog"]),
    catalog() {
      return this.getCatalog
    },
  },

  methods: {
    ...mapActions(["createCatalogCategory", "createCatalog"]),
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
