import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Login from './components/Login.vue';
import SignUp from './components/SignUp.vue';
import OAuthCallback from './components/OAuthCallback.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: App,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    props: (route) => ({
      pb: route.query.pb,
      currentUser: route.query.currentUser,
    }),
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    props: (route) => ({
      pb: route.query.pb,
      currentUser: route.query.currentUser,
    }),
  },
  {
    path: '/oauth/callback',
    name: 'OAuthCallback',
    component: OAuthCallback,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
