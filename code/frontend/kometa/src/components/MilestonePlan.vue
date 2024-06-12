<template>
    <div class="p-6 max-w-4xl mx-auto bg-white rounded-xl shadow-md space-y-4">
      <h1 class="text-2xl font-bold mb-4">{{ milestonePlan.project_name }}</h1>
      <div v-for="milestone in milestonePlan.milestones" :key="milestone.id" class="space-y-4">
        <div class="p-4 border rounded-lg">
          <h2 class="text-xl font-semibold mb-2">{{ milestone.name }}</h2>
          <p><strong>Description:</strong> {{ milestone.description }}</p>
          <p><strong>Start Date:</strong> {{ milestone.start_date }}</p>
          <p><strong>End Date:</strong> {{ milestone.end_date }}</p>
          <h3 class="text-lg font-semibold mt-4">Tasks</h3>
          <ul class="list-disc list-inside">
            <li v-for="task in milestone.tasks" :key="task.id" class="mt-2">
              <p><strong>Task:</strong> {{ task.name }}</p>
              <p><strong>Description:</strong> {{ task.description }}</p>
              <p><strong>Status:</strong>
                <span
                  :class="{
                    'text-green-500': task.status === 'completed',
                    'text-yellow-500': task.status === 'in-progress',
                    'text-red-500': task.status === 'not-started'
                  }"
                >
                  {{ task.status }}
                </span>
              </p>
              <p><strong>Due Date:</strong> {{ task.due_date }}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    milestonePlan: {
      type: Object,
      required: true
    }
  });
  </script>
  
  <style scoped>
  /* Additional custom styles can go here */
  </style>
  