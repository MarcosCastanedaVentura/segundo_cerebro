---
titulo: "Métodos de posicionamiento GNSS (absoluto, diferencial, RTK, PPP, estático)"
asignatura: "geomatica"
tema: "Tema 4 - GNSS"
tipo: "procedimiento"
relacionado: ["fundamentos-gnss", "gnss-errores-precision", "practica-6-gnss"]
patrones_error: [3, 7]
examen_relevancia: "alta"
fuente: ["Tema 4_GNSS.pdf", "Practicas geomatica/Práctica_6.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Existen varios métodos para obtener una posición con GNSS, y cada uno ofrece una precisión radicalmente
distinta según use medidas de **código** (bastas) o de **fase de la portadora** (precisas), y según use uno o
varios receptores simultáneos.

- **Posicionamiento absoluto (1 receptor, código)**: SPS con código C/A → del orden de 4-100 m. Es el modo
  navegación de cualquier smartphone.
- **DGPS/DGNSS (2+ receptores, código diferencial)**: una base conocida corrige en tiempo real los errores
  comunes → ~50 cm.
- **RTK (Real-Time Kinematic, 2+ receptores, fase)**: usa la fase de la portadora con correcciones en tiempo
  real desde una base o red de estaciones → precisión centimétrica (2 cm + 2 ppm).
- **PPP (Precise Point Positioning, 1 receptor, fase)**: no necesita base local; usa efemérides y correcciones
  de reloj ultraprecisas globales (post-proceso o en tiempo real) → ~1 cm, aunque normalmente requiere tiempos
  de observación más largos que el RTK.
- **Estático / estático rápido (2+ receptores, fase, postproceso)**: observación prolongada con procesado
  posterior → 5 mm + 1 ppm.
- **Estático continuo (CORS, 2+ receptores, fase)**: estaciones permanentes → 2 mm + 1 ppm, la máxima
  precisión alcanzable.

## Por qué / de dónde viene

La clave física es qué se mide: el **código** (C/A, P) es una secuencia repetitiva que el receptor correla con
la que genera él mismo; el desfase temporal de esa correlación da la pseudodistancia, pero con una resolución
limitada por la longitud de onda "efectiva" del código. La **fase de la portadora** (la onda L1/L2 en sí) tiene
una longitud de onda de centímetros, por lo que medir su fase con precisión sub-milimétrica multiplica la
resolución angular en varios órdenes de magnitud — a cambio, hay que resolver la "ambigüedad de fase" (cuántos
ciclos enteros de onda hay entre satélite y receptor), lo que exige tiempo de observación o algoritmos de
resolución rápida (RTK).

El **modo diferencial** funciona porque los errores del satélite (efemérides, reloj, ionosfera, troposfera)
afectan casi por igual a dos receptores relativamente próximos: al restar las medidas de ambos, esos errores
comunes se cancelan. Esta cancelación se degrada con la distancia entre receptores (la "baselínea"): el error
diferencial residual es aproximadamente `Error_Orbital / 20.000 km × Distancia_Vector`, porque más lejos, más
diferente es el camino que recorre la señal a través de la atmósfera hacia cada receptor.

## Fórmula / procedimiento

Escala de precisión (código naranja, fase azul):

| Método | Receptores | Observable | Precisión típica |
|---|---|---|---|
| SPS código C/A | 1 | Código | 4-10 m |
| PPS código P(Y) | 1 | Código | ~1 m |
| PPP | 1 | Fase | ~10 mm (pero requiere post-proceso o convergencia) |
| DGPS | 2+ | Código diferencial | ~50 cm |
| RTK / VRS / cinemático | 2+ | Fase | 20 mm + 2 ppm |
| Estático rápido | 2+ | Fase | 5 mm + 1 ppm |
| Estático continuo (CORS) | 2+ | Fase | 2 mm + 1 ppm |

Regla general: la incertidumbre altimétrica (Z) es aproximadamente 1,5 veces mayor que la planimétrica (X, Y),
y hasta 2,5 veces en PPP, porque geométricamente hay menos satélites visibles por debajo del horizonte que
alrededor, lo que debilita la componente vertical (VDOP > HDOP, ver [[gnss-errores-precision]]).

Elección del método óptimo (según el material, "no existe un método GNSS perfecto, solo el óptimo para las
restricciones del proyecto"): depende de (1) precisión requerida, (2) si se necesita el dato en tiempo real o
vale postproceso, (3) equipo disponible (código vs código+fase), (4) coste/logística.

## Ejemplo resuelto

En la Práctica 6 se comparó un receptor Trimble TDC100 (SBAS, precisión métrica: <1,5 m típico en tiempo real)
frente a un Leica Zeno FLX100 (RTK, 2-3 cm en tiempo real). Al levantar el mismo punto ("Pilar") con ambos
equipos, la diferencia de coordenadas fue de -0,005 m en X y -0,006 m en Y — coherente con que el Zeno RTK es
muchísimo más preciso que el Trimble basado en corrección SBAS/EGNOS. Esto ilustra por qué, para deslinde de
parcelas agrícolas o replanteo, se exige RTK y no un GPS de navegación.

## Conexión con otros conceptos

- [[fundamentos-gnss]] — segmentos y observables sobre los que se construyen estos métodos.
- [[gnss-errores-precision]] — por qué cada método tiene ese techo de precisión (DOP, UERE).
- [[practica-6-gnss]] — comparación real Trimble vs Zeno en campo.
- [[../vegetales/MOC]] — el RTK es el estándar en agricultura de precisión (guiado de tractores, mapas de
  aplicación a dosis variable) porque combina precisión centimétrica con tiempo real.

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmulas sin verificar las condiciones de uso)**: este es el concepto con más riesgo de
activar este patrón en Geomática. Hay 6-7 métodos con precisiones que difieren en órdenes de magnitud (de 100 m
a 2 mm): antes de responder "¿qué precisión tiene este método?" hay que identificar primero si es código o
fase, y si es 1 receptor o 2+, exactamente igual que en Electrotecnia había que identificar triángulo vs
estrella antes de aplicar la fórmula.

**Patrón 7 (dar por bueno algo que "suena razonable")**: si un resultado da, por ejemplo, "3 metros de precisión
para un RTK", hay que desconfiar inmediatamente — el orden de magnitud correcto es centimétrico, no métrico.
Verificar siempre el orden de magnitud esperado según la tabla anterior.

## Relevancia en examen

Alta. Tema 4, P1 (ventaja del RTK: fase + corrección en tiempo real → precisión centimétrica), P4 (PPP no
requiere base local, usa efemérides y correcciones de reloj ultraprecisas), P5 (pregunta directa de "indica la
más precisa" entre varias opciones — clásica trampa de Patrón 7).
