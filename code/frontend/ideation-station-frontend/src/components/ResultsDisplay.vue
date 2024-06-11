<template>
    <div>
      <div>
        <div v-if="headline" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Headline:</h3>
          <div v-html="headline" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150">
          </div>
        </div>
        <div v-if="description" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">description:</h3>
          <div v-html="description" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
        <div v-if="target_audience" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Target Audience:</h3>
          <div v-html="target_audience" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
        <div v-if="pricing" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Pricing:</h3>
          <div v-html="pricing" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
        <div v-if="marketing" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Marketing:</h3>
          <div v-html="marketing" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
          </div>
        <div v-if="stand_out" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Stand Out:</h3>
          <div v-html="stand_out" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
      </div>
      <div class="flex">
        <div v-if="dos" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Dos:</h3>
          <div v-html="dos" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
        <div v-if="donts" class="p-2">
          <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Donts:</h3>
          <div v-html="donts" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
        </div>
      </div>
      <div v-if="milestone_plan">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Milestone Plan:</h3>
        <div v-html="milestone_plan" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
      </div>
      <div v-if="gant_chart">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Gant Chart:</h3>
        <div v-html="gant_chart" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
      </div>
      <div v-if="raid_chart">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Raid Chart:</h3>
        <div v-html="raid_chart" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
      </div>
      <div v-if="task_table">
        <h3 class="shadow-lg bg-weather-primary text-white text-3xl font-Roboto p-2">Task Table:</h3>
        <div v-html="task_table" class="bg-weather-secondary text-white px-4 py-2 rounded-lg mt-4 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50 hover:bg-weather-secondary duration-150"></div>
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
      headline: {
        type: String,
        required: false,
        default: null
      },
      description: {
        type: String,
        required: false,
        default: null
      },
      target_audience: {
        type: String,
        required: false,
        default: null
      },
      pricing: {
        type: String,
        required: false,
        default: null
      },
      marketing: {
        type: String,
        required: false,
        default: null
      },
      stand_out: {
        type: String,
        required: false,
        default: null
      },
      dos: {
        type: String,
        required: false,
        default: null
      },
      donts: {
        type: String,
        required: false,
        default: null
      },
      milestone_plan: {
        type: String,
        required: false,
        default: null
      },
      gant_chart: {
        type: String,
        required: false,
        default: null
      },
      raid_chart: {
        type: String,
        required: false,
        default: null
      },
      task_table: {
        type: String,
        required: false,
        default: null
      },
      loading: {
        type: Boolean,
        required: false,
        default: false
      }
    }
  };
  </script>
  
  <style scoped>
  .list {
    /* Add your styling here */
  }
  </style>
  