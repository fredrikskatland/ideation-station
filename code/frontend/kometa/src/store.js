// src/store.js
import { defineStore } from 'pinia';
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user: null,
    ideas: []
  }),
  actions: {
    login(user, router) {
      this.user = user;
      this.isLoggedIn = true;
      localStorage.setItem('user', JSON.stringify(user));
      this.fetchIdeas();
      router.push('/workspace'); // Redirect to workspace
    },
    logout() {
      this.user = null;
      this.isLoggedIn = false;
      this.ideas = [];
      localStorage.removeItem('user');
    },
    checkAuth() {
      const user = localStorage.getItem('user');
      if (user) {
        this.user = JSON.parse(user);
        this.isLoggedIn = true;
        this.fetchIdeas();
      }
    },
    async fetchIdeas() {
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
    }
  },
});
