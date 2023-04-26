import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import homeView from '../components/homeView.vue'
import Introduction from "../components/Introduction.vue";
import testModal from "@/components/testModal.vue";
import login from "@/components/login.vue"
import login2 from "@/components/login2.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: '/homeView',
    name: 'homeView',
    component: homeView,
    meta: {
      keepAlive: true
    }
  },
    {
    path: '/Introduction',
    name: 'Introduction',
    component: Introduction,
    meta: {
      keepAlive: true
    }
  },
    {
    path: '/testModal',
    name: 'testModal',
    component: testModal,
    meta: {
      keepAlive: true
    }
  },
    {
    path: '/',
    name: 'Initial',
    component: login,
    // meta: {
    //   keepAlive: true
    // }
  },

  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
