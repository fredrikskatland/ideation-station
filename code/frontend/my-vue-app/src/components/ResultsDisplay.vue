<template>
    <div>
      <div v-if="response" class="list">
        <h3>Response:</h3>
        <div v-html="response" class="list"></div>
      </div>
      <div v-if="plans" class="list">
        <h3>Plan:</h3>
        <div v-html="plans" class="list"></div>
      </div>
    </div>
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
  .list {
    /* Add your styling here */
  }
  </style>
  