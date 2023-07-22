<template>
  <section class="benefits">
    <div class="container">
      <div class="benefits__body">
        <h2 class="benefits__title">Что для нас важно</h2>
        <div class="benefits__list">
          <div class="benefits__item">
            <img
              src="@/assets/media/icons/quality.svg"
              alt=""
              class="benefits__icon"
            />
            <h3 class="benefits__benefit">Качество</h3>
            <span class="benefits__description"
              >Наши профессионалы работают на лучшем оборудовании для пошива
              одежды беспрецедентного качества</span
            >
          </div>
          <div class="benefits__item">
            <img
              src="@/assets/media/icons/gear.svg"
              alt=""
              class="benefits__icon"
            />
            <h3 class="benefits__benefit">Скорость</h3>
            <span class="benefits__description"
              >Благодаря отлаженной системе в Womazing мы можем отшивать до
              20-ти единиц продукции в наших собственных цехах</span
            >
          </div>
          <div class="benefits__item">
            <img
              src="@/assets/media/icons/hand.svg"
              alt=""
              class="benefits__icon"
            />
            <h3 class="benefits__benefit">Ответственность</h3>
            <span class="benefits__description"
              >Мы заботимся о людях и планете. Безотходное производство и
              комфортные условия труда - все это Womazing</span
            >
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {}
</script>
<style lang="scss">
.benefits {
  &__title {
    @include heading-h2;
  }

  &__list {
    margin-top: 90px;
    display: flex;
    justify-content: space-between;
  }

  &__item {
    display: flex;
    flex-direction: column;
    max-width: 305px;
    max-height: 270px;
    row-gap: 25px;
  }

  &__icon {
    align-self: start;
    max-height: 65px;
  }
  &__benefit {
    @include heading-h3;
  }

  &__description {
    @include text;
  }
}
</style>
