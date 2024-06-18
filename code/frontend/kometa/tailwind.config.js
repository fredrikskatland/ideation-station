/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    'node_modules/flowbite-vue/**/*.{js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        "weather-primary": "#748B6F",
        "weather-secondary": "#2A403D",
        "weather-alternative": "#C0A9BD",
      }
    },
  },
  plugins: [require('daisyui'), require('flowbite/plugin')],
}

