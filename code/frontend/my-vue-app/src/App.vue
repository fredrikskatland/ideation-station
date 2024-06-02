<template>
  <div class="min-h-screen bg-gray-100">
    <header class="bg-gray-800 text-white p-4">
      <div>
        Header
        <div>
          Welcome: {{ currentUser?.username || 'Guest' }}
        </div>
        <div v-if="currentUser">
          <button type="button" @click="doLogout">Logout</button>
        </div>
        <div v-else>
          <router-link to="/login">Login</router-link> | 
          <router-link to="/signup">Sign Up</router-link>
        </div>
      </div>
    </header>
    <main class="container mx-auto p-6">
      <section id="ShowCase" class="w-full">
        <ShowCase />
      </section>
      <section id="TestForm" class="w-full">
        <TestForm />
      </section>
      <router-view :pb="pb" :currentUser="currentUser" @update-user="updateUser" />
    </main>
    <footer class="bg-gray-800 text-white p-4">
      Footer
    </footer>
  </div>
</template>

<script setup>
import ShowCase from './components/ShowCase.vue';
import TestForm from './components/TestForm.vue';
import { onMounted, ref } from 'vue';
import PocketBase from 'pocketbase';

const currentUser = ref(null);
const pb = new PocketBase('http://127.0.0.1:8090');

onMounted(async () => {
  console.log('onMounted');

  // Check if there's already an authenticated user
  if (pb.authStore.isValid) {
    currentUser.value = pb.authStore.model;
  }
});

const doLogout = async () => {
  console.log('doLogout');
  if (pb && pb.authStore) {
    await pb.authStore.clear();
    currentUser.value = null;
  } else {
    console.error('PocketBase instance or authStore is not initialized');
  }
};

const updateUser = (user) => {
  currentUser.value = user;
};
</script>

<style scoped>
/* Styles as before */
</style>
