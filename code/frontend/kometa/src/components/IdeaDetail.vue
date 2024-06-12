<template>
  <div v-if="idea" class="px-32 py-12">
    <h1 v-html="idea.headline" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700"></h1>
    <div v-html="idea.description"></div>
    <div v-html="idea.target_audience"></div>
    <div v-html="idea.pricing"></div>
    <div v-html="idea.marketing"></div>
    <div v-html="idea.stand_out"></div>
    <div v-html="idea.dos"></div>
    <div v-html="idea.donts"></div>
    <div v-if="idea.milestone_plan">
      <MilestonePlan :milestonePlan="idea.milestone_plan" />
    </div>
    <div v-if="idea.gant_chart">
      <GanttChart :ganttChart="idea.gant_chart" />
    </div>
    <div v-if="idea.raid_chart">
      <RaidChart :raidChart="idea.raid_chart" />
    </div>
    <!-- Add other fields as needed and use v-html to render them -->
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import PocketBase from 'pocketbase';
import { marked } from 'marked';
import RaidChart from './RaidChart.vue';  // Import the RaidChart component
import GanttChart from './GanttChart.vue';  // Import the GanttChart component
import MilestonePlan from './MilestonePlan.vue';

const pb = new PocketBase('http://127.0.0.1:8090');
const route = useRoute();
const idea = ref(null);

const fetchIdea = async (id) => {
  try {
    const record = await pb.collection('ideas').getOne(id);
    idea.value = {
      headline: record.idea_output.concept.headline,
      description: record.idea_output.concept.description,
      target_audience: record.idea_output.concept.target_audience,
      pricing: record.idea_output.concept.pricing,
      marketing: record.idea_output.concept.marketing,
      stand_out: record.idea_output.concept.stand_out,
      dos: record.idea_output.concept.dos,
      donts: record.idea_output.concept.donts,

      milestone_plan: record.idea_output.plans.milestone_plan,
      gant_chart: record.idea_output.plans.gant_chart,
      raid_chart: record.idea_output.plans.raid_chart,
      task_table: record.idea_output.plans.task_table,

      // Add other fields as needed
    };
  } catch (error) {
    console.error('Error fetching idea:', error);
  }
};

const renderMarkdown = (markdown) => {
  return marked(markdown);
};

onMounted(() => {
  fetchIdea(route.params.id);
});
</script>

<style scoped>
/* Additional custom styles can go here */
</style>
