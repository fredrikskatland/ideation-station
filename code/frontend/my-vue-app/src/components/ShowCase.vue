<template>
    <div class="bg-white p-6 rounded-lg shadow-lg flex items-center space-x-4">
        <!-- Logo -->
        <img src="../assets/logo.webp" class="logo"/>
    </div>
    <h2>Want to start a business, create a product or a project but need some help getting started?</h2>
    <h3>Ideation Station will speed up your ideation and planning process</h3>
    <div class="product-tiles">
      <div class="tile" v-for="(product, index) in products" :key="index">
        <h2>{{ product.title }}</h2>
        <p>{{ product.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: [
          { title: 'Use case 1', description: 'Description for use case 1' },
          { title: 'Use case 2', description: 'Description for use case 2' },
          { title: 'Use case 3', description: 'Description for use case 3' },
        ]
      };
    },
  };
  </script>
  
  <style scoped>
  .product-tiles {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2%;
  }
  
  .tile {
    min-width: 30%;
    min-height: 500px;
    scroll-snap-align: start;
    padding: 2%;
    box-sizing: border-box;
    border: 1px solid #ccc;
    margin-right: 2%;
  }
  </style>
  