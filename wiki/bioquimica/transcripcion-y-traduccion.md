---
titulo: "Transcripción, código genético y traducción"
asignatura: "bioquimica"
tema: "Tema 9 - Ácidos nucleicos: flujo de la información genética"
tipo: "concepto"
relacionado: ["estructura-acidos-nucleicos", "replicacion-adn", "aminoacidos-y-estructura-proteica", "tecnicas-biologia-molecular"]
patrones_error: [2, 6]
examen_relevancia: "media"
fuente: ["Tema 9.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El dogma central de la biología molecular describe el flujo "unidireccional" clásico de la información
genética: ADN → (replicación) → ADN; ADN → (transcripción) → ARN; ARN → (traducción) → proteína. La
transcripción copia un gen de ADN a ARN; la traducción usa el código genético para convertir la secuencia de
ARN mensajero en una secuencia de aminoácidos.

## Por qué / de dónde viene

La transcripción usa solo una de las dos hebras de ADN como molde (la hebra "sin sentido" o (−), no
codificante) para generar un ARN idéntico en secuencia a la otra hebra (la hebra "con sentido" o (+),
codificante, salvo que el ARN lleva U en vez de T). No necesita cebador porque la ARN polimerasa sí puede
iniciar cadenas de novo (a diferencia de la ADN polimerasa) — pero paga el precio de una fidelidad mucho menor
(1 error/10⁴-10⁵ nucleótidos, frente a 1/10⁹-10¹⁰ en la replicación), tolerable porque el ARN tiene vida
media corta y no se transmite a la descendencia. El código genético traduce esa secuencia de nucleótidos (4
bases) a aminoácidos (20) usando tripletes (codones): 4³=64 combinaciones posibles para solo 20 aminoácidos +
señales de inicio/parada, de ahí que el código sea degenerado (varios codones sinónimos para el mismo
aminoácido) pero nunca ambiguo (cada codón concreto especifica un único aminoácido).

## Fórmula / procedimiento

**Transcripción — requerimientos y propiedades:**
- Precursores: ATP, UTP, CTP, GTP (NTPs, no dNTPs) + Mg²⁺.
- Molde: ADN de doble cadena, solo se usa la hebra molde/no codificante para cada gen.
- No requiere cebador.
- RNA polimerasa de E. coli: holoenzima α2ββ'ωσ — la subunidad σ reconoce los promotores; α se une a
  proteínas reguladoras; β se une a los NTPs; β' se une al ADN molde.
- Carece de actividad exonucleasa de corrección (por eso su tasa de error es mayor que la de la ADN
  polimerasa).
- En eucariotas, transcripción y traducción NO están acopladas (ocurren en compartimentos distintos: núcleo
  vs citosol), a diferencia de procariotas donde sí lo están.

**Maduración del ARNm en eucariotas** (no ocurre en procariotas, o mínimamente):
1. Adición de caperuza (CAP) en 5'.
2. Splicing (eliminación de intrones).
3. Adición de cola poli-A en 3'.

**Código genético — reglas:**
- Codón = triplete de nucleótidos, lectura sin solapamientos, 3 posibles marcos de lectura (fijados por el
  codón de inicio, normalmente AUG=Met).
- Universal (con pocas excepciones, ej. mitocondrial).
- Degenerado pero no ambiguo (varios codones para un mismo aminoácido, pero cada codón da un único
  aminoácido).
- 3 codones de parada/sin sentido: UAA (ocre), UAG (ámbar), UGA (ópalo).
- Apareamiento codón-anticodón antiparalelo, con "balanceo" (wobble) en la 3ª posición del codón (1ª del
  anticodón) — permite que un mismo tRNA reconozca varios codones sinónimos, evitando necesitar 64 tRNAs
  distintos.

**Traducción — etapas**: iniciación, elongación, terminación. Se lee el ARNm 5'→3'; la proteína se sintetiza
desde el extremo amino hasta el carboxilo. Requiere ribosomas, tRNAs, aminoacil-tRNA sintetasas, factores
proteicos (IF/EF/RF en procariotas; eIF/eEF/eRF en eucariotas) y energía (ATP y GTP).

## Ejemplo resuelto

*Ejercicio del Tema 9 (transcripción de una hebra dada).* ADN:
5'-TAGCCGTCCTGGAATTTA-3' / 3'-ATCGGCAGGACCTTAAAT-5'.
La ARN polimerasa usa como molde la hebra 3'→5' (aquí, la hebra inferior) y sintetiza el ARN en dirección
5'→3', complementaria a ese molde:
ARN resultante: **5'-UAGCCGUCCUGGAAUUUA-3'** — idéntico en secuencia a la hebra superior de ADN (la hebra
codificante o "con sentido"), salvo T→U. Procedimiento correcto: identificar primero cuál hebra es el molde
(3'→5' respecto al sentido de síntesis) antes de transcribir, no asumir que cualquiera de las dos sirve.

## Conexión con otros conceptos

- [[estructura-acidos-nucleicos]]: complementariedad de bases, ahora aplicada a un dúplex ADN-ARN transitorio.
- [[replicacion-adn]]: comparte maquinaria conceptual (polimerasa, molde) pero difiere en fidelidad y
  necesidad de cebador.
- [[aminoacidos-y-estructura-proteica]]: destino final de la información traducida.
- [[tecnicas-biologia-molecular]]: la retrotranscripción (RT) de virus ARN (VIH) invierte el dogma clásico —
  ARN como molde para sintetizar ADN.

## Errores frecuentes de Marcos aquí

**Patrón 2** (confundir términos parecidos): "hebra molde/no codificante/(−)" y "hebra codificante/con
sentido/(+)" son fáciles de intercambiar — la hebra que se lee como molde es la que NO se parece al ARN
resultante; la hebra "con sentido" es la que sí se parece (salvo T/U). Exige verbalizar cuál es cuál antes de
transcribir.

**Patrón 6** (copiar mal los datos): al transcribir una secuencia dada, es fácil invertir accidentalmente
cuál hebra actúa de molde o olvidar cambiar T por U — verificar siempre ambos puntos antes de dar la
secuencia de ARN por buena.

## Relevancia en examen

**Media.** Menor peso relativo que los temas de metabolismo intermediario en los exámenes finales revisados,
pero forma parte del temario de teoría y aparece en ejercicios de transcripción de secuencias y en preguntas
sobre el código genético (degeneración, codones de parada) en el material de clase.
