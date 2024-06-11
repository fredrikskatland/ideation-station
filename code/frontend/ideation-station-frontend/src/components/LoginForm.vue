<template>
    <div class="login-form bg-weather-secondary">
      <h1>LOGIN</h1>
      <div class="sm:col-span-2 sm:col-start-1 mt-4">
        <label for="username" class="block text-sm font-medium leading-6 text-white">Email Address</label>
        <div class="mt-2">
          <input v-model="username" type="text" name="username" id="username" autocomplete="none"
            placeholder="Enter Email Address "
            class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2 sm:col-start-1 mt-2">
        <label for="password" class="block text-sm font-medium leading-6 text-white">Password</label>
        <div class="mt-2">
          <input v-model="password" type="password" name="password" id="password" autocomplete="none"
            placeholder="Enter Password "
            class=" px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2 sm:col-start-1 mt-2">
        <button type="button" @click="doLogin"
          class="mr-3 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Login</button>
        <button type="button" @click="$emit('switch-mode')"
          class="mr-3 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Create
          Account</button>
        <button type="button" @click="handleGoogleLogin"
          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
          Login with Google</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import PocketBase from 'pocketbase';
  
  const emit = defineEmits(['login-success', 'switch-mode']);
  
  const username = ref("");
  const password = ref("");
  
  const pb = new PocketBase('http://127.0.0.1:8090');
  
  const doLogin = async () => {
    try {
      const authData = await pb.collection('users').authWithPassword(username.value, password.value);
      console.log(pb.authStore.isValid);
      console.log(pb.authStore.token);
      console.log(pb.authStore.model);
      emit('login-success', pb.authStore.model);
    } catch (error) {
      alert(error.message);
    }
  }
  
  const handleGoogleLogin = async () => {
    try {
      const authData = await pb.collection('users').authWithOAuth2({ provider: 'google' });
      emit('login-success', pb.authStore.model);
      alert('Logged in with Google successfully');
    } catch (error) {
      console.error('Error logging in with Google:', error);
      alert('Error logging in with Google');
    }
  };
  </script>
  
  <style scoped>
  </style>
  