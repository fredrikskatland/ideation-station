<template>
    <div class="signup">
      <h2>Sign Up</h2>
      <form @submit.prevent="handleSignUp">
        <div>
          <label for="email">Email:</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <div>
          <label for="username">Username:</label>
          <input v-model="username" type="text" id="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" type="password" id="password" required />
        </div>
        <button type="submit">Sign Up</button>
      </form>
      <button @click="handleGoogleSignUp">Sign Up with Google</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { defineEmits, defineProps } from 'vue';
  
  const props = defineProps({
    pb: {
      type: Object,
      required: true
    }
  });
  
  const emit = defineEmits(['update-user']);
  const router = useRouter();
  
  const email = ref('');
  const username = ref('');
  const password = ref('');
  
  const handleSignUp = async () => {
    try {
      const newUser = {
        email: email.value,
        username: username.value,
        password: password.value,
        passwordConfirm: password.value
      };
      await props.pb.collection('users').create(newUser);
      
      // Authenticate the new user immediately after creation
      const authData = await props.pb.collection('users').authWithPassword(username.value, password.value);
      
      // Update currentUser
      emit('update-user', props.pb.authStore.model);
  
      alert('User created and logged in successfully');
      router.push('/');
    } catch (error) {
      console.error('Error creating user:', error);
      alert('Error creating user');
    }
  };
  
  const handleGoogleSignUp = async () => {
    try {
      const authData = await props.pb.collection('users').authWithOAuth2({ provider: 'google' });
      // Update currentUser
      emit('update-user', props.pb.authStore.model);
      
      alert('Signed up with Google successfully');
      router.push('/');
    } catch (error) {
      console.error('Error signing up with Google:', error);
      alert('Error signing up with Google');
    }
  };
  </script>
  
  <style scoped>
  .signup {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  .signup h2 {
    margin-bottom: 20px;
    text-align: center;
  }
  .signup form {
    display: flex;
    flex-direction: column;
  }
  .signup form > div {
    margin-bottom: 10px;
  }
  .signup button {
    margin-top: 10px;
  }
  </style>
  