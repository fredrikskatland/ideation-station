<template>
  <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
    <div class="flex flex-col justify-between lg:flex-row">
      <div class="mb-12 lg:max-w-lg lg:pr-5 lg:mb-0">
        <div class="max-w-xl mb-6">
          <h2 class="max-w-lg mb-6 font-sans text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl sm:leading-none">
            Log in to start<br class="hidden md:block" />
             exploring
            <span class="inline-block text-deep-purple-accent-400">ideas.</span>
          </h2>
          <p class="text-base text-gray-700 md:text-lg">
            Go from interest, to idea to concept to execution in minutes with Ideation Station. Our platform is designed to take you from zero to one, faster.
          </p>
        </div>
        <hr class="mb-6 border-gray-300" />
        <div class="flex">
          <a href="/" aria-label="Play Song" class="mr-3">
            <div class="flex items-center justify-center w-10 h-10 text-white transition duration-300 transform rounded-full shadow-md bg-deep-purple-accent-400 hover:bg-deep-purple-accent-700 hover:scale-110">
              <svg class="w-6" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M16.53,11.152l-8-5C8.221,5.958,7.833,5.949,7.515,6.125C7.197,6.302,7,6.636,7,7v10 c0,0.364,0.197,0.698,0.515,0.875C7.667,17.958,7.833,18,8,18c0.184,0,0.368-0.051,0.53-0.152l8-5C16.822,12.665,17,12.345,17,12 S16.822,11.335,16.53,11.152z"
                ></path>
              </svg>
            </div>
          </a>
          <div class="flex flex-col">
            <div class="text-sm font-semibold">
              Back to front page
            </div>
            <div class="text-xs text-gray-700">ideationstation.ai</div>
          </div>
        </div>
      </div>
      <div class="px-5 pt-6 pb-5 text-center border border-gray-300 rounded lg:w-2/5">
        <div class="mb-5 font-semibold">Log into your account</div>
        <p class="max-w-md px-5 mb-3 text-xs text-gray-600 sm:text-sm md:mb-5">
          Log in to access the workbench and work on your ideas.
        </p>
        <div class="flex justify-center w-full mb-3">
          <div class="flex items-center">
          <button 
          class="mr-3 font-semibold text-gray-700 text-center border border-gray-300 rounded-md shadow-md px-3 py-3"
          @click="handleGoogleLogin"
          role="button"
          tabindex="0"
          @keypress.enter="handleGoogleLogin"
          @keypress.space="handleGoogleLogin"
          >
              Login with Google
              <font-awesome-icon :icon="['fab', 'google']" />
          </button>
          </div>
        </div>

        <div class="flex items-center w-full mb-5">
          <hr class="flex-1 border-gray-300" />
          <div class="px-3 text-xs text-gray-500 sm:text-sm">or</div>
          <hr class="flex-1 border-gray-300" />
        </div>
        <div class="flex justify-center w-full mb-3">
          <div class="flex items-center">
            <!-- Input form email, password and confirm password -->
            <form @submit.prevent="createUser">
                <div class="mb-1 sm:mb-2">
                  <label for="email" class="inline-block mb-1 font-medium">E-mail</label>
                  <input
                    v-model="username"
                    placeholder="john.doe@example.org"
                    required
                    type="text"
                    class="flex-grow w-full h-12 px-4 mb-2 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
                    id="email"
                    name="email"
                  />
                </div>
                <div class="mb-1 sm:mb-2">
                  <label for="password" class="inline-block mb-1 font-medium">Password</label>
                  <input
                    v-model="password"
                    placeholder=""
                    required
                    type="password"
                    class="flex-grow w-full h-12 px-4 mb-2 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
                    id="password"
                    name="password"
                  />
                </div>
                <div class="mt-4 mb-2 sm:mb-4">
                  <button 
                    type="submit"
                    @click="doLogin"
                    class="mr-3 font-semibold text-gray-700 text-center shadow-md px-3 py-3 border border-gray-300 rounded-md"
                    role="button"
                    tabindex="0"
                    @keypress.enter="doLogin"
                    @keypress.space="doLogin"
                    >
                        Log in email 
                    <font-awesome-icon :icon="['fas', 'envelope']" />
                </button>
                </div>
              </form>
            </div>
          <a
            href="/"
            class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md md:w-auto bg-deep-purple-accent-400 hover:bg-deep-purple-accent-700 focus:shadow-outline focus:outline-none"
          >
          </a>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import PocketBase from 'pocketbase';
import { useAuthStore } from '../store';  // adjust the path if needed
import { useRouter } from 'vue-router';

const username = ref("");
const password = ref("");

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');
const authStore = useAuthStore();
const router = useRouter();

const doLogin = async () => {
  try {
    const authData = await pb.collection('users').authWithPassword(username.value, password.value);
    console.log(pb.authStore.isValid);
    console.log(pb.authStore.token);
    console.log(pb.authStore.model);
    authStore.login(pb.authStore.model, router);
  } catch (error) {
    alert(error.message);
  }
}

const handleGoogleLogin = async () => {
  try {
    const authData = await pb.collection('users').authWithOAuth2({ provider: 'google' });
    const user = authData.record; // Extract user data
    const meta = authData.meta;
    const avatar = meta.avatarUrl; // Assuming the user data contains an avatar URL
    user.avatar = avatar; // Add avatar URL to user object

    authStore.login(user, router);
    alert('Logged in with Google successfully');
  } catch (error) {
    console.error('Error logging in with Google:', error);
    alert('Error logging in with Google');
  }
};
</script>
