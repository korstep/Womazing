import axios from "axios"
const state = {
  catalog: null,
}
const getters = {
  getCatalog: (state) => state.catalog,
}
const actions = {
  async createCatalog({ commit, getters }, sortBy = "") {
    const catalog = await axios
      .get(`${getters.getBackendUrl}v1/products/?sort_by=${sortBy}`)
      .then((response) => response.data)
    commit("setCatalog", catalog)
  },
  async createCatalogCategory({ commit, getters }, context) {
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
}
const mutations = {
  setCatalog(state, catalog) {
    state.catalog = catalog
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
