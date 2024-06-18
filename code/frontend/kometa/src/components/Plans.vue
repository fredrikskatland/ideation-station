<template>
    <div>
      <div v-if="idea_plans">
        <MilestonePlan :milestonePlan="idea_plans.milestone_plan" />
        <GanttChart :ganttChart="idea_plans.gantt_chart" />
        <RaidChart :raidChart="idea_plans.raid_chart" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import MilestonePlan from './IdeaDetails/MilestonePlan.vue';
  import GanttChart from './IdeaDetails/GanttChart.vue';
  import RaidChart from './IdeaDetails/RaidChart.vue';
  import { useRoute } from 'vue-router';
  import PocketBase from 'pocketbase';
  import {
    fetchIdea,
    fetchIdeaDetails,
    fetchIdeaPlans,
    fetchIdeaQuality,
  } from '../services/apiService';
  
  const props = defineProps({  
    idea_plans: Object,
  });

  const loading = ref(false);
  const pb = new PocketBase('http://127.0.0.1:8090');
  const route = useRoute();
  
    
  //onMounted(async () => {
  //  loading.value = true;
  //  try {
  //    if (!localIdeaPlans.value) {
  //      await fetchAndSetIdeaPlans(route.params.id);
  //    }
  //  } catch (error) {
  //    console.error('Error on mounted:', error);
  //  } finally {
  //    loading.value = false;
  //  }
  //});
  
  </script>
  
  <style scoped>
  /* Additional styles */
  </style>
  