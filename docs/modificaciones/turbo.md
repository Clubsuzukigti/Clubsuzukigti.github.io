---
title: Turbo builds
description: De 200 hp en internals stock hasta 376 whp documentados · TD04 · T2871 · Masterpower
---

# Turbo builds

<div class="gti-quote" markdown>
*El G13B turbocargado es el secreto mejor guardado del JDM. 376 whp documentados con un motor de 1.3 litros de 1989.*

<cite>— RÉCORDS DE LA COMUNIDAD</cite>
</div>

El G13B turbocargado lleva el motor a territorio que Suzuki nunca imaginó. Internals forjados de fábrica permiten boost agresivo sin reconstruir el bloque hasta cierto punto. Más allá, comienza el territorio de pistones forjados, head studs ARP y ECU standalone.

<hr class="gti-rule">

## Niveles de potencia documentados {#niveles}

<div class="gti-stat"><span class="num">200</span><span class="lbl">HP · INTERNALS STOCK · 10 PSI</span></div>
<div class="gti-stat"><span class="num">290</span><span class="lbl">HP · SWAP RWD SUECIA</span></div>
<div class="gti-stat"><span class="num">355</span><span class="lbl">HP · DYNO @ 25.7 PSI · GT2871R</span></div>
<div class="gti-stat"><span class="num">376</span><span class="lbl">WHP · MÁXIMO DOCUMENTADO YOUTUBE</span></div>

<hr class="gti-rule">

## Builds turbo documentados {#builds}

| Build | Potencia | Setup | Fuente |
|---|---|---|---|
| Argentina foroswift 6-year build | **206 hp dyno** | Masterpower R4449-2, MS2 v3, NPR Vitara 75mm, CR 8.5:1 | foroswift.com.ar |
| Suecia RWD swap | **290 hp / 11.8s 1/4 @ 120mph** | Knife-edge crank, Pauter rods, Venolia 8.5:1 | Engine Swap Depot |
| Build extremo dyno | **355 hp @ 8100rpm** | GT2871R @ 25.7 psi, Megasquirt | TeamSwift archive |
| ⭐ YouTube récord live | **376 whp** | G13B turbo dyno test documentado | YouTube live record |
| Autoculture balanced build | **176 BHP** | Balanced G13B turbo | Autoculture video |

<hr class="gti-rule">

## Niveles de boost según internals {#boost-levels}

| PSI | hp esperado | Internals necesarios |
|---|---|---|
| Hasta 10 | 130-180 | **Stock OK** (sin cambiar gasket ni timing) |
| 10-15 | 200-250 | Pistones bajo CR (G16 Vitara bore +0.40 a 75mm, CR 8.8:1), bielas forjadas |
| 15+ | 250-300+ | ECU standalone obligatorio, bielas forjadas Pauter, head gasket reforzado |
| 300+ | 300-400 | Pistones forjados baja CR, head gasket caro, ECU programable, head studs ARP |

<hr class="gti-rule">

## Setups turbo comunes {#setups}

### Entrada — TD04 (10-12 psi)
- Turbo: TD04L de Subaru Legacy/Forester (~$200-400 usado)
- Manifold: tubular custom o adaptado de SR20DET
- Intercooler: front-mount 22"×6"×2.5" económico
- Inyectores: 380-440 cc/min
- ECU: Megasquirt MS2 v3 o piggyback
- Potencia esperada: **200-230 hp**

### Intermedio — Garrett T2871R (15-18 psi)
- Turbo: GT2871R-52 trim
- Manifold: tubular Schedule 40 ó cast iron
- Intercooler: 24"×7"×3" tube-and-fin
- Inyectores: 550-720 cc/min
- ECU: Haltech Sprint o Megasquirt MS3X
- Pistones: forjados Wiseco 74.5mm @ 8.5:1
- Bielas: Pauter forjadas + ARP rod bolts
- Potencia esperada: **280-330 whp**

### Tope — GT2871R @ 25+ psi
- Turbo: GT2871R-56 trim
- Manifold: stainless 304 schedule 10 con wastegate externa
- Wastegate: Tial 38mm
- Intercooler: bar-and-plate 28"×7"×3.5"
- Inyectores: 1000 cc/min siemens deka
- Fuel: bomba Walbro 450 + AEM regulator
- ECU: Haltech Elite 1500
- Head studs ARP
- Potencia esperada: **350-376 whp**

<hr class="gti-rule">

## Reglas de oro del G13B turbo {#reglas}

1. ⛔ **10 PSI MAX en internals stock** — sobre eso, forjar pistones de baja CR.
2. ⛔ **Conservar el distribuidor en builds >250 hp es un riesgo** — convertir a coil-on-plug elimina el punto débil del CAS interno.
3. ✅ **Bore +1mm con pistones G16 Vitara** = 1300→1400cc económicamente.
4. ⛔ **Nunca usar head gasket Felpro stock** sobre 15 psi — buscar Cometic MLS o ARP head studs.
5. ✅ **Aceite 10W-40 sintético mínimo** — los bearings sufren con boost.
6. ⛔ **Detonación en G13B con 11.5:1 JDM** es la causa #1 de pistón fundido — bajar CR antes de cualquier turbo serio.
7. ✅ **Wideband O2 obligatorio** — tunear con narrowband es jugar a la ruleta.

<hr class="gti-rule">

## Recursos {#recursos}

- [Modificaciones aspirado (N/A)](aspirado.md) — base antes del turbo
- [Engine swaps](engine-swaps.md) — alternativa al turbo: motor moderno
- [ECU standalone](ecu.md) — Megasquirt, Haltech, AEM
- [Foroswift Argentina](https://www.foroswift.com.ar/) — sección Preparación-Potenciación con 471 temas
- [TeamSwift Archive](https://tsarchive.suzukiswiftrepository.com/) — builds históricos

[← Volver al índice de modificaciones](index.md)
