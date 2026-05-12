"""Traduce el bundle premium ES → EN.
Strategy: dict literal de strings ES → EN. Aplica sobre el HTML como
reemplazo textual. Solo strings user-facing; CSS selectors y JS
identifiers no se tocan.

Sobre la deep-nav inyectada: la traducimos a inglés y ajustamos
paths para que apunten a /en/<section>/.
"""
from pathlib import Path

SRC = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.html")
OUT = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs/landing/index.en.html")

# Translation map. Order matters: long phrases first to avoid sub-string clashes.
T = [
    # === HERO ===
    ("Preservando el legado del", "Preserving the legacy of the"),
    ("Preservando\\nel legado del", "Preserving\\nthe legacy of the"),
    ("Suzuki GTi Car Club — Preservando el legado del Swift GTi",
     "Suzuki GTi Car Club — Preserving the Swift GTi legacy"),
    ("Archivo técnico, repuestos y comunidad mundial",
     "Technical archive, parts and worldwide community"),
    ("ARCHIVO TÉCNICO · REPUESTOS · COMUNIDAD MUNDIAL",
     "TECHNICAL ARCHIVE · PARTS · WORLDWIDE COMMUNITY"),
    ("ENTRAR AL GARAGE", "ENTER THE GARAGE"),
    ("EXPLORAR EL ARCHIVO", "EXPLORE THE ARCHIVE"),
    ("SCROLL PARA ABRIR EL ARCHIVO", "SCROLL TO OPEN THE ARCHIVE"),
    ("scroll para abrir el archivo", "scroll to open the archive"),

    # === STATS ===
    ("DATOS EN FRÍO", "COLD HARD FACTS"),
    ("EL AUTO, EL CLUB", "THE CAR, THE CLUB"),
    ("CIFRAS VERIFICADAS · MAYO 2026", "VERIFIED FIGURES · MAY 2026"),
    ("PS · PICO", "PS · PEAK"),
    ("CC · CILINDRADA", "CC · DISPLACEMENT"),
    ("KG · PESO", "KG · WEIGHT"),
    ("RPM · REDLINE", "RPM · REDLINE"),
    ("MIEMBROS", "MEMBERS"),
    ("GRUPOS · 24 PAÍSES", "GROUPS · 24 COUNTRIES"),
    ("PAÍSES", "COUNTRIES"),

    # === MANIFIESTO ===
    ("MANIFIESTO DEL CLUB", "CLUB MANIFESTO"),
    ("POR QUÉ ESTE SITIO EXISTE", "WHY THIS SITE EXISTS"),
    ("Por qué este sitio existe y por", "Why this site exists and"),
    ("qué importa ahora.", "why it matters now."),
    ("En 8 años pasamos de unos 50 autos circulando a menos de",
     "In 8 years we went from about 50 active cars to less than"),
    ("MANIFIESTO", "MANIFESTO"),

    # === MOTOR G13B ===
    ("El motor que", "The engine that"),
    ("no debería existir", "shouldn't exist"),
    ("Soporta", "Holds"),
    ("Máximo documentado", "Documented max"),
    ("TRES ETAPAS DEL G13B", "THREE STAGES OF THE G13B"),
    ("Original", "Original"),
    ("Mercado Japón", "Japan market"),
    ("Build turbo", "Turbo build"),
    ("PS · OEM", "PS · OEM"),
    ("BLUEPRINT · G13B", "BLUEPRINT · G13B"),
    ("Colector escape", "Exhaust manifold"),
    ("bloque", "block"),

    # === HERENCIA / DECALS ===
    ("DECALS · VITRINAS", "DECALS · DISPLAY CASES"),
    ("REPUESTOS IDENTIFICADOS", "IDENTIFIED PARTS"),
    ("layout museo · 3 vitrinas en grid", "museum layout · 3 cases in grid"),
    ("Tezeni era estudiante en Tokyo", "Tezeni was a student at Tokyo"),
    ("University of the Arts. Después diseñaría",
     "University of the Arts. He would later design"),
    ("el Shinkansen Serie 300.", "the Shinkansen Series 300."),
    ("NOTA AL PIE · ARCHIVO HISTÓRICO", "FOOTNOTE · HISTORICAL ARCHIVE"),
    ("ARCHIVO HISTÓRICO", "HISTORICAL ARCHIVE"),

    # === GARAGE DEL CLUB ===
    ("GARAGE DEL CLUB", "CLUB GARAGE"),
    ("Garage del Club", "Club Garage"),
    ("AUTOS ARCHIVADOS", "CARS ARCHIVED"),
    ("BUILDS ACTIVOS", "ACTIVE BUILDS"),
    ("GRID ASIMÉTRICO · POLAROIDS", "ASYMMETRIC GRID · POLAROIDS"),
    ("ROTACIÓN", "ROTATION"),
    ("EL ÚLTIMO SLOT LO LLENAS TÚ", "THE LAST SLOT IS YOURS TO FILL"),
    ("Los supervivientes", "The survivors"),
    ("Tu auto merece", "Your car deserves to"),
    ("estar aquí.", "be here."),
    ("SLOT 87 ABIERTO", "SLOT 87 OPEN"),
    ("ENVÍALO Y LO ARMAMOS CONTIGO", "SEND IT IN, WE BUILD IT WITH YOU"),
    ("ENVIAR MI PROYECTO POR", "SEND MY PROJECT VIA"),
    ("TELEGRAM", "TELEGRAM"),
    ("tu polaroid", "your polaroid"),
    ("DETALLE · GTI", "DETAIL · GTI"),
    ("FOTO · VERTO · 3/4 TRASERA", "PHOTO · VERTO · 3/4 REAR"),
    ("FOTO · BUBALOO", "PHOTO · BUBALOO"),
    ("FOTO · SWIFT AMARILLO", "PHOTO · SWIFT AMARILLO"),
    ("FOTO · SUKI · OPEN HOOD", "PHOTO · SUKI · OPEN HOOD"),

    # === COLABORAR ===
    # NOTA: NO traducir "que" → "that" suelto: rompe querySelector → thatrySelector
    # Hacer match en frase completa
    ("¿Tienes algo\\nque\\nsume?\\nSúbelo.", "Got something\\nthat\\nadds up?\\nUpload it."),
    ("¿Tienes algo que sume? Súbelo.", "Got something that adds up? Upload it."),
    ("¿Tienes algo que sume?", "Got something that adds up?"),
    ("¿Tienes algo", "Got something"),
    ("Súbelo.", "Upload it."),
    ("? Súbelo", "? Upload it"),
    ("sume?", "adds up?"),
    ("Manuales escaneados, fotos de tu auto, un torque-spec garabateado en",
     "Scanned manuals, photos of your car, a torque spec scribbled on"),
    ("una servilleta, un screenshot del EPC, un emblema en la mano antes de",
     "a napkin, an EPC screenshot, an emblem in your hand before"),
    ("pegarlo. Todo cuenta. Todo entra al archivo con tu crédito y queda para",
     "you stick it on. It all counts. Everything enters the archive with your credit and stays"),
    ("siempre.", "forever."),
    ("Fotos de tu auto, idealmente con número de chasis",
     "Photos of your car, ideally with chassis number"),
    ("Manuales escaneados — taller, partes, propietario",
     "Scanned manuals — service, parts, owner"),
    ("Torque specs y procedimientos no documentados",
     "Torque specs and undocumented procedures"),
    ("Screenshots del EPC y catálogos electrónicos",
     "Screenshots from EPC and electronic catalogs"),
    ("Part numbers verificados con proveedor",
     "Part numbers verified with supplier"),
    ("Historia oral - entrevistas con dueños y mecánicos",
     "Oral history - interviews with owners and mechanics"),
    ("Cualquier cosa rara que solo tú tienes",
     "Anything rare that only you have"),
    ("SUBIR", "SUBMIT"),
    ("aporte", "contribution"),
    ("POR TELEGRAM", "VIA TELEGRAM"),
    ("presiona — se hunde con bounce", "press — sinks with bounce"),
    ("APORTES YA RECIBIDOS", "CONTRIBUTIONS RECEIVED"),
    ("ACEPTADO", "ACCEPTED"),
    ("EN REVISIÓN", "UNDER REVIEW"),
    ("POLAROID · CULTUS 4WD", "POLAROID · CULTUS 4WD"),
    ("SCREENSHOT · EPC", "SCREENSHOT · EPC"),
    ("FLYWHEEL EXPLODED", "FLYWHEEL EXPLODED"),
    ("cabeza", "head"),
    ("torque sequence", "torque sequence"),
    ("servilleta del taller", "napkin from the shop"),
    ("FOTO · EMBLEMA GTI", "PHOTO · GTI EMBLEM"),
    ("SOSTENIDO EN MANO", "HELD IN HAND"),

    # === COMUNIDAD ===
    ("COMUNIDAD MUNDIAL", "WORLDWIDE COMMUNITY"),
    ("Comunidad mundial", "Worldwide community"),

    # === CTA FINAL ===
    ("Estos autos no pueden", "These cars cannot"),
    ("morir en silencio.", "die in silence."),
    ("Si tienes uno, conoces uno, o quieres aprender a",
     "If you have one, know one, or want to learn how to"),
    ("resucitar uno — este es tu lugar.",
     "resurrect one — this is your place."),

    # === FOOTER ===
    ("EST. 2017 · QUETZALTENANGO, GUATEMALA",
     "EST. 2017 · QUETZALTENANGO, GUATEMALA"),  # unchanged
    ("EL PORTÓN NUNCA SE CIERRA", "THE GATE NEVER QUITE"),
    ("DEL TODO.", "CLOSES."),
    ("Navegar", "Navigate"),
    ("Encontrarnos", "Find us"),
    ("Archivo", "Archive"),
    ("Motor G13B", "Motor G13B"),
    ("Garage", "Garage"),
    ("Comunidad", "Community"),
    ("Colaborar", "Collaborate"),
    ("Sitio creado por", "Site built by"),
    ("Abriendo el garage", "Opening the garage"),

    # === DEEP NAV (inyectada) ===
    (">Historia<", ">History<"),
    (">Manuales<", ">Manuals<"),
    (">Reparaciones<", ">Repairs<"),
    (">Modificaciones<", ">Modifications<"),
    (">Repuestos<", ">Parts<"),
    (">Garage<", ">Garage<"),
    (">Comunidad<", ">Community<"),
    (">Blog<", ">Blog<"),
    (">Contacto<", ">Contact<"),

    # Deep-nav paths to EN
    ('href="/historia/"', 'href="/en/historia/"'),
    ('href="/manuales/"', 'href="/en/manuales/"'),
    ('href="/reparaciones/"', 'href="/en/reparaciones/"'),
    ('href="/modificaciones/"', 'href="/en/modificaciones/"'),
    ('href="/repuestos/"', 'href="/en/repuestos/"'),
    ('href="/garage/"', 'href="/en/garage/"'),
    ('href="/comunidad/"', 'href="/en/comunidad/"'),
    ('href="/blog/"', 'href="/en/blog/"'),
    ('href="/contacto/"', 'href="/en/contacto/"'),
    ('href="/en/" class="lang"', 'href="/" class="lang"'),  # switch to ES
    ('>EN<', '>ES<'),

    # === lang attribute ===
    ('<html lang="es">', '<html lang="en">'),
]

html = SRC.read_text(encoding='utf-8')
original_len = len(html)
replacements_made = 0

for es, en in T:
    if es in html:
        count = html.count(es)
        html = html.replace(es, en)
        replacements_made += count

OUT.write_text(html, encoding='utf-8')
print(f"Source: {original_len} bytes")
print(f"Translated: {len(html)} bytes ({len(html) - original_len:+d})")
print(f"Replacements applied: {replacements_made}")
print(f"Output: {OUT}")
