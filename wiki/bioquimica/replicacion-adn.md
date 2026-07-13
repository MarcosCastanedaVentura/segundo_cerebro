---
titulo: "Replicación del ADN: características generales y ADN polimerasas"
asignatura: "bioquimica"
tema: "Tema 9 - Ácidos nucleicos: flujo de la información genética"
tipo: "procedimiento"
relacionado: ["estructura-acidos-nucleicos", "transcripcion-y-traduccion", "tecnicas-biologia-molecular"]
patrones_error: [2, 5]
examen_relevancia: "media"
fuente: ["Tema 9.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La replicación es el proceso por el que una molécula de ADN se duplica antes de la división celular, de forma
que cada célula hija reciba una copia completa e idéntica del material genético. Es semiconservativa: cada
doble hélice hija contiene una hebra completa del ADN parental y una hebra recién sintetizada.

## Por qué / de dónde viene

El carácter antiparalelo de las dos hebras del ADN (una 5'→3', la otra 3'→5') genera un problema mecánico:
la ADN polimerasa solo puede sintetizar en dirección 5'→3'. Como las dos hebras se separan a la vez en la
horquilla de replicación, una hebra (la conductora) se puede copiar de forma continua en la misma dirección
que avanza la horquilla, pero la otra (la retrasada) debe copiarse en fragmentos discontinuos (fragmentos de
Okazaki) que luego se unen — de ahí que el proceso global se llame "semidiscontinuo" (no confundir con
"semiconservativo", que se refiere a otra cosa: qué hebra parental se conserva, no cómo se sintetiza la
nueva).

## Fórmula / procedimiento

**7 características de la replicación (resumen, orden no estrictamente secuencial salvo donde se indica):**
1. Proceso semiconservativo.
2. Comienza en sitio(s) específico(s): origen de replicación (ori). Bacterias: 1 oriC; eucariotas: cientos o
   miles de orígenes por genoma.
3. Hay que separar las dos hebras (helicasas, con gasto de ATP) y compensar el superenrollamiento resultante
   (girasas/topoisomerasas).
4. Procede de modo bidireccional (2 horquillas de replicación, avanzando en direcciones opuestas desde el
   ori).
5. Las nuevas cadenas se sintetizan siempre en sentido 5'→3', de forma antiparalela a la hebra molde.
6. La síntesis es semidiscontinua: hebra conductora (continua) + hebra retrasada (discontinua, fragmentos de
   Okazaki, después sellados por la ADN ligasa).
7. Requiere cebadores de ARN (sintetizados por la primasa) que aportan el extremo 3'-OH libre necesario para
   que la ADN polimerasa empiece a añadir nucleótidos — las ADN polimerasas NO pueden iniciar una cadena de
   novo.

**Actividades de las ADN polimerasas:**
- Polimerasa 5'→3': síntesis de la nueva cadena.
- Exonucleasa 3'→5': corrección de errores (proofreading), elimina el último nucleótido mal incorporado.
- Exonucleasa 5'→3': elimina los cebadores de ARN y repara errores.

**En bacterias (E. coli)**: Pol I elimina cebadores y rellena huecos con ADN; Pol II repara; **Pol III**
realiza la mayor parte de la síntesis. Fidelidad in vivo ≈ 1 error / 10⁹-10¹⁰ nucleótidos.

**En eucariotas**: replicación en el núcleo, múltiples orígenes simultáneos, varias ADN polimerasas (α, δ, β,
ε, γ — cada una con función específica: síntesis de cadena rezagada/conductora, reparación, replicación
mitocondrial), velocidad ~10 veces menor que en bacterias, fragmentos de Okazaki más cortos (~200 nt frente a
~2000 nt en procariotas), y terminación distinta por ser ADN lineal (telómeros, que se acortan ~100 pb por
división — a diferencia de la terminación circular bacteriana mediante secuencias Ter y topoisomerasas).

## Ejemplo resuelto

Ejercicio típico: dada una hebra de ADN 5'-TAGCCGTCCTGGAATTTA-3', escribir su complementaria antiparalela.
Procedimiento correcto: (1) escribir la complementaria base a base (A↔T, G↔C) en el mismo sentido de lectura
(esto da la hebra "reversa+complementaria" pero aún en orden 3'→5' respecto a la original), (2) invertir el
orden para expresarla en su propio sentido 5'→3'. Resultado:
3'-ATCGGCAGGACCTTAAAT-5' (equivalente a 5'-TAAATTCCAGGACGGCTA-3').

## Conexión con otros conceptos

- [[estructura-acidos-nucleicos]]: la complementariedad de bases y el carácter antiparalelo son la base
  física de todo este proceso.
- [[transcripcion-y-traduccion]]: comparte mecanismo similar (polimerasa, molde de ADN) pero sin necesidad de
  cebador y con menor fidelidad.
- [[tecnicas-biologia-molecular]]: la PCR reproduce artificialmente esta lógica (ADN polimerasa
  termorresistente, cebadores, síntesis 5'→3').

## Errores frecuentes de Marcos aquí

**Patrón 2** (confundir términos parecidos): "semiconservativo" (qué hebra parental se conserva en cada
hélice hija) y "semidiscontinuo" (cómo se sintetiza cada hebra nueva, continua vs discontinua) suenan
parecidos y describen aspectos distintos del mismo proceso — exige verbalizar la definición exacta de cada
uno antes de usarlo en una respuesta.

**Patrón 5** (orden incorrecto en procedimientos con secuencia estricta): al escribir la hebra complementaria
de una secuencia dada, invertir el orden de escritura antes de complementar (o al revés) sin verificar el
sentido 5'/3' final es el error más común — verificar siempre qué extremo queda a la izquierda antes de dar
la secuencia por buena.

## Relevancia en examen

**Media.** No aparece como problema numérico extenso en los exámenes oficiales revisados, pero sí como base
conceptual de preguntas de teoría sobre el dogma central y como ejercicio de complementariedad de secuencias
en el material de clase (Tema 9). Menor peso relativo que enzimología o metabolismo en los exámenes finales
revisados, que se centran más en la parte de metabolismo intermediario.
