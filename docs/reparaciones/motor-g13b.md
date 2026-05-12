---
title: Motor G13B DOHC 16V
description: Especificaciones técnicas completas del Suzuki G13B — el motor que mantiene vivos a los Swift GTi 35 años después
---

# Motor G13B DOHC 16V

<div class="gti-quote" markdown>
El motor que no debería existir.

<cite>— BLUEPRINT · G13B · 1989-2003</cite>
</div>

El **G13B DOHC 16V** es la razón por la que estos autos siguen rodando 35 años después. Bloque, bielas y pistones forjados de fábrica. Cabezal pentroof inspirado en el Ford RS1600 BDA. Ajustadores hidráulicos automáticos. Y una redline de fábrica que ningún ingeniero conservador habría firmado para un subcompacto de 680 kg.

<hr class="gti-rule">

## Especificación rápida {#especificaciones}

<div class="gti-stat"><span class="num">1,298</span><span class="lbl">CC · CILINDRADA</span></div>
<div class="gti-stat"><span class="num">16V</span><span class="lbl">DOHC</span></div>
<div class="gti-stat"><span class="num">9,000</span><span class="lbl">RPM · LÍMITE INTERNALS STOCK</span></div>
<div class="gti-stat"><span class="num">376</span><span class="lbl">WHP · MÁXIMO DOCUMENTADO TURBO</span></div>

| Parámetro | Valor |
|---|---|
| Bloque | Aluminio fundido · 288 mm largo |
| Diámetro × Carrera | 74.0 × 75.5 mm |
| Disposición | Inline-4, transverse FWD |
| Cabezal | Aluminio · DOHC · 16V · pentroof |
| Distribución | Correa dentada (timing belt) · 2 árboles |
| Ajustadores válvula | Hidráulicos automáticos (HLA) |
| Bielas | Forjadas OEM (todas las versiones) |
| Pistones | Forjados OEM (todas las versiones N/A) |
| Inyección | Multi-Point Fuel Injection (MPI) |
| Encendido | DLI distribuidor electrónico · CAS |

<hr class="gti-rule">

## Tres etapas del G13B {#etapas}

### 01 · Stock export

**101 PS / 113 N·m** · Mercados Europa, Australia, USA (Swift GT), Canadá.

| Spec | Valor |
|---|---|
| Compresión | 10.0:1 |
| Headers | Manifold fundido |
| Cams | Standard duration / lift |
| ECU | Suzuki OEM no recalibrada |
| RPM peak | 6,500 |
| Redline | 7,500 |
| Restricción | Catalizador + airbox cerrado |

> Esta es la versión más común fuera de Japón. La que probablemente tienes en el garaje si vives en LatAm, USA o Europa.

### 02 · JDM Cultus GTi

**115 PS JIS / 110 N·m @ 6,500 rpm** · Solo mercado japonés (AA34S / AB34S / AF34S 4WD).

| Spec | Valor |
|---|---|
| Compresión | **11.5:1** (vs 10.0 export) |
| Headers | Tubulares de fábrica 4-2-1 |
| Cams | Duración mayor, lift agresivo |
| ECU | Recalibrada para 95 RON gasolina japonesa |
| RPM peak | 6,800 |
| Redline | 7,500 |
| Restricción | Mínima — gentlemen's agreement japonés 280 PS irrelevante |

> La rareza absoluta es la variante **AF34S** — Cultus GTi 4WD con el mismo G13B JDM acoplado a transmisión integral. Producción mínima 1990-1994.

### 03 · Turbo build

**200–376 whp documentados** · Internals forjados de fábrica permiten compresión bajada + turbo significativo sin re-build.

| Spec | Rango común |
|---|---|
| Compresión (forzada) | **8.5:1 forjada** custom |
| Turbo | TD04 (200-260 whp) · T2871 (300-376 whp) |
| Boost | 10–25 psi (según target) |
| Inyectores | 550-1000 cc/min |
| ECU | Standalone Megasquirt o Haltech |
| Fuel | Gasolina premium + meth injection o E85 |
| Redline operativa | 8,000-8,500 rpm |

<div class="gti-quote" markdown>
Soporta *9,000 rpm* con internals stock. Máximo documentado: *376 whp*.

<cite>— DYNO RUN · TEAMSWIFT FORUM · 2019</cite>
</div>

<hr class="gti-rule">

## Por qué este motor sobrevive {#por-que-sobrevive}

El G13B fue diseñado por Suzuki con sobre-ingeniería deliberada: el equipo de motores compartía pasillo con los de moto deportiva, donde la confiabilidad a alto RPM es regla. Los componentes forjados de fábrica que Suzuki nunca documentó como tales son:

- **Bielas forjadas** — todas las versiones, incluyendo Stock export
- **Cigüeñal forjado** — soporta hasta ~500 hp con buena lubricación
- **Pistones forjados** N/A — solo el turbo OEM (que nunca existió de fábrica para G13B) habría usado cast

Resultado: un motor 1.3L que tolera abuso que motores 2.0L modernos no aguantan.

<hr class="gti-rule">

## Torques de apriete críticos {#torques}

| Componente | Torque | Notas |
|---|---|---|
| Tornillos cabeza · Step 1 | 22 ft-lb | 30 N·m secuencia FSM |
| Tornillos cabeza · Step 2 | + 80° | Angle method |
| Pernos main bearing cap | 36 ft-lb | 49 N·m |
| Pernos biela | 26 ft-lb | 35 N·m |
| Polea cigüeñal | 80 ft-lb | 108 N·m |
| Bujías | 18 ft-lb | 25 N·m · NGK BKR6E |
| Cárter cabeza (valve cover) | 4 ft-lb | 5 N·m · no excederse |
| Sensor de aceite | 12 ft-lb | 16 N·m |
| Bobina ignición DLI | 8 ft-lb | 10 N·m |

> Secuencia de torque cabeza: ver [Manual SF413 §6A-12](../manuales/sf413-gti.md). Siempre 2 pasos + ángulo final.

<hr class="gti-rule">

## Problemas comunes documentados {#problemas-comunes}

### Empaque de cabeza
**Síntoma:** sobrecalentamiento + aceite lechoso. **Causa raíz:** años + ciclos térmicos. **Fix:** reemplazo + retorque a 100, 500 y 1500 km.

### Distribuidor CAS (Crank Angle Sensor)
**Síntoma:** misfire intermitente, ralentí irregular. **Fix:** [TSB Suzuki G13B Engine Adjustments](../manuales/tsb.md) detalla el gap correcto del CAS.

### Cadena timing belt
**Síntoma:** ninguno — y eso es el problema. **Fix:** cambio preventivo cada 80,000 km o 5 años. Romper = válvulas chocan pistón = motor muerto.

### TPS (Throttle Position Sensor)
**Síntoma:** ralentí errático, hesitación al acelerar. **Fix:** calibración con ohmímetro según FSM §6E-23.

<hr class="gti-rule">

## Recursos relacionados

- [Manual SF413 GTi Service](../manuales/sf413-gti.md) — sección 6A motor completo
- [TSB G13B Engine Adjustments](../manuales/tsb.md) — ajustes de fábrica documentados
- [Modificaciones N/A (aspirado)](../modificaciones/aspirado.md) — bolt-on hasta 165 hp
- [Turbo builds](../modificaciones/turbo.md) — TD04/T2871 hasta 376 whp
- [Engine swaps](../modificaciones/engine-swaps.md) — M16A, K20, EJ20 conversiones

[← Volver al índice de Reparaciones](index.md)
