<template>
    <div class="px-4 py-8 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-8">
      <div class="text-xl sm:text-2xl lg:text-3xl font-extrabold px-4 py-8 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-8">SCAMPER Variations</div>
      <div class="grid gap-8 row-gap-5 sm:row-gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'rotate']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Substitute</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.substitute }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fab', 'creative-commons-remix']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Combine</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.combine }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'pencil']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Adapt</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.adapt }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'screwdriver-wrench']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Modify</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.modify }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'route']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Put to another use</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.put_to_other_use }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'trash']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Eliminate</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.eliminate }}
          </p>
          
        </div>
        <div>
          <div class="flex items-center justify-center w-10 h-10 mb-4 rounded-full bg-indigo-50">
            <font-awesome-icon :icon="['fas', 'layer-group']" />
          </div>
          <h6 class="mb-2 font-semibold leading-5">Rearrange</h6>
          <p class="mb-3 text-sm text-gray-900">
            {{ idea_scamper.rearrange }}
          </p>
          
        </div>
      </div>
    </div>
  </template>

  <script setup>

  const props = defineProps({  
    idea_scamper: Object,
  });

</script>