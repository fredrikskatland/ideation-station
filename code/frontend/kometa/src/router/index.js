import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Workspace from '../components/Workspace.vue'
import IdeaDetail from '../components/IdeaDetail.vue'
import About from '../components/About.vue'
import Pricing from '../components/Pricing.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/workspace', component: Workspace },
  { path: '/about', component: About },
  { path: '/pricing', component: Pricing },
  { path: '/idea/:id', component: IdeaDetail, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
