<template>
    <div>
        <header>
            <nav class="bg-black shadow">
                <div  v-if="currentUser" class="container px-6 py-6 mx-auto md:flex md:justify-between md:items-center">
                    Welcome {{ currentUser?.email }}
                </div>
                <div v-else>Hello</div>
            </nav>
        </header>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>