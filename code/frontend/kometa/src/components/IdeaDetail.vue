<template>
  <div v-if="idea" class="px-32 py-12">
    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p v-html="idea.headline" class="text-3xl font-extrabold leading-none sm:text-4xl xl:text-4xl"></p>
        </div>
        <p v-html="idea.description" class="text-gray-700"></p>
    </div>

    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Target Audience</p>
        </div>
        <p v-html="idea.target_audience" class="text-gray-700"></p>
    </div>

    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Pricing</p>
        </div>
        <p v-html="idea.pricing" class="text-gray-700"></p>
    </div>

    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Marketing</p>
        </div>
        <p v-html="idea.marketing" class="text-gray-700"></p>
    </div>

    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Stand Out</p>
        </div>
        <p v-html="idea.stand_out" class="text-gray-700"></p>
    </div>

    <div class="flex">
      <div class="sm:col-span-3 lg:col-span-2 p-2">
          <div class="mb-3">
            <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Dos</p>
          </div>
          <p v-html="idea.dos" class="text-gray-700"></p>
      </div>

      <div class="sm:col-span-3 lg:col-span-2 p-2">
          <div class="mb-3">
            <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Donts</p>
          </div>
          <p v-html="idea.donts" class="text-gray-700"></p>
      </div>
    </div>

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
import RaidChart from './IdeaDetails/RaidChart.vue';  // Import the RaidChart component
import GanttChart from './IdeaDetails/GanttChart.vue';  // Import the GanttChart component
import MilestonePlan from './IdeaDetails/MilestonePlan.vue';

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
