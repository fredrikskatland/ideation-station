<template>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20">
      <div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
        <div>
          <p class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400">
            Manage your account
          </p>
        </div>
        <h2 class="max-w-lg mb-6 font-sans text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto">
          <span class="relative inline-block">
            <svg viewBox="0 0 52 24" fill="currentColor" class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block">
              <defs>
                <pattern id="84d09fa9-a544-44bd-88b2-08fdf4cddd38" x="0" y="0" width=".135" height=".30">
                  <circle cx="1" cy="1" r=".7"></circle>
                </pattern>
              </defs>
              <rect fill="url(#84d09fa9-a544-44bd-88b2-08fdf4cddd38)" width="52" height="24"></rect>
            </svg>
            <span class="relative">Here</span>
          </span>
          you can make changes to your account
        </h2>
        <p class="text-base text-gray-700 md:text-lg">
          Update email, add credits or remove account.
        </p>
      </div>
      <div class="grid gap-8 row-gap-5 md:row-gap-8 lg:grid-cols-3">
        <div class="p-5 duration-300 transform bg-white border-2 border-dashed rounded shadow-sm border-deep-purple-accent-100 hover:-translate-y-2">
          <div class="flex items-center mb-2">
            <p class="flex items-center justify-center w-10 h-10 mr-2 text-lg font-bold text-white rounded-full bg-deep-purple-accent-400">
              1
            </p>
            <p class="text-lg font-bold leading-5">Email</p>
          </div>
          <p class="text-sm text-gray-900">
            {{ authStore.user.email }}
            <div class="flex items-center mt-2">
              <input v-model="inputData" placeholder="Enter new email" type="text" class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline" />            </div>
          </p>
        </div>
        <div class="p-5 duration-300 transform bg-white border-2 border-dashed rounded shadow-sm border-deep-purple-accent-200 hover:-translate-y-2">
          <div class="flex items-center mb-2">
            <p class="text-lg font-bold leading-5">Remaining credits</p>
            </div>
                <p class="text-sm text-gray-900 px-5 flex items-center space-x-3">
                    <div class="flex items-center justify-center h-12 w-12 rounded-full bg-weather-secondary">
                        <span class="text-white font-bold text-2xl">
                            {{ 10 + authStore.user.credits }}
                        </span>
                    </div>
                    <button class="flex items-center justify-center w-full h-12 px-3 font-medium tracking-wide transition duration-200 rounded shadow-md md:w-auto bg-weather-primary hover:bg-weather-secondary focus:shadow-outline focus:outline-none text-white">
                        <router-link to="/pricing" class="font-medium tracking-wide text-white transition-colors duration-200 hover:text-deep-purple-accent-400">Add credits</router-link>
                    </button>
                </p>
            </div>
        <div class="relative p-5 duration-300 transform bg-white border-2 rounded shadow-sm border-deep-purple-accent-700 hover:-translate-y-2">
          <div class="flex items-center mb-2">
            <p class="flex items-center justify-center w-10 h-10 mr-2 text-lg font-bold text-white rounded-full bg-deep-purple-accent-400">
              3
            </p>
            <p class="text-lg font-bold leading-5">Delete account</p>
          </div>
          <p class="text-sm text-gray-900">
            <button @click="deleteAccount" class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide  transition duration-200 rounded shadow-md md:w-auto bg-red-500 hover:bg-red-700 focus:shadow-outline focus:outline-none text-white">
              Delete account
            </button>
          </p>
          <p class="absolute top-0 right-0 flex items-center justify-center w-8 h-8 -mt-4 -mr-4 font-bold rounded-full bg-deep-purple-accent-400 sm:-mt-5 sm:-mr-5 sm:w-10 sm:h-10">
            <svg class="text-white w-7" stroke="currentColor" viewBox="0 0 24 24">
              <polyline fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="6,12 10,16 18,8"></polyline>
            </svg>
          </p>
        </div>
      </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useAuthStore } from '../store';  // adjust the path if needed
    import PocketBase from 'pocketbase';
    import router from '../router';
    
    const authStore = useAuthStore();
    const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL);  // Initialize PocketBase client
    
    const deleteAccount = async () => {
        if (confirm('Are you sure you want to delete your account?')) {
            await pb.collection('users').delete(authStore.user.id);
            authStore.logout();
            // Redirect to home page
            router.push('/');
        }
    }


</script>