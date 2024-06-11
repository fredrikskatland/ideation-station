<template>
    <div v-if="idea">
      <h1>{{ idea.headline }}</h1>
      <p>{{ idea.description }}</p>
      <!-- Add other fields as needed -->
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import { useRoute } from 'vue-router';
  import PocketBase from 'pocketbase';
  
  const pb = new PocketBase('http://127.0.0.1:8090');
  const route = useRoute();
  const idea = ref(null);
  
  const fetchIdea = async (id) => {
    try {
      const record = await pb.collection('ideas').getOne(id);
      idea.value = {
        headline: record.idea_output.markdown.headline,
        description: record.idea_output.markdown.description,
        // Add other fields as needed
      };
    } catch (error) {
      console.error('Error fetching idea:', error);
    }
  };
  
  onMounted(() => {
    fetchIdea(route.params.id);
  });
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  