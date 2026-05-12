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
<style>
  /* Scroll progress bar */
  .gti-progress {{
    position: fixed; top: 0; left: 0;
    height: 2px; width: 0%;
    background: linear-gradient(90deg, #E20A17 0%, #FFB347 100%);
    z-index: 10000;
    transition: width .15s ease-out;
    pointer-events: none;
    box-shadow: 0 0 8px rgba(255,179,71,0.6);
  }}

  /* Floating deep-nav */
  .deep-nav {{
    position: fixed; top: 0; left: 0; right: 0;
    z-index: 9998;
    background: rgba(10,9,8,0.88);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 10px 24px;
    display: flex; gap: 18px; align-items: center; justify-content: center;
    flex-wrap: wrap;
    font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 10.5px; font-weight: 500; letter-spacing: 2.2px; text-transform: uppercase;
    border-bottom: 1px solid rgba(255,179,71,0.18);
    opacity: 0; transform: translateY(-100%);
    transition: opacity .55s ease, transform .55s ease;
    pointer-events: none;
  }}
  .deep-nav.visible {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
  .deep-nav a {{ color: #F5EFE0; text-decoration: none; opacity: 0.72; transition: opacity .2s, color .2s; padding: 4px 2px; }}
  .deep-nav a:hover {{ color: #FFB347; opacity: 1; }}
  .deep-nav a.lang {{ margin-left: 14px; border-left: 1px solid rgba(255,179,71,0.22); padding-left: 16px; color: #FFB347; font-weight: 600; }}
  .deep-nav .dot {{ width: 4px; height: 4px; border-radius: 50%; background: #FFB347; opacity: 0.6; box-shadow: 0 0 8px #FFB347; }}
  @media (max-width: 720px) {{
    .deep-nav {{ font-size: 9px; gap: 10px; padding: 8px 12px; letter-spacing: 1.4px; }}
    .deep-nav a.lang {{ margin-left: 4px; padding-left: 8px; }}
  }}

  /* Section deep-link CTAs */
  .gti-section-cta {{
    display: block;
    margin: 3em auto 1em;
    max-width: 580px;
    padding: 1.2em 1.8em;
    background: rgba(255,179,71,0.04);
    border: 1px solid rgba(255,179,71,0.28);
    border-radius: 4px;
    color: #FFB347;
    text-decoration: none;
    font-family: 'Inter Tight', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    text-align: center;
    transition: all .3s cubic-bezier(.34,1.56,.64,1);
    position: relative;
    overflow: hidden;
  }}
  .gti-section-cta::before {{
    content: ''; position: absolute; left: -100%; top: 0; height: 100%; width: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,179,71,0.12), transparent);
    transition: left .6s;
  }}
  .gti-section-cta:hover::before {{ left: 100%; }}
  .gti-section-cta:hover {{
    background: rgba(255,179,71,0.1);
    border-color: #FFB347;
    color: #FFD580;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(255,179,71,0.18);
  }}
  .gti-section-cta::after {{
    content: '  →';
    display: inline-block;
    margin-left: 4px;
    transition: transform .3s;
  }}
  .gti-section-cta:hover::after {{ transform: translateX(6px); }}

  /* Back-to-top floating button */
  .gti-back-top {{
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
  }}
  .gti-back-top.show {{ opacity: 1; transform: translateY(0); }}
  .gti-back-top:hover {{ border-color: #FFB347; color: #FFD580; }}
  @media (max-width: 720px) {{
    .gti-back-top {{ bottom: 16px; right: 16px; width: 38px; height: 38px; }}
  }}
</style>

<script>
(function() {{
  if (window.__gtiOverlayInit) return;
  window.__gtiOverlayInit = true;

  var CTAS = {ctas_js};
  var BACK_LABEL = "{back_to_top}";

  var navHTML = '<div id="deepNav" class="deep-nav">' +
    '<span class="dot"></span>' +
    '{nav_links_html}' +
    '<a href="{lang_href}" class="lang">{lang_label}</a>' +
    '</div>';

  var progressHTML = '<div class="gti-progress" id="gtiProgress"></div>';
  var backTopHTML = '<button class="gti-back-top" id="gtiBackTop" aria-label="' + BACK_LABEL + '">↑</button>';

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
    // 4. Section CTAs
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
