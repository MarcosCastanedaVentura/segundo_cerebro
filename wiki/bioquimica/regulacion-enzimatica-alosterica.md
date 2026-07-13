---
titulo: "Regulación enzimática: enzimas alostéricos, regulación covalente e isoenzimas"
asignatura: "bioquimica"
tema: "Tema 2 - Enzimas"
tipo: "concepto"
relacionado: ["cinetica-michaelis-menten", "inhibicion-enzimatica", "enzimas-estructura-funcion", "glucolisis", "ciclo-krebs"]
patrones_error: [2, 3]
examen_relevancia: "alta"
fuente: ["Tema 2_Enzimas.pdf", "Tema 4 -Met de Glucidos.pdf", "Preguntas metabolismo glucidos y oxidativo 1.pdf", "examenes/wuolah-free-Examen ordinario (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Además de la regulación por factores inespecíficos (temperatura, pH, iones), la célula regula enzimas clave
por dos mecanismos específicos y reversibles: **regulación alostérica** (unión no covalente de un metabolito
regulador en un sitio distinto del centro activo) y **regulación covalente** (modificación química reversible,
típicamente fosforilación/desfosforilación). Además existen **isoenzimas**: formas moleculares distintas de
un mismo enzima que catalizan la misma reacción pero con propiedades cinéticas diferentes.

## Por qué / de dónde viene

Las rutas metabólicas necesitan "válvulas" que respondan rápidamente al estado energético de la célula sin
esperar a sintetizar o degradar proteína nueva. Los enzimas alostéricos son grandes, oligoméricos
(estructura cuaternaria) y tienen un sitio regulador distinto del sitio de unión al sustrato: cuando un
efector se une ahí, cambia la conformación de todas las subunidades (cooperatividad) y por tanto la afinidad
por el sustrato en las demás subunidades. Por eso su cinética no es hiperbólica sino sigmoidal (a la Km se le
llama K0,5), y responden de forma mucho más sensible a pequeños cambios de concentración del efector que un
enzima michaeliano.

## Fórmula / procedimiento

**Enzimas alostéricos**
- Gran tamaño, estructura oligomérica (4ª).
- Modulador o efector: activador (+) o inhibidor (-) que se une de forma no covalente y reversible.
- Cinética no michaeliana: curva sigmoidal de V vs [S] (cooperatividad entre subunidades).
- Ejemplo clave de examen: **isocitrato deshidrogenasa** (Ciclo de Krebs) — proteína de 8 monómeros idénticos,
  activada alostéricamente por ADP; el ADP actúa sobre el parámetro K0,5 (no sobre Vmax).

**Regulación covalente reversible (fosforilación/desfosforilación)**
- Una proteína quinasa transfiere el γ-fosfato del ATP a un residuo de Ser/Thr/Tyr del enzima:
  Enzima + ATP → Enzima-P + ADP (activa o inactiva el enzima según el caso).
- Una fosfatasa hidroliza el grupo fosfato: Enzima-P + H₂O → Enzima + Pi.
- Ejemplo clave: complejo piruvato deshidrogenasa — la fosforilación (por piruvato-DH-quinasa, activada por
  NADH y acetil-CoA) **inactiva** el complejo; la desfosforilación (por una fosfatasa activada por Ca²⁺ y
  Mg²⁺) lo **reactiva**.
- Ejemplo clásico: glucógeno fosforilasa, activa cuando está fosforilada (al revés que la piruvato
  deshidrogenasa — **hay que comprobar en cada caso si la forma activa es la fosforilada o la
  desfosforilada**, no se puede generalizar).

**Isoenzimas**
- Mismo tipo de reacción, distinta secuencia/composición de aminoácidos → distinta Km y Vmax, distinta
  respuesta a pH/T/moduladores. Se separan por electroforesis (ver [[tecnicas-biologia-molecular]]).
- Ejemplo de examen: alcohol deshidrogenasa (ADH) hepática y aldehído deshidrogenasa (ALDH-I y ALDH-II); el
  40-50% de la población asiática tiene un déficit de ALDH-II → intolerancia al alcohol (acumulación de
  acetaldehído).
- Ejemplo metabólico: hexoquinasa (general, todos los tejidos) vs glucoquinasa (isoenzima hepática,
  específica de glucosa, distinta Km — mucho más alta, lo que le permite responder a la glucosa postprandial
  sin saturarse).

## Ejemplo resuelto

*Adaptado de Problemas de Metabolismo 2.pdf, pregunta 5.* La isocitrato deshidrogenasa mitocondrial es una
proteína de 8 monómeros idénticos cuya actividad depende fuertemente de [ADP], con una curva sigmoidal frente
a [ADP]. a) La curva sigmoidal (no hiperbólica) indica cinética **cooperativa/alostérica**, no michaeliana.
b) El ADP actúa como **activador alostérico**. c) El parámetro afectado es la **K0,5** (equivalente a la Km
de un enzima michaeliano, pero llamado así en enzimas alostéricos).

## Conexión con otros conceptos

- [[glucolisis]]: la PFK-1 (fosfofructoquinasa-1) es el ejemplo alostérico más citado — activada por AMP y
  fructosa-2,6-bisfosfato, inhibida por ATP y citrato.
- [[ciclo-krebs]]: isocitrato deshidrogenasa y α-cetoglutarato deshidrogenasa, reguladas por la relación
  NAD⁺/NADH y ADP/ATP.
- [[inhibicion-enzimatica]]: comparte el concepto de "unión no covalente reversible" pero la inhibición
  alostérica es fisiológica (feedback), no un fármaco/tóxico externo.
- [[metabolismo-lipidos-beta-oxidacion]]: acetil-CoA carboxilasa (ACC), regulada tanto alostéricamente
  (citrato activa, palmitoil-CoA inhibe) como por fosforilación covalente (glucagón/adrenalina inactivan).

## Errores frecuentes de Marcos aquí

**Patrón 2** (confundir términos parecidos): "activador alostérico" y "efector alostérico" a veces se
confunden con "cofactor" — un cofactor es necesario para la catálisis en sí, un efector alostérico modula
la actividad desde un sitio distinto sin ser necesario para la catálisis del centro activo. Exige verbalizar
la diferencia antes de clasificar un caso.

**Patrón 3** (aplicar fórmulas/reglas sin verificar el caso): no se puede asumir que "fosforilar siempre
activa" o "siempre inactiva" — depende del enzima concreto (la piruvato deshidrogenasa se inactiva al
fosforilarse, la glucógeno fosforilasa se activa). Verifica siempre cuál es el caso concreto antes de
responder.

## Relevancia en examen

**Alta.** Pregunta de "ponga un ejemplo de enzima alostérico que participe en el metabolismo de la glucosa y
sus moduladores" en el examen final 2022-2023. Preguntas V/F sobre activadores/inhibidores de PFK-1,
piruvato quinasa y piruvato deshidrogenasa en varios exámenes. Mecanismo de regulación covalente reversible
(con esquema) pedido explícitamente en el examen ordinario 2022-2023 y en la recuperación 2023-2024.
