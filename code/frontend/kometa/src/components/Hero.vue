<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="flex flex-col items-center justify-between lg:flex-row">
        <div class="mb-10 lg:max-w-lg lg:pr-5 lg:mb-0">
          <div class="max-w-xl mb-6">
            <div>
              <p class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-gray-700 uppercase rounded-full bg-teal-accent-400 bg-weather-primary">
                Brand new
              </p>
            </div>
            <h2 class="max-w-lg mb-6 font-sans text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl sm:leading-none">
                Develop your interest or ideas<br class="hidden md:block" />
                
              <span class="inline-block text-deep-purple-accent-400">into product and business concepts in seconds.</span>
            </h2>
            <p class="text-base text-gray-700 md:text-lg">
                Generate product or business concept, with plans, marketing, pricing, and dos and donts to help you succeed in creating it.
            </p>
          </div>
          <div class="flex items-center md:flex-row justify-center">
            <div 
            class="inline-flex items-center justify-center w-full h-12 md:h-12 lg:h-12 font-medium tracking-wide text-white transition duration-200 rounded shadow-md md:w-auto md:mr-4 md:mb-0 bg-deep-purple-accent-400 hover:bg-deep-purple-accent-700 focus:shadow-outline focus:outline-none bg-weather-primary border border-gray-700"
            >
              <!-- If logged in link to /workspace, otherwise link to /signup -->
              <div v-if="isLoggedIn">
                <router-link to="/workspace" class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-deep-purple-accent-400 p-12">Go to workspace</router-link>
              </div>
              <div v-else>
                <router-link to="/signup" class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-deep-purple-accent-400 p-12">Sign up and test for free!</router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="relative lg:w-1/2">
          <div class="relative w-full transition-shadow duration-300 hover:shadow-xl">
              <LiteYouTubeEmbed
              id="_4zGesP1oJI"
              title="Ideation Station App Demo"
          />
          </div>
        </div>
      </div>
      <HowItWorks />
      <HowItWorksSteps />
    </div>
</template>
  

<script setup>
  import { ref, onMounted } from 'vue';
  import LiteYouTubeEmbed from 'vue-lite-youtube-embed';
  import HowItWorks from './HowItWorks.vue';
  import HowItWorksSteps from './HowItWorksSteps.vue';
  import PocketBase from 'pocketbase';
  import { useAuthStore } from '../store';  // adjust the path if needed

  const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');
  const authStore = useAuthStore();
  const isLoggedIn = ref(false);

  onMounted(() => {
    isLoggedIn.value = pb.authStore.isValid;
  });
</script>
