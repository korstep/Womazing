<template>
  <div class="contacts">
    <div class="container">
      <div class="contacts__body">
        <div class="contacts__item">
          <span class="contacts__item-heading">Телефон</span>
          <h4 class="contacts__item-contact">+7 (495) 823-54-12</h4>
        </div>
        <div class="contacts__item">
          <span class="contacts__item-heading">E-mail</span>
          <h4 class="contacts__item-contact">info@sitename.com</h4>
        </div>
        <div class="contacts__item">
          <span class="contacts__item-heading">Адрес</span>
          <h4 class="contacts__item-contact">
            г. Москва, 3-я улица Строителей, 25
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss">
.contacts {
  &__body {
    display: flex;
    column-gap: 100px;
  }
  &__item {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
  &__item-heading {
    @include text;
  }
  &__item-contact {
    @include heading-h4;
  }
}
</style>
