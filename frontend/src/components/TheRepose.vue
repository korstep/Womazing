<template>
  <div class="repose">
    <div class="container">
      <div class="repose__body">
        <swiper
          class="repose__slider"
          :speed="800"
          :slides-per-view="1"
          :loop="true"
          :modules="modules"
          :autoplay="{
            delay: 7000,
            disableOnInteraction: false,
            pauseOnMouseEnter: true,
            waitForTransition: true,
          }"
          :pagination="pagination"
          @swiper="onSwiper"
        >
          <swiper-slide v-for="index in 3" :key="index" class="repose__slide">
            <div class="repose__text">
              <span class="repose__title">Новые поступления в этом сезоне</span>
              <div class="repose__text-limiter">
                <span class="repose__subtitle"
                  >Утонченные сочетания и бархатные оттенки - вот то, что вы
                  искали в этом сезоне. Время исследовать.</span
                >
                <div class="repose__buttons">
                  <a href="#new-colections">
                    <img
                      class="repose__arrow"
                      src="@/assets/media/icons/arrow-d.svg"
                      alt=""
                  /></a>
                  <router-link :to="{ name: 'store' }" class="repose__button"
                    >Открыть магазин</router-link
                  >
                </div>
              </div>
            </div>
            <div class="repose__images">
              <img src="@/assets/media/images/repose-image.png" alt="" />
            </div>
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue"
import { Pagination, Autoplay } from "swiper"
import "swiper/css"
import "swiper/css/autoplay"
export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  methods: {
    onSwiper(swiper) {
      this.swiper = swiper
    },
  },
  setup() {
    return {
      pagination: {
        clickable: true,
        renderBullet: function (index, className) {
          return '<span class="repose__bullet ' + className + '">' + "</span>"
        },
      },
      modules: [Pagination, Autoplay],
    }
  },
}
</script>
<style lang="scss">
.repose {
  &__body {
    padding-top: 10px;
  }
  &__slider {
  }
  &__slide {
    display: flex;
    justify-content: space-between;
  }
  &__text {
    max-width: 585px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    row-gap: 45px;
  }
  &__text-limiter {
    width: 75%;
    display: flex;
    flex-direction: column;
    row-gap: 50px;
    align-items: end;
    text-align: end;
  }
  &__title {
    @include heading-h1;
  }
  &__subtitle {
    @include text-large;
  }
  &__buttons {
    display: flex;
  }
  &__arrow {
    cursor: pointer;
  }
  &__button {
    @include button-filled;
  }
  &__images {
  }
  &__bullet {
    height: 4px;
    width: 30px;
    background: #d1d1d1;
  }
  .swiper-pagination {
    width: 100%;
    position: absolute;
    left: 25%;
    bottom: 0;
    display: flex;
    column-gap: 10px;
    z-index: 2;
  }
  .swiper-pagination-bullet-active {
    background: #000;
  }
}
</style>
