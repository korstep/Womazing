import axios from "axios"

export default {
  state: {
    categories: null,
  },

  getters: {
    getCategories: (state) => state.categories,
  },

  actions: {
    async createCategories({ commit, getters }) {
      console.log("here")
      const categories = await axios
        .get(`${getters.getBackendUrl}v1/categories/`)
        .then((response) => response.data)
      commit("setCategories", categories)
    },
  },

  mutations: {
    setCategories(state, categories) {
      state.categories = categories
    },
  },
}
