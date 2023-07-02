import { createRouter, createWebHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/contacts",
    name: "contacts",
    component: () => import("../views/ContactsView.vue"),
  },
  {
    path: "/store",
    name: "store",
    component: () => import("../views/StoreView.vue"),
    children: [
      {
        path: ":category",
        name: "category",
        component: () => import("../views/StoreView.vue"),
      },
    ],
  },
  {
    path: "/:productSlug/:colorSlug",
    name: "product",
    component: () => import("../views/ProductView.vue"),
  },
  {
    path: "/:pathMatch(.*)",
    name: "not-found",
    component: () => import("../views/NotFoundView.vue"),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  pathToRegexpOptions: {
    strict: true,
  },
})

export default router
