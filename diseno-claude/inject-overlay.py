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
    /* === Silueta sol naciente — visible solo en el hero (fixed con fade por scroll) === */
    'html body .gti-hero-bg {{',
    '  position: fixed !important;',
    '  top: 0 !important; left: 0 !important;',
    '  width: 100% !important; height: 100vh !important;',
    '  z-index: 1 !important;',
    '  pointer-events: none !important;',
    '  opacity: 0.42 !important;',
    '  background-color: #FFB347 !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/swift-rising-sun.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/swift-rising-sun.svg") !important;',
    '  -webkit-mask-size: 56% auto !important;',
    '  mask-size: 56% auto !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: right 4% center !important;',
    '  mask-position: right 4% center !important;',
    '  transition: opacity .4s ease !important;',
    '}}',
    'html body .gti-hero-bg.hidden {{ opacity: 0 !important; }}',
    '@media (max-width: 720px) {{',
    '  html body .gti-hero-bg {{ -webkit-mask-position: center center !important; mask-position: center center !important; -webkit-mask-size: 92% auto !important; mask-size: 92% auto !important; opacity: 0.32 !important; }}',
    '}}',
    /* === 4 logos Suzuki "S" antiguo - pequeños, rojos GTi, con flotacion === */
    'html body .gti-s-logo {{',
    '  position: fixed !important;',
    '  z-index: 1 !important;',
    '  pointer-events: none !important;',
    '  width: 22px !important; height: 22px !important;',
    '  background-color: #E20A17 !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/suzuki-s-logo.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/suzuki-s-logo.svg") !important;',
    '  -webkit-mask-size: contain !important;',
    '  mask-size: contain !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: center !important;',
    '  mask-position: center !important;',
    '  opacity: 0.65 !important;',
    '  transition: opacity .4s ease !important;',
    '  filter: drop-shadow(0 0 6px rgba(226,10,23,0.35)) !important;',
    '}}',
    'html body .gti-s-logo.hidden {{ opacity: 0 !important; }}',
    /* 4 posiciones repartidas como los marcadores blancos del bundle */
    'html body .gti-s-logo.pos-1 {{ top: 18% !important; left: 28% !important; animation: gti-s-float-a 6s ease-in-out infinite !important; }}',
    'html body .gti-s-logo.pos-2 {{ top: 12% !important; left: 56% !important; animation: gti-s-float-b 7s ease-in-out infinite -1.5s !important; }}',
    'html body .gti-s-logo.pos-3 {{ top: 34% !important; left: 12% !important; animation: gti-s-float-a 8s ease-in-out infinite -3s !important; }}',
    'html body .gti-s-logo.pos-4 {{ top: 22% !important; left: 72% !important; animation: gti-s-float-b 5.5s ease-in-out infinite -2s !important; }}',
    '@keyframes gti-s-float-a {{',
    '  0%, 100% {{ transform: translateY(0) rotate(-4deg); }}',
    '  50% {{ transform: translateY(-7px) rotate(3deg); }}',
    '}}',
    '@keyframes gti-s-float-b {{',
    '  0%, 100% {{ transform: translateY(0) rotate(5deg); }}',
    '  50% {{ transform: translateY(6px) rotate(-4deg); }}',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-s-logo {{ width: 16px !important; height: 16px !important; opacity: 0.55 !important; }}',
    '  html body .gti-s-logo.pos-3 {{ display: none !important; }}',
    '}}',
    /* === Ilustracion swift-front-half en seccion archivo (zona crema) === */
    'html body .gti-archivo-illust {{',
    '  position: absolute !important;',
    '  top: -475px !important; left: 3% !important;',
    '  width: 425px !important; height: 425px !important;',
    '  z-index: 2 !important;',
    '  pointer-events: none !important;',
    '  background-color: #2C1810 !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/swift-front-half.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/swift-front-half.svg") !important;',
    '  -webkit-mask-size: contain !important;',
    '  mask-size: contain !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: center !important;',
    '  mask-position: center !important;',
    '  opacity: 0.68 !important;',
    '  transform: scaleX(-1) rotate(2deg) !important;',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-archivo-illust {{ width: 250px !important; height: 250px !important; top: -325px !important; left: 50% !important; transform: translateX(-50%) scaleX(-1) rotate(2deg) !important; opacity: 0.55 !important; }}',
    '}}',
    /* === Ilustracion swift-rear-detail en seccion colab (zona oscura, derecha) === */
    'html body .gti-colab-illust {{',
    '  position: absolute !important;',
    '  top: calc(18% + 570px) !important; right: -3% !important;',
    '  width: 425px !important; height: 425px !important;',
    '  z-index: 2 !important;',
    '  pointer-events: none !important;',
    '  background-color: #F5EFE0 !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/swift-rear-detail.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/swift-rear-detail.svg") !important;',
    '  -webkit-mask-size: contain !important;',
    '  mask-size: contain !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: center !important;',
    '  mask-position: center !important;',
    '  opacity: 0.42 !important;',
    '  transform: scaleX(-1) rotate(2deg) !important;',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-colab-illust {{ width: 250px !important; height: 250px !important; top: auto !important; bottom: 8% !important; right: 50% !important; transform: translateX(50%) scaleX(-1) rotate(2deg) !important; opacity: 0.32 !important; }}',
    '}}',
    /* === Reemplazo del contenido del element del S brand (inyectado por JS) === */
    'html body .gti-brand-s-fill {{',
    '  display: block !important;',
    '  position: absolute !important;',
    '  top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;',
    '  width: 100% !important; height: 100% !important;',
    '  background-color: #FFFFFF !important;',
    '  -webkit-mask-image: url("/assets/img/siluetas/suzuki-s-logo.svg") !important;',
    '  mask-image: url("/assets/img/siluetas/suzuki-s-logo.svg") !important;',
    '  -webkit-mask-size: 88% auto !important;',
    '  mask-size: 88% auto !important;',
    '  -webkit-mask-repeat: no-repeat !important;',
    '  mask-repeat: no-repeat !important;',
    '  -webkit-mask-position: center !important;',
    '  mask-position: center !important;',
    '  pointer-events: none !important;',
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
  var sLogosHTML = '<div class="gti-s-logo pos-1" aria-hidden="true"></div>' +
                   '<div class="gti-s-logo pos-2" aria-hidden="true"></div>' +
                   '<div class="gti-s-logo pos-3" aria-hidden="true"></div>' +
                   '<div class="gti-s-logo pos-4" aria-hidden="true"></div>';
  var brandOverrideHTML = '<div class="gti-brand-s-override" id="gtiBrandSOverride" aria-hidden="true"></div>';

  function attachListeners() {{
    var nav = document.getElementById('deepNav');
    var bar = document.getElementById('gtiProgress');
    var back = document.getElementById('gtiBackTop');

    var heroBg = document.getElementById('gtiHeroBg');
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
      if (heroBg) {{
        /* fade out al pasar 80% del primer viewport */
        var hide = scrolled > window.innerHeight * 0.8;
        heroBg.classList.toggle('hidden', hide);
        document.querySelectorAll('.gti-s-logo').forEach(function(el) {{ el.classList.toggle('hidden', hide); }});
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

  function injectHeroBg() {{
    if (document.getElementById('gtiHeroBg')) return true;
    if (!document.body) return false;
    /* position: absolute relativo al body. Cubre solo primer viewport (100vh). */
    document.body.insertAdjacentHTML('afterbegin', heroBgHTML);
    return true;
  }}

  function injectSLogos() {{
    if (document.querySelector('.gti-s-logo')) return true;
    if (!document.body) return false;
    document.body.insertAdjacentHTML('afterbegin', sLogosHTML);
    return true;
  }}

  /* Busca el elemento real del bundle que contiene la "S" cursiva del brand box.
     Heuristica: hoja DOM cuyo textContent EXACTO es "S", ubicada en cuadrante top-left,
     con un fondo rojo (parent inmediato o ancestro cercano). Reemplaza su contenido
     con el logo Suzuki antiguo en blanco via mask-image. */
  function replaceBrandS() {{
    if (document.querySelector('[data-gti-brand-replaced]')) return true;
    if (!document.body) return false;
    var candidates = document.body.querySelectorAll('*');
    for (var i = 0; i < candidates.length; i++) {{
      var el = candidates[i];
      if (el.children.length > 0) continue;
      var text = (el.textContent || '').trim();
      if (text !== 'S') continue;
      var rect = el.getBoundingClientRect();
      if (rect.top > 350 || rect.left > 500) continue;
      if (rect.width < 14 || rect.width > 250) continue;
      /* verificar que un ancestro tenga fondo rojo (brand box) */
      var hasRedAncestor = false;
      var p = el;
      for (var depth = 0; depth < 6 && p; depth++) {{
        var bg = window.getComputedStyle(p).backgroundColor;
        var m = bg.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/);
        if (m) {{
          var r = +m[1], g = +m[2], b = +m[3];
          if (r > 150 && g < 80 && b < 80) {{ hasRedAncestor = true; break; }}
        }}
        p = p.parentElement;
      }}
      if (!hasRedAncestor) continue;
      /* MATCH — reemplazar contenido */
      el.textContent = '';
      var cs = window.getComputedStyle(el);
      if (cs.position === 'static') el.style.position = 'relative';
      var fill = document.createElement('span');
      fill.className = 'gti-brand-s-fill';
      fill.setAttribute('aria-hidden', 'true');
      el.appendChild(fill);
      el.setAttribute('data-gti-brand-replaced', 'true');
      return true;
    }}
    return false;
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
    // 4b. Logos Suzuki "S" antiguos (4 instancias en el hero)
    injectSLogos();
    // 4c. Reemplazo del S cursivo del brand box (busqueda DOM real)
    replaceBrandS();
    // 4d. Ilustracion swift-front-half en seccion archivo
    var arch = document.getElementById('archivo');
    if (arch && !arch.querySelector('.gti-archivo-illust')) {{
      var cs = window.getComputedStyle(arch);
      if (cs.position === 'static') arch.style.position = 'relative';
      arch.insertAdjacentHTML('afterbegin', '<div class="gti-archivo-illust" aria-hidden="true"></div>');
    }}
    // 4e. Ilustracion swift-rear-detail en seccion colab
    var colab = document.getElementById('colab');
    if (colab && !colab.querySelector('.gti-colab-illust')) {{
      var ccs = window.getComputedStyle(colab);
      if (ccs.position === 'static') colab.style.position = 'relative';
      if (ccs.overflow === 'visible') colab.style.overflow = 'hidden';
      colab.insertAdjacentHTML('afterbegin', '<div class="gti-colab-illust" aria-hidden="true"></div>');
    }}
    // 4z. TEMP — log heights de todas las secciones a console
    if (!window.__gtiHeightsLogged) {{
      window.__gtiHeightsLogged = true;
      setTimeout(function() {{
        var rows = [];
        document.querySelectorAll('section').forEach(function(s, i) {{
          rows.push((i+1) + ' | id=' + (s.id || '(sin id)').padEnd(12) + ' | alt=' + s.offsetHeight + 'px | top=' + Math.round(s.getBoundingClientRect().top + window.scrollY) + 'px');
        }});
        console.log('%c[GTi Sections]', 'background:#E20A17;color:white;padding:2px 6px;font-weight:bold;border-radius:3px;', '\\n' + rows.join('\\n'));
      }}, 1500);
    }}
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
