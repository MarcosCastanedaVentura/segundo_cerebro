---
titulo: "El ATP y los compuestos de alto y bajo nivel energético"
asignatura: "bioquimica"
tema: "Tema 3 - Bioenergética"
tipo: "concepto"
relacionado: ["termodinamica-bioenergetica", "glucolisis", "ciclo-krebs", "cadena-transporte-electrones-fosforilacion-oxidativa"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Tema 3 Bioenergetica.pdf", "examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El ATP (adenosín trifosfato) es la "moneda energética" universal de la célula: el intermediario que conecta
las reacciones que liberan energía (catabolismo) con las que la requieren (anabolismo). El sistema
ATP/ADP/AMP está presente en todas las formas de vida, en concentración total constante (2-10 mM), siendo el
ATP el más abundante (~80%).

## Por qué / de dónde viene

El ATP tiene tres tipos de enlace: N-glucosídico (azúcar-base), éster (fosfato-azúcar) y anhídrido (entre
fosfatos). Los enlaces anhídrido (fosfoanhidro) son los que se rompen para liberar energía, y su ΔG0' de
hidrólisis es muy negativo por tres razones: (1) disminución de las tensiones electrostáticas/repulsión de
cargas entre los fosfatos adyacentes tras la hidrólisis, (2) estabilización por resonancia de los productos,
y (3) aumento de entropía (los productos, ADP+Pi, tienen más libertad conformacional e ionización que el ATP
íntegro). Aunque la hidrólisis es muy exergónica, el ATP es cinéticamente estable a pH 7 — solo se hidroliza
si un enzima cataliza la reacción, lo que permite que la célula lo use como "batería" controlada y no se
descargue espontáneamente.

## Fórmula / procedimiento

**Dos formas de hidrolizar el ATP:**
- Ortofosfatolítica (la más frecuente): ATP + H₂O → ADP + Pi, ΔG0' = −7,3 kcal/mol
- Pirofosfatolítica: ATP + H₂O → AMP + PPi, ΔG0' = −7,7 kcal/mol (el pirofosfato PPi se hidroliza después a
  2 Pi, ΔG0'=−8,0 kcal/mol, lo que desplaza el equilibrio y hace irreversible la reacción global — mecanismo
  usado por ejemplo en la activación de ácidos grasos, ver [[metabolismo-lipidos-beta-oxidacion]])
- El AMP vuelve al ciclo mediante la adenilato quinasa: ATP + AMP ⇌ 2 ADP

**Compuestos de alto nivel energético** (ΔG0' de hidrólisis muy negativo, en valor absoluto mayor que el ATP):
fosfoenolpiruvato (−61,9 kJ/mol), 1,3-bisfosfoglicerato, fosfocreatina (enlace amida), acetil-CoA (enlace
tioéster, no libera fosfato pero es de alta energía). Se forman por ruptura enzimática de moléculas de
reserva (glucógeno, almidón) o por oxidaciones metabólicas.

**Compuestos de bajo nivel energético**: ésteres fosfóricos de alcoholes, como glucosa-6-fosfato. El ATP
ocupa una posición intermedia en la escala termodinámica y actúa de intermediario, transfiriendo fosfato
desde los compuestos de alto nivel energético a los de bajo nivel energético (reacciones acopladas,
catalizadas por quinasas).

**Tres mecanismos de síntesis de ATP:**
1. Fosforilación a nivel de sustrato (transferencia directa de un grupo fosfato de alta energía al ADP).
2. Fosforilación oxidativa (acoplada a la cadena de transporte de electrones, en la mitocondria).
3. Fotofosforilación (acoplada al transporte electrónico fotosintético, en organismos autótrofos).

## Ejemplo resuelto

*Reacciones acopladas, adaptado de Tema 3 Bioenergetica.pdf.* La fosforilación directa de la glucosa por Pi
sería endergónica: Pi + Glucosa → Glucosa-6-P + H₂O, ΔG0' = +13,8 kJ/mol (no espontánea). Pero acoplada a la
hidrólisis del ATP (ΔG0' = −30,5 kJ/mol), la reacción global es exergónica:

ATP + Glucosa → ADP + Glucosa-6-P, ΔG0' = 13,8 + (−30,5) = **−16,7 kJ/mol** (espontánea)

Este es exactamente el primer paso de la [[glucolisis]] (catalizado por hexoquinasa/glucoquinasa): la
reacción "cara" de fosforilar la glucosa se paga con la energía de romper un enlace fosfoanhidro del ATP.

## Conexión con otros conceptos

- [[termodinamica-bioenergetica]]: el ATP es el mecanismo concreto por el que se acoplan reacciones
  exergónicas y endergónicas para que la suma de ΔG sea negativa.
- [[glucolisis]] y [[ciclo-krebs]]: fuentes de fosforilación a nivel de sustrato (1,3-bisfosfoglicerato →
  3-fosfoglicerato + ATP; fosfoenolpiruvato → piruvato + ATP; succinil-CoA → succinato + GTP).
- [[cadena-transporte-electrones-fosforilacion-oxidativa]]: la vía principal de síntesis de ATP en
  condiciones aeróbicas.
- [[metabolismo-lipidos-beta-oxidacion]]: activación de ácidos grasos vía ruptura pirofosfatolítica del ATP.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): existen dos rutas de hidrólisis del ATP
(orto/pirofosfatolítica) con productos y ΔG0' distintos — usar el valor de una cuando el enunciado describe
la otra es un error típico. Antes de aplicar un ΔG0', identifica explícitamente qué enlace se rompe (entre
qué fosfatos) y qué productos se generan.

## Relevancia en examen

**Alta.** "Explique qué es la hidrólisis ortofosfatolítica del ATP, dé un ejemplo de reacción enzimática y su
significado metabólico" aparece **literalmente en los 4 exámenes/hojas de ejercicios revisados** (final
2022-23, final 2023-24, ordinario, ejercicios de examen) — es de las preguntas de desarrollo más repetidas
de toda la asignatura.
