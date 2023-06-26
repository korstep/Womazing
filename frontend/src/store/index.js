import axios from "axios"
import { createStore } from "vuex"

export default createStore({
  actions: {
    async createCategories({ commit, getters }) {
      const categories = await axios
        .get(`${getters.getBackendUrl}v1/categories/`)
        .then((response) => response.data)
      commit("setCategories", categories)
    },
    async createCatalog({ commit, getters }, sortBy = "") {
      const catalog = await axios
        .get(`${getters.getBackendUrl}v1/products/?sort_by=${sortBy}`)
        .then((response) => response.data)
      commit("setCatalog", catalog)
    },
    async createCatalogCategory({ commit, getters }, context) {
      console.log(context.category, context.sortBy)
      const categories = getters.getCategories.map((item) => item.slug)
      if (getters.getCategories && categories.includes(context.category)) {
        try {
          const catalog = await axios
            .get(
              `${getters.getBackendUrl}v1/products/${context.category}/?sort_by=${context.sortBy}`
            )
            .then((response) => response.data)
          commit("setCatalog", catalog)
        } catch (error) {
          commit("setCatalog", null)
        }
      } else {
        return
      }
    },
  },
  state: {
    backendBaseUrl: "http://127.0.0.1:8000",
    backendApiUrl: "http://127.0.0.1:8000/api/",
    categories: null,
    catalog: null,
  },
  getters: {
    getBackendBaseUrl: (state) => state.backendBaseUrl,
    getBackendUrl: (state) => state.backendApiUrl,
    getCategories: (state) => state.categories,
    getCatalog: (state) => state.catalog,
  },
  mutations: {
    setCategories(state, categories) {
      state.categories = categories
    },
    setCatalog(state, catalog) {
      state.catalog = catalog
    },
  },
  modules: {},
})
