<template>
    <div class="p-6 max-w-4xl mx-auto bg-white rounded-xl shadow-md space-y-4">
      <h1 class="text-2xl font-bold mb-4">{{ raidChart.project_name }}</h1>
  
      <div v-if="raidChart.raid">
        <div class="space-y-6">
          <!-- Risks Section -->
          <div>
            <h2 class="text-xl font-semibold mb-2">Risks</h2>
            <div v-for="risk in raidChart.raid.risks" :key="risk.id" class="border p-4 rounded-lg">
              <p><strong>Description:</strong> {{ risk.description }}</p>
              <p><strong>Probability:</strong> {{ risk.probability }}</p>
              <p><strong>Impact:</strong> {{ risk.impact }}</p>
              <p><strong>Mitigation Plan:</strong> {{ risk.mitigation_plan }}</p>
            </div>
          </div>
  
          <!-- Assumptions Section -->
          <div>
            <h2 class="text-xl font-semibold mb-2">Assumptions</h2>
            <div v-for="assumption in raidChart.raid.assumptions" :key="assumption.id" class="border p-4 rounded-lg">
              <p><strong>Description:</strong> {{ assumption.description }}</p>
              <p><strong>Status:</strong> {{ assumption.status }}</p>
              <p><strong>Owner:</strong> {{ assumption.owner }}</p>
            </div>
          </div>
  
          <!-- Issues Section -->
          <div>
            <h2 class="text-xl font-semibold mb-2">Issues</h2>
            <div v-for="issue in raidChart.raid.issues" :key="issue.id" class="border p-4 rounded-lg">
              <p><strong>Description:</strong> {{ issue.description }}</p>
              <p><strong>Severity:</strong> {{ issue.severity }}</p>
              <p><strong>Resolution Plan:</strong> {{ issue.resolution_plan }}</p>
            </div>
          </div>
  
          <!-- Dependencies Section -->
          <div>
            <h2 class="text-xl font-semibold mb-2">Dependencies</h2>
            <div v-for="dependency in raidChart.raid.dependencies" :key="dependency.id" class="border p-4 rounded-lg">
              <p><strong>Description:</strong> {{ dependency.description }}</p>
              <p><strong>Due Date:</strong> {{ dependency.due_date }}</p>
              <p><strong>Status:</strong> {{ dependency.status }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    raidChart: {
      type: Object,
      required: true
    }
  });
  </script>
  
  <style scoped>
  /* Additional custom styles can go here */
  </style>
  