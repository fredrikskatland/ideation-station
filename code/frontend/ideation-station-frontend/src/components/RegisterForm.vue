<template>
    <div class="register-form bg-weather-secondary">
      <h1>CREATE ACCOUNT</h1>
      <div class="sm:col-span-2 sm:col-start-1 mt-4">
        <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Email Address</label>
        <div class="mt-2">
          <input v-model="username" type="text" name="username" id="username" autocomplete="none"
            placeholder="Enter Email Address "
            class=" px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2 sm:col-start-1 mt-2">
        <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
        <div class="mt-2">
          <input v-model="password" type="password" name="password" id="password" autocomplete="none"
            placeholder="Enter Password "
            class=" px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2 sm:col-start-1 mt-4">
        <label for="fullName" class="block text-sm font-medium leading-6 text-gray-900">Full Name</label>
        <div class="mt-2">
          <input v-model="fullName" type="text" name="fullName" id="fullName" autocomplete="none"
            placeholder="Enter Full Name "
            class=" px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
        </div>
      </div>
      <div class="sm:col-span-2 sm:col-start-1 mt-2">
        <button type="button" @click="doCreateAccount"
          class="mr-3 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save
          New User</button>
        <button type="button" @click="$emit('switch-mode')"
          class="rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-600">Cancel</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import PocketBase from 'pocketbase';
  
  const emit = defineEmits(['login-success', 'switch-mode']);
  
  const username = ref("");
  const password = ref("");
  const fullName = ref("");
  
  const pb = new PocketBase('http://127.0.0.1:8090');
  
  const doCreateAccount = async () => {
    try {
      const data = {
        "username": `user_${self.crypto.randomUUID().split("-")[0]}`,
        "email": username.value,
        "emailVisibility": true,
        "password": password.value,
        "passwordConfirm": password.value,
        "name": fullName.value
      };
  
      const record = await pb.collection('users').create(data);
      await doLogin();
    } catch (error) {
      alert(error.message);
    }
  }
  
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
  </script>
  
  <style scoped>
  </style>
  