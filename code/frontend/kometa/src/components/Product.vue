<template>
    <div>
        <HowItWorks />
        <UseCase />
        <HowItWorksSteps />
    </div>
</template>

<script setup>
    import HowItWorks from './HowItWorks.vue';
    import UseCase from './UseCase.vue';
    import HowItWorksSteps from './HowItWorksSteps.vue';


    import { reactive, computed } from 'vue';
    import { useHead } from '@vueuse/head';


    const siteData = reactive({
        title: 'Ideation Station - The product',
        description: 'Ideation Station is a GPT-4o wrapper that helps you generate business ideas and concepts. It is a tool for creators and builders to explore and evaluate ideas and concepts',
    });

    useHead({
        title: computed(() => siteData.title),
        meta: [
        {
            name: 'description',
            content: computed(() => siteData.description),
        },
        ],
    });

</script>