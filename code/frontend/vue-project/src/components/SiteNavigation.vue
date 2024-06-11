<template>
    <div>
        <header class="sticky top-0 bg-weather-primary shadow-lg">
            <nav class="container flex flex-col sm:flex-row items-center gap-4 text-white py-6">
                <div class="flex items-center gap-3">
                    <i class="fa-regular fa-lightbulb text-2xl"></i>
                    <p class="text-3xl">Ideation Station ( {{ currentUser?.username || 'Guest' }} )</p>
                </div>
                <div class="flex gap-3 flex-1 justify-end">
                    <i class="fa-solid fa-circle-info text-xl hover:text-weather-secondary duration-150"></i>
                </div>
            </nav>
        </header>
    </div>
</template>

<script setup>
const currentUser = defineProps({
    currentUser: {
      type: Object,
      required: true
    }
  });

</script>
