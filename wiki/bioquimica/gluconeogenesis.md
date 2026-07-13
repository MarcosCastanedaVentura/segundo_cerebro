---
titulo: "Gluconeogénesis: síntesis de glucosa y regulación recíproca con la glucólisis"
asignatura: "bioquimica"
tema: "Tema 4 - Metabolismo de glúcidos"
tipo: "procedimiento"
relacionado: ["glucolisis", "ciclo-alanina-glucosa-cahill", "metabolismo-lipidos-beta-oxidacion", "regulacion-enzimatica-alosterica"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Tema 4 -Met de Glucidos.pdf", "Problemas de Metabolismo 2.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La gluconeogénesis (glykos=dulce, neo=de nuevo, genesis=síntesis) es la síntesis de glucosa a partir de
precursores no glucídicos: lactato, aminoácidos (excepto Leu y Lys), glicerol e intermediarios del ciclo de
Krebs. Ocurre principalmente en el hígado (90%) y en menor medida en la corteza renal (10%), en el citosol
(aunque el primer paso empieza en la mitocondria).

## Por qué / de dónde viene

El cerebro adulto consume ~120 g de glucosa/día y el organismo completo ~160 g/día, pero las reservas de
glucógeno solo cubren ~190 g — apenas un día de ayuno. Por eso, pasado ese margen (ayuno prolongado, ejercicio
intenso), el organismo necesita fabricar glucosa de novo. No es la simple inversión de la glucólisis: los 3
pasos irreversibles de la glucólisis (hexoquinasa, PFK-1, piruvato quinasa, cada uno con ΔG0' muy negativo)
no se pueden revertir con el mismo enzima, así que la gluconeogénesis los rodea con 3 enzimas distintos,
gastando más energía de la que se recuperaría si simplemente se invirtiera la glucólisis. Este gasto extra
(4 ATP + 2 GTP por glucosa, frente a los 2 ATP que se ganarían si la glucólisis fuera reversible sin más) es
lo que garantiza que la ruta global sea irreversible en el sentido de síntesis y no se cicle inútilmente con
la glucólisis (ciclo fútil).

## Fórmula / procedimiento

**Los 3 rodeos de la gluconeogénesis (sustituyen a los 3 pasos irreversibles de la glucólisis):**

1. Piruvato → Oxalacetato (piruvato carboxilasa, matriz mitocondrial, ATP-dependiente, biotina como
   coenzima, enzima alostérico activado por acetil-CoA) → Oxalacetato → Fosfoenolpiruvato (PEP
   carboxiquinasa, citosol, GTP-dependiente, reversible). Sustituye a la piruvato quinasa.
2. Fructosa-1,6-bisfosfato → Fructosa-6-fosfato (fructosa-1,6-bisfosfatasa, hidrólisis, enzima alostérico).
   Sustituye a la PFK-1.
3. Glucosa-6-fosfato → Glucosa (glucosa-6-fosfatasa, retículo endoplasmático de hígado y riñón — el cerebro y
   el músculo esquelético carecen de este enzima, por eso **no pueden liberar glucosa a la sangre** aunque
   hagan glucogenólisis). Sustituye a la hexoquinasa/glucoquinasa.

**Balance global**: 2 Piruvato + 4 ATP + 2 GTP + 2 NADH + 6 H₂O → Glucosa + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺ + 2
H⁺ (ΔG' = −9 kcal/mol). Si la glucólisis pudiera revertirse literalmente sin cambiar de enzima, costaría solo
2 ATP + 2 NADH y tendría ΔG' = +20 kcal/mol (no espontánea) — el gasto extra de 2 ATP+2GTP es precisamente el
coste de hacerla espontánea.

**Regulación recíproca glucólisis/gluconeogénesis** — dos reguladores clave:
- Acetil-CoA: activa piruvato carboxilasa (gluconeogénesis) e inhibe piruvato quinasa (glucólisis).
- Carga energética (ATP/ADP): carga baja → activa glucólisis, inhibe gluconeogénesis (y viceversa).
- Fructosa-2,6-bisfosfato (controlada por insulina/glucagón vía PFK-2): activa PFK-1 (glucólisis) e inhibe
  fructosa-1,6-bisfosfatasa (gluconeogénesis).

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-preguntas-examen.pdf, pregunta 8.* Coste energético de sintetizar 1
molécula de glucosa a partir de 2 moléculas de lactato: cada lactato → piruvato, y cada piruvato necesita
1 ATP (piruvato carboxilasa) + 1 GTP (PEP carboxiquinasa) para llegar a PEP, más 1 ATP extra en el paso
3-fosfoglicerato→1,3-bisfosfoglicerato (fosfoglicerato quinasa a la inversa). Por molécula de piruvato: 2 ATP
equivalentes (1 ATP + 1 GTP) + 1 ATP = 3 ATP equivalentes. Por 2 piruvatos (1 glucosa): **6 nucleótidos de
alta energía = 6 ATP equivalentes**.

## Conexión con otros conceptos

- [[glucolisis]]: regulación recíproca y enzimas compartidos/distintos en los 3 pasos irreversibles.
- [[ciclo-alanina-glucosa-cahill]]: la alanina que llega desde el músculo se convierte en piruvato en el
  hígado, precursor directo de esta ruta.
- [[metabolismo-lipidos-beta-oxidacion]]: el glicerol de la lipólisis es precursor de gluconeogénesis, pero
  **los ácidos grasos NO lo son** (no hay ruta neta de acetil-CoA a piruvato/OAA sin perder los carbonos como
  CO2) — trampa habitual de examen.
- [[ciclo-krebs]]: los intermediarios del ciclo (vía oxalacetato) son también precursores.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): dar por hecho que la gluconeogénesis es la
glucólisis "al revés" con los mismos enzimas es el error más grave posible aquí — obliga a identificar
primero cuál de los 3 pasos irreversibles se está tratando y qué enzima específico de la gluconeogénesis lo
sustituye, antes de escribir ninguna reacción.

## Relevancia en examen

**Alta.** La tabla de rutas metabólicas con Gluconeogénesis (tipo, localización, sustratos, productos)
aparece en los 4 exámenes/hojas revisados. Preguntas sobre qué enzimas son comunes/distintos entre glucólisis
y gluconeogénesis y el coste en ATP de sintetizar glucosa desde lactato aparecen explícitamente en
examenes/wuolah-free-preguntas-examen.pdf.
