<template>
  <div class="team">
    <div class="container">
      <div class="team__body">
        <h2 class="team__title">Команда мечты Womazing</h2>
        <div class="team__content">
          <swiper
            class="team__slider"
            :slides-per-view="1"
            :loop="true"
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
              <a href="{% url 'about' %}" class="team__link"
                >Подробнее о бренде</a
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
  // setup() {
  //   return {
  //     pagination: {
  //       clickable: true,
  //       renderBullet: function (index, className) {
  //         return (
  //           '<span class="top-slider__bullet ' +
  //           className +
  //           '">0' +
  //           (index + 1) +
  //           "</span>"
  //         )
  //       },
  //     },
  //     modules: [Pagination],
  //   }
  // },
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
  }
}
</style>
