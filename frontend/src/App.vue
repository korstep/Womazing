<template>
  <div class="wrapper">
    <the-header />
    <main class="main">
      <bread-crumbs v-if="shouldShowComponent" />
      <router-view />
    </main>
    <the-footer />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"

import TheHeader from "@/components/TheHeader.vue"
import TheFooter from "@/components/TheFooter.vue"
import BreadCrumbs from "@/components/BreadCrumbs.vue"

export default {
  name: "App",
  components: {
    TheHeader,
    TheFooter,
    BreadCrumbs,
  },
  computed: {
    ...mapGetters(["getCategories"]),
    shouldShowComponent() {
      return this.$route.name !== "home" && this.$route.name !== "not-found"
    },
  },
  created: async function () {
    await this.createCategories()
  },

  methods: {
    ...mapActions(["createCategories"]),
  },
}
</script>

<style lang="scss"></style>
