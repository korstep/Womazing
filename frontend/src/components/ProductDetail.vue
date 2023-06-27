<template>
  <div class="detail">
    <div class="container">
      <div v-if="this.getProductDetail" class="detail__body">
        <swiper class="detail__slider" :slides-per-view="1" @swiper="onSwiper">
          <swiper-slide
            v-for="imagePath in this.getProductDetail.images"
            :key="imagePath"
            ><img class="detail__image" :src="getImageUrl(imagePath)" alt=""
          /></swiper-slide>
        </swiper>
        <div class="detail__detail">
          <div class="detail__prices">
            <span class="detail__price"
              >${{ this.getProductDetail.price }}</span
            >
            <span
              v-if="this.getProductDetail.oldPrice"
              class="detail__old-price"
              >${{ this.getProductDetail.oldPrice }}</span
            >
          </div>
          <div class="detail__options">
            <span class="detail__text">Выберите размер</span>
            <span
              class="detail__size"
              :class="{
                detail__size_selected: isSelectedSize(size),
                detail__size_disabled: isQuantityZero(quantity),
              }"
              v-for="[size, quantity] in Object.entries(
                this.getProductDetail.sizes
              )"
              :key="size"
              @click="selectSize(size, quantity)"
              >{{ size }}</span
            >
          </div>
          <div class="detail__options">
            <span class="detail__text">Выберите цвет</span>
            <div
              @click="selectColor(color.slug)"
              v-for="color in this.getProductDetail.colors"
              :key="color.slug"
              class="detail__color"
              :class="{ detail__color_selected: isSelectedColor(color.slug) }"
            >
              <img
                :src="getImageUrl(color.image)"
                alt=""
                class="detail__color-image"
              />
            </div>
          </div>
          <button class="detail__btn">Добавить в корзину</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex"
import { Swiper, SwiperSlide } from "swiper/vue"
// import router from "@/router"

export default {
  data() {
    return {
      selectedSize: null,
    }
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  computed: {
    ...mapGetters(["getProductDetail", "getBackendBaseUrl"]),
    getCurrentColor() {
      return this.$route.params.colorSlug
    },
  },
  methods: {
    ...mapActions(["createProductDetail"]),
    isQuantityZero(quantity) {
      return quantity === 0
    },
    async selectColor(color) {
      if (!this.isSelectedColor(color)) {
        this.$router.push({
          name: "product",
          params: {
            productSlug: this.$route.params.productSlug,
            colorSlug: color,
          },
        })
        await this.createProductDetail({
          productSlug: this.$route.params.productSlug,
          colorSlug: color,
        })
        this.selectedSize = null
      }
    },
    isSelectedColor(color) {
      return this.getCurrentColor === color
    },
    isSelectedSize(size) {
      return this.selectedSize === size
    },
    selectSize(size, quantity) {
      if (!this.isQuantityZero(quantity)) {
        this.selectedSize = size
      }
    },
    onSwiper(swiper) {
      this.swiper = swiper
    },
    getImageUrl(imagePath) {
      return `${this.getBackendBaseUrl}${imagePath}`
    },
    currentColor() {
      return this.$route.params.colorSlug
    },
  },
}
</script>
<style lang="scss">
.detail {
  &__body {
    display: flex;
    column-gap: 100px;
  }
  &__slider {
    margin: 0;
    width: 50%;
  }
  &__image {
    width: 100%;
    object-fit: cover;
    object-position: center;
    max-height: 760px;
  }
  &__detail {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    row-gap: 60px;
  }
  &__prices {
    display: flex;
    column-gap: 30px;
    align-items: center;
  }
  &__price {
    @include heading-h2;
    color: #998e78;
  }
  &__old-price {
    @include heading-h3;
    color: #9c9c9c;
    text-decoration: line-through;
  }
  &__options {
    display: flex;
    column-gap: 15px;
    row-gap: 35px;
    flex-wrap: wrap;
  }
  &__text {
    @include heading-h4;
    width: 100%;
  }
  &__size {
    @include text;
    padding: 10px 15px;
    border: 1px solid #000;
    cursor: pointer;
  }
  &__size_selected {
    color: #fff;
    background-color: #000;
  }
  &__size_disabled {
    opacity: 0.95;
    border: 1px solid #9c9c9c;
    color: #9c9c9c;
    cursor: default;
  }
  &__color {
  }
  &__color-image {
    cursor: pointer;
    border: 1px solid #000;
    border-radius: 100px;
  }
  &__color_selected {
    opacity: 0.95;
    .detail__color-image {
      border: 2px solid #9c9c9c;
    }
  }
  &__btn {
    @include button-filled;
  }
}
</style>
