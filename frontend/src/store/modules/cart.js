// import axios from "axios"
export default {
  actions: {},
  state: {
    cart: [],
  },
  getters: {
    getCart: (state) => state.cart,
  },
  mutations: {
    createCart(state, cart) {
      state.cart = cart
    },
    addToCart(state, productContext) {
      if (productContext) {
        state.cart.push(productContext)
      }
    },
  },
}
