<template>
  <div class="modal">
    <div class="modal__body">
      <slot></slot>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss">
.modal {
  z-index: 6;
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(110, 156, 159, 0.95);
  display: flex;
  justify-content: center;
  align-items: center;

  &__body {
    background-color: #fff;
    padding: 70px;
  }
}
</style>
