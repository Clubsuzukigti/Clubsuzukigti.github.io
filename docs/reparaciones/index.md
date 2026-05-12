---
title: Reparaciones
description: Guías de reparación basadas en manual SF413 oficial + TSBs Suzuki + experiencia acumulada del club
---

# Reparaciones

<div class="gti-quote" markdown>
Los autos se rompen. El conocimiento de cómo arreglarlos también — si nadie lo escribe.

<cite>— ARCHIVO DEL TALLER · CLUB SUZUKI GTi</cite>
</div>

Guías de reparación y mantenimiento basadas en el manual oficial Suzuki SF413, los TSBs (Technical Service Bulletins) oficiales y la experiencia acumulada del club durante 8 años manteniendo vivos a estos autos.

!!! warning "Lee primero"
    Trabajar en un Swift GTi requiere herramientas básicas + paciencia. Estas guías son referencia, no reemplazan el criterio del mecánico. Ante duda crítica (frenos, seguridad), consulta a un profesional.

<hr class="gti-rule">

## El taller en números {#cifras}

<div class="gti-stat"><span class="num">10</span><span class="lbl">PROBLEMAS COMUNES DOCUMENTADOS</span></div>
<div class="gti-stat"><span class="num">5</span><span class="lbl">SISTEMAS · MOTOR · ELÉCTRICO · TRANS · FRENOS · CARROCERÍA</span></div>
<div class="gti-stat"><span class="num">9</span><span class="lbl">TORQUES CRÍTICOS DOCUMENTADOS</span></div>
<div class="gti-stat"><span class="num">9</span><span class="lbl">CÓDIGOS DIAGNÓSTICO ECM</span></div>

<hr class="gti-rule">

## Por sistema {#sistemas}

<div class="card-grid" markdown>

<div class="card" markdown>
### 🔧 [Motor G13B][motor-g13b]
Empaque cabezal, distribuidor + CAS sensor, timing belt + bomba de agua, presión de aceite, compresión, vacío del motor.

[motor-g13b]: motor-g13b.md
</div>

<div class="card" markdown>
### ⚡ [Sistema eléctrico][electrico]
ECM y códigos de diagnóstico, TPS, AFM hot-wire, sensores WTS / oxígeno, bobinas, arnés, fusibleras (interna + externa).

[electrico]: electrico.md
</div>

<div class="card" markdown>
### ⚙ [Transmisión][transmision]
Crunch en 2da/3ra (synchros), aceite GL-4 obligatorio, embrague Exedy/Sachs, volante aligerado, swap caja Lancia.

[transmision]: transmision.md
</div>

<div class="card" markdown>
### 🛑 [Frenos y suspensión][frenos]
Pastillas DOT 3, mangueras, bujes control arms, tie rods, ball joints, coilovers BC Racing, big brake kits.

[frenos]: frenos-suspension.md
</div>

<div class="card" markdown>
### 🪛 [Carrocería y óxido][carroceria]
Puntos críticos de óxido (rocker panels, floor pans, control arm mounts), reparación de huecos, prevención.

[carroceria]: carroceria.md
</div>

</div>

<hr class="gti-rule">

## Especificaciones rápidas — TSB Oficial Suzuki G13B {#tsb}

### Tiempo de encendido
**12° ± 6° BTDC @ 800 rpm** en ralentí (DOHC G13B GTi)

### CAS (Pick-up Coil Air Gap)
**0.20 - 0.30 mm** (0.008 - 0.012 in)

### Holgura de válvulas
**No requiere ajuste** — ajustadores hidráulicos automáticos

### Velocidad ralentí
- A/C OFF: 800-900 rpm (manual) / 700-800 rpm (auto)
- A/C ON: 950-1050 rpm / 800-950 rpm

### Aceite motor
**3.6 L total** · API SF o SF/CC · **SAE 5W-30** recomendado (especialmente <0°C)

### Bujías
**NGK BPR6ES** (BP6ES) o **NIPPON DENSO W20EPR-U**  
Gap **0.7-0.8 mm** · Torque **25-30 N·m**

### Refrigerante
**50/50** agua + glicol etilénico · Presión radiador 0.9 kg/cm²

### Líquido de frenos
**DOT 3 o SAE J1703** — nunca mezclar con otros tipos

### Transmisión manual
**Aceite GL-4 ONLY** — GL-5 destruye los synchros con sus aditivos sulfurosos

<hr class="gti-rule">

## Torques de apriete principales {#torques}

| Componente | N·m | lb-ft |
|---|---|---|
| **Pernos de culata** | 65-70 | 47.5-50.5 |
| **Pernos cojinete principal** | 50-57 | 36.5-41.0 |
| **Tuerca tapa biela** | 33-37 | 24.0-26.5 |
| **Polea cigüeñal (timing belt)** | 105-115 | 76.0-83.0 |
| Polea árbol de levas | 56-64 | 41.0-46.0 |
| **Bujías** | 25-30 | 18.0-21.5 |
| **Volante** | 57-65 | 41.5-47.0 |
| **Tapón de drenaje aceite** | 30-40 | 22.0-28.5 |
| Tuerca tubo de escape | 40-60 | 29.0-43.0 |

[Tabla completa de torques →](motor-g13b.md#torques)

<hr class="gti-rule">

## Códigos de diagnóstico ECM {#diagnostico}

| Código | Sistema | Probable falla |
|---|---|---|
| 12 | Normal | OK (ningún otro código) |
| 13 | Sensor O2 | Sensor oxígeno (lambda) |
| 14, 15 | WTS | Sensor temperatura agua |
| 21, 22 | TPS | Sensor posición acelerador |
| 24 | VSS | Sensor velocidad |
| 33, 34 | AFM | Medidor flujo de aire |
| 41 | Encendido | Sin señal ignición |
| 42 | CAS | Sin señal sensor ángulo cigüeñal |
| ON continuo | ECM | Falla interna ECM |

<hr class="gti-rule">

## Top 10 problemas más frecuentes en el club {#top-10}

1. **Crunch en 2da/3ra** → Synchros desgastados (cambiar + usar GL-4)
2. **No arranca / no chispa** → CAS sensor en distribuidor (entrehierro 0.2-0.3mm)
3. **Pierde fuerza después de calentar** → MAP sensor pasaje tapado
4. **Idle oscilatorio** → ISC valve atascada (limpiar con carb cleaner)
5. **Aceite en bujías** → Empaque cabezal (revisar sistema refrigeración primero)
6. **Codigo P0302 (cilindro 2 misfire)** → Bujía / bobina / cable HT
7. **Códigos 13/14/15 (sensores)** → Limpiar conectores + verificar WTS/O2 resistencias
8. **Óxido en rocker panels** → Limpieza skirts laterales + tratamiento anti-óxido
9. **Bomba de agua falla con timing belt** → SIEMPRE cambiar juntos cada 100K km
10. **Distribuidor rotor agrietado** → Reemplazar con OEM (los aftermarket sin index spring son trampa)
