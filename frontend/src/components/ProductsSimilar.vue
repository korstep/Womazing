<template>
  <div v-if="getProductDetail" class="similar">
    <div class="container">
      <div class="similar__body">
        <span class="paragraph">Связанные товары</span>
        <swiper class="similar__slider" :slides-per-view="3" @swiper="onSwiper">
          <swiper-slide
            v-for="product in getProductDetail.similar"
            :key="product.productSlug"
            class="similar__item"
          >
            <product-cart
              :name="product.name"
              :price="product.price"
              :productSlug="product.productSlug"
              :colorSlug="product.colorSlug"
              :oldPrice="product.oldPrice"
              :imagePath="product.image"
            />
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue"
import ProductCart from "./ProductCart.vue"

import "swiper/css"
import { mapGetters } from "vuex"
export default {
  data() {
    return {
      swiper: null,
    }
  },
  computed: {
    ...mapGetters(["getProductDetail"]),
  },
  components: {
    ProductCart,
    Swiper,
    SwiperSlide,
  },
  methods: {
    onSwiper(swiper) {
      this.swiper = swiper
    },
  },
}
</script>
<style lang="scss">
.similar {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 70px;
  }
  .paragraph {
    @include heading-h2;
  }
  &__slider {
    overflow: visible;
    width: 100%;
  }
  &__item {
  }
  .product-cart {
    width: 100%;
    height: 100%;
  }
}
</style>
