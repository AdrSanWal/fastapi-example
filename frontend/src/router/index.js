import { createRouter, createWebHistory } from 'vue-router'
import LeafletMapView from '../views/LeafletMapView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path:'/',
    name: "map",
    component: LeafletMapView,
    // meta: {
    //   authRequired: false
    // }
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
    // meta: {
    //   authRequired: false
    // }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
