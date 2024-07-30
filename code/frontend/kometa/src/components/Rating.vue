<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-8">
        <div class="text-xl sm:text-2xl lg:text-3xl font-extrabold px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-8">Rating</div>
        <div class="grid grid-cols-2 row-gap-8 md:grid-cols-4">
          <div class="text-center md:border-r">
            <div class="radial-progress bg-weather-primary text-white border-4 border-weather-primary" :style="{ '--value': idea_quality.originality }"  role="progressbar">{{ idea_quality.originality }}</div>
            <p class="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
              Originality
            </p>
          </div>
          <div class="text-center md:border-r">
            <div class="radial-progress bg-weather-primary text-white border-4 border-weather-primary" :style="{ '--value': idea_quality.feasibility }"  role="progressbar">{{ idea_quality.feasibility }}</div>
            <p class="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
              Feasibility
            </p>
          </div>
          <div class="text-center md:border-r">
            <div class="radial-progress bg-weather-primary text-white border-4 border-weather-primary" :style="{ '--value': idea_quality.difficulty }"  role="progressbar">{{ idea_quality.difficulty }}</div>
            <p class="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
              Difficulty
            </p>
          </div>
          <div class="text-center">
            <div class="radial-progress bg-weather-primary text-white border-4 border-weather-primary" :style="{ '--value': idea_quality.profitability }"  role="progressbar">{{ idea_quality.profitability }}</div>
            <p class="text-sm font-medium tracking-widest text-gray-800 uppercase lg:text-base">
              Profitability
            </p>
          </div>
        </div>
        <div class="p-8 text-gray-700">{{ idea_quality.description  }}</div>
      </div>
</template>

<script setup>

import { ref, onMounted } from 'vue';

const props = defineProps({  
  idea_quality: Object,
});

</script>

<style lang="scss" scoped>

</style>