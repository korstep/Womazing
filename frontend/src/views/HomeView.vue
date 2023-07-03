<template>
  <TheRepose />
  <NewCollection id="new-colections" />
  <OurBenefits />
  <OurTeam />
</template>

<script>
import TheRepose from "@/components/TheRepose.vue"
import OurBenefits from "@/components/OurBenefits.vue"
import OurTeam from "@/components/OurTeam.vue"
import NewCollection from "@/components/NewCollection.vue"
export default {
  name: "HomeView",
  components: {
    OurBenefits,
    OurTeam,
    NewCollection,
    TheRepose,
  },
}
</script>
<style lang="scss"></style>
