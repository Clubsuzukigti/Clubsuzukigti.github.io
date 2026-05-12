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

# Static CSS for deep-nav overlay — outside f-string para evitar escape de {} CSS
OVERLAY_CSS = """
  <style id="gti-overlay-styles">
    .gti-progress {
      position: fixed; top: 0; left: 0;
      height: 2px; width: 0%;
      background: linear-gradient(90deg, #E20A17 0%, #FFB347 100%);
      z-index: 10000;
      transition: width .15s ease-out;
      pointer-events: none;
      box-shadow: 0 0 8px rgba(255,179,71,0.6);
    }
    .deep-nav {
      position: fixed; top: 0; left: 0; right: 0;
      z-index: 9998;
      background: rgba(10,9,8,0.92);
      backdrop-filter: blur(14px) saturate(140%);
      -webkit-backdrop-filter: blur(14px) saturate(140%);
      padding: 12px 24px;
      display: flex; gap: 10px; align-items: center; justify-content: center;
      flex-wrap: wrap;
      font-family: 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
      border-bottom: 1px solid rgba(255,179,71,0.22);
      opacity: 0; transform: translateY(-100%);
      transition: opacity .55s ease, transform .55s ease;
      pointer-events: none;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    .deep-nav.visible { opacity: 1; transform: translateY(0); pointer-events: auto; }
    .deep-nav a {
      display: inline-flex; align-items: center;
      padding: 7px 14px;
      border-radius: 22px;
      background: rgba(255,255,255,0.025);
      border: 1px solid rgba(255,179,71,0.18);
      color: #F5EFE0;
      text-decoration: none;
      font-size: 10.5px;
      font-weight: 600;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      transition: all .25s ease;
      white-space: nowrap;
      line-height: 1;
    }
    .deep-nav a:hover {
      color: #FFB347;
      background: rgba(255,179,71,0.1);
      border-color: rgba(255,179,71,0.55);
      transform: translateY(-1px);
      box-shadow: 0 4px 10px rgba(255,179,71,0.18);
    }
    .deep-nav a.lang {
      margin-left: 6px;
      background: rgba(226,10,23,0.18);
      border-color: rgba(226,10,23,0.5);
      color: #F5EFE0;
      font-weight: 700;
      letter-spacing: 2.2px;
    }
    .deep-nav a.lang:hover {
      background: #E20A17;
      border-color: #E20A17;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(226,10,23,0.4);
    }
    .deep-nav .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #FFB347;
      box-shadow: 0 0 10px #FFB347, 0 0 4px rgba(255,179,71,0.6);
      flex-shrink: 0;
      margin-right: 4px;
      animation: gti-bulb-pulse 4s ease-in-out infinite;
    }
    @keyframes gti-bulb-pulse {
      0%,100% { opacity: 0.85; }
      50% { opacity: 0.45; }
    }
    .gti-section-cta {
      display: block;
      margin: 3em auto 1em;
      max-width: 580px;
      padding: 1.2em 1.8em;
      background: rgba(255,179,71,0.04);
      border: 1px solid rgba(255,179,71,0.28);
      border-radius: 4px;
      color: #FFB347;
      text-decoration: none;
      font-family: 'Inter Tight',sans-serif;
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      text-align: center;
      transition: all .3s cubic-bezier(.34,1.56,.64,1);
      position: relative;
      overflow: hidden;
    }
    .gti-section-cta::before {
      content: ''; position: absolute; left: -100%; top: 0; height: 100%; width: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,179,71,0.12), transparent);
      transition: left .6s;
    }
    .gti-section-cta:hover::before { left: 100%; }
    .gti-section-cta:hover {
      background: rgba(255,179,71,0.1);
      border-color: #FFB347;
      color: #FFD580;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(255,179,71,0.18);
    }
    .gti-section-cta::after {
      content: '  \\2192';
      display: inline-block;
      margin-left: 4px;
      transition: transform .3s;
    }
    .gti-section-cta:hover::after { transform: translateX(6px); }
    .gti-back-top {
      position: fixed;
      bottom: 24px; right: 24px;
      z-index: 9997;
      width: 44px; height: 44px;
      border-radius: 50%;
      background: rgba(10,9,8,0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,179,71,0.3);
      color: #FFB347;
      cursor: pointer;
      opacity: 0; transform: translateY(20px);
      transition: opacity .4s, transform .4s, border-color .25s;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    }
    .gti-back-top.show { opacity: 1; transform: translateY(0); }
    .gti-back-top:hover { border-color: #FFB347; color: #FFD580; }
    @media (max-width: 900px) {
      .deep-nav { padding: 10px 12px; gap: 6px; }
      .deep-nav a { padding: 6px 10px; font-size: 9.5px; letter-spacing: 1.4px; }
      .deep-nav a.lang { margin-left: 2px; }
    }
    @media (max-width: 720px) {
      .gti-back-top { bottom: 16px; right: 16px; width: 38px; height: 38px; }
    }
    @media (max-width: 480px) {
      .deep-nav { padding: 8px; gap: 5px; }
      .deep-nav a { padding: 5px 8px; font-size: 9px; letter-spacing: 1px; border-radius: 16px; }
      .deep-nav .dot { display: none; }
    }
  </style>
"""


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
""" + OVERLAY_CSS


def _unused_dupe_block():
    """Removed — CSS now lives in OVERLAY_CSS above"""
    return """
  <style id="gti-overlay-styles-dupe">
    .gti-progress {
      position: fixed; top: 0; left: 0;
      height: 2px; width: 0%;
      background: linear-gradient(90deg, #E20A17 0%, #FFB347 100%);
      z-index: 10000;
      transition: width .15s ease-out;
      pointer-events: none;
      box-shadow: 0 0 8px rgba(255,179,71,0.6);
    }
    .deep-nav {
      position: fixed; top: 0; left: 0; right: 0;
      z-index: 9998;
      background: rgba(10,9,8,0.92);
      backdrop-filter: blur(14px) saturate(140%);
      -webkit-backdrop-filter: blur(14px) saturate(140%);
      padding: 12px 24px;
      display: flex; gap: 10px; align-items: center; justify-content: center;
      flex-wrap: wrap;
      font-family: 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
      border-bottom: 1px solid rgba(255,179,71,0.22);
      opacity: 0; transform: translateY(-100%);
      transition: opacity .55s ease, transform .55s ease;
      pointer-events: none;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    .deep-nav.visible { opacity: 1; transform: translateY(0); pointer-events: auto; }
    .deep-nav a {
      display: inline-flex; align-items: center;
      padding: 7px 14px;
      border-radius: 22px;
      background: rgba(255,255,255,0.025);
      border: 1px solid rgba(255,179,71,0.18);
      color: #F5EFE0;
      text-decoration: none;
      font-size: 10.5px;
      font-weight: 600;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      transition: all .25s ease;
      white-space: nowrap;
      line-height: 1;
    }
    .deep-nav a:hover {
      color: #FFB347;
      background: rgba(255,179,71,0.1);
      border-color: rgba(255,179,71,0.55);
      transform: translateY(-1px);
      box-shadow: 0 4px 10px rgba(255,179,71,0.18);
    }
    .deep-nav a.lang {
      margin-left: 6px;
      background: rgba(226,10,23,0.18);
      border-color: rgba(226,10,23,0.5);
      color: #F5EFE0;
      font-weight: 700;
      letter-spacing: 2.2px;
    }
    .deep-nav a.lang:hover {
      background: #E20A17;
      border-color: #E20A17;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(226,10,23,0.4);
    }
    .deep-nav .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #FFB347;
      box-shadow: 0 0 10px #FFB347, 0 0 4px rgba(255,179,71,0.6);
      flex-shrink: 0;
      margin-right: 4px;
      animation: gti-bulb-pulse 4s ease-in-out infinite;
    }
    @keyframes gti-bulb-pulse {
      0%,100% { opacity: 0.85; }
      50% { opacity: 0.45; }
    }
    .gti-section-cta {
      display: block;
      margin: 3em auto 1em;
      max-width: 580px;
      padding: 1.2em 1.8em;
      background: rgba(255,179,71,0.04);
      border: 1px solid rgba(255,179,71,0.28);
      border-radius: 4px;
      color: #FFB347;
      text-decoration: none;
      font-family: 'Inter Tight',sans-serif;
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      text-align: center;
      transition: all .3s cubic-bezier(.34,1.56,.64,1);
      position: relative;
      overflow: hidden;
    }
    .gti-section-cta::before {
      content: ''; position: absolute; left: -100%; top: 0; height: 100%; width: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,179,71,0.12), transparent);
      transition: left .6s;
    }
    .gti-section-cta:hover::before { left: 100%; }
    .gti-section-cta:hover {
      background: rgba(255,179,71,0.1);
      border-color: #FFB347;
      color: #FFD580;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(255,179,71,0.18);
    }
    .gti-section-cta::after {
      content: '  →';
      display: inline-block;
      margin-left: 4px;
      transition: transform .3s;
    }
    .gti-section-cta:hover::after { transform: translateX(6px); }
    .gti-back-top {
      position: fixed;
      bottom: 24px; right: 24px;
      z-index: 9997;
      width: 44px; height: 44px;
      border-radius: 50%;
      background: rgba(10,9,8,0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,179,71,0.3);
      color: #FFB347;
      cursor: pointer;
      opacity: 0; transform: translateY(20px);
      transition: opacity .4s, transform .4s, border-color .25s;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    }
    .gti-back-top.show { opacity: 1; transform: translateY(0); }
    .gti-back-top:hover { border-color: #FFB347; color: #FFD580; }
    @media (max-width: 900px) {
      .deep-nav { padding: 10px 12px; gap: 6px; }
      .deep-nav a { padding: 6px 10px; font-size: 9.5px; letter-spacing: 1.4px; }
      .deep-nav a.lang { margin-left: 2px; }
    }
    @media (max-width: 720px) {
      .gti-back-top { bottom: 16px; right: 16px; width: 38px; height: 38px; }
    }
    @media (max-width: 480px) {
      .deep-nav { padding: 8px; gap: 5px; }
      .deep-nav a { padding: 5px 8px; font-size: 9px; letter-spacing: 1px; border-radius: 16px; }
      .deep-nav .dot { display: none; }
    }
  </style>
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
