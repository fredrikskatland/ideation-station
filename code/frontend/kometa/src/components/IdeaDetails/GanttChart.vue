<template>
    <div class="wrapper">
      <p class="text-2xl font-extrabold leading-none sm:text-2xl xl:text-2xl py-4 px-3">Suggested Gantt Chart</p>
      <g-gantt-chart
        :chart-start="chartStart"
        :chart-end="chartEnd"
        precision="week"
        width="100%"
        bar-start="startDate"
        bar-end="endDate"
        push-on-overlap="true"
      >
        <g-gantt-row
          v-for="task in taskBars"
          :key="task.ganttBarConfig.id"
          :label="task.ganttBarConfig.category"
          :bars="[task]"
          :bar-tooltip="task.ganttBarConfig.category"
          :highlight-on-hover="true"
        />
        <template v-slot:bar-tooltip="{ bar }">
        <div class="tooltip-content">
          <div><strong>Task:</strong> {{ bar.ganttBarConfig.label }}</div>
          <div><strong>Category:</strong> {{ bar.ganttBarConfig.category }}</div>
          <div><strong>Start:</strong> {{ bar.startDate }}</div>
          <div><strong>End:</strong> {{ bar.endDate }}</div>
        </div>
      </template>
      </g-gantt-chart>
    </div>
    <div v-if="ganttChart" class="p-6 max-w-4xl mx-auto bg-white rounded-xl shadow-md space-y-4">
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
  import { ref, computed } from "vue"

  
  const props = defineProps({
    ganttChart: {
      type: Object,
      required: true
    }
  });

  const paddingDays = 15;

  // Utility function to add days to a date
  function addDays(dateStr, days) {
    const date = new Date(dateStr);
    date.setDate(date.getDate() + days);
    return date.toISOString().split('T')[0];
  }

  // Find the earliest and latest dates in the tasks
  const earliestDate = props.ganttChart.tasks.reduce((earliest, task) => {
    return task.start_date < earliest ? task.start_date : earliest;
  }, props.ganttChart.tasks[0].start_date);

  const latestDate = props.ganttChart.tasks.reduce((latest, task) => {
    return task.end_date > latest ? task.end_date : latest;
  }, props.ganttChart.tasks[0].end_date);

  // Calculate chart start and end with padding
  const chartStart = computed(() => {
    return addDays(earliestDate, -paddingDays) + ' 00:00';
  });

  const chartEnd = computed(() => {
    return addDays(latestDate, paddingDays) + ' 23:59';
  });

  const taskBars = computed(() => {
    return props.ganttChart.tasks.map(task => ({
      startDate: task.start_date + ' 00:00',
      endDate: task.end_date + ' 23:59',
      ganttBarConfig: {
        id: task.id.toString(),
        category: task.label,
        label: task.name,
        status: task.status,
        immobile: true,        
        style: {
          // arbitrary CSS styling for your bar
          background: "#748B6F",
          borderRadius: "20px",
          padding: "5px",
          color: "white",
        }
      }
    }));
  });


  </script>
  
  <style scoped>
  .tooltip-content {
    background: weather-seconrary;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  </style>
  