<template>
  <div class="wrapper">
    <the-header />
    <main class="main">
      <router-view />
    </main>
    <the-footer />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"

import TheHeader from "./components/TheHeader.vue"
import TheFooter from "./components/TheFooter.vue"

export default {
  name: "App",
  components: {
    TheHeader,
    TheFooter,
  },
  computed: {
    ...mapGetters(["getBackendUrl", "getCategories"]),
  },
  created() {
    this.getCategoriesFromBackend()
  },

  methods: {
    ...mapActions(["getCategoriesFromBackend"]),
  },
}
</script>

<style lang="scss"></style>
