<template>
  <div class="bg-weather-primary text-center max-w-1/2 mx-auto">
    <Sidebar :isOpen="isSidebarOpen" @toggle="toggleSidebar" />
    <div class="ml-0 transition-all duration-300" :class="{ 'ml-64': isSidebarOpen }">
      <button @click="toggleSidebar" class="m-4 p-2 bg-blue-500 text-white rounded">Toggle Sidebar</button>
      <!-- Main content goes here -->
      <div class="p-4">
        <h1 class="text-2xl font-bold">Main Content</h1>
        <p>Welcome to the main content area.</p>
      </div>
    </div>
    <div>
      <div v-if="currentUser">
        <div class="flex justify-center bg-weather-secondary">
          <h1 class="text-white text-3xl p-8">Welcome {{ currentUser?.email }}</h1>
          <div>
            <button type="button" @click="doLogout"
              class="rounded-md bg-indigo-600 px-3 py-2 p-8 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Logout</button>
          </div>
        </div>
        <div class="flex justify-center">
          <div v-if="ideas.length">
            <h2 class="text-white text-2xl p-3">Your Ideas</h2>
            <ul>
              <li v-for="idea in ideas" :key="idea.id" @click="selectIdea(idea)" class="cursor-pointer text-white text-1xl">
                {{ idea.headline }}
              </li>
            </ul>
          </div>
          <div>
            <h2 class="text-white text-2xl p-3">New Idea?</h2>
            <InputForm />
          </div>
        </div>
      </div>
      <div v-else class="text-white">
        <LoginForm v-if="loginMode" @switch-mode="loginMode = false" @login-success="handleLoginSuccess" />
        <RegisterForm v-else @switch-mode="loginMode = true" @login-success="handleLoginSuccess" />
      </div>
    </div>
    <div v-if="selectedIdea">
      <ResultsDisplay 
        :headline="selectedIdea.headline" 
        :description="selectedIdea.description"
        :target_audience="selectedIdea.target_audience"
        :pricing="selectedIdea.pricing"
        :marketing="selectedIdea.marketing"
        :stand_out="selectedIdea.stand_out"
        :dos="selectedIdea.dos"
        :donts="selectedIdea.donts"
        :milestone_plan="selectedIdea.milestone_plan"
        :gantt_chart="selectedIdea.gantt_chart"
        :raid_chart="selectedIdea.raid_chart"
        :task_table="selectedIdea.task_table"
      />
    </div>
    <div  v-else class="text-white">
      <UseCases />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PocketBase from 'pocketbase';
import LoginForm from './components/LoginForm.vue';
import RegisterForm from './components/RegisterForm.vue';
import ResultsDisplay from './components/ResultsDisplay.vue';
import InputForm from './components/InputForm.vue';
import UseCases from './components/UseCases.vue';
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue'


let pb = null;
const currentUser = ref();
const loginMode = ref(true);
const ideas = ref([]);
const selectedIdea = ref(null);

const isSidebarOpen = ref(false)

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

onMounted(async () => {
  pb = new PocketBase('http://127.0.0.1:8090');
  pb.authStore.onChange(() => {
    currentUser.value = pb.authStore.model;
    if (currentUser.value) {
      fetchIdeas();
    }
  }, true);
});

const doLogout = () => {
  pb.authStore.clear();
  currentUser.value = null;
  ideas.value = [];  // Clear ideas on logout
  selectedIdea.value = null;  // Clear selected idea on logout
};

const handleLoginSuccess = (user) => {
  currentUser.value = user;
  fetchIdeas();
};

const fetchIdeas = async () => {
  try {
    const records = await pb.collection('ideas').getFullList({
      filter: `user_id = "${currentUser.value.id}"`, // Fetch ideas for the current user
      sort: '-created', // Sort by creation date descending
    });
    ideas.value = records.map(record => ({
      id: record.id,
      topic: record.idea_output.topic,
      headline: record.idea_output.markdown.headline,
      description: record.idea_output.markdown.description,
      target_audience: record.idea_output.markdown.target_audience,
      pricing: record.idea_output.markdown.pricing,
      marketing: record.idea_output.markdown.marketing,
      stand_out: record.idea_output.markdown.stand_out,
      dos: record.idea_output.markdown.dos,
      donts: record.idea_output.markdown.donts,
      milestone_plan: record.idea_output.plans.milestone_plan,
      gantt_chart: record.idea_output.plans.gantt_chart,
      raid_chart: record.idea_output.plans.raid_chart,
      task_table: record.idea_output.plans.task_table,
      created: record.created
    }));
  } catch (error) {
    console.error('Error fetching ideas:', error);
  }
};

const selectIdea = (idea) => {
  selectedIdea.value = idea;
};
</script>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
