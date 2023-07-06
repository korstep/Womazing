<template>
  <template v-if="!successfully">
    <div class="callback">
      <div class="callback__body">
        <img
          v-if="!successfully"
          @click="toggleShowCallback()"
          class="callback__cross"
          src="@/assets/media/icons/cross.svg"
          alt=""
        />
        <h3 class="callback__title">Заказать обратный звонок</h3>
        <TheForm
          v-if-
          :showName="true"
          :showEmail="true"
          :showPhone="true"
          @formPassed="formPassedHandler()"
        >
          <template v-slot:buttonText>Отправить</template>
        </TheForm>
        <span v-if="successfully" class="callback__successfully-title"
          >Отлично! Мы скоро вам перезвоним.</span
        >
        <span
          v-if="successfully"
          @click="toggleShowCallback()"
          class="callback__successfully-button"
          >Закрыть</span
        >
      </div>
    </div>
  </template>
  <template v-if="successfully">
    <div class="successfully">
      <div class="successfully__body">
        <span class="successfully__title"
          >Отлично! Мы скоро вам перезвоним.</span
        >
        <span @click="toggleShowCallback()" class="successfully__button"
          >Закрыть</span
        >
      </div>
    </div>
  </template>
</template>
<script>
import { mapGetters, mapMutations } from "vuex"
import TheForm from "./TheForm.vue"
export default {
  components: { TheForm },
  data() {
    return {
      successfully: false,
    }
  },
  computed: {
    ...mapGetters(["getShowCallback"]),
  },
  methods: {
    ...mapMutations(["toggleShowCallback"]),
    formPassedHandler(context) {
      console.log(context)
      this.successfully = true
    },
  },
}
</script>
<style lang="scss">
.callback {
  &__body {
    position: relative;
    display: flex;
    flex-direction: column;
    row-gap: 35px;
  }
  &__cross {
    cursor: pointer;
    position: absolute;
    top: -30px;
    right: -30px;
  }
  &__title {
    @include heading-h3;
  }
  .form__button {
    width: 100%;
  }
}
.successfully {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 35px;
  }
  &__title {
    @include heading-h3;
    align-self: center;
  }
  &__button {
    @include button-outlined;
    cursor: pointer;
    align-self: center;
  }
}
</style>
