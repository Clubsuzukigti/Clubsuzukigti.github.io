"""Inyecta meta tags SEO/OG/PWA en el <head> de ambos bundles.

Adds:
  - Preconnect a Google Fonts (carga más rápida)
  - Open Graph + Twitter Card meta
  - Theme-color para mobile address bar
  - Manifest.json link (PWA support)
  - Apple touch icon
  - Canonical URL
  - Lang attribute correcto

Idempotente: detecta si ya se inyectó y no duplica.
"""
from pathlib import Path

TARGETS = {
    'es': {
        'path': Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.html"),
        'title': 'Suzuki GTi Car Club — Preservando el legado del Swift GTi',
        'description': 'Archivo técnico, repuestos y comunidad mundial del Suzuki Swift GTi (G13B DOHC 16V, 1989-1994). 800K+ miembros en 24 países.',
        'url': 'https://clubsuzukigti.github.io/landing/',
        'lang': 'es',
    },
    'en': {
        'path': Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.en.html"),
        'title': 'Suzuki GTi Car Club — Preserving the Swift GTi legacy',
        'description': 'Technical archive, parts and worldwide community of the Suzuki Swift GTi (G13B DOHC 16V, 1989-1994). 800K+ members in 24 countries.',
        'url': 'https://clubsuzukigti.github.io/en/landing/',
        'lang': 'en',
    },
}

INJECT_MARKER = '<!-- gti-head-injected -->'


def build_head(t):
    return f"""  {INJECT_MARKER}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <meta name="description" content="{t['description']}">
  <meta name="theme-color" content="#0A0908">
  <meta name="color-scheme" content="dark">
  <link rel="canonical" href="{t['url']}">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="/assets/img/logo-final.png">
  <link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
  <link rel="icon" type="image/png" href="/assets/img/favicon.png">
  <link rel="shortcut icon" href="/assets/img/favicon.ico">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{'es_GT' if t['lang']=='es' else 'en_US'}">
  <meta property="og:title" content="{t['title']}">
  <meta property="og:description" content="{t['description']}">
  <meta property="og:url" content="{t['url']}">
  <meta property="og:site_name" content="Suzuki GTi Car Club">
  <meta property="og:image" content="https://clubsuzukigti.github.io/assets/img/og-image.svg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['title']}">
  <meta name="twitter:description" content="{t['description']}">
  <meta name="twitter:image" content="https://clubsuzukigti.github.io/assets/img/og-image.svg">

  <!-- Cross-locale link rel alternate -->
  <link rel="alternate" hreflang="es" href="https://clubsuzukigti.github.io/landing/">
  <link rel="alternate" hreflang="en" href="https://clubsuzukigti.github.io/en/landing/">
  <link rel="alternate" hreflang="x-default" href="https://clubsuzukigti.github.io/landing/">
"""


def inject(path, meta):
    html = path.read_text(encoding='utf-8')
    if INJECT_MARKER in html:
        # Remove previous injection (between marker and just before "<style>" or "</head>")
        marker_idx = html.find(INJECT_MARKER)
        # Find where head meta ends — search for next sibling significant tag
        head_end = html.find('</head>', marker_idx)
        # Find the last <link> or <meta> our injection added, which is before any subsequent <style> or </head>
        # Strategy: drop from INJECT_MARKER's line start to the last </link> or </meta> before next <noscript>/<style>
        # Easier: find the last <link rel="alternate"> we inject (the cross-locale ones)
        last_inject = html.find('hreflang="x-default"', marker_idx)
        if last_inject != -1:
            # Move to next ">"
            close = html.find('>', last_inject) + 1
            html = html[:marker_idx] + html[close:]
            # Normalize the seam
            html = html.replace('\n\n\n', '\n\n')
            print(f"  Removed previous head injection in {path.name}")

    head = build_head(meta)
    new = html.replace('</head>', head + '</head>', 1)
    # Also fix lang attribute on <html>
    if meta['lang'] == 'en':
        new = new.replace('<html lang="es">', '<html lang="en">', 1)
    path.write_text(new, encoding='utf-8')
    print(f"  Injected {len(head)} bytes head meta into {path.name}")


for code, t in TARGETS.items():
    print(f"=== {t['path'].name} ({code}) ===")
    inject(t['path'], t)
print("Done.")
