<template>
  <div class="not-found">
    <div class="not-found__body">
      <span class="not-found__title">Страница не найдена</span>
      <router-link :to="{ name: 'home' }" class="not-found__link"
        >Перейти на главную</router-link
      >
    </div>
  </div>
</template>
<script></script>
<style lang="scss">
.not-found {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;

  &__body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    row-gap: 50px;
  }
  &__title {
    @include heading-h1;
  }
  &__link {
    @include button-outlined;
  }
}
</style>
