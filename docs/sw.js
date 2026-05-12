/**
 * Suzuki GTi Car Club — Service Worker
 *
 * Strategy:
 *  - Static assets (CSS, JS, fonts, images): cache-first
 *  - HTML pages: network-first, fallback to cache, then offline.html
 *  - Update on version bump (CACHE_NAME change)
 *
 * Why: Permite consultar manuales y reparaciones desde el taller con
 * señal pobre. Crítico para uso real del archivo.
 */

const VERSION = 'v1.4.0';  /* 4 logos Suzuki S antiguo agregados al hero junto al sol naciente */
const CACHE_NAME = `gti-cache-${VERSION}`;
const RUNTIME_CACHE = `gti-runtime-${VERSION}`;

const PRECACHE_URLS = [
  '/offline.html',
  '/manifest.json',
  '/assets/img/favicon.svg',
  '/assets/img/logo-final.png',
  '/assets/img/og-image.svg',
  '/assets/css/landing-theme.css',
];

const STATIC_EXTENSIONS = ['.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.woff', '.woff2', '.ttf', '.ico', '.gif'];
const HTML_ACCEPT = 'text/html';

// === INSTALL: precache critical assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_URLS).catch((err) => {
        console.warn('[SW] Precache partial failure:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

// === ACTIVATE: cleanup old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((k) => k !== CACHE_NAME && k !== RUNTIME_CACHE)
            .map((k) => caches.delete(k))
      );
    }).then(() => self.clients.claim())
  );
});

// === FETCH: route based on request type
self.addEventListener('fetch', (event) => {
  const req = event.request;

  // Only handle GET
  if (req.method !== 'GET') return;

  // Skip cross-origin (Google Fonts, etc. — let browser handle)
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // Skip SW itself and analytics
  if (url.pathname === '/sw.js' || url.pathname.startsWith('/_/')) return;

  const isHTML = req.headers.get('Accept')?.includes(HTML_ACCEPT) ||
                 (!url.pathname.match(/\.[a-z0-9]+$/i) && req.mode === 'navigate');
  const isStatic = STATIC_EXTENSIONS.some(ext => url.pathname.endsWith(ext));

  if (isHTML) {
    // Network-first for HTML
    event.respondWith(
      fetch(req)
        .then((response) => {
          // Cache successful HTML responses
          if (response.ok) {
            const clone = response.clone();
            caches.open(RUNTIME_CACHE).then((cache) => cache.put(req, clone));
          }
          return response;
        })
        .catch(() => {
          // Network failed: try cache, then offline page
          return caches.match(req).then((cached) => {
            return cached || caches.match('/offline.html');
          });
        })
    );
  } else if (isStatic) {
    // Cache-first for static assets
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((response) => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(RUNTIME_CACHE).then((cache) => cache.put(req, clone));
          }
          return response;
        });
      })
    );
  }
  // Else: pass through (no caching)
});

// === MESSAGE: skipWaiting trigger from page
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
