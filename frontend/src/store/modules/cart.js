export default {
  actions: {},
  state: {
    cart: [],
  },
  getters: {
    getCart: (state) => state.cart,
  },
  mutations: {
    removeProduct(state, context) {
      state.cart = this.getters.getCart.filter((item) => {
        return (
          item.productSlug !== context.productSlug &&
          item.colorSlug !== context.colorSlug &&
          item.size !== context.size
        )
      })
    },

    increaseQuantity(state, context) {
      const product = this.getters.getCart.find((item) => {
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
      const product = this.getters.getCart.find((item) => {
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
    addToCart(state, productContext) {
      if (productContext) {
        state.cart.push(productContext)
      }
    },
  },
}
