import axios from "axios"
export default {
  actions: {
    async addItemToCart({ getters, commit }, context) {
      const { productSlug, colorSlug, size } = context
      const response = await axios
        .get(
          `${
            getters.getBackendUrl
          }v1/products/${productSlug}/${colorSlug}/${size.toUpperCase()}/`
        )
        .then((response) => response.data)

      commit("addToCart", response)
    },
  },
  state: {
    cart: [],
    total: 0,
  },
  getters: {
    getCart: (state) => state.cart,
  },
  mutations: {
    setTotal(state) {
      state.total = state.cart.reduce(
        (accumulator, current) =>
          accumulator + current.price * current.quantity,
        0
      )
    },
    removeProduct(state, context) {
      const index = state.cart.findIndex((item) => {
        return (
          item.productSlug === context.productSlug &&
          item.colorSlug === context.colorSlug &&
          item.size === context.size
        )
      })
      if (index !== -1) {
        state.cart.splice(index, 1)
      }
    },
    increaseQuantity(state, context) {
      const product = state.cart.find((item) => {
        return (
          item.productSlug === context.productSlug &&
          item.colorSlug === context.colorSlug &&
          item.size === context.size
        )
      })
      if (product) {
        product.quantity += 1
      }
    },
    reduceQuantity(state, context) {
      const product = state.cart.find((item) => {
        return (
          item.productSlug === context.productSlug &&
          item.colorSlug === context.colorSlug &&
          item.size === context.size
        )
      })
      if (product) {
        product.quantity -= 1
      }
    },
    createCart(state, cart) {
      state.cart = cart
    },
    addToCart(state, data) {
      if (data) {
        data.quantity = 1
        state.cart.push(data)
      }
    },
  },
}
