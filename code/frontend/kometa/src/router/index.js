import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Workspace from '../components/Workspace.vue'
import IdeaDetail from '../components/IdeaDetail.vue'
import About from '../components/About.vue'
import Pricing from '../components/Pricing.vue'
import Product from '../components/Product.vue'
import Feedback from '../components/Feedback.vue'
import MyUserProfile from '../components/MyUserProfile.vue'
import Hero from '../components/Hero.vue'
import IdeaDetailScroll from '../components/IdeaDetailScroll.vue'

const routes = [
  { path: '/', component: Hero },
  { path: '/login', component: Login },
  { path: '/signup', component: Signup},
  { path: '/workspace', component: Workspace },
  { path: '/about', component: About },
  { path: '/pricing', component: Pricing },
  { path: '/product', component: Product },
  { path: '/feedback', component: Feedback },
  { path: '/myuserprofile', component: MyUserProfile },
  { path: '/idea/:id', component: IdeaDetailScroll, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
