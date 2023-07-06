<template>
  <div class="writeus">
    <div class="container">
      <div class="writeus__body">
        <h3 class="writeus__title">Напишите нам</h3>
        <TheForm
          :showName="true"
          :showEmail="true"
          :showPhone="true"
          :showMessage="true"
        >
          <template v-slot:buttonText>Отправить</template>
        </TheForm>
      </div>
    </div>
  </div>
</template>

<script>
import TheForm from "./TheForm.vue"
export default {
  components: {
    TheForm,
  },
  data() {
    return {}
  },
  computed: {},
  methods: {},
  watch: {},
}
</script>

<style lang="scss">
.writeus {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 60px;
  }

  &__title {
    @include heading-h3;
  }
  &__form {
    max-width: 450px;
    display: flex;
    flex-direction: column;
    row-gap: 40px;
    align-items: start;
  }

  &__group {
    display: flex;
    flex-direction: column;
    row-gap: 10px;
    width: 80%;
  }

  &__group_wide {
    width: 100%;
  }

  &__input {
    min-height: 50px;
    width: 100%;
    border-bottom: 1px solid #000;
  }

  &__input_vertical-resize {
    resize: vertical;
    max-height: 160px;
  }
  &__input-length {
    @include text-small;
    color: #9c9c9c;
  }

  &__button {
    @include button-filled;
  }
  &__input-length_warning {
    color: #9c3030;
  }
  &__success {
    @include text;
    width: 450px;
    background: #f1eadc;
    padding-top: 30px;
    padding-bottom: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  &__error {
    @include text-small;
    color: #9c3030;
  }
}
</style>
