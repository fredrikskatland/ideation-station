<template>
  <div v-if="idea" class="px-32 py-12">
    <div class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3">
          <p v-html="idea.headline" class="text-3xl font-extrabold leading-none sm:text-4xl xl:text-4xl"></p>
        </div>
        <p v-html="idea.description" class="text-gray-700"></p>
    </div>
    <div v-if="idea_details" class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="grid max-w-screen-lg gap-8 row-gap-10 mx-auto lg:grid-cols-2">
        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Target Audience</h6>
            <p v-html="idea_details.target_audience" class="mb-3 text-sm text-gray-900"></p>
          </div>
        </div>
        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Pricing</h6>
            <p v-html="idea_details.pricing" class="mb-3 text-sm text-gray-900"></p>
          </div>
        </div>
        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Marketing</h6>
            <p v-html="idea_details.marketing" class="mb-3 text-sm text-gray-900"></p>
          </div>
        </div>
        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Stand Out</h6>
            <p v-html="idea_details.stand_out" class="mb-3 text-sm text-gray-900"></p>
          </div>
        </div>

        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Dos</h6>
            <ul v-for="dos in idea_details.dos" :key="dos.id" class="list-disc list-inside text-lg text-gray-700 space-y-2">
              <li v-html="dos" class="mb-3 text-sm text-gray-900"></li>
            </ul>
          </div>
        </div>

        <div class="flex flex-col max-w-md sm:mx-auto sm:flex-row">
          <div>
            <h6 class="mb-3 text-xl font-bold leading-5">Donts</h6>
            <ul v-for="donts in idea_details.donts" :key="donts.id" class="list-disc list-inside text-lg text-gray-700 space-y-2">
              <li v-html="donts" class="mb-3 text-sm text-gray-900"></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
        <div class="mb-3 flex">
          <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Like the concept or idea so far? Generate details and plans!</p>
          <button @click="generateDetails" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
            <span v-if="!loading">Generate Details</span>
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

    <div v-if="idea_plans">
      <MilestonePlan :milestonePlan="idea_plans.milestone_plan" />
    </div>
    <div v-if="idea_plans">
      <GanttChart :ganttChart="idea_plans.gantt_chart" />
    </div>
    <div v-if="idea_plans">
      <RaidChart :raidChart="idea_plans.raid_chart" />
    </div>

    <div v-else class="sm:col-span-3 lg:col-span-2 p-2">
      <div class="mb-3 flex">
        <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl">Generate project management plans!</p>
        <button @click="generatePlans" class="bg-weather-primary hover:bg-weather-secondary text-white font-bold py-2 px-2 rounded mx-12">
          <span v-if="!loading">Generate Plans</span>
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


    <!-- Add other fields as needed and use v-html to render them -->
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
  <!--
  <div v-if="idea.milestone_plan">
    <MilestonePlan :milestonePlan="idea.milestone_plan" />
  </div>
  <div v-if="idea.gant_chart">
    <GanttChart :ganttChart="idea.gant_chart" />
  </div>
  <div v-if="idea.raid_chart">
    <RaidChart :raidChart="idea.raid_chart" />
  </div>
  -->
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import PocketBase from 'pocketbase';
import RaidChart from './IdeaDetails/RaidChart.vue';  // Import the RaidChart component
import GanttChart from './IdeaDetails/GanttChart.vue';  // Import the GanttChart component
import MilestonePlan from './IdeaDetails/MilestonePlan.vue';

const loading = ref(false);
const pb = new PocketBase('http://127.0.0.1:8090');
const route = useRoute();
const idea = ref(null);
const idea_details = ref(null);
const idea_plans = ref(null);

const fetchIdea = async (id) => {
  loading.value = true;
  try {
    const record = await pb.collection('ideas').getOne(id);
    idea.value = {

      id: record.id,
      headline: record.idea_output?.concept?.headline,
      description: record.idea_output?.concept?.description,
      //target_audience: record.idea_output?.concept?.target_audience,
      pricing: record.idea_output?.concept?.pricing,
      marketing: record.idea_output?.concept?.marketing,
      stand_out: record.idea_output?.concept?.stand_out,
      dos: record.idea_output?.concept?.dos,
      donts: record.idea_output?.concept?.donts,

      milestone_plan: record.idea_output?.plans?.milestone_plan,
      gant_chart: record.idea_output?.plans?.gant_chart,
      raid_chart: record.idea_output?.plans?.raid_chart,
      task_table: record.idea_output?.plans?.task_table,

      // Add other fields as needed
    };
  } catch (error) {
    console.error('Error fetching idea:', error);
  } finally {
    loading.value = false;
  }
  
};

// get details based on idea_id (relation to idea)
const fetchIdeaDetails = async (id) => {

  loading.value = true;

  try {
    const record = await pb.collection('idea_details').getList(1, 1, {
            filter: `idea_id = "${route.params.id}"`,
        });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      idea_details.value = {
        target_audience: item.target_audience,
        pricing: item.pricing,
        marketing: item.marketing,
        stand_out: item.stand_out,
        dos: item.dos,
        donts: item.donts,
      };
    }
  } catch (error) {
    console.error('Error fetching idea details:', error);
  } finally {
    loading.value = false;
  }
};

const fetchIdeaPlans = async (id) => {
  loading.value = true;

  try {
    const record = await pb.collection('idea_plans').getList(1, 1, {
            filter: `idea_id = "${route.params.id}"`,
        });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      idea_details.value = {
        milestone_plan: item.milestone_plan,
        gantt_chart: item.gantt_chart,
        raid_chart: item.raid_chart,
        stand_out: item.stand_out,
      };
    }
  } catch (error) {
    console.error('Error fetching idea plans:', error);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchIdea(route.params.id);
  fetchIdeaDetails();
  fetchIdeaPlans();
});

const generateDetails = async (id) => {
  loading.value = true;
  try {
    const res = await fetch('http://127.0.0.1:8000/idea-details-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: { concept_description: idea.value.description }, config: {} })
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

    fetchIdeaDetails();

  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading.value = false;
  }
};

const generatePlans = async () => {
  loading.value = true;

  // Create text string from idea and idea details. Add headlines and linebreaks.
  let payload = idea.value.description + '\n\n' + idea_details.value.target_audience + '\n\n' + idea_details.value.pricing + '\n\n' + idea_details.value.marketing + '\n\n' + idea_details.value.stand_out + '\n\n' + idea_details.value.dos + '\n\n' + idea_details.value.donts;
  try {
    // Call correct endpoint
    const res = await fetch('http://127.0.0.1:8000/idea-plans-chain/invoke', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: { concept_details: payload }, config: {} })
    });

    if (!res.ok) {
      throw new Error('Network response was not ok');
    }

    const jsonResponse = await res.json();

    idea_plans.value = {
      milestone_plan: jsonResponse.output?.plans?.milestone_plan,
      gantt_chart: jsonResponse.output?.plans?.gantt_chart,
      raid_chart: jsonResponse.output?.plans?.raid_chart,
    };

    const data = {
      idea_id: route.params.id,
      milestone_plan: idea_plans.value.milestone_plan,
      gantt_chart: idea_plans.value.gantt_chart,
      raid_chart: idea_plans.value.raid_chart,
      created: new Date().toISOString(),
      updated: new Date().toISOString(),
    };

    await pb.collection('idea_plans').create(data);

    fetchIdeaPlans();
    fetchIdeaDetails();

  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  } finally {
    loading.value = false;
  }
};

</script>

<style scoped>
/* Additional custom styles can go here */
</style>
