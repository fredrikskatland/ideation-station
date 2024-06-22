// src/store.js
import { defineStore } from 'pinia';
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user: null,
    token: null,
    ideas: []
  }),
  actions: {
    login(user, router) {
      this.user = user;
      this.isLoggedIn = true;
      this.token = pb.authStore.token;
      localStorage.setItem('user', JSON.stringify(user));
      localStorage.setItem('token', this.token)
      this.fetchIdeas();
      router.push('/workspace'); // Redirect to workspace
    },
    logout() {
      this.user = null;
      this.isLoggedIn = false;
      this.token = null;
      this.ideas = [];
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      pb.authStore.clear(); // Clear the authStore on logout
    },
    checkAuth() {
      const user = localStorage.getItem('user');
      const token = localStorage.getItem('token');
      if (user && token) {
        this.user = JSON.parse(user);
        this.token = token;
        pb.authStore.save(token, JSON.parse(user)); // Restore token and user model in authStore
        this.isLoggedIn = true;
        this.fetchIdeas();
      }
    },
    async fetchIdeas() {
      if (!this.user) return; // Return if there is no user
      try {
        const records = await pb.collection('ideas').getFullList({
          filter: `user_id = "${this.user.id}"`, // Fetch ideas for the current user
          sort: '-created', // Sort by creation date descending
        });
        this.ideas = records.map(record => ({
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
    },
    updateCredits(newCredits) {
      this.user.credits = newCredits;
    }
    
  },
});
