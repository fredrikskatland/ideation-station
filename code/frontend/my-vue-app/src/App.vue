<script setup>
import MyForm from './components/MyForm.vue'
</script>

<template>
  <div class="ideation-template">
    <h1>Ideation Station</h1>
    <img src="./assets/DALL·E 2024-05-31 21.49.33 - A single logo for an ideation and project management app called Ideation Station, with a serious tone. The design should be extremely clean and simple.webp" class="logo" alt="logo" />
  </div>
  <h2>What ideas do you want to explore?</h2>
  <MyForm/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.ideation-template {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: url('@/assets/DALL·E 2024-05-31 21.53.18 - Two minimalist background images for an app, using white and gray nuances with some green accents. The design should be clean and simple, featuring ab.webp') no-repeat center center/cover; /* Adjust the path accordingly */
}

.background-image {
  background-color: rgba(255, 255, 255, 0.8); /* Optional: To make the text area more readable */
  padding: 20px;
  border-radius: 10px;
}
</style>
