<template>
    <h2>What ideas do you want to explore?</h2>
    <div>
        <form @submit.prevent="handleSubmit">
            <div>
                <textarea ref="el" placeholder="What are your interests?" v-model="inputData" class="styled-textarea"></textarea>
            </div>
            <button 
                type="submit"
                v-bind:disabled="inputData.length < 1"
                class="styled-button"
                >Submit</button>
        </form>
        <div v-if="loading" class="spinner"></div>
        <ResultsDisplay :response="response" :plans="plans" v-if="!loading"/>
    </div>
  </template>
  
  <script>
    import { ref, onMounted } from 'vue';
    import { marked } from 'marked';
    import ResultsDisplay from './ResultsDisplay.vue';  // Ensure the path is correct
    export default {
        components: {
          ResultsDisplay
        },
        data() {
        return {
            inputData: '',
            response: null,
            plans: null,
            loading: false
        };
        },
        methods: {
        async handleSubmit() {
            this.loading = true; // Start loading
            this.response = null; // Clear previous response
            this.plans = null; // Clear previous plans
            try {
            const res = await fetch('http://localhost:8000/pirate-speak/invoke', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                //body: JSON.stringify({ data: this.inputData })
                body: JSON.stringify({input:{topic: this.inputData},config:{}})
            });
    
            if (!res.ok) {
                throw new Error('Network response was not ok');
            }
    
            const jsonResponse = await res.json();
            this.response = marked(jsonResponse.output.markdown, null, 2);
            this.plans = marked(jsonResponse.output.plans, null, 2);
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
                this.response = marked(`**Error:** ${error.message}`);
            } finally {
                this.loading = false; // End loading
            }
        }
        }
    };
  </script>
  
  <style scoped>

.styled-textarea {
    width: 300px;
    height: 150px;
    padding: 15px;
    border: 2px solid #cccccc;
    border-radius: 10px;
    font-size: 16px;
    resize: none;
    outline: none;
    transition: all 0.3s ease-in-out;
  }
  
  .styled-textarea:focus {
    border-color: #66afe9;
    box-shadow: 0 0 8px rgba(102, 175, 233, 0.6);
  }
  
  .styled-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #4CAF50;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out, transform 0.3s ease-in-out;
  }
  
  .styled-button:hover {
    background-color: #45a049;
    transform: scale(1.05);
  }


  .spinner {
    border: 16px solid #f3f3f3;
    border-top: 16px solid #3498db;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
    margin: 20px auto;
    }

    @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    }
  </style>
  