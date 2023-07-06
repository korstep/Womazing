<template>
  <header :class="{ 'header_not-fixed': !showPhoneAndCartIcon }" class="header">
    <div class="container">
      <div class="header__body">
        <div class="header__brand">
          <img
            src="@/assets/media/icons/dress.svg"
            alt=""
            class="header__brand-logo"
          />
          <router-link :to="{ name: 'home' }" class="header__brand-name"
            >WOMAZING</router-link
          >
        </div>
        <nav class="navbar">
          <router-link :to="{ name: 'home' }" class="navbar__element"
            >Главная</router-link
          >
          <router-link :to="{ name: 'store' }" class="navbar__element"
            >Магазин</router-link
          >
          <router-link :to="{ name: 'about' }" class="navbar__element"
            >О бренде</router-link
          >
          <router-link :to="{ name: 'contacts' }" class="navbar__element"
            >Контакты</router-link
          >
        </nav>
        <div class="header__contacts">
          <div class="header__phone-items">
            <svg
              v-if="showPhoneAndCartIcon"
              @click="toggleShowCallback"
              class="phone-icon"
              width="15"
              height="15"
              viewBox="0 0 15 15"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M2.25235 2.81643C0.750523 4.31823 0.750523 6.7618 2.25232 8.2636L3.05001 7.46592C1.9881 6.40402 1.98807 4.67613 3.05004 3.61417C4.11197 2.55224 5.83985 2.55224 6.90179 3.61414L7.69947 2.81646C6.1977 1.31463 3.75412 1.31466 2.25235 2.81643Z"
              />
              <path
                d="M3.84133 4.39118C3.20916 5.02334 3.20913 6.052 3.8413 6.6842L4.63901 5.88651C4.54584 5.79334 4.49453 5.66946 4.49453 5.5377C4.49453 5.40597 4.54587 5.28209 4.63904 5.18892C4.73221 5.09574 4.8561 5.04443 4.98782 5.04443C5.11958 5.04443 5.24349 5.09574 5.33664 5.18892L6.13432 4.3912C5.50215 3.75901 4.4735 3.75901 3.84133 4.39118Z"
              />
              <path
                d="M13.7482 2.43512L11.855 0.548462L7.92331 4.47365L9.44752 6.04779C9.19208 6.50124 8.63784 7.36988 7.69327 8.31445C6.74859 9.25916 5.8736 9.81969 5.41581 10.0792L3.87255 8.55561L0.00219727 12.4029L1.88504 14.2983C2.60479 15.0181 3.69992 15.2046 4.61014 14.7625C5.99915 14.0879 8.0954 12.8431 10.1942 10.7443C12.2931 8.64551 13.5378 6.54922 14.2124 5.16021C14.3723 4.83107 14.4499 4.47786 14.4499 4.1269C14.4499 3.50718 14.2077 2.89463 13.7482 2.43512ZM13.1977 4.66731C12.5609 5.97844 11.3845 7.95864 9.39655 9.94657C7.40862 11.9345 5.42842 13.1109 4.11729 13.7477C3.63929 13.9799 3.06281 13.8806 2.68414 13.5019L1.59739 12.4079L3.87537 10.1436L5.19009 11.4415L5.54184 11.2849C5.59899 11.2595 6.95941 10.6438 8.4911 9.11213C10.0238 7.57946 10.6266 6.23053 10.6515 6.17385L10.804 5.82682L9.50671 4.48703L11.8558 2.14177L12.9511 3.23325C13.3306 3.61328 13.4298 4.18951 13.1977 4.66731Z"
              />
            </svg>
            <span class="phone-number">+7 (495) 823-54-12</span>
          </div>
          <router-link
            v-show="showPhoneAndCartIcon"
            class="cart-icon"
            :to="{ name: 'cart' }"
          >
            <img
              src="@/assets/media/icons/cart.svg"
              alt=""
              class="cart-icon__icon"
            />
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
import { mapMutations } from "vuex"

export default {
  props: {
    showPhoneAndCartIcon: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  methods: {
    ...mapMutations(["toggleShowCallback"]),
  },
}
</script>
<style lang="scss">
.header {
  background-color: rgba(255, 255, 255, 1);
  z-index: 4;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;

  &__body {
    height: 95px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__contacts {
    display: flex;
    column-gap: 65px;
  }

  &__phone-items {
    display: flex;
    column-gap: 15px;
    align-items: center;

    .phone-icon {
      fill: #6e9c9f;
      padding: 4px;
      height: 25px;
      width: 25px;
      cursor: pointer;

      &:hover {
        transition: background-color 0.5s ease;
        border-radius: 10px;
        background-color: #6e9c9f;
        fill: white;
      }
    }

    .cart-icon {
    }
  }
}

.navbar {
  display: flex;
  column-gap: 45px;

  &__element {
    @include text-small;
    cursor: pointer;

    &:hover {
      color: #6e9c9f;
      font-weight: 700;
      transition: font-weight 0.5s ease;
    }
  }
}

.header__brand {
  display: flex;
  column-gap: 10px;
  align-items: center;

  &-logo {
  }

  &-name {
    @include custom-text-styles(16px, 500, 120%, 0.1em);
  }
}

.phone-number {
  @include text-small;
  white-space: nowrap;
}
.header_not-fixed {
  background-color: rgba(255, 255, 255, 0);
  position: inherit;
  .header__body {
    height: auto;
  }
}
</style>
