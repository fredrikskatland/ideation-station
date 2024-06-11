<template>
  <div 
    class="flex flex-col min-h-screen font-Roboto bg-weather-primary"
    >
    <SiteNavigation :currentUser="currentUser"/>
    <UseCases />
    <Login :pb="pb" @update-user="updateUser" />
    <InputForm />
</div>
</template>

<script setup>
  import { RouterView } from 'vue-router';
  import SiteNavigation from './components/SiteNavigation.vue';
  import UseCases from './components/UseCases.vue';
  import InputForm from './components/InputForm.vue';

  import { onMounted, ref } from 'vue';
  import PocketBase from 'pocketbase';
  import Login from './components/Login.vue';
  import OAuthCallback from './components/OAuthCallback.vue';


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

