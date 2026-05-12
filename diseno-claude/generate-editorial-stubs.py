"""Genera stubs editoriales para sub-páginas en construcción.
Cada stub mantiene la atmósfera del sitio (quote, stats, tip,
CTA Telegram) y reemplaza el placeholder genérico "página en
construcción" con un teaser real del contenido.
"""
from pathlib import Path

BASE = Path(r"c:/Users/PcTec/Claude Code/suzuki owners/sitio-web/docs")

# Definición por página: title, description, quote, intro, stats [(num, lbl)x4], teaser items
PAGES = {
    'comunidad/facebook.md': {
        'title': 'Grupos Facebook',
        'desc': '40+ grupos verificados · Pakistán 430K miembros · Argentina/Colombia/Chile activos LatAm',
        'quote': 'El mapa real de la comunidad — Pakistán manda en volumen, LatAm en pasión.',
        'cite': 'FACEBOOK · COMUNIDAD VERIFICADA 2026',
        'intro': 'Inventario completo de los **40+ grupos Facebook** verificados con member-count real. Desde los grupos masivos de Pakistán (430K+ miembros) hasta los pequeños grupos LatAm con la mayor actividad por miembro.',
        'stats': [('40+', 'GRUPOS VERIFICADOS'), ('800K+', 'MIEMBROS TOTAL'), ('430K', 'PAKISTÁN · 5 GRUPOS'), ('24+', 'PAÍSES')],
        'teaser': [
            'Top 10 grupos por member count (Pakistan, Indonesia, Worldwide)',
            'Grupos LatAm activos por país (Argentina, Colombia, Chile, Ecuador)',
            'Admins conocidos para outreach (Fran, Toto, Chris, Samuel)',
            'Grupos cerrados premium (con criterios de admisión)',
            'Páginas verificadas vs grupos comunidad',
        ],
        'parent': '../comunidad/',
    },
    'comunidad/foros.md': {
        'title': 'Foros internacionales',
        'desc': '14 foros activos · Geo Metro Forum hub USA · foroswift.com.ar · TeamSwift archive',
        'quote': 'Lo que se discutió hace 10 años sigue ahí. Los foros sobreviven porque guardan la conversación.',
        'cite': 'FOROS · ARCHIVO PERMANENTE',
        'intro': '14 foros internacionales activos donde la comunidad Swift GTi documenta builds, soluciona problemas y archiva el conocimiento. Algunos tienen 20+ años de threads buscables.',
        'stats': [('14', 'FOROS ACTIVOS'), ('471', 'TEMAS · FOROSWIFT ARGENTINA'), ('5,204', 'POSTS · CLUB SV'), ('20+', 'AÑOS · GEO METRO FORUM')],
        'teaser': [
            'Geo Metro Forum (USA) — el hub principal en inglés',
            'TeamSwift Archive — sucesor en suzukiswiftrepository.com',
            'foroswift.com.ar — Argentina, sección Preparación con 471 temas',
            'Foros LatAm — Salvador, España, México',
            'Pakwheels — Pakistán masivo (Cultus mercado vivo)',
            'Mighty Car Mods Forum — Australia G13B builds',
        ],
        'parent': '../comunidad/',
    },
    'comunidad/youtube.md': {
        'title': 'Canales YouTube',
        'desc': '30+ canales · Zukidream Italia rebuild G13B · Mighty Car Mods · Monster Tajima Pikes Peak',
        'quote': 'Ver un G13B desarmarse en video vale más que leer el manual tres veces.',
        'cite': 'YOUTUBE · ARCHIVO VISUAL',
        'intro': '30+ canales YouTube con contenido específico de Swift GTi / Cultus / Forsa. Rebuilds paso a paso, builds turbo dyno, racing histórico, restauraciones.',
        'stats': [('30+', 'CANALES'), ('700', 'HP · TAJIMA TWIN-ENGINE'), ('376', 'WHP · YOUTUBE DYNO RECORD'), ('5+', 'PARTES · ZUKIDREAM REBUILD')],
        'teaser': [
            'Zukidream (Italia) — rebuild G13B serie 5 partes',
            'Mighty Car Mods (Australia) — MOOG\'s Suzuki build',
            'Monster Tajima — 700HP Twin-Engine Pikes Peak 1993',
            'Engine Swap Depot — RWD G13B Swift Sweden',
            'danST Engineering — bike carb dyno',
            'Videos icónicos en español',
        ],
        'parent': '../comunidad/',
    },
    'historia/convertibles.md': {
        'title': 'Convertibles G13B',
        'desc': 'El unicornio absoluto · JDM Feb 1992-Early 1993 · build Verto en Centroamérica · conversiones documentadas',
        'quote': 'Suzuki nunca lo dijo en voz alta — pero produjo un convertible con G13B. Solo 11 meses. Solo Japón.',
        'cite': 'CONVERTIBLE · JDM 1992-1993',
        'intro': 'El **Suzuki Cultus Convertible** es la variante más rara y deseada del modelo. Producido solo entre febrero de 1992 y principios de 1993 exclusivamente para Japón. Plus las conversiones G13B realizadas sobre Geo Metro / Suzuki Forsa Convertible alrededor del mundo.',
        'stats': [('11', 'MESES · PRODUCCIÓN JDM TOTAL'), ('2', 'PUERTAS · CONFIGURACIÓN ÚNICA'), ('JDM', 'SOLO JAPÓN · NUNCA EXPORTADO'), ('VERTO', 'BUILD ÚNICO EN CENTROAMÉRICA')],
        'teaser': [
            'Cultus Convertible JDM (1992-1993) — ficha técnica + producción real',
            'Suzuki Forsa Convertible / Geo Metro Convertible — base para conversiones',
            'Build "Verto" — único en Centroamérica con G13B swap completo',
            'Identificación y autenticidad (placa firewall, VIN, badges)',
            'Mercado y precios actuales',
            'Recursos de restauración para techo blando',
        ],
        'parent': '../historia/',
    },
    'historia/cultus-gti-jdm.md': {
        'title': 'Cultus GTi JDM',
        'desc': 'Versiones japonesas · AA34S 2dr · AB34S 5dr · AF34S 4WD · 115 PS JIS · CR 11.5:1',
        'quote': 'En Japón se llamó Cultus. Tres códigos de carrocería. Tres variantes con el mismo G13B JDM más potente del mundo.',
        'cite': 'CULTUS GTi · JDM 1989-2002',
        'intro': 'En el mercado japonés el modelo se vendió como **Cultus GTi** con tres códigos de carrocería distintos. El motor G13B JDM tenía especificación superior a la export: **115 PS JIS, CR 11.5:1, headers tubulares de fábrica**. Sólo en Japón.',
        'stats': [('AA34S', '3-PUERTAS HATCH'), ('AB34S', '5-PUERTAS HATCH'), ('AF34S', '4WD VISCOUS LSD'), ('115', 'PS JIS · MOTOR JDM')],
        'teaser': [
            'AA34S — hatchback 3 puertas (la más común JDM)',
            'AB34S — hatchback 5 puertas (raro)',
            'AF34S — 4WD viscous coupling (la rareza absoluta)',
            'Cultus Sedán 4 puertas — pub. suplementaria oficial',
            'Cultus Convertible (1992-1993) — solo 11 meses producción',
            'Diferencias motor JDM vs export (CR, cams, ECU)',
            'Cómo importar un Cultus JDM (25-year rule USA, etc.)',
        ],
        'parent': '../historia/',
    },
    'historia/variantes-mundiales.md': {
        'title': 'Variantes mundiales',
        'desc': 'Forsa GTi LatAm · Swift GT Canadá/USA · Pontiac Firefly · Chevy Sprint · Maruti 1000 · Cultus Pakistán',
        'quote': 'El mismo auto. Catorce nombres. Veinticuatro países. Una sola plataforma japonesa que no debería haber sido tan querida.',
        'cite': 'VARIANTES · GLOBAL 1983-2016',
        'intro': 'El Swift GTi se vendió bajo **14 nombres distintos** alrededor del mundo entre 1983 y 2016. Misma plataforma SF413 con motor G13B, pero con badging y mercado completamente diferentes según región.',
        'stats': [('14', 'NOMBRES COMERCIALES'), ('24+', 'PAÍSES VENDIDOS'), ('33', 'AÑOS · DE 1983 A 2016'), ('PAK', 'CULTUS · MERCADO MÁS GRANDE')],
        'teaser': [
            'Suzuki Swift GTi — Europa, Australia, Asia Sureste',
            'Suzuki Forsa GTi — Ecuador, Colombia, Centroamérica',
            'Suzuki Swift GT — USA, Canadá (sin la "i" por demanda VW)',
            'Pontiac Firefly Turbo — Canadá (G10T 1.0L)',
            'Chevrolet Sprint Turbo — USA (G10T 1.0L)',
            'Geo Metro — USA (1.0L NA, base para conversiones)',
            'Maruti 1000 / Esteem — India',
            'Suzuki Cultus / Margalla — Pakistán (33 años producción)',
            'Holden Barina — Australia',
            'Subaru Justy — algunos mercados Europa',
        ],
        'parent': '../historia/',
    },
    'manuales/suplementarios.md': {
        'title': 'Manuales suplementarios',
        'desc': '4 suplementarios MK2 · facelift 1991 crítico · 4WD AF34S · sedán · inyección electrónica',
        'quote': 'El manual base no es suficiente. Los suplementarios son los que documentan los cambios que mantuvieron al modelo vivo.',
        'cite': 'SUPLEMENTARIOS · PUB. 99501-XXXX',
        'intro': 'Los manuales suplementarios son las publicaciones oficiales de Suzuki que documentan cambios específicos sobre el manual base SF413 — facelift 1991, variante 4WD, sedán, sistema de inyección. Conocer cuál suplemento aplica a tu auto es la diferencia entre arreglarlo bien o causarte daño.',
        'stats': [('4', 'SUPLEMENTARIOS MK2'), ('127', 'PG · FACELIFT 1991 CRÍTICO'), ('259', 'PG · 4WD AF34S'), ('195', 'PG · INYECCIÓN ELECTRÓNICA')],
        'teaser': [
            'Pub. 99501-64B00 — SF413 GTi Facelift Junio 1991 (127 pg) ⭐ el crítico',
            'Pub. 99501-63B01 — SF413 Inyección Electrónica (195 pg)',
            'Pub. 99501-63B20 — SF413 Sedán 4 puertas (92 pg)',
            'Pub. 99501-63B30 — SF413 4WD (259 pg)',
            'Pub. 99501-60B00 — SF310 1.0L (192 pg, en español)',
            'Pub. 99501-80E00 — SF Series 1996 MK3 (524 pg)',
            'Pub. 99501-80E01 — MK3 con ABS + Airbag (122 pg)',
        ],
        'parent': '../manuales/',
    },
    'manuales/tsb.md': {
        'title': 'TSB oficiales Suzuki',
        'desc': 'TSB G13B Engine Adjustments 1996 · timing · CAS · TPS · ralentí · documentado oficial',
        'quote': 'Los TSB son los ajustes que Suzuki documentó después de descubrir problemas reales en producción. Más confiables que cualquier blog.',
        'cite': 'TSB · TECHNICAL SERVICE BULLETIN OFICIAL',
        'intro': 'Los **Technical Service Bulletins** son los documentos oficiales que Suzuki publica para que mecánicos actualicen procedimientos después de descubrir patrones en producción. El TSB G13B Engine Adjustments (©1996) es la biblia para tunear el motor a especificación oficial.',
        'stats': [('19', 'PÁGINAS · G13B TSB'), ('1996', 'AÑO · ©MITCHELL REPAIR'), ('4', 'AJUSTES CRÍTICOS DOCUMENTADOS'), ('TSB', 'OFICIAL · NO TUTORIAL DE FORO')],
        'teaser': [
            'TSB G13B Engine Adjustments (©1996 Mitchell Repair Information)',
            'Timing de encendido — 12° ± 6° BTDC @ 800 rpm ralentí',
            'CAS Pick-up Coil Air Gap — 0.20-0.30 mm',
            'TPS calibración con ohmímetro',
            'Velocidad de ralentí por condición A/C',
            'Otros TSBs relacionados (transmisión, frenos, eléctrico)',
        ],
        'parent': '../manuales/',
    },
    'modificaciones/aspirado.md': {
        'title': 'Modificaciones N/A (aspirado)',
        'desc': 'Bolt-on hasta 165hp documentados · headers 4-2-1 · DCOE/GSXR throttles · porting cabezal · pistones G16 Vitara',
        'quote': 'Sin turbo, sin nitro, sin trucos. Solo cabezal trabajado y respiración. El G13B aspirado da 165hp si lo dejas respirar.',
        'cite': 'N/A BUILDS · 100→165 HP DOCUMENTADO',
        'intro': 'La ruta aspirada (Naturally Aspirated) del G13B llega hasta **165 hp documentados @ 8500 rpm safe revs**. Sin perder confiabilidad. Sin necesidad de boost. Solo headers, cams, porting, intake serio y un build de cabezal que respete al motor.',
        'stats': [('165', 'HP · BUILD N/A MÁXIMO'), ('8,500', 'RPM · SAFE REVS BUILD COMPLETO'), ('1,400', 'CC · BORE-OVER G16 VITARA'), ('4', 'NIVELES PROGRESIVOS')],
        'teaser': [
            'Nivel 1 — Bolt-on básico (100-115hp): filtro, headers, escape',
            'Nivel 2 — Cabezal trabajado (130-150hp): porting, válvulas, cams',
            'Nivel 3 — Intake serio (150-180hp): DCOE / GSXR throttles',
            'Nivel 4 — Build máximo (165hp+): bore-over, knife-edge crank',
            'Headers comparativos: 4-2-1 vs 4-1 vs equal-length',
            'Cams: Piper / DBilas / Cat Cams comparativa',
        ],
        'parent': '../modificaciones/',
    },
    'modificaciones/ecu.md': {
        'title': 'ECU standalone',
        'desc': 'Megasquirt MS2/MS3X · Haltech Sprint/Elite · AEM · conversión distributor→COP · maps base disponibles',
        'quote': 'La ECU stock del GTi es honesta hasta cierto punto. Cuando empiezas a meter turbo o cams agresivos, te pide jubilarse.',
        'cite': 'ECU STANDALONE · MS · HALTECH · AEM',
        'intro': 'Una vez que sales del territorio bolt-on, la ECU stock del Swift GTi limita el potencial del motor. Standalone ECUs como **Megasquirt MS2/MS3X**, **Haltech Sprint/Elite** o **AEM** permiten mapeo completo de combustible + chispa, control de boost, launch control, anti-lag.',
        'stats': [('MS3X', 'MEGASQUIRT · TOP OPEN-SOURCE'), ('ELITE', 'HALTECH · 1500/2500 PRO'), ('COP', 'COIL-ON-PLUG · ELIMINA CAS'), ('$400', 'PRESUPUESTO MS2 ENTRADA')],
        'teaser': [
            'Megasquirt MS2 v3 — entrada económica con todas las features básicas',
            'Megasquirt MS3X — sequential injection + ignition independiente',
            'Haltech Sprint — semi-pro con buena UI',
            'Haltech Elite 1500/2500 — pro builds turbo serios',
            'AEM Infinity-6 — alternativa premium',
            'Conversión distributor → Coil-On-Plug (elimina CAS interno)',
            'Maps base disponibles de la comunidad',
            'Wideband O2 (AEM, Innovate, PLX) — obligatorio',
        ],
        'parent': '../modificaciones/',
    },
    'modificaciones/engine-swaps.md': {
        'title': 'Engine swaps',
        'desc': 'M16A Swift Sport · Honda K20Z2 · Hayabusa moto · VR6 biturbo · lo posible y lo loco',
        'quote': 'Cuando ya no quieres más G13B, la carrocería Swift acepta casi cualquier motor con suficiente paciencia y herramientas.',
        'cite': 'ENGINE SWAPS · ROUTE DOCUMENTADA',
        'intro': 'Cuando el camino del G13B llega a su límite (o ya tienes uno reventado), la carrocería **SF413/AF34S** se vuelve plataforma para swaps que van desde lo sensato (**M16A** del Swift Sport moderno) hasta lo absolutamente loco (**Hayabusa de moto** o **VR6 biturbo**).',
        'stats': [('M16A', '125 HP · SWIFT SPORT MODERN'), ('K20Z2', '197 HP · HONDA TYPE R'), ('VR6T', '350+ HP · BUILD EXTREMO'), ('1300CC', 'HAYABUSA · MOTO SWAP')],
        'teaser': [
            'M16A — del Swift Sport ZC31S/ZC32S (lo más sensato, MAF compatible)',
            'Honda K20Z2 — Type R potencia con kit Hasport',
            'EJ20 Subaru turbo — la opción rally',
            'VR6 Volkswagen + biturbo — el monstruo',
            'Hayabusa motor — moto a auto (RWD swap obligatorio)',
            'Consideraciones eje, transmisión, ECU, cooling',
        ],
        'parent': '../modificaciones/',
    },
    'modificaciones/suspension-frenos.md': {
        'title': 'Suspensión y frenos',
        'desc': 'Coilovers BC Racing · Tein · big brake Wilwood Brembo CEIKA · LSD RacingDiffs Phantom Grip · llantas 14-15',
        'quote': 'El G13B turbo te lleva rápido en recta. Sin suspensión y frenos modernos, te lleva rápido directo a una baranda.',
        'cite': 'CHASIS · COILOVERS · LSD · BIG BRAKE',
        'intro': 'Modificar el motor sin modificar el chasis es buscar accidente. La plataforma SF413 acepta coilovers premium, big brake kits, LSD diferencial para FWD, llantas 14-15 con tires apropiados, y bushings reforzados que transforman el comportamiento.',
        'stats': [('BC RACING', 'COILOVERS · ENTRADA'), ('WILWOOD', 'BIG BRAKE KIT PREMIUM'), ('RACINGDIFFS', 'LSD PLUG&PLAY POLONIA'), ('+30mm', 'OFFSET LLANTAS 15X7')],
        'teaser': [
            'Coilovers BC Racing BR Series — entrada premium',
            'Coilovers Tein Flex Z — más caro pero más calidad',
            'Coilovers KSPORT — opción budget',
            'Big brake Wilwood / Brembo / CEIKA',
            'LSD RacingDiffs (Polonia) — 25% lock plug-and-play',
            'LSD Phantom Grip (USA) — alternativa económica',
            'Bushings poliuretano control arms',
            'Llantas 14×6 y 15×7 con tires 195/55R15 o 205/50R15',
        ],
        'parent': '../modificaciones/',
    },
    'reparaciones/carroceria.md': {
        'title': 'Carrocería y óxido',
        'desc': 'Puntos críticos de óxido · rocker panels · floor pans · control arm mounts · reparación y prevención',
        'quote': 'El motor se reconstruye con dinero. La carrocería con tiempo, paciencia, y a veces no se puede reconstruir.',
        'cite': 'ÓXIDO · LA MUERTE LENTA DEL MODELO',
        'intro': 'La carrocería del SF413 tiene **cavidades de diseño** que atrapan humedad y aceleran la oxidación. Conocer los puntos críticos antes de comprar, y tratarlos preventivamente si ya tienes el auto, es la diferencia entre 10 años más de vida útil o un proyecto perdido.',
        'stats': [('5', 'PUNTOS CRÍTICOS DE ÓXIDO'), ('ROCKER', 'PANELS LATERALES · #1 PROBLEMA'), ('FLOOR', 'PANS · PISO BAJO ASIENTOS'), ('25%', 'DEL VALOR · REPARACIÓN MAL HECHA')],
        'teaser': [
            'Rocker panels (skirts laterales) — el #1 problema documentado',
            'Floor pans (piso debajo de asientos) — humedad entrapment',
            'Control arm mounts (puntos suspensión) — peligroso si oxidado',
            'Wheel wells (interior de pasarueda) — fácil de inspeccionar',
            'Battery tray (bandeja batería) — leaks ácido común',
            'Prevención: rust converter, undercoating, drain hole cleanout',
            'Reparación: corte + soldadura + masilla + pintura',
        ],
        'parent': '../reparaciones/',
    },
    'reparaciones/electrico.md': {
        'title': 'Sistema eléctrico',
        'desc': 'ECM diagnóstico · TPS · AFM hot-wire · sensores WTS/O2 · bobinas · fusibleras interna y externa',
        'quote': 'Los autos antiguos no fallan eléctricos al azar. Fallan eléctricos por conectores oxidados que nadie limpió en 30 años.',
        'cite': 'ELÉCTRICO · DIAGNÓSTICO + REPARACIÓN',
        'intro': 'El sistema eléctrico del SF413 es relativamente simple — multi-port FI con ECM Suzuki, sensores que se pueden testear con multímetro, y un arnés que tiende a fallar más por conectores oxidados que por componentes muertos.',
        'stats': [('9', 'CÓDIGOS DIAGNÓSTICO ECM'), ('TPS', 'CALIBRACIÓN CON OHMÍMETRO'), ('AFM', 'HOT-WIRE · PROBLEMA #2'), ('CAS', 'PICK-UP · PROBLEMA #1 NO ARRANQUE')],
        'teaser': [
            'Códigos de diagnóstico ECM (12 normal, 13-42 fallas)',
            'TPS — calibración con ohmímetro paso a paso',
            'AFM hot-wire — limpieza con MAF cleaner',
            'Sensores WTS (water temp) — resistencia a temperatura',
            'Sensor O2 lambda — códigos vs voltaje real',
            'Bobinas y cables HT — testing chispa',
            'CAS (Crank Angle Sensor) — gap 0.20-0.30mm',
            'Fusibleras interna + externa — mapeo completo',
            'Arnés común failure points',
        ],
        'parent': '../reparaciones/',
    },
    'reparaciones/frenos-suspension.md': {
        'title': 'Frenos y suspensión',
        'desc': 'Pastillas DOT 3 · mangueras · bujes control arms · tie rods · ball joints · alineación correcta',
        'quote': 'Si no compras buenos frenos, estás ahorrando dinero a costa de tu seguridad.',
        'cite': 'FRENOS + SUSPENSIÓN · STOCK + UPGRADES',
        'intro': 'Mantener el sistema de frenos y suspensión del Swift GTi en spec es crítico. Los discos delanteros ventilados 233mm son adecuados para el peso del auto, pero los componentes se desgastan: pastillas, mangueras, bujes, tie rods, ball joints. Ignorarlos compromete la seguridad.',
        'stats': [('233mm', 'DISCOS DELANTEROS VENTILADOS'), ('180mm', 'TAMBORES TRASEROS'), ('DOT 3', 'LÍQUIDO FRENOS OEM'), ('80K', 'KM · INTERVALO PASTILLAS COMÚN')],
        'teaser': [
            'Pastillas: OEM vs Akebono vs EBC Greenstuff comparativa',
            'Mangueras stainless — upgrade económico',
            'Bujes control arms — poliuretano vs OEM goma',
            'Tie rods + ball joints — replacement intervals',
            'Cilindros traseros — fugas comunes',
            'Master cylinder — síntomas de falla',
            'Alineación correcta SF413 (toe, camber, caster)',
            'Big brake conversions (Vitara front, Wilwood)',
        ],
        'parent': '../reparaciones/',
    },
    'reparaciones/transmision.md': {
        'title': 'Transmisión',
        'desc': 'Crunch 2da/3ra synchros · aceite GL-4 obligatorio · embrague Exedy · swap caja Lancia · LSD options',
        'quote': 'El 80% de las transmisiones GTi muertas en LatAm es por usar aceite GL-5. Los aditivos sulfurosos destruyen los synchros de bronce.',
        'cite': 'TRANSMISIÓN MANUAL · GL-4 OBLIGATORIO',
        'intro': 'La transmisión manual del Swift GTi (5-velocidades) tiene **un punto débil documentado**: synchros de 2da y 3ra que sufren con uso intenso. Los problemas más comunes son rebuilable, pero requieren parts específicos. Y sobre todo: NUNCA usar aceite GL-5.',
        'stats': [('GL-4', 'OBLIGATORIO · GL-5 DESTRUYE'), ('2da/3ra', 'SYNCHROS · #1 PROBLEMA'), ('EXEDY', 'EMBRAGUE OEM 190MM'), ('225MM', 'PCD · 18 SPLINES STOCK')],
        'teaser': [
            'Crunch en 2da/3ra — diagnóstico (synchros vs aceite vs cable)',
            'Aceite GL-4 — Redline MTL, Pennzoil, Castrol Syntrans',
            'Por qué GL-5 destruye (aditivos sulfurosos)',
            'Embrague Exedy stock — 190mm, 18 splines, 225mm PCD',
            'Embrague upgrade: Exedy HD, Sachs racing',
            'Flywheel aligerado RSX Racing Solutions (2.8kg vs 6kg stock)',
            'Swap a caja Lancia — gears más cortos',
            'LSD options: RacingDiffs, Phantom Grip',
        ],
        'parent': '../reparaciones/',
    },
    'repuestos/ebay-global.md': {
        'title': 'eBay por país',
        'desc': 'USA · UK · Australia · Canadá · precios verificados cross-region · engines · rebuild kits · intake manifolds',
        'quote': 'eBay es el mercado más activo del modelo. Saber dónde buscar según qué pieza ahorra cientos de dólares.',
        'cite': 'EBAY · 4 MERCADOS GLOBALES',
        'intro': 'eBay tiene **el inventario más grande mundial** de repuestos Swift GTi, pero los precios y disponibilidad varían dramáticamente entre USA, UK, Australia y Canadá. Esta guía documenta qué buscar en cada mercado con precios verificados.',
        'stats': [('$1500', 'USD MIN · JDM ENGINE COMPLETE USA'), ('£180', 'UK · REBUILD KIT MÍNIMO'), ('AU$983', 'AUSTRALIA · ENGINE COMPLETO'), ('CAD$80', 'CANADÁ · PARTIAL KITS')],
        'teaser': [
            'eBay USA — mejor para engines completos JDM ($1500-3500)',
            'eBay UK — mejor para parts UK-spec + Dansts overstock',
            'eBay Australia — caro pero parts AU-spec exclusive',
            'eBay Canadá — ofertas dispersas, mejor para envío cross-border USA',
            'Comparativa rebuild kits 4 mercados',
            'Search terms tips (SF413 vs Cultus vs Forsa vs Swift GT)',
            'Saved searches recommendations',
            'Shipping costs reality check',
        ],
        'parent': '../repuestos/',
    },
    'repuestos/epc-online.md': {
        'title': 'Catálogos EPC online',
        'desc': 'PartSouq · Amayama · 7zap · Megazip · catálogos oficiales gratis · diagramas + part numbers',
        'quote': 'Antes de comprar cualquier repuesto, valida el part number en EPC. Toma 5 minutos y ahorra cientos en errores.',
        'cite': 'EPC · ELECTRONIC PARTS CATALOGS',
        'intro': 'Los **EPC (Electronic Parts Catalogs)** son los catálogos electrónicos oficiales de Suzuki que listan cada parte del auto con su diagrama, número de parte y compatibilidad. Hay 4 mirrors gratuitos navegables. Conocerlos es la diferencia entre comprar la pieza correcta o devolver tres.',
        'stats': [('4', 'EPC ONLINE GRATIS'), ('PARTSOUQ', 'MÁS COMPLETO · UAE'), ('AMAYAMA', 'STOCK REAL JDM JAPÓN'), ('7ZAP', 'OFFICIAL-STYLE INTERFACE')],
        'teaser': [
            'PartSouq.com — el más completo, navegable gratis',
            'Amayama.com — JDM con stock real Japan/UAE/Europa',
            'Megazip.net — diagramas + tienda online integrada',
            'Suzuki 7Zap — interface oficial-style',
            'Cómo identificar tu chasis (SF413-2 MK2, SF413-3 Magyar MK3)',
            'Cómo leer un diagrama EPC paso a paso',
            'Trucos para encontrar parts descontinuados',
            'Cross-reference entre mercados (USA vs JDM vs Europa)',
        ],
        'parent': '../repuestos/',
    },
    'repuestos/latam.md': {
        'title': 'LatAm marketplaces',
        'desc': 'MercadoLibre Colombia/Argentina/Chile/Ecuador · Facebook Twincam Bogotá · Forsa Ecuador · Mundo Repuestos Chile',
        'quote': 'En Latinoamérica el GTi se llamó Forsa. Los marketplaces locales tienen partes que no encuentras en USA — pero también la peor calidad de tracking.',
        'cite': 'LATAM · MERCADOLIBRE + FACEBOOK',
        'intro': 'En Latinoamérica el Swift GTi se vendió como **Forsa GTi** (Ecuador, Colombia, Centroamérica) o se importó del mercado USA. Los marketplaces locales tienen una mezcla de partes OEM heredadas + aftermarket económico. La guía documenta qué buscar y en quién confiar.',
        'stats': [('🇨🇴', 'COLOMBIA · PARTES VARIAS TWINCAM BOGOTÁ'), ('🇪🇨', 'ECUADOR · FORSA REPUESTOS QUITO'), ('🇦🇷', 'ARGENTINA · MERCADOLIBRE ACTIVO'), ('🇨🇱', 'CHILE · MUNDO REPUESTOS')],
        'teaser': [
            'MercadoLibre Colombia — repuestos Swift GTi (búsqueda)',
            'MercadoLibre Argentina — partes específicas Forsa',
            'MercadoLibre Chile — vendedores premium',
            'Mundo Repuestos Chile — Swift GTi dedicado',
            'Facebook: Partes Varias Suzuki Swift GTi Twincam (Bogotá) ⭐',
            'Facebook: Suzuki Forsa Ecuador repuestos (Quito)',
            'Suzuki Club El Salvador — foro + marketplace',
            'Tips: pago seguro + verificación vendedor + tracking',
        ],
        'parent': '../repuestos/',
    },
    'repuestos/vendedores-mundiales.md': {
        'title': 'Vendedores premium worldwide',
        'desc': 'CNC Innovations Malaysia · Dansts UK · Suzukird · RacingDiffs · Nengun Japan · 25+ tiendas especializadas',
        'quote': 'Cuando ya no estás buscando repuestos económicos sino piezas que el mecánico promedio nunca verá, estos vendedores son los que las tienen.',
        'cite': 'VENDEDORES PREMIUM · ESPECIALISTAS MUNDIALES',
        'intro': '25+ vendedores especializados worldwide que solo se dedican a Swift GTi / Cultus / Forsa / SF413. Throttle bodies billet, intake manifolds CNC, LSD premium, headers tubulares, JDM partes raras. La élite del ecosistema de repuestos.',
        'stats': [('25+', 'VENDEDORES PREMIUM'), ('CNC INN', 'MALAYSIA · BILLET MANIFOLDS'), ('DANSTS', 'UK · TBs + INTAKE'), ('NENGUN', 'JAPÓN · JDM DIRECTO 150 PAÍSES')],
        'teaser': [
            'Nengun Performance (Japón) — JDM directo, envío 150 países',
            'Dansts Engineering (UK) — throttle bodies + intake manifolds (£48-1250)',
            'CNC Innovations (Malaysia) — billet intake manifolds custom CNC',
            'Tegiwa Imports (UK) — Exedy clutches + performance parts',
            'Ozmotorsport (Australia) — part finder SF413 GTi dedicado',
            'SuzukiRD — LSD premium worldwide',
            'RacingDiffs (Polonia) — LSD plug-and-play 25% lock',
            'Suzuki Fort Motors (Pakistán) — mercado masivo Cultus',
            'NDEStore (Pakistán) — colección Cultus 3-cilindros',
        ],
        'parent': '../repuestos/',
    },
}


def build_page(filename, data):
    parent_link = f"[← Volver]({data['parent']})"
    stats_html = '\n'.join(
        f'<div class="gti-stat"><span class="num">{n}</span><span class="lbl">{l}</span></div>'
        for n, l in data['stats']
    )
    teaser_list = '\n'.join(f'- {item}' for item in data['teaser'])
    return f"""---
title: {data['title']}
description: {data['desc']}
---

# {data['title']}

<div class="gti-quote" markdown>
*{data['quote']}*

<cite>— {data['cite']}</cite>
</div>

{data['intro']}

<hr class="gti-rule">

## En cifras {{{{ #cifras }}}}

{stats_html}

<hr class="gti-rule">

## Lo que vivirá en esta página {{{{ #contenido }}}}

!!! info "Página en construcción activa"
    Esta sección se está documentando con investigación verificada por la comunidad. Lo que está confirmado por venir:

{teaser_list}

<hr class="gti-rule">

## Mientras tanto {{{{ #mientras-tanto }}}}

¿Tienes información para esta sección? Contribuir es la forma más rápida de que se complete.

[Enviar aporte por Telegram →](../comunidad/telegram.md){{ .md-button .md-button--primary }}
[Escribir al equipo →](../contacto.md){{ .md-button }}

{parent_link}
"""


def write_all():
    written = 0
    for filename, data in PAGES.items():
        path = BASE / filename
        if not path.exists():
            print(f"  SKIP (not exists): {filename}")
            continue
        path.write_text(build_page(filename, data), encoding='utf-8')
        written += 1
        print(f"  [OK] {filename}")
    print(f"\nTotal: {written} stub pages converted to editorial.")


if __name__ == '__main__':
    write_all()
