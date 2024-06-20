<template>
    <div class="p-4 bg-weather-primary">
        <form @submit.prevent="handleSubmit">
            <label for="message" class="block mb-2 text-sm font-medium dark:text-white text-white">What ideas do you want to explore?</label>
            <textarea 
                ref = "el" 
                id="message" 
                rows="4" 
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                placeholder="Write your interests/ideas here..."  
                v-model="inputData"
                >
            </textarea>
            <button 
                type="submit"
                v-bind:disabled="inputData.length < 1"
                class="bg-white text-gray-900 px-4 py-2 rounded-lg mt-4 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-blue-500 dark:focus:ring-opacity-50  hover:bg-weather-secondary duration-150"
                >Submit</button>
        </form>
        <loading :active.sync="loading" :can-cancel="false" :is-full-page="true"></loading>
        <p id="resultText" class="whitespace-pre-line"></p>
        <ResultsDisplay 
          :headline="headline" 
          :description="description"
          :target_audience="target_audience"
          :pricing="pricing"
          :marketing="marketing"
          :stand_out="stand_out"
          :dos="dos"
          :donts="donts"
          :milestone_plan="milestone_plan"
          :gant_chart="gant_chart"
          :raid_chart="raid_chart"
          :task_table="task_table"

        v-if="!loading"/>
    </div>
    
</template>

<script>

    import { ref, onMounted } from 'vue';
    import { marked } from 'marked';
    import ResultsDisplay from './ResultsDisplay.vue';  // Ensure the path is correct
    import PocketBase from 'pocketbase';
    import Loading from 'vue-loading-overlay';

    const pb = new PocketBase('http://127.0.0.1:8090');  // Initialize PocketBase client
    const loading = ref(false);

    
    export default {
        components: {
          ResultsDisplay
        },
        data() {
        return {
            inputData: '',
            //response: null,
            //plans: null,
            headline: null,
            description: null,
            target_audience: null,
            pricing: null,
            marketing: null,
            stand_out: null,
            dos: null,
            donts: null,
            milestone_plan: null,
            gant_chart: null,
            raid_chart: null,
            task_table: null,
            loading: false
        };
        },
        methods: {
            async handleSubmit() {
                
                loading.value = true;
                // this.response = null; // Clear previous response
                // this.plans = null; // Clear previous plans
                this.headline = null;
                this.description = null;
                this.target_audience = null;
                this.pricing = null;
                this.marketing = null;
                this.stand_out = null;
                this.dos = null;
                this.donts = null;
                this.milestone_plan = null;
                this.gant_chart = null;
                this.raid_chart = null;
                this.task_table = null;


                try {
                    const res = await fetch('https://ideation-station-langserve.fly.dev/pirate-speak/invoke', {
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

                    this.headline = marked(jsonResponse.output.markdown.headline, null, 2);
                    this.description = marked(jsonResponse.output.markdown.description, null, 2);
                    this.target_audience = marked(jsonResponse.output.markdown.target_audience, null, 2);
                    this.pricing = marked(jsonResponse.output.markdown.pricing, null, 2);
                    this.marketing = marked(jsonResponse.output.markdown.marketing, null, 2);
                    this.stand_out = marked(jsonResponse.output.markdown.stand_out, null, 2);
                    this.dos = marked(jsonResponse.output.markdown.dos, null, 2);
                    this.donts = marked(jsonResponse.output.markdown.donts, null, 2);
                    this.milestone_plan = marked(jsonResponse.output.plans.milestone_plan, null, 2);
                    this.gant_chart = marked(jsonResponse.output.plans.gant_chart, null, 2);
                    this.raid_chart = marked(jsonResponse.output.plans.raid_chart, null, 2);
                    this.task_table = marked(jsonResponse.output.plans.task_table, null, 2);

                    const data = {
                        idea_output: jsonResponse.output,
                        user_id: pb.authStore.model.id,
                        created: new Date().toISOString(),
                        updated: new Date().toISOString(),
                    };

                    console.log(pb.authStore.token.id)
                    console.log(pb.authStore.token)

                    console.log(pb.authStore.model.id)
                    console.log(pb.authStore.model)

                    await pb.collection('ideas').create(data);

                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                    this.headline = marked(`**Error:** ${error.message}`);
                } finally {
                    loading.value = false;
                }
            }
        }
    };

</script>

<style lang="scss" scoped>
    .loading-spinner {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
    margin: 20px auto;
    text-align: center;
    }

    @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    }

</style>