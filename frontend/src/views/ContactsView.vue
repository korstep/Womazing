<template>
  <store-location-map />
  <the-contacts />
  <contact-us-form />
</template>
<script>
import TheContacts from "@/components/TheContacts.vue"
import StoreLocationMap from "@/components/StoreLocationMap.vue"
import ContactUsForm from "@/components/ContactUsForm.vue"
export default {
  components: { TheContacts, StoreLocationMap, ContactUsForm },
}
</script>
<style lang="scss"></style>
