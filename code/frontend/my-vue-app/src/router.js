import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Login from './components/Login.vue';
import SignUp from './components/SignUp.vue';

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
