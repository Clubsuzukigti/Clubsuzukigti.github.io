"""Inject floating deep-nav into Claude Design bundle.
The bundle replaces document.body on unpack, so we use MutationObserver
on documentElement (which is never replaced) to re-inject after render.
"""
from pathlib import Path

TARGET = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/index.html")

INJECTION = """  <style>
    .deep-nav {
      position: fixed; top: 0; left: 0; right: 0;
      z-index: 9998;
      background: rgba(10,9,8,0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      padding: 10px 24px;
      display: flex; gap: 18px;
      justify-content: center; align-items: center;
      flex-wrap: wrap;
      font-family: 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
      font-size: 10.5px;
      font-weight: 500;
      letter-spacing: 2.2px;
      text-transform: uppercase;
      border-bottom: 1px solid rgba(255,179,71,0.18);
      opacity: 0;
      transform: translateY(-100%);
      transition: opacity .55s ease, transform .55s ease;
      pointer-events: none;
    }
    .deep-nav.visible { opacity: 1; transform: translateY(0); pointer-events: auto; }
    .deep-nav a { color: #F5EFE0; text-decoration: none; opacity: 0.72; transition: opacity .2s, color .2s; padding: 4px 2px; }
    .deep-nav a:hover { color: #FFB347; opacity: 1; }
    .deep-nav a.lang { margin-left: 14px; border-left: 1px solid rgba(255,179,71,0.22); padding-left: 16px; color: #FFB347; font-weight: 600; }
    .deep-nav .dot { width: 4px; height: 4px; border-radius: 50%; background: #FFB347; opacity: 0.6; box-shadow: 0 0 8px #FFB347; }
    @media (max-width: 720px) { .deep-nav { font-size: 9px; gap: 10px; padding: 8px 12px; letter-spacing: 1.4px; } .deep-nav a.lang { margin-left: 4px; padding-left: 8px; } }
  </style>
  <script>
  (function(){
    var navHTML = '<div id="deepNav" class="deep-nav">' +
      '<span class="dot"></span>' +
      '<a href="/historia/">Historia</a>' +
      '<a href="/manuales/">Manuales</a>' +
      '<a href="/reparaciones/">Reparaciones</a>' +
      '<a href="/modificaciones/">Modificaciones</a>' +
      '<a href="/repuestos/">Repuestos</a>' +
      '<a href="/garage/">Garage</a>' +
      '<a href="/comunidad/">Comunidad</a>' +
      '<a href="/blog/">Blog</a>' +
      '<a href="/contacto/">Contacto</a>' +
      '<a href="/en/" class="lang">EN</a>' +
      '</div>';
    function attachScrollListener(){
      window.addEventListener('scroll', function(){
        var n = document.getElementById('deepNav'); if(!n) return;
        if(window.scrollY > 240) n.classList.add('visible'); else n.classList.remove('visible');
      }, { passive: true });
    }
    function ensureNav(){
      if (document.getElementById('deepNav')) return true;
      if (!document.body) return false;
      var hasContent = document.querySelector('section, [id="archivo"], [id="motor"], [id="garage"]');
      if (!hasContent) return false;
      document.body.insertAdjacentHTML('afterbegin', navHTML);
      attachScrollListener();
      return true;
    }
    /* The bundle replaces body via replaceWith, so observe documentElement */
    var obs = new MutationObserver(function(){
      if (ensureNav()) { /* keep observing; bundle may re-render */ }
    });
    obs.observe(document.documentElement, { childList: true, subtree: true });
    /* Fallback polling */
    var tries = 0;
    var iv = setInterval(function(){
      tries++;
      if (ensureNav() || tries > 80) clearInterval(iv);
    }, 250);
  })();
  </script>
"""

html = TARGET.read_text(encoding='utf-8')
if 'id="deepNav"' in html:
    print("Already injected, skipping")
else:
    new = html.replace('</body>', INJECTION + '\n</body>', 1)
    TARGET.write_text(new, encoding='utf-8')
    print(f"Injected {len(INJECTION)} chars before </body>")
    print(f"New file size: {len(new)} bytes")
