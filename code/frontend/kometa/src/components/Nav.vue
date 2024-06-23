<template>
  <div class="bg-weather-primary px-4 py-5 mx-auto sm:max-w-xl md:max-w-full md:px-24 lg:px-8">
    <div class="relative flex grid items-center grid-cols-2 lg:grid-cols-3">
      <ul class="flex items-center hidden space-x-8 lg:flex">
        <li>
          <router-link to="/Product" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Product</router-link>
        </li>
        <li>
          <router-link to="/about" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">About</router-link>
        </li>
        <li>
          <router-link to="/Pricing" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Pricing</router-link>
        </li>
        <li>
          <router-link to="/Feedback" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Feedback</router-link>
        </li>
      </ul>
      <router-link to="/" class="inline-flex items-center lg:mx-auto">
        <font-awesome-icon icon="lightbulb" class="text-2xl text-gray-800" />
        <span class="ml-2 font-bold tracking-wide text-gray-800 uppercase text-2xl">Ideation Station</span>
      </router-link>
      <ul class="flex items-center hidden ml-auto space-x-8 lg:flex">
        <template v-if="authStore.isLoggedIn">
          <li>
            <router-link to="/workspace" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Workspace</router-link>
          </li>
          <li>
            <img :src="authStore.user.avatar" alt="User Avatar" class="w-8 h-8 rounded-full" />
            <div class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-weather-primary bg-white border-2 border-white rounded-full -top-3 dark:border-gray-900">{{ 10 - authStore.user.credits }}</div>
          </li>
          <!-- Number of credits left. Inside a white cicle -->
          <li>
            <button @click="authStore.logout" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Logout</button>
          </li>
        </template>
        <template v-else>
          <li>
            <router-link to="/login" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Sign in</router-link>
          </li>
          <li>
            <router-link to="/" class="inline-flex items-center justify-center h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-deep-purple-accent-400 hover:bg-deep-purple-accent-700 focus:shadow-outline focus:outline-none">Sign up</router-link>
          </li>
        </template>
      </ul>
      <div class="ml-auto lg:hidden">
        <button aria-label="Open Menu" title="Open Menu" class="p-2 -mr-1 transition duration-200 rounded focus:outline-none focus:shadow-outline hover:bg-deep-purple-50 focus:bg-deep-purple-50" @click="isMenuOpen = true">
          <svg class="w-5 text-gray-600" viewBox="0 0 24 24">
            <path fill="currentColor" d="M23,13H1c-0.6,0-1-0.4-1-1s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,13,23,13z"></path>
            <path fill="currentColor" d="M23,6H1C0.4,6,0,5.6,0,5s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,6,23,6z"></path>
            <path fill="currentColor" d="M23,20H1c-0.6,0-1-0.4-1-1s0.4-1,1-1h22c0.6,0,1,0.4,1,1S23.6,20,23,20z"></path>
          </svg>
        </button>
        <div v-if="isMenuOpen" class="absolute top-0 left-0 w-full">
          <div class="p-5 bg-white border rounded shadow-sm">
            <div class="flex items-center justify-between mb-4">
              <div>
                <router-link to="/" class="inline-flex items-center">
                  <svg class="w-8 text-deep-purple-accent-400" viewBox="0 0 24 24" stroke-linejoin="round" stroke-width="2" stroke-linecap="round" stroke-miterlimit="10" stroke="currentColor" fill="none">
                    <rect x="3" y="1" width="7" height="12"></rect>
                    <rect x="3" y="17" width="7" height="6"></rect>
                    <rect x="14" y="1" width="7" height="6"></rect>
                    <rect x="14" y="11" width="7" height="12"></rect>
                  </svg>
                  <span class="ml-2 text-xl font-bold tracking-wide text-gray-800 uppercase">Company</span>
                </router-link>
              </div>
              <div>
                <button aria-label="Close Menu" title="Close Menu" class="p-2 -mt-2 -mr-2 transition duration-200 rounded hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" @click="isMenuOpen = false">
                  <svg class="w-5 text-gray-600" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M19.7,4.3c-0.4-0.4-1-0.4-1.4,0L12,10.6L5.7,4.3c-0.4-0.4-1-0.4-1.4,0s-0.4,1,0,1.4l6.3,6.3l-6.3,6.3 c-0.4,0.4-0.4,1,0,1.4C4.5,19.9,4.7,20,5,20s0.5-0.1,0.7-0.3l6.3-6.3l6.3,6.3c0.2,0.2,0.5,0.3,0.7,0.3s0.5-0.1,0.7-0.3 c0.4-0.4,0.4-1,0-1.4L13.4,12l6.3-6.3C20.1,5.3,20.1,4.7,19.7,4.3z"></path>
                  </svg>
                </button>
              </div>
            </div>
            <nav>
              <ul class="space-y-4">
                <li>
                  <router-link to="/" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Product</router-link>
                </li>
                <li>
                  <router-link to="/" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Features</router-link>
                </li>
                <li>
                  <router-link to="/" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Pricing</router-link>
                </li>
                <template v-if="authStore.isLoggedIn">
                  <li>
                    <router-link to="/workspace" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Workspace</router-link>
                  </li>
                  <li>
                    <button @click="authStore.logout" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Logout</button>
                  </li>
                </template>
                <template v-else>
                  <li>
                    <router-link to="/login" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Sign in</router-link>
                  </li>
                  <li>
                    <router-link to="/" class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-deep-purple-accent-400 hover:bg-deep-purple-accent-700 focus:shadow-outline focus:outline-none">Sign up</router-link>
                  </li>
                </template>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../store';  // adjust the path if needed

const isMenuOpen = ref(false);
const authStore = useAuthStore();

</script>
<style>
@keyframes flame {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.flame {
  position: absolute;
  width: 10px;
  height: 20px;
  background: radial-gradient(circle, rgba(255,69,0,1) 0%, rgba(255,140,0,1) 70%, rgba(255,215,0,1) 100%);
  border-radius: 50% 50% 0 0;
  top: -25px;
  left: 50%;
  transform: translateX(-50%);
  animation: flame 0.5s infinite ease-in-out;
}
</style>
