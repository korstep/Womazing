import { createStore } from "vuex"
import categories from "./modules/categories.js"
import catalog from "./modules/catalog"
import productDetail from "./modules/productDetail"
import cart from "./modules/cart.js"

const store = createStore({
  actions: {},
  state: {
    backendBaseUrl: "http://127.0.0.1:8000",
    backendApiUrl: "http://127.0.0.1:8000/api/",
  },
  getters: {
    getBackendBaseUrl: (state) => state.backendBaseUrl,
    getBackendUrl: (state) => state.backendApiUrl,
  },
  mutations: {},
  modules: {
    categories,
    catalog,
    productDetail,
    cart,
  },
})
export default store
