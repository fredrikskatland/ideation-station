<template>
  <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
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
              <pattern id="679d5905-e08c-4b91-a66c-84aefbb9d2f5" x="0" y="0" width=".135" height=".30">
                <circle cx="1" cy="1" r=".7"></circle>
              </pattern>
            </defs>
            <rect fill="url(#679d5905-e08c-4b91-a66c-84aefbb9d2f5)" width="52" height="24"></rect>
          </svg>
        </span>
        Develop your interest or ideas into product and business concepts in seconds.
      </h2>
      <p class="text-base text-gray-700 md:text-lg">
        Generate product or business concept, with plans, marketing, pricing, and dos and donts to help you succeed in creating it.
      </p>
    </div>
    <div class="mx-auto lg:max-w-2xl">
      <div class="relative w-full transition-shadow duration-300 hover:shadow-xl">
        <LiteYouTubeEmbed
        id="_4zGesP1oJI"
        title="Ideation Station App Demo"
      />
      </div>
    </div>
    <HowItWorks />
    <HowItWorksSteps />
    <div>
      Listed on: 
      <a href="https://tap4.ai/" title="Tap4 AI Tools Directory">Tap4 AI Tools Diresctory</a>
    </div>
  </div>
  
 
</template>
<script setup>
  import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
  import 'vue-lite-youtube-embed/style.css'
  import HowItWorks from './HowItWorks.vue';
  import HowItWorksSteps from './HowItWorksSteps.vue';


  import { reactive, computed } from 'vue';
  import { useHead } from '@vueuse/head';


  const siteData = reactive({
    title: 'Ideation Station - Home',
    description: 'Watch the demo, login in and start turning your interests or ideas into product and business concepts in seconds.',
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