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
    /* === SILUETAS DEL GTi — identidad visual sutil === */
    /* Watermark hero: sol naciente JDM gigante fijo, opacity bajísima */
    'html body .gti-watermark-hero {{',
    '  position: fixed !important;',
    '  top: 50% !important; right: -6% !important;',
    '  transform: translateY(-50%) !important;',
    '  width: 92vmin !important; height: 92vmin !important;',
    '  max-width: 980px !important; max-height: 980px !important;',
    '  pointer-events: none !important;',
    '  z-index: 1 !important;',
    '  opacity: 0.22 !important;',
    '  background-image: url("/assets/img/siluetas/gti-rising-sun.svg") !important;',
    '  background-size: contain !important;',
    '  background-repeat: no-repeat !important;',
    '  background-position: center !important;',
    '  transition: opacity 1.4s ease !important;',
    '}}',
    '@media (max-width: 720px) {{',
    '  html body .gti-watermark-hero {{ right: -22% !important; width: 130vmin !important; height: 130vmin !important; opacity: 0.18 !important; }}',
    '}}',
    /* Sección dividers — silueta lateral pequeña entre bloques */
    'html body .gti-divider {{',
    '  display: flex !important; align-items: center !important; justify-content: center !important;',
    '  gap: 22px !important;',
    '  margin: 4em auto 3em !important;',
    '  max-width: 720px !important;',
    '  opacity: 0.85 !important;',
    '  pointer-events: none !important;',
    '  position: relative !important;',
    '  z-index: 5 !important;',
    '}}',
    'html body .gti-divider::before, html body .gti-divider::after {{',
    '  content: "" !important;',
    '  flex: 1 !important;',
    '  height: 1px !important;',
    '  background: linear-gradient(90deg, transparent, rgba(255,179,71,0.35), transparent) !important;',
    '}}',
    'html body .gti-divider svg {{',
    '  width: 130px !important; height: auto !important;',
    '  color: #E20A17 !important;',
    '  opacity: 0.9 !important;',
    '  flex-shrink: 0 !important;',
    '  filter: drop-shadow(0 1px 3px rgba(0,0,0,0.15)) !important;',
    '}}',
    'html body .gti-divider::before, html body .gti-divider::after {{',
    '  background: linear-gradient(90deg, transparent, rgba(226,10,23,0.45), transparent) !important;',
    '}}',
    /* Footer mark — silueta trasera "alejándose" */
    'html body .gti-footer-mark {{',
    '  display: flex !important; flex-direction: column !important;',
    '  align-items: center !important; gap: 12px !important;',
    '  margin: 5em auto 3em !important;',
    '  padding: 0 24px !important;',
    '  max-width: 380px !important;',
    '  pointer-events: none !important;',
    '  opacity: 0.75 !important;',
    '  position: relative !important;',
    '  z-index: 5 !important;',
    '  transition: opacity .6s ease !important;',
    '}}',
    'html body .gti-footer-mark:hover {{ opacity: 0.85 !important; }}',
    'html body .gti-footer-mark svg {{',
    '  width: 100% !important; height: auto !important;',
    '  color: #E20A17 !important;',
    '  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.18)) !important;',
    '}}',
    'html body .gti-footer-mark .gti-footer-mark-caption {{',
    "  font-family: 'Inter Tight','Inter',sans-serif !important;",
    '  font-size: 10px !important;',
    '  font-weight: 600 !important;',
    '  letter-spacing: 3.5px !important;',
    '  text-transform: uppercase !important;',
    '  color: rgba(44,24,16,0.65) !important;',
    '  mix-blend-mode: difference !important;',
    '}}',
    /* Deep-nav: silueta lateral micro reemplazando el dot */
    'html body div.deep-nav .gti-nav-silhouette {{',
    '  width: 28px !important; height: 11px !important;',
    '  margin-right: 6px !important;',
    '  color: #FFB347 !important;',
    '  flex-shrink: 0 !important;',
    '  opacity: 0.9 !important;',
    '  filter: drop-shadow(0 0 4px rgba(255,179,71,0.5)) !important;',
    '}}',
    '@media (max-width: 480px) {{',
    '  html body div.deep-nav .gti-nav-silhouette {{ display: none !important; }}',
    '}}',
    /* Section accents — silueta frontal/trasera flotante como ornamento */
    'html body .gti-section-accent {{',
    '  position: absolute !important;',
    '  width: 240px !important; height: auto !important;',
    '  opacity: 0.32 !important;',
    '  pointer-events: none !important;',
    '  color: #E20A17 !important;',
    '  z-index: 1 !important;',
    '  mix-blend-mode: multiply !important;',
    '}}',
    'html body .gti-section-accent.left {{ left: 4% !important; top: 14% !important; transform: rotate(-6deg) !important; }}',
    'html body .gti-section-accent.right {{ right: 4% !important; bottom: 10% !important; transform: rotate(4deg) !important; }}',
    '@media (max-width: 900px) {{',
    '  html body .gti-section-accent {{ width: 140px !important; opacity: 0.2 !important; }}',
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

  /* Silueta lateral en formato inline para deep-nav (no requiere fetch externo) */
  var SIL_SIDE_MINI = '<svg class="gti-nav-silhouette" viewBox="0 0 540 200" fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M 38 148 L 38 138 Q 42 122 62 118 L 110 110 Q 130 70 168 58 L 230 50 L 340 50 Q 372 52 392 70 L 414 96 L 470 104 Q 498 108 504 126 L 504 148"/>' +
    '<path d="M 168 58 L 192 96 M 260 50 L 260 96 M 340 50 L 326 96"/>' +
    '<circle cx="132" cy="160" r="26"/>' +
    '<circle cx="425" cy="160" r="26"/>' +
    '</svg>';

  var navHTML = '<div id="deepNav" class="deep-nav">' +
    SIL_SIDE_MINI +
    '{nav_links_html}' +
    '<a href="{lang_href}" class="lang">{lang_label}</a>' +
    '</div>';

  var progressHTML = '<div class="gti-progress" id="gtiProgress"></div>';
  var backTopHTML = '<button class="gti-back-top" id="gtiBackTop" aria-label="' + BACK_LABEL + '">↑</button>';
  var watermarkHTML = '<div class="gti-watermark-hero" id="gtiWatermarkHero" aria-hidden="true"></div>';

  /* Footer mark con silueta trasera "alejándose" + caption */
  var footerMarkHTML = '<div class="gti-footer-mark" aria-hidden="true">' +
    '<svg viewBox="0 0 320 220" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">' +
    '<path d="M 92 28 L 228 28 Q 250 32 254 50 L 262 84"/>' +
    '<path d="M 58 84 L 66 50 Q 70 32 92 28"/>' +
    '<path d="M 66 84 L 254 84" stroke-width="1.8" opacity="0.7"/>' +
    '<rect x="124" y="22" width="72" height="6" rx="2" stroke-width="1.8"/>' +
    '<path d="M 58 84 L 42 100 L 42 138 L 278 138 L 278 100 L 262 84"/>' +
    '<rect x="50" y="104" width="62" height="26" rx="3" stroke-width="2.2"/>' +
    '<rect x="208" y="104" width="62" height="26" rx="3" stroke-width="2.2"/>' +
    '<rect x="138" y="112" width="44" height="10" rx="1.5" stroke-width="1.4" opacity="0.6"/>' +
    '<path d="M 42 138 L 30 168 L 30 184 Q 30 196 44 198 L 276 198 Q 290 196 290 184 L 290 168 L 278 138"/>' +
    '<path d="M 56 158 L 264 158" stroke-width="1.4" opacity="0.5"/>' +
    '<rect x="124" y="166" width="72" height="20" rx="1.5" stroke-width="1.6" opacity="0.7"/>' +
    '<ellipse cx="244" cy="200" rx="14" ry="6" stroke-width="2"/>' +
    '</svg>' +
    '<span class="gti-footer-mark-caption">Hasta la próxima vuelta</span>' +
    '</div>';

  /* Divider con silueta lateral */
  var dividerHTML = '<div class="gti-divider" aria-hidden="true">' +
    '<svg viewBox="0 0 540 200" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">' +
    '<path d="M 38 148 L 38 138 Q 42 122 62 118 L 110 110 Q 130 70 168 58 L 230 50 L 340 50 Q 372 52 392 70 L 414 96 L 470 104 Q 498 108 504 126 L 504 148"/>' +
    '<path d="M 168 58 L 192 96 M 260 50 L 260 96 M 340 50 L 326 96"/>' +
    '<circle cx="132" cy="160" r="26" stroke-width="3"/>' +
    '<circle cx="425" cy="160" r="26" stroke-width="3"/>' +
    '</svg>' +
    '</div>';

  /* Accent ornamental — silueta frontal o trasera flotante para secciones específicas */
  function makeAccent(kind, side) {{
    var paths = kind === 'front'
      ? '<path d="M 90 30 L 230 30 Q 252 32 256 46 L 264 78"/><path d="M 56 78 L 64 46 Q 68 32 90 30"/><path d="M 56 78 L 40 96 L 40 130 L 280 130 L 280 96 L 264 78"/><rect x="52" y="100" width="62" height="22" rx="3"/><rect x="206" y="100" width="62" height="22" rx="3"/><rect x="124" y="108" width="72" height="14" rx="1.5"/><path d="M 40 130 L 30 160 L 30 178 Q 30 190 44 192 L 276 192 Q 290 190 290 178 L 290 160 L 280 130"/>'
      : '<path d="M 92 28 L 228 28 Q 250 32 254 50 L 262 84"/><path d="M 58 84 L 66 50 Q 70 32 92 28"/><rect x="124" y="22" width="72" height="6" rx="2"/><path d="M 58 84 L 42 100 L 42 138 L 278 138 L 278 100 L 262 84"/><rect x="50" y="104" width="62" height="26" rx="3"/><rect x="208" y="104" width="62" height="26" rx="3"/><path d="M 42 138 L 30 168 L 30 184 Q 30 196 44 198 L 276 198 Q 290 196 290 184 L 290 168 L 278 138"/>';
    var vb = kind === 'front' ? '0 0 320 220' : '0 0 320 220';
    return '<div class="gti-section-accent ' + side + '" aria-hidden="true">' +
      '<svg viewBox="' + vb + '" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">' +
      paths +
      '</svg></div>';
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

  function injectAccent(sectionId, kind, side) {{
    var sec = document.getElementById(sectionId);
    if (!sec) return false;
    if (sec.querySelector('.gti-section-accent')) return true;
    var cs = window.getComputedStyle(sec);
    if (cs.position === 'static') sec.style.position = 'relative';
    sec.insertAdjacentHTML('afterbegin', makeAccent(kind, side));
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
    // 6. Section accents (siluetas frontal/trasera flotantes en secciones temáticas)
    injectAccent('motor', 'front', 'right');
    injectAccent('garage', 'rear', 'left');
    injectAccent('comunidad', 'front', 'left');
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
