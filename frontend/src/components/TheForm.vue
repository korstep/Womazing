<template>
  <form @submit.prevent="submitForm" class="form">
    <div
      v-if="showName"
      class="form__group"
      :class="{ form__group_reduced: this.showMessage }"
    >
      <input
        @input="nameError = false"
        type="text"
        v-model="name"
        class="form__input"
        placeholder="Имя"
        required
      />
      <span v-if="nameError" class="form__error"
        >* Только буквы и не более 16 символов</span
      >
    </div>

    <div
      v-if="showEmail"
      class="form__group"
      :class="{ form__group_reduced: this.showMessage }"
    >
      <input
        type="email"
        v-model="email"
        class="form__input"
        placeholder="E-mail"
        required
      />
    </div>

    <div
      v-if="showPhone"
      class="form__group"
      :class="{ form__group_reduced: this.showMessage }"
    >
      <input
        @input="phoneError = false"
        type="tel"
        v-model="phone"
        class="form__input"
        placeholder="Телефон"
      />
      <span v-if="phoneError" class="form__error"
        >* Неккоректный ввод номера телефона
      </span>
    </div>

    <div v-if="showMessage" class="form__group form__group_wide">
      <textarea
        v-model="message"
        class="form__input form__input_vertical-resize"
        placeholder="Сообщение"
        rows="5"
      ></textarea>
      <span
        v-if="messageLength"
        class="form__input-length"
        :class="{
          'form__input-length_warning': messageLength === 500,
        }"
        >{{ messageLength }}/500</span
      >
    </div>

    <button type="submit" class="form__button">
      <slot name="buttonText"></slot>
    </button>
  </form>
</template>
<script>
import { validateName, validatePhone } from "@/helpers/validation.js"
export default {
  props: {
    showName: { type: Boolean, required: false, default: false },
    showEmail: { type: Boolean, required: false, default: false },
    showPhone: { type: Boolean, required: false, default: false },
    showMessage: { type: Boolean, required: false, default: false },
  },
  data() {
    return {
      name: "",
      email: "",
      phone: "",
      message: "",
      nameError: false,
      phoneError: false,
    }
  },
  computed: {
    messageLength() {
      return this.message.length
    },
  },
  methods: {
    submitForm() {
      if (!validateName(this.name)) {
        this.nameError = true
      }
      if (this.phone && !validatePhone(this.phone)) {
        this.phoneError = true
      }
      if (!this.phoneError && !this.nameError) {
        this.$emit("formPassed", {
          name: this.name,
          email: this.email,
          phone: this.phone,
          message: this.message,
        })
        this.resetForm()
      }
    },
    resetForm() {
      this.name = ""
      this.email = ""
      this.phone = ""
      this.message = ""
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
.form {
  max-width: 450px;
  display: flex;
  flex-direction: column;
  row-gap: 35px;
  align-items: start;
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 60px;
  }

  &__title {
    @include heading-h3;
  }

  &__group {
    display: flex;
    flex-direction: column;
    row-gap: 10px;
    width: 100%;
  }
  &__group_reduced {
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
