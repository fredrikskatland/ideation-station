<template>
    <div class="login bg-white p-2 shadow-lg" >
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="email">Email/Username:</label>
          <input v-model="identifier" type="text" id="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <button @click="handleGoogleLogin">Login with Google</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const props = defineProps({
    pb: {
      type: Object,
      required: true
    }
  });
  
  const emit = defineEmits(['update-user']);
  const router = useRouter();
  
  const identifier = ref('');
  const password = ref('');
  
  const handleLogin = async () => {
    try {
      const authData = await props.pb.collection('users').authWithPassword(identifier.value, password.value);
      // Update currentUser
      emit('update-user', props.pb.authStore.model);
      alert('Logged in successfully');
      router.push('/');
    } catch (error) {
      console.error('Error logging in:', error);
      alert('Error logging in');
    }
  };
  
  const handleGoogleLogin = async () => {
    try {
      const authUrl = props.pb.collection('users').getOAuth2Url('google', redirectUrl);
      window.location.href = authUrl;
      //const authData = await props.pb.collection('users').authWithOAuth2({ provider: 'google' });
      // Update currentUser
      emit('update-user', props.pb.authStore.model);
      alert('Logged in with Google successfully');
      router.push('/');
    } catch (error) {
      console.error('Error logging in with Google:', error);
      alert('Error logging in with Google');
    }
  };
  </script>
  
  <style scoped>
  
  </style>
  