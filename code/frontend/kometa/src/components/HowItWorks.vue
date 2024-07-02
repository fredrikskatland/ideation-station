<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="p-8 rounded shadow-xl sm:p-16">
        <div class="flex flex-col lg:flex-row">
          <div class="mb-6 lg:mb-0 lg:w-1/2 lg:pr-5">
            <h2 class="font-sans text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl sm:leading-none">
              How does it work?<br class="hidden md:block" />
              What value
              <span class="inline-block text-deep-purple-accent-400">does it bring?</span>
            </h2>
          </div>
          <div class="lg:w-1/2">
            <p class="mb-4 text-base text-gray-700">
              Yes, this is a GPT-4 wrapper. 
              It accepts your input, processes it through a prompt template, and forwards it to the GPT-4 model. 
              The prompt is designed to create an original response and help you, as a creator or builder, examine the various aspects of realizing your idea. 
              The output is parsed to ensure a tidy and structured result, which is then displayed nicely in the app.      
            </p>
          </div>
        </div>
      </div>
    </div>
  </template>

  <script setup>

    import { reactive, computed } from 'vue';
    import { useHead } from '@vueuse/head';


    const siteData = reactive({
      title: 'Ideation Station - How does it work?',
      description: 'Ideation takes your interests or idea keywords as prompts and creates a business concept or product around it.',
    });

    useHead({
      title: computed(() => siteData.title),
      meta: [
        {
          name: 'description',
          content: computed(() => siteData.description),
        },
      ],
    });

  </script>