<template>
    <div class="p-6 max-w-4xl mx-auto bg-white rounded-xl shadow-md space-y-4">
      <h1 class="text-2xl font-bold mb-4">{{ ganttChart.project_name }}</h1>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white">
          <thead class="bg-gray-800 text-white">
            <tr>
              <th class="w-1/3 py-3 px-4 uppercase font-semibold text-sm">Task</th>
              <th class="w-1/3 py-3 px-4 uppercase font-semibold text-sm">Start Date</th>
              <th class="w-1/3 py-3 px-4 uppercase font-semibold text-sm">End Date</th>
              <th class="w-1/3 py-3 px-4 uppercase font-semibold text-sm">Status</th>
            </tr>
          </thead>
          <tbody class="text-gray-700">
            <tr v-for="task in ganttChart.tasks" :key="task.id">
              <td class="py-3 px-4">{{ task.name }}</td>
              <td class="py-3 px-4">{{ task.start_date }}</td>
              <td class="py-3 px-4">{{ task.end_date }}</td>
              <td class="py-3 px-4">
                <span
                  :class="{
                    'text-green-500': task.status === 'completed',
                    'text-yellow-500': task.status === 'in-progress',
                    'text-red-500': task.status === 'not-started'
                  }"
                >
                  {{ task.status }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script setup>
  
  const props = defineProps({
    ganttChart: {
      type: Object,
      required: true
    }
  });
  </script>
  
  <style scoped>
  /* Additional custom styles can go here */
  </style>
  