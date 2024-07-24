<template>
  <div v-if="idea" class="px-4 py-6 sm:px-6 lg:px-8 lg:py-12">
    <div class="sm:col-span-3 lg:col-span-2 p-2">
      <div class="mb-3">
        <p v-html="idea.headline" class="text-2xl sm:text-3xl lg:text-4xl font-extrabold leading-none"></p>
      </div>
      <p v-html="idea.description" class="text-gray-700"></p>
    </div>
  </div>
  <div class="px-4 sm:px-6 lg:px-8">
    <flowbite-themable :theme="theme">
      <fwb-tabs v-model="activeTab" class="p-2 sm:p-5">
        <fwb-tab name="first" title="Details" class="text-2xl sm:text-4xl hover:bg-weather-secondary active:bg-weather-secondary">
          <div v-if="idea_details" class="px-4 py-6 sm:px-6 lg:px-8 lg:py-16">
            <div class="grid gap-8 row-gap-10 lg:grid-cols-2">
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Target Audience</h6>
                  <p v-html="idea_details.target_audience" class="mb-3 text-sm sm:text-base text-gray-900"></p>
                </div>
              </div>
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Pricing</h6>
                  <p v-html="idea_details.pricing" class="mb-3 text-sm sm:text-base text-gray-900"></p>
                </div>
              </div>
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Marketing</h6>
                  <p v-html="idea_details.marketing" class="mb-3 text-sm sm:text-base text-gray-900"></p>
                </div>
              </div>
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Stand Out</h6>
                  <p v-html="idea_details.stand_out" class="mb-3 text-sm sm:text-base text-gray-900"></p>
                </div>
              </div>
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Dos</h6>
                  <ul v-for="dos in idea_details.dos" :key="dos.id" class="list-disc list-inside text-base sm:text-lg text-gray-700 space-y-2">
                    <li v-html="dos" class="mb-3 text-sm sm:text-base text-gray-900"></li>
                  </ul>
                </div>
              </div>
              <div class="flex flex-col max-w-md mx-auto sm:flex-row">
                <div>
                  <h6 class="mb-3 text-lg sm:text-xl font-bold leading-5">Donts</h6>
                  <ul v-for="donts in idea_details.donts" :key="donts.id" class="list-disc list-inside text-base sm:text-lg text-gray-700 space-y-2">
                    <li v-html="donts" class="mb-3 text-sm sm:text-base text-gray-900"></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
            <div class="mb-3 flex">
              <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Like the concept or idea so far? Generate details and plans!</p>
              <button @click="generateDetails" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
                <span v-if="!loading_details">Generate Details</span>
                <span v-else class="flex items-center">
                  <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                  </svg>
                  Loading...
                </span>
              </button>
            </div>
            <p class="text-gray-700">Get target audience, pricing, marketing, stand out, dos, donts and project management templates.</p>
          </div>
        </fwb-tab>
        <fwb-tab name="second" title="Quality">
          <div v-if="idea_quality">
            <Rating :idea_quality="idea_quality" />
          </div>
          <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
            <div class="mb-3 flex">
              <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Rate the idea!</p>
              <button @click="generateQualityRatings" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
                <span v-if="!loading_quality">Rate Idea</span>
                <span v-else class="flex items-center">
                  <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                  </svg>
                  Loading...
                </span>
              </button>
            </div>
          </div>
        </fwb-tab>
        <fwb-tab name="third" title="Gantt Chart">
          <div v-if="idea_gantt_chart">
            <GanttChart :ganttChart="idea_gantt_chart" />
          </div>
          <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
            <div class="mb-3 flex">
              <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Generate Gantt Chart</p>
              <button @click="generateGanttChart" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
                <span v-if="!loading_gantt_chart">Generate Gantt Chart</span>
                <span v-else class="flex items-center">
                  <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                  </svg>
                  Loading...
                </span>
              </button>
            </div>
          </div>
        </fwb-tab>
        <fwb-tab name="fourth" title="SCAMPER">
          <div v-if="idea_scamper">
            <Scamper :idea_scamper="idea_scamper" />
          </div>
          <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
            <div class="mb-3 flex">
              <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Run SCAMPER method</p>
              <button @click="generateScamper" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
                <span v-if="!loading_scamper">Run SCAMPER</span>
                <span v-else class="flex items-center">
                  <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                  </svg>
                  Loading...
                </span>
              </button>
            </div>
          </div>
        </fwb-tab>
        <fwb-tab name="fifth" title="Planning" disabled>
          <div v-if="idea_plans">
            <Plans :idea_plans="idea_plans" />
          </div>
          <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
            <div class="mb-3 flex">
              <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Generate project management plans!</p>
              <button @click="generatePlans" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
                <span v-if="!loading_plans">Generate Plans</span>
                <span v-else class="flex items-center">
                  <svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                  </svg>
                  Loading...
                </span>
              </button>
            </div>
          </div>
        </fwb-tab>
        <fwb-tab name="sixth" title="Competitive landscape" disabled>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste dolores qui quos asperiores in officiis natus odit enim modi eius mollitia reprehenderit, repudiandae rem corrupti. Aliquid porro consequatur voluptatem qui?
        </fwb-tab>
        <fwb-tab name="seventh" title="Design Thinking" disabled>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste dolores qui quos asperiores in officiis natus odit enim modi eius mollitia reprehenderit, repudiandae rem corrupti. Aliquid porro consequatur voluptatem qui?
        </fwb-tab>
      </fwb-tabs>
    </flowbite-themable>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { FwbTab, FwbTabs, FlowbiteThemable } from 'flowbite-vue';
import RaidChart from './IdeaDetails/RaidChart.vue';
import GanttChart from './IdeaDetails/GanttChart.vue';
import MilestonePlan from './IdeaDetails/MilestonePlan.vue';
import Plans from './Plans.vue';
import Rating from './Rating.vue';
import Scamper from './Scamper.vue';
import {
  fetchIdea,
  fetchIdeaDetails,
  fetchIdeaPlans,
  fetchIdeaQuality,
  fetchIdeaScamper,
  fetchIdeaGanttChart,
} from '../services/apiService';
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');
const activeTab = ref('first');
const theme = 'green';
const loading_details = ref(false);
const loading_plans = ref(false);
const loading_quality = ref(false);
const loading_scamper = ref(false);
const loading_gantt_chart = ref(false);

const route = useRoute();
const idea = ref(null);
const idea_details = ref(null);
const idea_plans = ref(null);
const idea_quality = ref(null);
const idea_scamper = ref(null);
const idea_gantt_chart = ref(null);

onMounted(async () => {
  loading_details.value = true;
  loading_plans.value = true;
  loading_quality.value = true;
  loading_scamper.value = true;
  loading_gantt_chart.value = true;
  try {
    idea.value = await fetchIdea(route.params.id);
    console.log(idea.value);
    // Check if idea_details.value is null run the  generate details function, otherwise run the fetchIdeaDetails function
    if (!idea_details.value) {
      await generateDetails();
    } else {
      idea_details.value = await fetchIdeaDetails(route.params.id);
    }

    idea_details.value = await fetchIdeaDetails(route.params.id);
    console.log(idea_details.value);
    idea_plans.value = await fetchIdeaPlans(route.params.id);
    console.log(idea_plans.value);
    idea_quality.value = await fetchIdeaQuality(route.params.id);
    console.log(idea_quality.value);
    idea_scamper.value = await fetchIdeaScamper(route.params.id);
    console.log(idea_scamper.value);
    idea_gantt_chart.value = await fetchIdeaGanttChart(route.params.id);
    console.log(idea_gantt_chart.value);
    // env variable
    console.log('PocketBase url', import.meta.env.VITE_POCKETBASE_URL);
  } catch (error) {
    console.error('Error fetching data:', error);
  } finally {
    loading_details.value = false;
    loading_plans.value = false;
    loading_quality.value = false;
    loading_scamper.value = false;
    loading_gantt_chart.value = false;
  }
});

const generateDetails = async () => {
  loading_details.value = true;
  try {
    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-details-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: { concept_description: idea.value.description }, config: {} }),
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    idea_details.value = {
      target_audience: jsonResponse.output?.details?.target_audience,
      pricing: jsonResponse.output?.details?.pricing,
      marketing: jsonResponse.output?.details?.marketing,
      stand_out: jsonResponse.output?.details?.stand_out,
      dos: jsonResponse.output?.details?.dos,
      donts: jsonResponse.output?.details?.donts,
    };

    const data = {
      idea_id: route.params.id,
      target_audience: idea_details.value.target_audience,
      pricing: idea_details.value.pricing,
      marketing: idea_details.value.marketing,
      stand_out: idea_details.value.stand_out,
      dos: idea_details.value.dos,
      donts: idea_details.value.donts,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_details').create(data);

    idea.value = await fetchIdea(route.params.id);
    idea_details.value = await fetchIdeaDetails(route.params.id);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading_details.value = false;
  }
};

const generateQualityRatings = async () => {
  loading_quality.value = true;
  let payload =
    idea.value.description +
    '\n\n' +
    idea_details.value.target_audience +
    '\n\n' +
    idea_details.value.pricing +
    '\n\n' +
    idea_details.value.marketing +
    '\n\n' +
    idea_details.value.stand_out +
    '\n\n' +
    idea_details.value.dos +
    '\n\n' +
    idea_details.value.donts;
  try {
    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-quality-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: { concept_details: payload }, config: {} }),
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    idea_quality.value = {
      originality: jsonResponse.output?.quality?.originality,
      feasibility: jsonResponse.output?.quality?.feasibility,
      difficulty: jsonResponse.output?.quality?.difficulty,
      profitability: jsonResponse.output?.quality?.profitability,
      description: jsonResponse.output?.quality?.description,
    };

    const data = {
      idea_id: route.params.id,
      originality: idea_quality.value.originality,
      feasibility: idea_quality.value.feasibility,
      difficulty: idea_quality.value.difficulty,
      profitability: idea_quality.value.profitability,
      description: idea_quality.value.description,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_quality').create(data);

    idea.value = await fetchIdea(route.params.id);
    idea_details.value = await fetchIdeaDetails(route.params.id);
    idea_plans.value = await fetchIdeaPlans(route.params.id);
    idea_quality.value = await fetchIdeaQuality(route.params.id);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading_quality.value = false;
  }
};

const generatePlans = async () => {
  loading_plans.value = true;

  try {
    // Create text string from idea and idea details. Add headlines and linebreaks.
    let payload =
      idea.value.description +
      '\n\n' +
      idea_details.value.target_audience +
      '\n\n' +
      idea_details.value.pricing +
      '\n\n' +
      idea_details.value.marketing +
      '\n\n' +
      idea_details.value.stand_out +
      '\n\n' +
      idea_details.value.dos +
      '\n\n' +
      idea_details.value.donts;

    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-plans-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: { concept_details: payload }, config: {} }),
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    if (!jsonResponse.output || !jsonResponse.output.plans) {
      throw new Error('Invalid response structure');
    }

    const data = {
      idea_id: route.params.id,
      milestone_plan: jsonResponse.output.plans.milestone_plan,
      gantt_chart: jsonResponse.output.plans.gantt_chart,
      raid_chart: jsonResponse.output.plans.raid_chart,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_plans').create(data);

    console.log('Data successfully saved to PocketBase');
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading_plans.value = false;
    idea_plans.value = await fetchIdeaPlans(route.params.id);
  }
};

const generateScamper = async () => {
  loading_scamper.value = true;
  let payload =
    idea.value.description +
    '\n\n' +
    idea_details.value.target_audience +
    '\n\n' +
    idea_details.value.pricing +
    '\n\n' +
    idea_details.value.marketing +
    '\n\n' +
    idea_details.value.stand_out +
    '\n\n' +
    idea_details.value.dos +
    '\n\n' +
    idea_details.value.donts;
  try {
    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-scamper-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: { concept_description: payload }, config: {} }),
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    idea_scamper.value = {
      substitute: jsonResponse.output?.scamper?.substitute,
      combine: jsonResponse.output?.scamper?.combine,
      adapt: jsonResponse.output?.scamper?.adapt,
      modify: jsonResponse.output?.scamper?.modify,
      put_to_other_use: jsonResponse.output?.scamper?.put_to_other_use,
      eliminate: jsonResponse.output?.scamper?.eliminate,
      rearrange: jsonResponse.output?.scamper?.rearrange,
    };

    const data = {
      idea_id: route.params.id,
      substitute: idea_scamper.value.substitute,
      combine: idea_scamper.value.combine,
      adapt: idea_scamper.value.adapt,
      modify: idea_scamper.value.modify,
      put_to_other_use: idea_scamper.value.put_to_other_use,
      eliminate: idea_scamper.value.eliminate,
      rearrange: idea_scamper.value.rearrange,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_scamper').create(data);

    idea.value = await fetchIdea(route.params.id);
    idea_scamper.value = await fetchIdeaScamper(route.params.id);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading_scamper.value = false;
  }
};

const generateGanttChart = async () => {
  loading_gantt_chart.value = true;
  let payload =
    idea.value.description +
    '\n\n' +
    idea_details.value.target_audience +
    '\n\n' +
    idea_details.value.pricing +
    '\n\n' +
    idea_details.value.marketing +
    '\n\n' +
    idea_details.value.stand_out +
    '\n\n' +
    idea_details.value.dos +
    '\n\n' +
    idea_details.value.donts;
  try {
    const res = await fetch('https://ideation-station-langserve.fly.dev/idea-gantt-chart-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: { concept_details: payload }, config: {} }),
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    idea_gantt_chart.value = {
      gantt_chart: jsonResponse.output?.gantt_chart,
    };

    const data = {
      idea_id: route.params.id,
      gantt_chart: idea_gantt_chart.value.gantt_chart,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_gantt_chart').create(data);

    idea.value = await fetchIdea(route.params.id);
    idea_gantt_chart.value = await fetchIdeaGanttChart(route.params.id);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading_gantt_chart.value = false;
  }
};
</script>
<style scoped>
/* Additional custom styles can go here */
</style>
