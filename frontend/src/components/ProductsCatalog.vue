<template>
  <section class="catalog">
    <div class="container">
      <div v-if="getCatalog" class="catalog__body">
        <section v-if="getCatalog" class="products">
          <product-cart
            v-for="(product, index) in paginatedCatalog"
            :key="index"
            :name="product.name"
            :price="product.price"
            :productSlug="product.productSlug"
            :colorSlug="product.colorSlug"
            :categorySlug="product.categorySlug"
            :oldPrice="product.oldPrice"
            :imagePath="product.image"
          />
        </section>
        <div class="catalog__pagination-info">
          Показано: {{ currentRange }} из {{ getCatalog.length }} товаров
        </div>
        <div class="catalog__pagination">
          <img
            @click="goToPrevPage"
            v-if="currentPage !== 1"
            class="catalog__arrow catalog__arrow_prev"
            src="@/assets/media/icons/arrow-r.svg"
            alt="<-"
          />
          <span
            v-for="page in totalPages"
            :key="page"
            @click="goToPage(page)"
            :class="{ catalog__page_active: page === currentPage }"
            class="catalog__page"
            >{{ page }}</span
          >
          <img
            @click="goToNextPage"
            v-if="currentPage !== totalPages"
            class="catalog__arrow catalog__arrow_next"
            src="@/assets/media/icons/arrow-r.svg"
            alt="->"
          />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import { mapActions, mapGetters } from "vuex"
import ProductCart from "./ProductCart.vue"

export default {
  components: {
    ProductCart,
  },
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 9,
    }
  },
  mounted() {
    this.manageCatalog()
  },
  computed: {
    ...mapGetters(["getCatalog", "getCategories"]),
    paginatedCatalog() {
      const start = (this.currentPage - 1) * this.itemsPerPage
      const end = start + this.itemsPerPage
      return this.getCatalog.slice(start, end)
    },
    totalPages() {
      return Math.ceil(this.getCatalog.length / this.itemsPerPage)
    },
    currentRange() {
      const end = this.currentPage * this.itemsPerPage
      return Math.min(end, this.getCatalog.length)
    },
    currentCategory() {
      return this.$route.params.category
    },
    isStorePage() {
      return this.$route.name === "store"
    },
  },
  methods: {
    ...mapActions(["createCatalogCategory", "createCatalog"]),
    goToNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
      }
    },
    goToPage(page) {
      this.currentPage = page
    },
    goToPrevPage() {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    async manageCatalog() {
      if (this.isStorePage) {
        await this.createCatalog()
      } else {
        await this.createCatalogCategory({
          category: this.currentCategory,
          sortBy: "",
        })
      }
    },
  },
  watch: {
    "$route.params.category"(newCategory, oldCategory) {
      if (newCategory !== oldCategory) {
        this.currentPage = 1
        this.manageCatalog()
      }
    },
  },
}
</script>
<style lang="scss">
.catalog {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 65px;
  }
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
  &__pagination {
    display: flex;
    justify-content: center;
    align-content: center;
    column-gap: 15px;
  }
  &__page {
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    background-color: #fff;
    border: 1px solid #000;
    transition: background-color 0.5s ease;
  }
  &__page_active {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    background-color: #000;
    color: #fff;
  }
  &__arrow {
    width: 25px;
  }
  &__arrow_prev {
    transform: rotate(180deg);
  }
}
</style>
