<template>
  <article class="product-cart">
    <div @click="redirectToProductPage()" class="product-cart__image">
      <img class="product-cart__image-img" :src="getImageUrl()" alt="" />
      <div class="product-cart__image-hover">
        <img src="@/assets/media/icons/arrow-r_white.svg" alt="" />
      </div>
    </div>
    <div class="product-cart__text">
      <router-link
        :to="{
          name: 'product',
          params: {
            category: categorySlug,
            productSlug: productSlug,
            colorSlug: colorSlug,
          },
        }"
        class="product-cart__name"
        >{{ name }}</router-link
      >
      <div class="product-cart__prices">
        <span v-if="oldPrice" class="product-cart__old-price"
          >${{ oldPrice }}</span
        >
        <span class="product-cart__curr-price">${{ price }}</span>
      </div>
    </div>
  </article>
</template>
<script>
import { mapGetters } from "vuex"

export default {
  props: {
    name: { type: String, required: true },
    price: { type: Number, required: true },
    oldPrice: { type: Number, required: false, default: null },
    productSlug: { type: String, required: true },
    colorSlug: { type: String, required: true },
    categorySlug: { type: String, required: true },
    imagePath: { type: String, required: true },
  },
  computed: {
    ...mapGetters(["getBackendBaseUrl"]),
  },
  methods: {
    getImageUrl() {
      return `${this.getBackendBaseUrl}${this.imagePath}`
    },
    redirectToProductPage() {
      this.$router.push({
        name: "product",
        params: {
          category: this.categorySlug,
          productSlug: this.productSlug,
          colorSlug: this.colorSlug,
        },
      })
    },
  },
}
</script>
<style lang="scss">
.product-cart {
  max-width: 350px;
  max-height: 560px;
  display: flex;
  flex-direction: column;
  row-gap: 25px;
  &__image {
    position: relative;
    cursor: pointer;
    &:hover {
      .product-cart__image-hover {
        opacity: 1;
      }
    }
  }

  &__image-img {
    height: 480px;
    width: 100%;
    object-fit: cover;
  }

  &__image-hover {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(110, 156, 159, 0.64);
    transition: opacity 0.5s ease;
    opacity: 0;
  }

  &__text {
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 10px;
  }

  &__name {
    @include heading-h4;
    cursor: pointer;
  }
  &__prices {
    @include text-small;
    display: flex;
    column-gap: 5px;
  }

  &__curr-price {
    color: #998e78;
  }

  &__old-price {
    color: #9c9c9c;
    text-decoration: line-through;
  }
}
</style>
