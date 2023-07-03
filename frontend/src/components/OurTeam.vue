<template>
  <div class="team">
    <div class="container">
      <div class="team__body">
        <h2 class="paragraph team__title">Команда мечты Womazing</h2>
        <div class="team__content">
          <swiper
            class="team__slider"
            :slides-per-view="1"
            :loop="true"
            :modules="modules"
            :pagination="pagination"
            @swiper="onSwiper"
          >
            <swiper-slide class="team__item">
              <img
                class="team__img"
                src="@/assets/media/images/team.png"
                alt=""
              />
            </swiper-slide>
            <swiper-slide class="team__item">
              <img
                class="team__img"
                src="@/assets/media/images/team.png"
                alt=""
              />
            </swiper-slide>
            <swiper-slide class="team__item">
              <img
                class="team__img"
                src="@/assets/media/images/team.png"
                alt=""
              />
            </swiper-slide>
            <img
              @click="swiper.slidePrev()"
              class="team__arrow team__arrow-prev"
              src="@/assets/media/icons/arrow-r.svg"
              alt=""
            />
            <img
              @click="swiper.slideNext()"
              class="team__arrow"
              src="@/assets/media/icons/arrow-r.svg"
              alt=""
            />
          </swiper>
          <div class="team__text">
            <h3 class="team__subtitle">Для каждой</h3>
            <span class="team__description">
              Каждая девушка уникальна. Однако, мы схожи в миллионе мелочей.
            </span>
            <span class="team__description">
              Womazing ищет эти мелочи и создает прекрасные вещи, которые
              выгодно подчеркивают достоинства каждой девушки.
            </span>
            <span>
              <router-link :to="{ name: 'about' }" class="team__link"
                >Подробнее о бренде</router-link
              >
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue"
import { Pagination } from "swiper"
import "swiper/css"
export default {
  data() {
    return {
      swiper: null,
    }
  },
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
          return '<span class="team__bullet ' + className + '">' + "</span>"
        },
      },
      modules: [Pagination],
    }
  },
}
</script>
<style lang="scss">
.team {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 90px;
  }
  &__title {
    @include heading-h2;
  }
  &__content {
    display: flex;
    column-gap: 120px;
  }
  &__slider {
    position: relative;
  }
  &__item {
  }
  &__img {
  }
  &__text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    row-gap: 25px;
  }
  &__subtitle {
    @include heading-h3;
  }
  &__description {
    @include text;
  }
  &__link {
    color: #6e9c9f;

    &:hover {
      text-decoration: underline;
    }
  }
  &__arrow {
    cursor: pointer;
    position: absolute;
    bottom: 45%;
    right: 5px;
    z-index: 1;
  }
  &__arrow-prev {
    left: 5px;
    transform: rotate(-180deg);
  }
  &__bullet {
    height: 4px;
    width: 30px;
    background: rgba(255, 255, 255, 0.36);
  }
  .swiper-pagination {
    width: 100%;
    position: absolute;
    bottom: 60px;
    display: flex;
    justify-content: center;
    column-gap: 10px;
    z-index: 1;
  }
  .swiper-pagination-bullet-active {
    background: #fff;
  }
}
</style>
