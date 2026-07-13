---
titulo: "Remolacha azucarera: VTIR, fábrica azucarera y OCM del azúcar"
asignatura: "vegetales"
tema: "UT5 - Cultivos azucareros y de tubérculo"
tipo: "concepto"
relacionado: ["agua-en-sistemas-agricolas", "patata", "cereales", "../geomatica/MOC"]
patrones_error: [3, 6, 7]
examen_relevancia: "alta"
fuente: ["raw/.../vegetales/Tema 10.- Remolacha azucarera 2025.pdf", "raw/.../vegetales/apuntes_claude/vegetales_guia_v2.docx", "raw/.../vegetales/apuntes_claude/vegetales_guia_bloques.docx (veg_guide.js)", "raw/.../vegetales/Actividad práctica remolacha 2024 (resolución).xlsx (pendiente de procesar, ver MOC)"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La remolacha azucarera (*Beta vulgaris* var. *saccharifera*, Quenopodiáceas) se cultiva por su raíz engrosada, de la que se extrae **sacarosa** (~22% de la producción mundial de azúcar; el 78% restante viene de la caña). Es planta **bienal**: en el primer año (el que interesa al agricultor) crece vegetativamente acumulando sacarosa en la raíz; si se dejara un segundo año, con vernalización + días largos, alargaría el tallo y florecería (indeseable — "espigado" o subida a flor, uno de los objetivos de mejora genética es evitarlo). En España el cultivo se ha reducido drásticamente desde la reforma de la OCM del azúcar de 2006 (de ~160.000 ha en los 90 a 100-120.000 ha después), aunque el rendimiento por ha ha aumentado constantemente.

## Por qué / de dónde viene

**Morfología de la raíz**: pivotante y profunda; el engrosamiento se produce por anillos concéntricos sucesivos de cámbium (7-8 anillos) que alternan xilema/floema con parénquima — es la raíz, no el tallo, el órgano de almacenamiento (a diferencia de la patata, donde el tubérculo es un tallo).

**Ciclo y componentes del rendimiento**: primera mitad del ciclo predomina el crecimiento de la parte aérea (hojas, LAI), segunda mitad predomina el crecimiento de la raíz de almacenamiento. El rendimiento en azúcar depende de: (1) producción de raíz (densidad de planta × peso unitario, que a su vez depende de la radiación PAR interceptada y de la eficiencia en su uso, EUR/RUE) y (2) contenido de sacarosa en la raíz (polarización), que depende de factores genéticos, ambientales (temperatura nocturna baja y déficit de N la favorecen), y de manejo.

**Calidad industrial — VTIR (Valor Tecnológico Industrial de la Raíz)**: no basta con el contenido de sacarosa (polarización); las **impurezas** de la raíz (sodio, potasio, azúcares reductores, nitrógeno alfa-amino) reducen el azúcar recuperable en fábrica. La fórmula oficial completa es más compleja que una simple resta (se calcula vía el Rendimiento Industrial ó Índice de Calidad Industrial: RTOIN = (POL − AMr − 0,7)/POL × 100, donde AMr son las pérdidas de azúcar estimadas en melazas a partir de K, Na, azúcares reductores y N alfa-amino) — **la guía previa de apuntes_claude simplificaba esto a una fórmula lineal aproximada (VTIR = Polarización − 0,29×(K+Na) − 0,4×N amino − 0,6); esa versión es una aproximación pedagógica, no la fórmula oficial del sector, que usa las relaciones de Dévillers/AIMCRA descritas arriba** — para el examen basta con saber **qué variables entran** (polarización + Na, K, azúcares reductores, N alfa-amino) y el sentido del efecto (a más impurezas, menos rendimiento industrial), no reproducir la fórmula completa de memoria.

**Efecto del nitrógeno**: dosis excesiva → mayor crecimiento de la parte aérea pero **menor polarización** (menos azúcar) y mayor N alfa-amino y sodio (peor calidad industrial); dosis deficitaria → también reduce la calidad industrial. Hay una dosis óptima intermedia.

**OCM del azúcar**: muy regulada hasta la reforma de 2006 (cuotas de producción por país/empresa/agricultor, precios mínimos). La reforma de 2006 redujo drásticamente precios y cuotas de producción en la UE (de 19-20 Mt a 13-16 Mt) para acercarlos a precios mundiales, con pagos desacoplados de compensación — consecuencia directa: fuerte caída de la superficie de remolacha en España.

## Fórmula / procedimiento

- Azúcar envasado (t) = t raíz/ha × ha × polarización(%) × VTIR(%) / 10.000 (fórmula simplificada de examen).
- Proceso de fábrica: recepción/lavado → corte en cosetas → difusión (extracción con agua caliente) → purificación con cal + CO₂ (carbonatación) → filtración → evaporación (jarabe 40-70% sacarosa) → cristalización → centrifugación (separa azúcar de melaza) → secado/envasado.
- Subproductos: **melaza** (azúcar no cristalizado, para fermentación/pienso), **pulpa** (cosetas agotadas, alta fibra, pienso), **espuma de cal/carbonato cálcico** (enmienda agrícola).
- Fertilización N: se puede estimar por el **método del N-min**: Necesidades (kg N/ha) = 310 − 6×N-nítrico(mg/kg) − 70×MO(%).

## Ejemplo resuelto

Fábrica con 6.000 ha, 110 t raíz/ha, polarización 16%, VTIR 95%: t raíz totales = 6.000 × 110 = 660.000 t; azúcar = 660.000 × 0,16 × 0,95 = **100.320 t de azúcar** (los outputs de la fábrica no son solo azúcar: también melaza y pulpa).

## Conexión con otros conceptos

- El balance hídrico y el papel del LAI/PAR/EUR en la formación de biomasa (raíz y aérea) son los mismos conceptos de [[agua-en-sistemas-agricolas]] y [[cereales]] — de hecho las diapositivas de Tema 1 usan la remolacha como ejemplo numérico recurrente de esas fórmulas.
- Comparte unidad temática (UT5) con [[patata]]: ambos son "cultivos de raíz/tubérculo" con lógica de rendimiento por componentes similar, pero la remolacha SÍ tiene OCM (desde 1968, reformada en 2006) y la patata de consumo NO.
- Ejemplo destacado en el material oficial de uso de teledetección (NDVI, TCARI/OSAVI, dron/satélite) para diagnóstico nitrogenado y de estrés hídrico en campo (plataforma "Layers" de Hemav/Azucarera) — conexión directa con [[../geomatica/MOC]].

## Errores frecuentes de Marcos aquí

- **Patrón 3**: usar la fórmula simplificada del VTIR sin verificar que en el examen puede pedirse solo el razonamiento conceptual (qué variables influyen y en qué sentido) en vez de un cálculo numérico exacto — no todas las fórmulas "de la guía" son las oficiales del sector.
- **Patrón 6**: en el cálculo de azúcar envasado, olvidar convertir correctamente ha→t de raíz antes de aplicar los porcentajes, o confundir polarización con VTIR (son magnitudes relacionadas pero no intercambiables: VTIR ya descuenta impurezas, polarización es solo el % de sacarosa bruto).
- **Patrón 7**: dar por bueno un resultado de azúcar/ha que no se valida contra el orden de magnitud esperado (~10-20 t azúcar/ha es razonable; si sale 100 t/ha algo está mal en las unidades).

## Relevancia en examen

Alta — UT5 se examina junto con Patata. Preguntas típicas: qué variables componen el VTIR (sacarosa+Na+K+N alfa-amino, NO fósforo), efecto del N excesivo/deficitario sobre polarización y calidad, subproductos de la fábrica (melaza y pulpa, no solo azúcar), y un ejercicio numérico de cálculo de azúcar/ha o de eficiencia en el uso de N/agua a partir de datos de ensayo (frecuentemente con formato de pregunta de opción múltiple con cálculo integrado, como en el examen de junio 2025).
