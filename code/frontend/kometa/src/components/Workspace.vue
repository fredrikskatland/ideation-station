<template>
  <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
    <div class="mb-10 border-t border-b divide-y"></div>
    <div class="grid py-8 sm:grid-cols-4">
      <div class="mb-4 sm:mb-0"></div>
      <div class="sm:col-span-3 lg:col-span-2">
        <div class="mb-3">
          <a href="/" aria-label="Article" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
            <p class="text-3xl font-extrabold leading-none sm:text-4xl xl:text-4xl sm:text-center">
              Develop new idea?
            </p>
          </a>
        </div>
        <div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12 p-4">
          <p class="text-base text-gray-700 md:text-lg">
            What is your interest, idea or concept? Develop it here.
          </p>
        </div>
        <form @submit.prevent="handleSubmit" class="flex flex-col items-center w-full mb-4 md:flex-row md:px-16">
          <input
            v-model="inputData"
            placeholder="Idea or concept"
            required
            type="text"
            class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
          />
          <button
            type="submit"
            class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide  transition duration-200 rounded shadow-md md:w-auto bg-weather-primary hover:bg-weather-secondary focus:shadow-outline focus:outline-none text-white"
          >
          <span v-if="!loading" >Submit</span>
            <span v-else class="flex items-center">
            <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
            </svg>
            Loading...
          </span>
          </button>
        </form>
      </div>
    </div>
  </div>
  <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
    <div class="mb-10 border-t border-b divide-y">
      <div class="grid py-8 sm:grid-cols-4" v-for="idea in authStore.ideas" :key="idea.id">
        <div class="mb-4 sm:mb-0">
          <div class="space-y-1 text-xs font-semibold tracking-wide uppercase">
            <router-link :to="`/idea/${idea.id}`" aria-label="Article" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
              {{ idea.topic }}
            </router-link>
            <p class="text-gray-600">{{ new Date(idea.created).toLocaleDateString() }}</p>
          </div>
        </div>
        <div class="sm:col-span-3 lg:col-span-2">
          <div class="mb-3">
            <router-link :to="`/idea/${idea.id}`" aria-label="Article" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
              <p class="text-3xl font-extrabold leading-none sm:text-4xl xl:text-4xl">
                {{ idea.headline }}
              </p>
            </router-link>
          </div>
          <p class="text-gray-700">
            {{ idea.description }}
          </p>
        </div>
      </div>
    </div>
    <div class="text-center">
      <a href="/" aria-label="" class="inline-flex items-center font-semibold transition-colors duration-200 text-deep-purple-accent-400 hover:text-deep-purple-800">
        See all articles
        <svg class="inline-block w-3 ml-2" fill="currentColor" viewBox="0 0 12 12">
          <path d="M9.707,5.293l-5-5A1,1,0,0,0,3.293,1.707L7.586,6,3.293,10.293a1,1,0,1,0,1.414,1.414l5-5A1,1,0,0,0,9.707,5.293Z"></path>
        </svg>
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../store';  // adjust the path if needed
import PocketBase from 'pocketbase';
import { marked } from 'marked';  // Use named import for 'marked'

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');  // Initialize PocketBase client
const authStore = useAuthStore();

// Reactive state
const loading = ref(false);
const inputData = ref('');

const handleSubmit = async () => {
  loading.value = true;

  try {
    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-concept-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: { topic: inputData.value }, config: {} })
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    const data = {
      idea_output: jsonResponse.output,
      user_id: pb.authStore.model.id,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('ideas').create(data);

    authStore.fetchIdeas();

  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
    headline.value = marked(`**Error:** ${error.message}`);
  } finally {
    loading.value = false;
  }
};
</script>
