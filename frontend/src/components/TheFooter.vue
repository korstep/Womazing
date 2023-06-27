<template>
  <footer class="footer">
    <div class="container">
      <The-Header :showPhoneAndCartIcon="false" />

      <div class="footer__body">
        <span class="footer__mail">hello@womazing.com</span>
        <div class="footer__agreements-categories-container">
          <div class="footer__agreements">
            <span class="footer__presharing">© Все права защищены</span>
            <div>
              <a href="#" class="footer__agreement"
                >Политика конфиденциальности</a
              >
            </div>
            <div>
              <a href="#" class="footer__agreement">Публичная оферта</a>
            </div>
          </div>
          <div class="footer__categories">
            <div v-for="catg in getCategories" :key="catg.slug">
              <router-link
                @click="changeCategory(catg.slug)"
                :to="{ name: 'category', params: { category: catg.slug } }"
                class="footer__category"
                >{{ catg.name }}</router-link
              >
            </div>
          </div>
        </div>
        <div class="footer__contacts">
          <div class="footer__social-networks">
            <a class="footer__network" href="#">
              <img
                src="@/assets/media/icons/instagram.svg"
                alt=""
                class="footer__network"
              />
            </a>
            <a class="footer__network" href="#">
              <img
                src="@/assets/media/icons/facebook.svg"
                alt=""
                class="footer__network"
              />
            </a>
            <a class="footer__network" href="#">
              <img
                src="@/assets/media/icons/twitter.svg"
                alt=""
                class="footer__network"
              />
            </a>
          </div>
          <img
            src="@/assets/media/icons/payment-methods.svg"
            alt=""
            class="footer__payment-methods"
          />
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
import { mapActions, mapGetters } from "vuex"

import TheHeader from "./TheHeader.vue"
export default {
  components: {
    TheHeader,
  },
  computed: {
    ...mapGetters(["getBackendUrl", "getCategories"]),
  },
  methods: {
    ...mapActions(["createCatalogCategory"]),
    changeCategory(category) {
      this.createCatalogCategory({ category: category, sortBy: "" })
    },
  },
}
</script>
<style lang="scss">
.footer {
  padding-top: 90px;
  background-color: #f1eadc;
  padding-bottom: 85px;

  &__body {
    padding-top: 10px;
    background-color: #f1eadc;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 10px;
  }

  &__mail {
    @include text-small;
    text-align: end;
    width: 100%;
  }
  &__agreements-categories-container {
    display: flex;
    column-gap: 160px;
  }

  &__agreements {
    display: flex;
    flex-direction: column;
    align-self: end;
    row-gap: 5px;
  }

  &__agreement {
    @include custom-text-styles(13px, 400);
    color: #000000;

    &:hover {
      text-decoration: underline;
      color: #6e9c9f;
      //transition: color 0.5s ease;
    }
  }

  &__categories {
    max-height: 80px;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    column-gap: 20px;
    row-gap: 10px;
  }

  &__category {
    @include custom-text-styles(13px, 400);

    &:hover {
      text-decoration: underline;
      color: #6e9c9f;
      //transition: color 0.5s ease;
    }
  }

  &__contacts {
    display: flex;
    flex-direction: column;
    align-self: center;
    row-gap: 20px;
  }

  &__social-networks {
    display: flex;
    column-gap: 10px;
  }

  &__network {
    height: 20px;
  }
}
</style>
