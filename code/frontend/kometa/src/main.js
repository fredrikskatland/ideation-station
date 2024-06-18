import { createApp } from 'vue'
import { createPinia } from 'pinia';

import './index.css'
import App from './App.vue'
import router from './router'


// Import Font Awesome core
import { library } from '@fortawesome/fontawesome-svg-core'

// Import Font Awesome icon component
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Import specific icons
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

// import primevue
import PrimeVue from 'primevue/config';





// Add icons to the library
library.add(fas, far, fab)

// Create the Vue app
const pinia = createPinia()
const app = createApp(App)

// Use the router
app.use(router)

// Use the Pinia store
app.use(pinia)

// Use the PrimeVue plugin
app.use(PrimeVue, {
    unstyled: true
});

// Register the Font Awesome component globally
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')