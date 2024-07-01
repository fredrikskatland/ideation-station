// generate-sitemap.js
import { SitemapStream, streamToPromise } from 'sitemap';
import { createWriteStream } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Helper variables for module path resolution
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const sitemap = new SitemapStream({ hostname: 'https://ideationstation.ai' });

// Add your static and dynamic routes here
const routes = [
  { url: '/', changefreq: 'daily', priority: 1.0 },
  { url: '/about', changefreq: 'monthly', priority: 0.8 },
  { url: '/pricing', changefreq: 'monthly', priority: 0.8 },
  { url: '/product', changefreq: 'monthly', priority: 0.8 },
  { url: '/feedback', changefreq: 'monthly', priority: 0.8 },
  { url: '/myuserprofile', changefreq: 'monthly', priority: 0.8 },
  { url: '/login', changefreq: 'monthly', priority: 0.8 },
  { url: '/signup', changefreq: 'monthly', priority: 0.8 },
  { url: '/workspace', changefreq: 'monthly', priority: 0.8 },
  // Add more routes as needed
];

routes.forEach(route => sitemap.write(route));

sitemap.end();

streamToPromise(sitemap)
  .then(data => {
    const sitemapPath = path.resolve(__dirname, 'public', 'sitemap.xml');
    createWriteStream(sitemapPath).write(data);
  })
  .catch(console.error);
