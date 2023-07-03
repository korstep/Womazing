<template>
  <div class="writeus">
    <div class="container">
      <div class="writeus__body">
        <h3 class="writeus__title">Напишите нам</h3>
        <form @submit.prevent="submitForm" class="writeus__form">
          <div class="writeus__group">
            <input
              type="text"
              v-model="name"
              class="writeus__input"
              placeholder="Имя"
              required
            />
          </div>

          <div class="writeus__group">
            <input
              type="email"
              v-model="email"
              class="writeus__input"
              placeholder="E-mail"
              required
            />
          </div>

          <div class="writeus__group">
            <input
              type="tel"
              v-model="phone"
              class="writeus__input"
              placeholder="Телефон"
            />
          </div>

          <div class="writeus__group writeus__group_wide">
            <textarea
              v-model="message"
              class="writeus__input writeus__input_vertical-resize"
              placeholder="Сообщение"
              rows="5"
            ></textarea>
            <span
              v-if="messageLength"
              class="writeus__input-length"
              :class="{
                'writeus__input-length_warning': messageLength === 500,
              }"
              >{{ messageLength }}/500</span
            >
          </div>

          <button type="submit" class="writeus__button">Отправить</button>
        </form>
        <div v-if="isSubmit" class="writeus__success">
          Сообщение успешно отправлено
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSubmit: false,
      name: "",
      email: "",
      phone: "",
      message: "",
    }
  },
  computed: {
    messageLength() {
      return this.message.length
    },
  },
  methods: {
    submitForm() {
      
    },
  },
  watch: {
    message(newValue) {
      if (newValue.length > 500) {
        this.message = newValue.slice(0, 500)
      }
    },
  },
}
</script>

<style lang="scss">
/* Стили для формы */
.writeus {
  /* Стили для контейнера формы */

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
}
</style>
