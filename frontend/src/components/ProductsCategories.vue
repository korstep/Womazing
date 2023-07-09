<template>
  <div class="categories">
    <div class="container">
      <div class="categories__body">
        <router-link
          class="categories__category"
          :class="{ categories__category_selected: !isCategoryPage }"
          :to="{ name: 'store' }"
          >Все</router-link
        >
        <router-link
          class="categories__category"
          :class="{
            categories__category_selected: isCategorySelected(category.slug),
          }"
          v-for="category in getCategories"
          :key="category.slug"
          :to="{ name: 'category', params: { category: category.slug } }"
          @click="changeCategory(category.slug)"
          >{{ category.name }}</router-link
        >
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex"

export default {
  data() {
    return {}
  },
  mounted() {},
  computed: {
    ...mapGetters(["getCategories"]),
    getRouteCategory() {
      return this.$route.params.category ? this.$route.params.category : false
    },
    isCategoryPage() {
      return this.getRouteCategory
    },
  },
  methods: {
    getCategoryNameOnSlug(slug) {
      return this.getCategories.find((item) => item.slug === slug).name
    },
    isCategoryExist(category) {
      return this.getCategories && category in this.getCategories
    },
    changeCategory(category) {
      this.$router.push({ name: "category", params: { category: category } })
    },
    isCategorySelected(category) {
      return this.$route.params.category === category
    },
  },
  watch: {},
}
</script>
<style lang="scss">
.categories {
  &__body {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  &__category {
    @include text;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 0;
    width: calc(
      (100% - 3 * 10px) / 4
    ); // Расчет ширины с учетом 4 промежутков по 10px
    border: 1px solid #000000;
  }

  &__category_selected {
    color: #ffffff;
    background-color: #000000;
  }
}
</style>
