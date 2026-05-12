"""Inyección completa de overlay sobre el bundle de Claude Design.

Incluye:
  1. Deep-nav flotante superior (sticky top, aparece tras scroll 240px)
  2. CTAs hot-link al final de cada sección [4-8] del bundle
     que llevan al usuario a las páginas MkDocs profundas
  3. Scroll-progress bar superior (1px ámbar)
  4. Listener "Volver al inicio" en click del logo

El bundle reemplaza document.body al unpack, por eso usamos
MutationObserver sobre documentElement.

Idempotente: detecta si ya se inyectó y no duplica.
"""
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
TARGETS = [
    Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.html"),
    Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.en.html"),
]

# Per-target locale-specific strings
LOCALES = {
    "es": {
        "nav_items": [
            ("Historia",       "/historia/"),
            ("Manuales",       "/manuales/"),
            ("Reparaciones",   "/reparaciones/"),
            ("Modificaciones", "/modificaciones/"),
            ("Repuestos",      "/repuestos/"),
            ("Garage",         "/garage/"),
            ("Comunidad",      "/comunidad/"),
            ("Blog",           "/blog/"),
            ("Contacto",       "/contacto/"),
        ],
        "lang_switch": ("EN", "/en/"),
        "back_to_top": "Volver al inicio",
        # CTAs por seccion del bundle
        "ctas": {
            "archivo": ("Explorar archivo completo", "/manuales/"),
            "motor":   ("Especificaciones técnicas G13B completas", "/reparaciones/motor-g13b/"),
            "garage":  ("Ver garage completo del club", "/garage/"),
            "comunidad": ("Unirse a la comunidad", "/comunidad/"),
            "colab":   ("Conocer el archivo técnico", "/manuales/"),
        },
    },
    "en": {
        "nav_items": [
            ("History",       "/en/historia/"),
            ("Manuals",       "/en/manuales/"),
            ("Repairs",       "/en/reparaciones/"),
            ("Modifications", "/en/modificaciones/"),
            ("Parts",         "/en/repuestos/"),
            ("Garage",        "/en/garage/"),
            ("Community",     "/en/comunidad/"),
            ("Blog",          "/en/blog/"),
            ("Contact",       "/en/contacto/"),
        ],
        "lang_switch": ("ES", "/"),
        "back_to_top": "Back to top",
        "ctas": {
            "archivo": ("Explore the full archive", "/en/manuales/"),
            "motor":   ("Full G13B technical specifications", "/en/reparaciones/motor-g13b/"),
            "garage":  ("See the full club garage", "/en/garage/"),
            "comunidad": ("Join the community", "/en/comunidad/"),
            "colab":   ("Discover the technical archive", "/en/manuales/"),
        },
    },
}

INJECT_MARKER = "<!-- gti-overlay-injected -->"


def build_injection(locale):
    L = LOCALES[locale]
    nav_links_html = "".join(
        f'<a href="{href}">{label}</a>'
        for label, href in L["nav_items"]
    )
    lang_label, lang_href = L["lang_switch"]
    ctas_js = "{" + ",".join(
        f'"{key}":{{label:"{label}",href:"{href}"}}'
        for key, (label, href) in L["ctas"].items()
    ) + "}"
    back_to_top = L["back_to_top"]

    return f"""
{INJECT_MARKER}
<!-- Styles inyectados via JS porque el bundle hace document.documentElement.replaceWith() y borra el head original -->
<script>
(function() {{
  if (window.__gtiOverlayInit) return;
  window.__gtiOverlayInit = true;

  /* CSS as plain string (no template literal) — funciona en cualquier navegador */
  var OVERLAY_CSS_TEXT = [
    'html body div.deep-nav {{',
    '  position: fixed !important;',
    '  top: 0 !important; left: 0 !important; right: 0 !important;',
    '  z-index: 9998 !important;',
    '  background: rgba(10,9,8,0.92) !important;',
    '  backdrop-filter: blur(14px) saturate(140%) !important;',
    '  -webkit-backdrop-filter: blur(14px) saturate(140%) !important;',
    '  padding: 12px 24px !important;',
    '  display: flex !important; gap: 10px !important;',
    '  align-items: center !important; justify-content: center !important;',
    '  flex-wrap: wrap !important;',
    "  font-family: 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,sans-serif !important;",
    '  border-bottom: 1px solid rgba(255,179,71,0.22) !important;',
    '  opacity: 0; transform: translateY(-100%);',
    '  transition: opacity .55s ease, transform .55s ease !important;',
    '  pointer-events: none;',
    '  box-shadow: 0 4px 20px rgba(0,0,0,0.4) !important;',
    '  margin: 0 !important;',
    '}}',
    'html body div.deep-nav.visible {{ opacity: 1 !important; transform: translateY(0) !important; pointer-events: auto !important; }}',
    'html body div.deep-nav a {{',
    '  display: inline-flex !important; align-items: center !important;',
    '  padding: 7px 14px !important;',
    '  border-radius: 22px !important;',
    '  background: rgba(255,255,255,0.025) !important;',
    '  border: 1px solid rgba(255,179,71,0.18) !important;',
    '  color: #F5EFE0 !important;',
    '  text-decoration: none !important;',
    '  font-size: 10.5px !important; font-weight: 600 !important;',
    '  letter-spacing: 1.8px !important; text-transform: uppercase !important;',
    '  transition: all .25s ease !important;',
    '  white-space: nowrap !important; line-height: 1 !important;',
    "  font-family: 'Inter Tight','Inter',-apple-system,sans-serif !important;",
    '  margin: 0 !important;',
    '}}',
    'html body div.deep-nav a:hover {{',
    '  color: #FFB347 !important;',
    '  background: rgba(255,179,71,0.1) !important;',
    '  border-color: rgba(255,179,71,0.55) !important;',
    '  transform: translateY(-1px) !important;',
    '  box-shadow: 0 4px 10px rgba(255,179,71,0.18) !important;',
    '}}',
    'html body div.deep-nav a.lang {{',
    '  margin-left: 6px !important;',
    '  background: rgba(226,10,23,0.18) !important;',
    '  border-color: rgba(226,10,23,0.5) !important;',
    '  color: #F5EFE0 !important; font-weight: 700 !important;',
    '  letter-spacing: 2.2px !important;',
    '}}',
    'html body div.deep-nav a.lang:hover {{',
    '  background: #E20A17 !important; border-color: #E20A17 !important;',
    '  color: #FFFFFF !important;',
    '  box-shadow: 0 4px 12px rgba(226,10,23,0.4) !important;',
    '}}',
    'html body div.deep-nav .dot {{',
    '  width: 8px !important; height: 8px !important;',
    '  border-radius: 50% !important;',
    '  background: #FFB347 !important;',
    '  box-shadow: 0 0 10px #FFB347, 0 0 4px rgba(255,179,71,0.6) !important;',
    '  flex-shrink: 0 !important; margin-right: 4px !important;',
    '  animation: gti-bulb-pulse 4s ease-in-out infinite !important;',
    '}}',
    '@keyframes gti-bulb-pulse {{ 0%,100% {{ opacity: 0.85; }} 50% {{ opacity: 0.45; }} }}',
    'html body .gti-progress {{',
    '  position: fixed !important; top: 0 !important; left: 0 !important;',
    '  height: 2px !important; width: 0%;',
    '  background: linear-gradient(90deg, #E20A17 0%, #FFB347 100%) !important;',
    '  z-index: 10000 !important; pointer-events: none !important;',
    '  transition: width .15s ease-out !important;',
    '  box-shadow: 0 0 8px rgba(255,179,71,0.6) !important;',
    '}}',
    'html body .gti-back-top {{',
    '  position: fixed !important; bottom: 24px !important; right: 24px !important;',
    '  z-index: 9997 !important;',
    '  width: 44px !important; height: 44px !important;',
    '  border-radius: 50% !important;',
    '  background: rgba(10,9,8,0.85) !important;',
    '  backdrop-filter: blur(8px) !important;',
    '  border: 1px solid rgba(255,179,71,0.3) !important;',
    '  color: #FFB347 !important; cursor: pointer !important;',
    '  opacity: 0; transform: translateY(20px);',
    '  transition: opacity .4s, transform .4s, border-color .25s !important;',
    '  display: flex !important; align-items: center !important; justify-content: center !important;',
    '  font-size: 18px !important; box-shadow: 0 6px 20px rgba(0,0,0,0.5) !important;',
    '}}',
    'html body .gti-back-top.show {{ opacity: 1 !important; transform: translateY(0) !important; }}',
    '@media (max-width: 900px) {{',
    '  html body div.deep-nav {{ padding: 10px 12px !important; gap: 6px !important; }}',
    '  html body div.deep-nav a {{ padding: 6px 10px !important; font-size: 9.5px !important; letter-spacing: 1.4px !important; }}',
    '  html body div.deep-nav a.lang {{ margin-left: 2px !important; }}',
    '}}',
    '@media (max-width: 480px) {{',
    '  html body div.deep-nav {{ padding: 8px !important; gap: 5px !important; }}',
    '  html body div.deep-nav a {{ padding: 5px 8px !important; font-size: 9px !important; letter-spacing: 1px !important; border-radius: 16px !important; }}',
    '  html body div.deep-nav .dot {{ display: none !important; }}',
    '}}',
    /* === SECTION CTAs (.gti-section-cta) — bordes de seccion en bundle === */
    'html body a.gti-section-cta {{',
    '  display: block !important;',
    '  margin: 3em auto 2em !important;',
    '  max-width: 580px !important;',
    '  padding: 1.4em 2em !important;',
    '  background: rgba(255,179,71,0.04) !important;',
    '  border: 1px solid rgba(255,179,71,0.35) !important;',
    '  border-radius: 4px !important;',
    '  color: #FFB347 !important;',
    '  text-decoration: none !important;',
    "  font-family: 'Inter Tight',sans-serif !important;",
    '  font-size: 0.78rem !important;',
    '  font-weight: 600 !important;',
    '  letter-spacing: 2.5px !important;',
    '  text-transform: uppercase !important;',
    '  text-align: center !important;',
    '  transition: all .3s cubic-bezier(.34,1.56,.64,1) !important;',
    '  position: relative !important;',
    '  overflow: hidden !important;',
    '  cursor: pointer !important;',
    '}}',
    'html body a.gti-section-cta::before {{',
    '  content: \"\" !important;',
    '  position: absolute !important;',
    '  left: -100% !important; top: 0 !important;',
    '  height: 100% !important; width: 100% !important;',
    '  background: linear-gradient(90deg, transparent, rgba(255,179,71,0.14), transparent) !important;',
    '  transition: left .6s !important;',
    '  pointer-events: none !important;',
    '}}',
    'html body a.gti-section-cta:hover::before {{ left: 100% !important; }}',
    'html body a.gti-section-cta:hover {{',
    '  background: rgba(255,179,71,0.12) !important;',
    '  border-color: #FFB347 !important;',
    '  color: #FFD580 !important;',
    '  transform: translateY(-2px) !important;',
    '  box-shadow: 0 8px 24px rgba(255,179,71,0.22) !important;',
    '}}',
    'html body a.gti-section-cta::after {{',
    '  content: \" \\u2192\" !important;',
    '  display: inline-block !important;',
    '  margin-left: 6px !important;',
    '  transition: transform .3s !important;',
    '}}',
    'html body a.gti-section-cta:hover::after {{ transform: translateX(8px) !important; }}',
    /* === Silueta sol naciente — SOLO en el header/hero, contenida === */
    /* mask-image en vez de background-image: permite teñir el SVG via background-color */
    'html body .gti-hero-bg {{',
    '  position: absolute !important;',
    '  top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;',
    '  width: 100% !important; height: 100% !important;',
    '  z-index: 0 !important;',
    '  pointer-events: none !important;',
    '  opacity: 0.32 !important;',
    '  background-color: #FFB347 !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/swift-rising-sun.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/swift-rising-sun.svg") !important;',
    '  -webkit-mask-size: contain !important;',
    '  mask-size: contain !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: right center !important;',
    '  mask-position: right center !important;',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-hero-bg {{ -webkit-mask-position: center center !important; mask-position: center center !important; -webkit-mask-size: 140% !important; mask-size: 140% !important; opacity: 0.24 !important; }}',
    '}}'
  ].join('\\n');

  /* Inyecta los estilos en el <head> ACTUAL (re-llamable cada vez que documentElement cambia) */
  function ensureStyles() {{
    if (!document.head) return false;
    if (document.head.querySelector('#gti-overlay-styles')) return true;
    var styleEl = document.createElement('style');
    styleEl.id = 'gti-overlay-styles';
    styleEl.appendChild(document.createTextNode(OVERLAY_CSS_TEXT));
    document.head.appendChild(styleEl);
    return true;
  }}

  /* Llama inmediatamente y registra observer para re-aplicar tras replaceWith */
  ensureStyles();
  var headObs = new MutationObserver(function() {{
    /* Si el bundle reemplaza documentElement, head es nuevo. Re-inyectar. */
    ensureStyles();
  }});
  headObs.observe(document, {{ childList: true, subtree: true }});

  var CTAS = {ctas_js};
  var BACK_LABEL = "{back_to_top}";

  var navHTML = '<div id="deepNav" class="deep-nav">' +
    '<span class="dot"></span>' +
    '{nav_links_html}' +
    '<a href="{lang_href}" class="lang">{lang_label}</a>' +
    '</div>';

  var progressHTML = '<div class="gti-progress" id="gtiProgress"></div>';
  var backTopHTML = '<button class="gti-back-top" id="gtiBackTop" aria-label="' + BACK_LABEL + '">↑</button>';
  var heroBgHTML = '<div class="gti-hero-bg" id="gtiHeroBg" aria-hidden="true"></div>';

  function attachListeners() {{
    var nav = document.getElementById('deepNav');
    var bar = document.getElementById('gtiProgress');
    var back = document.getElementById('gtiBackTop');

    function onScroll() {{
      var doc = document.documentElement;
      var scrolled = doc.scrollTop || document.body.scrollTop;
      var height = (doc.scrollHeight - doc.clientHeight) || 1;
      var pct = (scrolled / height) * 100;
      if (bar) bar.style.width = pct + '%';
      if (nav) {{
        if (scrolled > 240) nav.classList.add('visible'); else nav.classList.remove('visible');
      }}
      if (back) {{
        if (scrolled > 600) back.classList.add('show'); else back.classList.remove('show');
      }}
    }}
    window.addEventListener('scroll', onScroll, {{ passive: true }});
    onScroll();

    if (back) {{
      back.addEventListener('click', function() {{
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }}
  }}

  function injectSectionCTA(sectionId, label, href) {{
    var sec = document.getElementById(sectionId);
    if (!sec) return false;
    if (sec.querySelector('.gti-section-cta')) return true; // already injected
    var a = document.createElement('a');
    a.className = 'gti-section-cta';
    a.href = href;
    a.textContent = label;
    sec.appendChild(a);
    return true;
  }}

  /* Detecta el contenedor del header/hero del bundle.
     Estrategia: <header>, primer <section> que no sea uno con id conocido (motor/garage/...),
     o el primer hijo del main/body antes de la primera section identificada. */
  function findHeroContainer() {{
    var h = document.querySelector('header');
    if (h && h.offsetHeight > 100) return h;
    var allSections = Array.from(document.querySelectorAll('section'));
    var identifiedIds = ['archivo','motor','garage','comunidad','colab','blog'];
    var first = allSections.find(function(s) {{ return !identifiedIds.includes(s.id); }});
    if (first) return first;
    return allSections[0] || null;
  }}

  function injectHeroBg() {{
    var hero = findHeroContainer();
    if (!hero) return false;
    if (hero.querySelector('#gtiHeroBg')) return true;
    var cs = window.getComputedStyle(hero);
    if (cs.position === 'static') hero.style.position = 'relative';
    if (cs.overflow === 'visible') hero.style.overflow = 'hidden';
    hero.insertAdjacentHTML('afterbegin', heroBgHTML);
    return true;
  }}

  function ensure() {{
    if (!document.body) return false;
    var hasContent = document.querySelector('[id="archivo"], [id="motor"], [id="garage"], section');
    if (!hasContent) return false;

    // 1. Progress bar
    if (!document.getElementById('gtiProgress')) {{
      document.body.insertAdjacentHTML('afterbegin', progressHTML);
    }}
    // 2. Deep-nav
    if (!document.getElementById('deepNav')) {{
      document.body.insertAdjacentHTML('afterbegin', navHTML);
    }}
    // 3. Back-to-top button
    if (!document.getElementById('gtiBackTop')) {{
      document.body.insertAdjacentHTML('beforeend', backTopHTML);
    }}
    // 4. Hero background (sol naciente — SOLO dentro del header/hero, no fixed)
    injectHeroBg();
    // 5. Section CTAs
    Object.keys(CTAS).forEach(function(k) {{
      injectSectionCTA(k, CTAS[k].label, CTAS[k].href);
    }});

    attachListeners();
    return true;
  }}

  // Observe DOM changes (bundle replaces body)
  var obs = new MutationObserver(function() {{ ensure(); }});
  obs.observe(document.documentElement, {{ childList: true, subtree: true }});

  // Polling fallback
  var tries = 0;
  var iv = setInterval(function() {{
    tries++;
    if (ensure() || tries > 100) clearInterval(iv);
  }}, 200);

  // PWA Service Worker registration (offline-first support)
  if ('serviceWorker' in navigator) {{
    window.addEventListener('load', function() {{
      navigator.serviceWorker.register('/sw.js', {{ scope: '/' }})
        .catch(function(err) {{ console.warn('[GTi] SW registration:', err); }});
    }});
  }}
}})();
</script>
"""


def inject(target_path, locale):
    html = target_path.read_text(encoding='utf-8')
    if INJECT_MARKER in html:
        # Remove old injection (idempotent)
        # Find the marker and remove from there until just before </body>
        idx = html.find(INJECT_MARKER)
        end = html.rfind('</body>')
        # Remove everything between marker and </body>
        html = html[:idx] + html[end:]
        print(f"  Removed previous overlay in {target_path.name}")

    # Also strip any old deep-nav-only injection (from F1)
    # Old marker pattern was <style>\n    .deep-nav { (without our INJECT_MARKER)
    if '<style>\n    .deep-nav {' in html and INJECT_MARKER not in html:
        # Strip from <style> up to </script> right before </body>
        old_start = html.find('<style>\n    .deep-nav {')
        # Find next </script>\n</body> after old_start
        end_marker = html.find('</body>', old_start)
        # The injection ended with </script>\n</body> structure
        # We need to remove the lines from old_start to just before </body>
        # Find the last </script> before </body>
        scripts_end = html.rfind('</script>', old_start, end_marker)
        if scripts_end != -1 and old_start < scripts_end:
            html = html[:old_start] + html[scripts_end + len('</script>'):]
            print(f"  Removed legacy F1 deep-nav injection in {target_path.name}")

    injection = build_injection(locale)
    new = html.replace('</body>', injection + '\n</body>', 1)
    target_path.write_text(new, encoding='utf-8')
    print(f"  Injected overlay ({len(injection)} bytes) into {target_path.name}")


for target in TARGETS:
    locale = 'en' if '.en.' in target.name else 'es'
    print(f"=== {target.name} ({locale}) ===")
    inject(target, locale)
print("Done.")
