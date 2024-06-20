<template>
    <div class="form-container">
        <textarea ref="el" placeholder="What are your interests?" v-model="inputData" class="styled-textarea"></textarea>
    </div>
    <div>
        <button 
            @click="submitForm"
            v-bind:disabled="name.length < 1"
            class="styled-button"
            >Submit</button>
    </div>
    <div v-if="jsonResponse">
      <h3>JSON Response:</h3>
      <pre>{{ jsonResponse }}</pre>
    </div>
</template>

<script>
    import { ref, onMounted } from 'vue'
    import { marked } from 'marked';
    export default {
        data() {
            return {
                inputData: '',
                response: null
            }
        },
        setup() {
            const name = ref('');
            const el = ref();
            const response = ref(null);
            const htmlResponse = ref(null);
            const jsonResponse = ref(null);


            const submitForm = async () => {
                try {
                    const res = await fetch('https://ideation-station-langserve.fly.dev/pirate-speak/invoke', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        //body: JSON.stringify({ input: { topic: name.value }, config: {} })
                        body: JSON.stringify({input:{chat_history:[],text: name.value},config:{}})
                    });
                    // const jsonResponse = await res.json();
                    const response = await res.json();
                    jsonResponse.value = JSON.stringify(response, null, 2); // Format the JSON response for better readability
                    const markdownResponse = jsonResponse.output; // Extract Markdown from the response
                    htmlResponse.value = marked(markdownResponse); // Convert Markdown to HTML

                } catch (error) {
                    console.error('Error:', error);
                }
            };

            return {
                name,
                response,
                submitForm
            };

            console.log(el.value)
            onMounted(() => {
                el.value.focus()
            })
            

            return { 
                el,
                name, 
                submitForm,
             }
        },
    }

</script>

<style> 
    .form-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
    background: url('@/assets/background.webp');
  }
  
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

  .background-image {
    background-color: rgba(255, 255, 255, 0.8); /* Optional: To make the text area more readable */
    padding: 20px;
    border-radius: 10px;
  }

</style>