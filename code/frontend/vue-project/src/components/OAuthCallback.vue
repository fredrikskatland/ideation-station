<template>
    <div>Processing OAuth callback...</div>
</template>
  
<script setup>
  import { onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  
  const props = defineProps({
    pb: {
      type: Object,
      required: true
    }
  });
  
  const emit = defineEmits(['update-user']);
  const router = useRouter();
  const route = useRoute();
  
  onMounted(async () => {
    try {
      const { code, state } = route.query;
      await props.pb.collection('users').authWithOAuth2Code('google', code, state);
      emit('update-user', props.pb.authStore.model);
      alert('Logged in with Google successfully');
      router.push('/');
    } catch (error) {
      console.error('Error processing OAuth callback:', error);
      alert('Error processing OAuth callback');
    }
  });
</script>
  
  <style scoped>
  /* Your styles here */
  </style>
  