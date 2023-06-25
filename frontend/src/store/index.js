import axios from "axios"
import { createStore } from "vuex"

export default createStore({
  actions: {
    async getCategoriesFromBackend({ commit, getters }) {
      const catg = await axios
        .get(`${getters.getBackendUrl}v1/categories/`)
        .then((response) => response.data)
      commit("setCategories", catg)
    },
  },
  state: {
    backendBaseUrl: "http://127.0.0.1:8000",
    backendApiUrl: "http://127.0.0.1:8000/api/",
    categories: null,
  },
  getters: {
    getBackendBaseUrl: (state) => state.backendBaseUrl,
    getBackendUrl: (state) => state.backendApiUrl,
    getCategories: (state) => state.categories,
  },
  mutations: {
    setCategories(state, categories) {
      state.categories = categories
    },
  },
  modules: {},
})
