import { createRouter, createWebHistory } from "vue-router"
import HomeView from "@/views/HomeView.vue"
import MainLayout from "@/layouts/MainLayout.vue"

const routes = [
  {
    path: "/",
    component: MainLayout,
    name: "main",
    redirect: { name: "home" },
    meta: {
      breadCrumbs: {
        title: "Главная",
      },
    },
    children: [
      {
        path: "",
        name: "home",
        component: HomeView,
        meta: {
          breadCrumbs: {
            hide: true,
            title: "",
          },
        },
      },
      {
        path: "about",
        name: "about",
        component: () => import("../views/AboutView.vue"),
        meta: {
          breadCrumbs: {
            title: "О бренде",
          },
        },
      },
      {
        path: "contacts",
        name: "contacts",
        component: () => import("../views/ContactsView.vue"),
        meta: {
          breadCrumbs: {
            title: "Контакты",
          },
        },
      },
      {
        path: "store",
        name: "store",
        component: () => import("../views/StoreView.vue"),
        meta: {
          breadCrumbs: {
            title: "Магазин",
          },
        },
      },
      {
        path: "cart",
        name: "cart",
        component: () => import("../views/CartView.vue"),
        meta: {
          breadCrumbs: {
            title: "Корзина",
          },
        },
      },
      {
        path: ":category",
        name: "category",
        redirect: { name: "categoryHome" },
        meta: {
          breadCrumbs: {
            title: "category",
          },
        },
        children: [
          {
            path: "",
            name: "categoryHome",
            meta: {
              breadCrumbs: {
                hide: true,
                title: "hello",
              },
            },
            component: () => import("../views/StoreView.vue"),
          },
          {
            path: ":productSlug/:colorSlug",
            name: "product",
            component: () => import("../views/ProductView.vue"),
            props: (route) => ({ query: route.query.q }),
            meta: {
              breadCrumbs: {
                title: "productSlug",
              },
            },
          },
        ],
      },
    ],
  },
  {
    path: "/:pathMatch(.*)*",
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
