<template>
  <template v-if="getCrumbs && getCrumbs.length > 1">
    <div class="crumbs">
      <div class="container">
        <div class="crumbs__body">
          <span
            class="crumbs__current"
            v-if="getLastCrumb && getCrumbTitle(getLastCrumb)"
            >{{ getCrumbTitle(getLastCrumb) }}</span
          >
          <ul class="crumbs__crumbs">
            <li
              v-for="(crumb, index) in getCrumbs"
              :key="index"
              class="crumbs__crumb-wrapper"
            >
              <router-link
                class="crumbs__crumb"
                :class="{ crumbs__crumb_muted: isLastCrumb(crumb) }"
                v-if="getCrumbTitle(crumb)"
                :to="{ name: crumb.name, params: this.$route.params }"
                >{{ getCrumbTitle(crumb) }}
              </router-link>
              <span v-if="!isLastCrumb(crumb)" class="crumbs__separator"
                >-</span
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
</template>
<script>
import { mapGetters } from "vuex"

export default {
  computed: {
    ...mapGetters(["getCategories", "getProductDetail"]),
    getCrumbs() {
      return this.$route.matched.filter((item) => !item.meta.breadCrumbs.hide)
    },
    getLastCrumb() {
      return this.getCrumbs.slice(-1)[0]
    },
  },
  methods: {
    isLastCrumb(crumb) {
      return crumb === this.getLastCrumb
    },
    getCrumbTitle(crumb) {
      if (crumb.name === "category" && this.getCategories) {
        return this.getCategories.find(
          (item) => item.slug === this.$route.params.category
        ).name
      }
      if (crumb.name === "product" && this.getProductDetail) {
        return this.getProductDetail.name
      }
      return crumb.meta.breadCrumbs.title
    },
  },
}
</script>
<style lang="scss">
.crumbs {
  &__body {
    display: flex;
    flex-direction: column;
    row-gap: 25px;
  }
  &__current {
    @include heading-h1;
  }
  &__crumbs {
    display: flex;
    column-gap: 10px;
  }
  &__crumb {
    @include text;
  }
  &__separator {
    margin-left: 10px;
  }
  &__crumb_muted {
    color: #909090;
  }
}
</style>
