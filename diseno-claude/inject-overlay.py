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
    /* === SILUETAS DEL GTi — arte real Swift GTi MK3 1989-1994 === */
    /* Watermark hero: sol naciente JDM + 3/4 del GTi */
    'html body .gti-watermark-hero {{',
    '  position: fixed !important;',
    '  top: 50% !important; right: -6% !important;',
    '  transform: translateY(-50%) !important;',
    '  width: 80vmin !important; height: 80vmin !important;',
    '  max-width: 880px !important; max-height: 880px !important;',
    '  pointer-events: none !important;',
    '  z-index: 1 !important;',
    '  opacity: 0.28 !important;',
    '  background-image: url("/assets/img/siluetas/swift-rising-sun.webp") !important;',
    '  background-size: contain !important;',
    '  background-repeat: no-repeat !important;',
    '  background-position: center !important;',
    '  transition: opacity 1.4s ease !important;',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-watermark-hero {{ right: -28% !important; top: 38% !important; width: 130vmin !important; height: 130vmin !important; opacity: 0.22 !important; }}',
    '}}',
    /* Dividers — silueta lateral filled blanco con mix-blend para adaptar a bg */
    'html body .gti-divider {{',
    '  display: flex !important; align-items: center !important; justify-content: center !important;',
    '  gap: 22px !important;',
    '  margin: 4.5em auto 3.5em !important;',
    '  max-width: 760px !important;',
    '  padding: 0 24px !important;',
    '  pointer-events: none !important;',
    '  position: relative !important;',
    '  z-index: 5 !important;',
    '}}',
    'html body .gti-divider::before, html body .gti-divider::after {{',
    '  content: "" !important;',
    '  flex: 1 !important;',
    '  height: 1px !important;',
    '  background: linear-gradient(90deg, transparent, rgba(226,10,23,0.5), transparent) !important;',
    '}}',
    'html body .gti-divider img {{',
    '  width: 150px !important; height: auto !important;',
    '  opacity: 0.85 !important;',
    '  flex-shrink: 0 !important;',
    '  mix-blend-mode: difference !important;',
    '  filter: drop-shadow(0 1px 4px rgba(0,0,0,0.25)) !important;',
    '}}',
    /* Footer mark — silueta trasera real "alejándose" */
    'html body .gti-footer-mark {{',
    '  display: flex !important; flex-direction: column !important;',
    '  align-items: center !important; gap: 14px !important;',
    '  margin: 5em auto 3em !important;',
    '  padding: 0 24px !important;',
    '  max-width: 320px !important;',
    '  pointer-events: none !important;',
    '  position: relative !important;',
    '  z-index: 5 !important;',
    '  transition: opacity .6s ease !important;',
    '}}',
    'html body .gti-footer-mark img {{',
    '  width: 100% !important; height: auto !important;',
    '  opacity: 0.78 !important;',
    '  mix-blend-mode: multiply !important;',
    '  filter: drop-shadow(0 4px 14px rgba(0,0,0,0.18)) !important;',
    '}}',
    'html body .gti-footer-mark .gti-footer-mark-caption {{',
    "  font-family: 'Inter Tight','Inter',sans-serif !important;",
    '  font-size: 10px !important;',
    '  font-weight: 600 !important;',
    '  letter-spacing: 3.5px !important;',
    '  text-transform: uppercase !important;',
    '  color: rgba(44,24,16,0.7) !important;',
    '}}',
    /* Deep-nav: silueta lateral mini */
    'html body div.deep-nav img.gti-nav-silhouette {{',
    '  width: 36px !important; height: auto !important;',
    '  margin-right: 8px !important;',
    '  flex-shrink: 0 !important;',
    '  opacity: 0.95 !important;',
    '  filter: drop-shadow(0 0 6px rgba(255,179,71,0.55)) !important;',
    '}}',
    '@media (max-width: 480px) {{',
    '  html body div.deep-nav img.gti-nav-silhouette {{ display: none !important; }}',
    '}}',
    /* Section accents — siluetas reales rotadas, blend para integrarse al fondo */
    'html body .gti-section-accent {{',
    '  position: absolute !important;',
    '  pointer-events: none !important;',
    '  z-index: 1 !important;',
    '  opacity: 0.42 !important;',
    '  mix-blend-mode: multiply !important;',
    '  filter: drop-shadow(0 6px 18px rgba(0,0,0,0.12)) !important;',
    '}}',
    'html body .gti-section-accent img {{ width: 100% !important; height: auto !important; display: block !important; }}',
    'html body .gti-section-accent.front-lineart {{ width: 220px !important; right: 5% !important; top: 8% !important; transform: rotate(-4deg) !important; }}',
    'html body .gti-section-accent.split-front-rear {{ width: 280px !important; left: 4% !important; bottom: 8% !important; transform: rotate(3deg) !important; }}',
    'html body .gti-section-accent.front-detail-poster {{ width: 200px !important; right: 6% !important; bottom: 10% !important; transform: rotate(2deg) !important; opacity: 0.55 !important; mix-blend-mode: lighten !important; }}',
    'html body .gti-section-accent.front-half {{ width: 200px !important; left: 5% !important; top: 12% !important; transform: rotate(-3deg) !important; }}',
    '@media (max-width: 900px) {{',
    '  html body .gti-section-accent.front-lineart, html body .gti-section-accent.split-front-rear, html body .gti-section-accent.front-detail-poster, html body .gti-section-accent.front-half {{ width: 130px !important; opacity: 0.3 !important; }}',
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

  /* Silueta lateral filled blanco (arte real Swift GTi MK3) */
  var SIL_SIDE_MINI = '<img class="gti-nav-silhouette" src="/assets/img/siluetas/swift-side-fill.webp" alt="" aria-hidden="true">';

  var navHTML = '<div id="deepNav" class="deep-nav">' +
    SIL_SIDE_MINI +
    '{nav_links_html}' +
    '<a href="{lang_href}" class="lang">{lang_label}</a>' +
    '</div>';

  var progressHTML = '<div class="gti-progress" id="gtiProgress"></div>';
  var backTopHTML = '<button class="gti-back-top" id="gtiBackTop" aria-label="' + BACK_LABEL + '">↑</button>';
  var watermarkHTML = '<div class="gti-watermark-hero" id="gtiWatermarkHero" aria-hidden="true"></div>';

  /* Footer mark con silueta trasera real (rear-detail) + caption */
  var footerMarkHTML = '<div class="gti-footer-mark" aria-hidden="true">' +
    '<img src="/assets/img/siluetas/swift-rear-detail.webp" alt="">' +
    '<span class="gti-footer-mark-caption">Hasta la próxima vuelta</span>' +
    '</div>';

  /* Divider con silueta lateral real (side-fill) */
  var dividerHTML = '<div class="gti-divider" aria-hidden="true">' +
    '<img src="/assets/img/siluetas/swift-side-fill.webp" alt="">' +
    '</div>';

  /* Accent ornamental — arte real Swift GTi por sección */
  /* variant: front-lineart | split-front-rear | front-detail-poster | front-half */
  function makeAccent(variant) {{
    var srcMap = {{
      'front-lineart':        '/assets/img/siluetas/swift-front-lineart.webp',
      'split-front-rear':     '/assets/img/siluetas/Suzukiswiftgti1992.webp',
      'front-detail-poster':  '/assets/img/siluetas/swift-front-detail.webp',
      'front-half':           '/assets/img/siluetas/swift-front-half.webp'
    }};
    var src = srcMap[variant] || srcMap['front-lineart'];
    return '<div class="gti-section-accent ' + variant + '" aria-hidden="true">' +
      '<img src="' + src + '" alt="">' +
      '</div>';
  }}

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

  function injectAccent(sectionId, variant) {{
    var sec = document.getElementById(sectionId);
    if (!sec) return false;
    if (sec.querySelector('.gti-section-accent')) return true;
    var cs = window.getComputedStyle(sec);
    if (cs.position === 'static') sec.style.position = 'relative';
    if (cs.overflow === 'visible') sec.style.overflow = 'hidden';
    sec.insertAdjacentHTML('afterbegin', makeAccent(variant));
    return true;
  }}

  function injectDividerBefore(sectionId) {{
    var sec = document.getElementById(sectionId);
    if (!sec) return false;
    if (sec.previousElementSibling && sec.previousElementSibling.classList && sec.previousElementSibling.classList.contains('gti-divider')) return true;
    sec.insertAdjacentHTML('beforebegin', dividerHTML);
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
    // 4. Hero watermark (sol naciente JDM, opacity ultra-baja)
    if (!document.getElementById('gtiWatermarkHero')) {{
      document.body.insertAdjacentHTML('afterbegin', watermarkHTML);
    }}
    // 5. Section CTAs
    Object.keys(CTAS).forEach(function(k) {{
      injectSectionCTA(k, CTAS[k].label, CTAS[k].href);
    }});
    // 6. Section accents (arte real Swift GTi MK3 por sección)
    injectAccent('motor', 'front-lineart');         // frontal completo en specs/motor
    injectAccent('garage', 'split-front-rear');     // split front+rear en garage
    injectAccent('comunidad', 'front-detail-poster'); // poster "SWIFT 1.3 GTi" en comunidad
    injectAccent('archivo', 'front-half');          // half-front dramatico en archivo
    injectAccent('colab', 'front-half');            // half-front en colab
    // 7. Dividers entre secciones principales
    injectDividerBefore('motor');
    injectDividerBefore('garage');
    injectDividerBefore('comunidad');
    injectDividerBefore('colab');
    // 8. Footer mark (silueta trasera + caption "Hasta la próxima vuelta")
    if (!document.querySelector('.gti-footer-mark')) {{
      var lastSection = document.querySelector('[id="colab"]') || document.querySelector('section:last-of-type');
      if (lastSection && lastSection.parentNode) {{
        lastSection.insertAdjacentHTML('afterend', footerMarkHTML);
      }} else {{
        document.body.insertAdjacentHTML('beforeend', footerMarkHTML);
      }}
    }}

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
