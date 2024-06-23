<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="max-w-2xl mx-auto sm:max-w-xl md:max-w-2xl">
        <div class="text-center">
          <div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
            <div>
              <p class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400">
                Brand new
              </p>
            </div>
            <h2 class="max-w-lg mb-6 font-sans text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto">
              <span class="relative inline-block">
                <svg viewBox="0 0 52 24" fill="currentColor" class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block">
                  <defs>
                    <pattern id="b039bae0-fdd5-4311-b198-8557b064fce0" x="0" y="0" width=".135" height=".30">
                      <circle cx="1" cy="1" r=".7"></circle>
                    </pattern>
                  </defs>
                  <rect fill="url(#b039bae0-fdd5-4311-b198-8557b064fce0)" width="52" height="24"></rect>
                </svg>
                <span class="relative">Any</span>
              </span>
              ideas, suggestions or complaints, leave them here.
            </h2>
            <p class="text-base text-gray-700 md:text-lg">
              You need to log in to leave feedback.
              <router-link to="/login" class="font-medium tracking-wide text-gray-700 transition-colors duration-200 hover:text-deep-purple-accent-400">Log in here</router-link>
            </p>
          </div>
          <form @submit.prevent="submitFeedback" class="flex flex-col items-center w-full mb-4 md:flex-row md:px-16">
          <input
            v-model="inputData"
            placeholder="Leave any feedback here"
            required
            type="text"
            class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
          />
          <button
            type="submit"
            class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide  transition duration-200 rounded shadow-md md:w-auto bg-weather-primary hover:bg-weather-secondary focus:shadow-outline focus:outline-none text-white"
          >
          Submit
          </button>
        </form>
          <p class="max-w-md mx-auto mb-10 text-xs text-gray-600 sm:text-sm md:mb-16">
            Any Feedback is appreciated. Thank you!
          </p>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../store';  // adjust the path if needed
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');  // Initialize PocketBase client
const authStore = useAuthStore();

const inputData = ref('');

const submitFeedback = async () => {
  // Check if user is logged in
  if (!authStore.isLoggedIn) {
    alert('You need to log in to leave feedback');
    return;
  }
  const data = {
    feedback_message: inputData.value,
    user_id: pb.authStore.model.id,
    created: new Date().toISOString(),
    updated: new Date().toISOString(),
  };
  
  await pb.collection('feedback').create(data);
  alert('Feedback submitted!')
}
</script>
