<template>
    <div
      class="fixed inset-y-0 left-0 transform bg-gray-800 text-white w-64 transition-transform duration-300"
      :class="{ '-translate-x-full': !isOpen, 'translate-x-0': isOpen }"
    >
      <div class="flex items-center justify-between h-16 px-4">
        <span class="text-lg font-semibold">Sidebar</span>
        <button
          @click="toggleSidebar"
          class="text-gray-400 hover:text-white focus:outline-none focus:text-white"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>
      <nav class="mt-2">
        <a
          href="#"
          class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-400 hover:text-white"
        >
          Dashboard
        </a>
        <a
          href="#"
          class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-400 hover:text-white"
        >
          Settings
        </a>
        <a
          href="#"
          class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-400 hover:text-white"
        >
          Profile
        </a>
      </nav>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  
  const props = defineProps({
    isOpen: {
      type: Boolean,
      required: true
    }
  })
  
  const emit = defineEmits(['toggle'])
  
  const toggleSidebar = () => {
    emit('toggle')
  }
  </script>
  
  <style scoped>
  /* Add any additional styling here */
  </style>
  