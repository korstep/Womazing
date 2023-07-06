import { createStore } from "vuex"
import categories from "./modules/categories.js"
import catalog from "./modules/catalog"
import productDetail from "./modules/productDetail"
import cart from "./modules/cart.js"

const store = createStore({
  actions: {},
  state: {
    showCallback: false,
    backendBaseUrl: "http://127.0.0.1:8000",
    backendApiUrl: "http://127.0.0.1:8000/api/",
  },
  getters: {
    getShowCallback: (state) => state.showCallback,
    getBackendBaseUrl: (state) => state.backendBaseUrl,
    getBackendUrl: (state) => state.backendApiUrl,
  },
  mutations: {
    toggleShowCallback(state) {
      state.showCallback = !state.showCallback
    },
  },
  modules: {
    categories,
    catalog,
    productDetail,
    cart,
  },
})
export default store
