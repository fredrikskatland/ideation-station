<template>
    <div class="form-container">
        <textarea ref="el" placeholder="What are your interests?" v-model="name" class="styled-textarea"></textarea>
    </div>
    <div>
        <button 
            @click="submitForm"
            v-bind:disabled="name.length < 1"
            class="styled-button"
            >Submit</button>
    </div>
</template>

<script>
    import { ref, onMounted } from 'vue'
    export default {
        setup() {
            const name = ref('')
            const el = ref()

            const submitForm = () => {
                console.log(`Name: ${name.value}`)
            }

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

</style>