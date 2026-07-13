---
titulo: "Probabilidad: axiomas, propiedades y probabilidad condicionada"
asignatura: "estadistica"
tema: "Tema 2.1 — Probabilidad"
tipo: "concepto"
relacionado: ["variable-aleatoria-discreta", "variable-aleatoria-continua", "distribucion-binomial", "estadistica-descriptiva-dos-variables"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["Tema_2.1_Probabilidad_25-26-2.pdf", "Cálculo de Probabilidades.pdf", "Enunciados Problemas de Probabilidad I.pdf", "Enunciados Problemas de Probabilidad II.pdf", "Enunciados Problemas de Probabilidad III.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La probabilidad es una función P(·) que asigna a cada **suceso** (subconjunto del espacio muestral E de un
experimento aleatorio) un número entre 0 y 1 que mide cuán verosímil es que ocurra. Un experimento es **aleatorio**
si: (1) se conocen a priori todos los resultados posibles, (2) puede repetirse indefinidamente en condiciones
idénticas, y (3) el resultado de cada repetición concreta se desconoce de antemano.

## Por qué / de dónde viene

Para que P(·) sea coherente (que la probabilidad de la intersección nunca sea mayor que la de la unión, etc.) se
exige que cumpla tres **axiomas**:

1. P(A) ≥ 0 para todo suceso A.
2. P(E) = 1 (el suceso seguro tiene probabilidad 1).
3. Si A₁, A₂,... son sucesos incompatibles (disjuntos dos a dos), P(∪Aᵢ) = ΣP(Aᵢ).

De estos tres axiomas se deducen todos los teoremas que se usan en la práctica — no hay que memorizarlos sueltos,
se derivan.

## Fórmula / procedimiento

**Teoremas derivados de los axiomas** (los más usados):

- P(∅) = 0
- P(Ā) = 1 − P(A) (probabilidad del complementario)
- Si A⊂B entonces P(A) ≤ P(B)
- **P(A∪B) = P(A) + P(B) − P(A∩B)** — válido siempre; si A y B son incompatibles (A∩B=∅), se reduce a P(A)+P(B).

**Regla de Laplace** (sucesos elementales equiprobables): P(A) = casos favorables / casos posibles.

**Probabilidad condicionada**: probabilidad de A sabiendo que ya ha ocurrido B:

P(A/B) = P(A∩B) / P(B),  con P(B) > 0

De aquí sale la **regla del producto**: P(A∩B) = P(A/B)·P(B) = P(B/A)·P(A).

**Independencia de sucesos**: A y B son independientes si y solo si P(A∩B) = P(A)·P(B), lo que equivale a que
P(A/B)=P(A) y P(B/A)=P(B) — saber que ha ocurrido B no cambia nada la probabilidad de A.

**Teorema de la probabilidad total**: si S₁,...,Sₙ son sucesos disjuntos que cubren todo E (causas mutuamente
excluyentes y exhaustivas),

P(B) = Σᵢ P(B/Sᵢ)·P(Sᵢ)

**Teorema de Bayes** (invierte el condicionamiento — "efecto conocido, ¿qué causa lo produjo?"):

P(Sᵢ/B) = [P(B/Sᵢ)·P(Sᵢ)] / Σⱼ P(B/Sⱼ)·P(Sⱼ)

## Ejemplo resuelto

(Adaptado de Cálculo de Probabilidades.pdf, problema 3.1) En una explotación con 200 vacas, 25 están enfermas
(12.5%). Se seleccionan 2 vacas al azar **con reemplazamiento** (cada extracción es independiente porque la vaca se
devuelve al rebaño). Sea A = "la primera está enferma", B = "la segunda está sana".

P(A) = 25/200 = 0.125. P(B) = 175/200 = 0.875. Como es con reemplazamiento, A y B son independientes:
P(A∩B) = P(A)·P(B) = 0.125×0.875 = 0.109375.

P(A∪B) = P(A) + P(B) − P(A∩B) = 0.125 + 0.875 − 0.109375 = 0.890625 (probabilidad de que la primera esté enferma o
la segunda esté sana, o ambas cosas).

## Conexión con otros conceptos

- [[variable-aleatoria-discreta]] y [[variable-aleatoria-continua]] — una variable aleatoria formaliza "asignar un
  número a cada resultado del experimento"; su función de probabilidad/densidad hereda todas estas propiedades.
- [[distribucion-binomial]] — se construye aplicando la regla del producto e independencia a n repeticiones de un
  experimento con dos resultados.
- [[estadistica-descriptiva-dos-variables]] — la independencia entre caracteres (fᵢⱼ=fᵢ.f.ⱼ) es el análogo empírico
  de la independencia de sucesos aquí.

## Errores frecuentes de Marcos aquí

Ninguno activo documentado en este bloque. Punto de vigilancia general (Patrón 6, copiar mal datos): en problemas de
Bayes/probabilidad total con varias "causas" Sᵢ, verificar siempre que las probabilidades a priori P(Sᵢ) sumen 1
antes de aplicar la fórmula — un error de transcripción aquí invalida todo el cálculo posterior.

## Relevancia en examen

Alta. Los "Enunciados Problemas de Probabilidad I/II/III" en `raw/` son listas de problemas de urnas, cartas, control
de calidad y diagnóstico médico que combinan regla de Laplace, condicionada, probabilidad total y Bayes — este es un
bloque que cae siempre en la 1ª parte del examen, normalmente como problema de 2-3 apartados encadenados (calcula
P(A), luego P(A/B), luego aplica Bayes).
