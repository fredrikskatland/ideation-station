import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HelloWorld.vue'
import Login from '../components/Login.vue'
import Workspace from '../components/Workspace.vue'
import IdeaDetail from '../components/IdeaDetail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/workspace', component: Workspace },
  { path: '/idea/:id', component: IdeaDetail, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
