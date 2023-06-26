<template>
  <div id="novelty" class="novelty">
    <div class="container">
      <div class="novelty__body">
        <h2 class="novelty__title">Новая коллекция</h2>
        <section v-if="products" class="products">
          <product-cart
            v-for="product in products"
            :key="product.productSlug"
            :name="product.name"
            :price="product.price"
            :oldPrice="product.oldPrice"
            :imagePath="product.image"
          />
        </section>
        <router-link :to="{ name: 'store' }"
          ><button class="novelty__link">Открыть магазин</button></router-link
        >
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"
import { mapGetters } from "vuex"
import ProductCart from "./ProductCart.vue"

export default {
  components: {
    ProductCart,
  },
  data() {
    return {
      products: null,
    }
  },
  mounted: function () {
    this.getProducts().then((response) => {
      this.products = response.data
    })
  },
  computed: {
    ...mapGetters(["getBackendUrl"]),
  },
  methods: {
    async getProducts() {
      return await axios.get(`${this.getBackendUrl}v1/products/?count=3`)
    },
  },
}
</script>
<style lang="scss">
.novelty {
}
.container {
}
.novelty__body {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.novelty__title {
  @include heading-h2;
  align-self: flex-start;
  margin-bottom: 90px;
}
.products {
  width: 100%;
  display: flex;
  justify-content: space-between;
  column-gap: 30px;
  margin-bottom: 65px;
}
.novelty__link {
  @include button-outlined;
}
.product-cart {
  width: calc(33.33% - 20px);
}
</style>
