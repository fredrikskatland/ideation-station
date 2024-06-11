<template>
  
    <div class="flex flex-col items-center justify-center">
      <div v-if="response">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Response:</h3>
        <div v-html="response" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150">
        </div>
      </div>
      <div v-if="plans">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Plan:</h3>
        <div v-html="plans" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
      </div>
    </div>
  <!--
    <div class="flex flex-col items-center justify-center">
      <div v-if="response">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Response:</h3>
        <div v-html="response" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150">
        </div>
      </div>
      <div v-if="plans">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Plan:</h3>
        <div v-html="plans" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
      </div>
    </div>
  -->
  </template>
  
  <script>
  export default {
    props: {
      response: {
        type: String,
        required: false,
        default: null
      },
      plans: {
        type: String,
        required: false,
        default: null
      }
    }
  };
  </script>
  
  <style scoped>

  </style>
  