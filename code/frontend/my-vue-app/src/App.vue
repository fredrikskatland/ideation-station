<script setup>
//import MyForm from './components/MyForm.vue';
import ShowCase from './components/ShowCase.vue';
import TestForm from './components/TestForm.vue';
</script>

<template>
<div class="min-h-screen bg-gray-100">
    <header class="bg-gray-800 text-white p-4">
      Header
    </header>
    <main class="container mx-auto p-6">
      <section id="ShowCase" class="w-full">
        <ShowCase/>
      </section>
      <section id="TestForm" class="w-full">
        <TestForm/>
      </section>
    </main>
    <footer class="bg-gray-800 text-white p-4">
      Footer
    </footer>
  </div>
</template>

<style scoped>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
    position: center;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
  }
  h2 {
    font-size: 1.5em;
    text-shadow: 0 0 0.2em #3a3b3d;
    margin: 1em 0;
  }

  h3 {
    font-size: 1.2em;
    color: #42b883;
    text-shadow: 0 0 0.4em #71f850;
    margin: 1em 0;
  }

  .cool-header {
    font-family: 'Pacifico', cursive;
    font-size: 3em;
    color: #2c3e50;
    text-align: center;
    margin: 20px 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }

</style>
