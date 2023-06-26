<template>
  <div class="sorting">
    <div class="container">
      <div class="sorting__body">
        <div class="sort-by sorting__item">
          <span @click="toggleSort()" class="sorting__title"
            >Сортировать по<img
              class="sorting__img"
              src="@/assets/media/icons/expand-more.svg"
              alt=""
          /></span>
          <ul class="sorting__select" v-show="isSortByOpen">
            <li
              class="sorting__option-container"
              v-for="option in sort_by"
              :key="option.id"
            >
              <input
                class="sort-by__radio"
                type="radio"
                :id="'sort__option_' + option.id"
                :value="option.text"
                v-model="selectedSortBy"
              />
              <label :for="'sort__option_' + option.id">{{
                option.text
              }}</label>
            </li>
            <button class="sorting__apply" @click="applySort()">
              Применить
            </button>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex"

export default {
  data() {
    return {
      sort_by: [
        { text: "По спаданию цены", id: 2 },
        { text: "По возрастанию цены", id: 1 },
        { text: "По новизне", id: 0 },
        { text: "По умолчанию", id: -1 },
      ],
      selectedSortBy: "По умолчанию",
      isSortByOpen: false,
    }
  },
  computed: {
    getCurrentCategory() {
      return this.$route.params.category
    },
  },
  methods: {
    ...mapActions(["createCatalog", "createCatalogCategory"]),
    async applySort() {
      if (this.$route.name == "store") {
        await this.createCatalog(
          this.sort_by.find((item) => item.text === this.selectedSortBy).id
        )
      } else {
        console.log("here")
        await this.createCatalogCategory({
          category: this.getCurrentCategory,
          sortBy: this.sort_by.find((item) => item.text === this.selectedSortBy)
            .id,
        })
      }
      this.toggleSort()
    },
    toggleSort() {
      this.isSortByOpen = !this.isSortByOpen
    },
  },
}
</script>

<style lang="scss">
.sorting {
  &__body {
    width: 100%;
  }
  &__title {
    cursor: pointer;
    @include heading-h4;
  }
  &__img {
    height: 100%;
  }
  &__item {
    position: relative;
  }
  &__select {
    background-color: beige;
    top: 30px;
    position: absolute;
    z-index: 3;
    padding: 25px;
  }
  &__option-container {
    position: relative;
    margin-bottom: 20px;
    @include text;
  }
  &__apply {
    @include button-filled;
    width: 100%;
  }
}
.sort-by {
  &__radio {
    cursor: pointer;
    margin-right: 10px;
    height: 20px;
    width: 20px;
  }
}
</style>
