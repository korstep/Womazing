<template>
  <NewCollection />
  <OurBenefits />
  <OurTeam />
</template>

<script>
import OurBenefits from "@/components/OurBenefits.vue"
import OurTeam from "@/components/OurTeam.vue"
import NewCollection from "@/components/NewCollection.vue"
export default {
  name: "HomeView",
  components: {
    OurBenefits,
    OurTeam,
    NewCollection,
  },
}
</script>
<style lang="scss"></style>
