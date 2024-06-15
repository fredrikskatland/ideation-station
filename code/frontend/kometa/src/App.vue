<template>
  <Nav />
  <router-view />
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import Nav from './components/Nav.vue'
  import HelloWorld from './components/HelloWorld.vue'
  import PocketBase from 'pocketbase';

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
          topic: record.idea_output?.topic,
          headline: record.idea_output?.concept?.headline,
          description: record.idea_output?.concept?.description,
          target_audience: record.idea_output?.concept?.target_audience,
          pricing: record.idea_output?.concept?.pricing,
          marketing: record.idea_output?.concept?.marketing,
          stand_out: record.idea_output?.concept?.stand_out,
          dos: record.idea_output?.concept?.dos,
          donts: record.idea_output?.concept?.donts,
          milestone_plan: record.idea_output?.plans?.milestone_plan,
          gant_chart: record.idea_output?.plans?.gant_chart,
          raid_chart: record.idea_output?.plans?.raid_chart,
          task_table: record.idea_output?.plans?.task_table,
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

</style>
