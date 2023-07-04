import axios from "axios"
const state = { productDetail: null }
const getters = { getProductDetail: (state) => state.productDetail }
const actions = {
  async createProductDetail({ commit, getters }, context) {
    const detail = await axios
      .get(
        `${getters.getBackendUrl}v1/products/${context.productSlug}/${context.colorSlug}/`
      )
      .then((response) => response.data)
    commit("setProductDetail", detail)
  },
}
const mutations = {
  setProductDetail(state, productDetail) {
    state.productDetail = productDetail
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
