<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="grid max-w-2xl mx-auto">
        <div class="flex">
          <div class="flex flex-col items-center mr-6">
            <div class="w-px h-10 opacity-0 sm:h-full"></div>
            <div>
              <div class="flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full">
                1
              </div>
            </div>
            <div class="w-px h-full bg-gray-300"></div>
          </div>
          <div class="flex flex-col pb-6 sm:items-center sm:flex-row sm:pb-0">
            <div class="sm:mr-5">
              <div class="flex items-center justify-center w-16 h-16 my-3 rounded-full bg-indigo-50 sm:w-24 sm:h-24">
                <font-awesome-icon :icon="['fas', 'user']" class="w-12 h-12" />
              </div>
            </div>
            <div>
              <p class="text-xl font-semibold sm:text-base">Log in</p>
              <p class="text-sm text-gray-700">
                Log in or create an account to access the workbench and start creating your product or business concept.
              </p>
            </div>
          </div>
        </div>
        <div class="flex">
          <div class="flex flex-col items-center mr-6">
            <div class="w-px h-10 bg-gray-300 sm:h-full"></div>
            <div>
              <div class="flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full">
                2
              </div>
            </div>
            <div class="w-px h-full bg-gray-300"></div>
          </div>
          <div class="flex flex-col pb-6 sm:items-center sm:flex-row sm:pb-0">
            <div class="sm:mr-5">
              <div class="flex items-center justify-center w-16 h-16 my-3 rounded-full bg-indigo-50 sm:w-24 sm:h-24">
                <font-awesome-icon :icon="['fas', 'keyboard']" class="w-12 h-12"/>
              </div>
            </div>
            <div>
              <p class="text-xl font-semibold sm:text-base">Input your interets or ideas</p>
              <p class="text-sm text-gray-700">
                Input your prompt; it can be a generall interest you want to build something around, or a concrete idea you want to develop further.
              </p>
            </div>
          </div>
        </div>
        <div class="flex">
          <div class="flex flex-col items-center mr-6">
            <div class="w-px h-10 bg-gray-300 sm:h-full"></div>
            <div>
              <div class="flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full">
                3
              </div>
            </div>
            <div class="w-px h-full opacity-0"></div>
          </div>
          <div class="flex flex-col pb-6 sm:items-center sm:flex-row sm:pb-0">
            <div class="sm:mr-5">
              <div class="flex items-center justify-center w-16 h-16 my-3 rounded-full bg-indigo-50 sm:w-24 sm:h-24">
                <font-awesome-icon :icon="['fab', 'wpexplorer']" class="w-12 h-12"/>
              </div>
            </div>
            <div>
              <p class="text-xl font-semibold sm:text-base">Explore deeper</p>
              <p class="text-sm text-gray-700">
                Explore the generated concept deeper by analyzing target audience, marketing, pricing options, and dos and donts to help you succeed in creating it.
              </p>
            </div>
          </div>
        </div>
        <div class="flex">
          <div class="flex flex-col items-center mr-6">
            <div class="w-px h-10 bg-gray-300 sm:h-full"></div>
            <div>
              <div class="flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full">
                4
              </div>
            </div>
            <div class="w-px h-full opacity-0"></div>
          </div>
          <div class="flex flex-col pb-6 sm:items-center sm:flex-row sm:pb-0">
            <div class="sm:mr-5">
              <div class="flex items-center justify-center w-16 h-16 my-3 rounded-full bg-indigo-50 sm:w-24 sm:h-24">
                <font-awesome-icon :icon="['fas', 'gauge-high']" class="w-12 h-12"/>
              </div>
            </div>
            <div>
              <p class="text-xl font-semibold sm:text-base">Evaluate the concept</p>
              <p class="text-sm text-gray-700">
                Use the built in AI functionality to get a sense of the quality of the concept, by rating it with respect to originality, feasibility, difficulty and profitability.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>