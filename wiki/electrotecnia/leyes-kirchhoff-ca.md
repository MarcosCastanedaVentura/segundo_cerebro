---
titulo: "Leyes de Kirchhoff en corriente alterna (fasores)"
asignatura: "electrotecnia"
tema: "Tema 6 — Corrientes alternas II: receptores R, L, C"
tipo: "concepto"
relacionado: ["circuitos-rlc-serie-paralelo", "corriente-alterna-fundamentos", "sistemas-trifasicos-estrella-triangulo"]
patrones_error: []
examen_relevancia: "media"
fuente: ["T6.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Las leyes de Kirchhoff (1ª: suma de intensidades en un nudo = 0; 2ª: suma de tensiones en una malla
cerrada = 0) son las mismas que en corriente continua, pero en alterna hay que aplicarlas con
**valores instantáneos o con fasores — nunca con valores eficaces sumados directamente**. Esta nota
recoge específicamente el punto flojo documentado de Marcos en teoría de circuitos DC (Kirchhoff,
nodos, mallas), extendido a su versión en alterna.

## Por qué / de dónde viene

En un nudo, la corriente que entra tiene que ser igual a la que sale en todo instante (conservación
de la carga). Si i₁, i₂, i₃ son senoidales de la misma frecuencia pero distinta fase, su suma
instantánea sen(ωt−φ₁) + sen(ωt−φ₂) + sen(ωt−φ₃) = 0 se cumple en cada instante t, pero **no** se
puede comprobar sumando los valores eficaces I₁+I₂+I₃ (eso ignora la fase de cada una). Al pasar a
notación fasorial (vectores complejos fijos, congelando t=0), la ley se convierte en una suma
vectorial: ΣĪ_k = 0. Es exactamente el mismo razonamiento por el que en Boucherot no se puede
sumar S directamente (ver [[metodo-boucherot]], Patrón 1): las magnitudes fasoriales no son
aditivas como escalares, solo lo son sus componentes (parte real e imaginaria, o dicho de otro
modo, cada fasor completo como vector).

## Fórmula / procedimiento

- **1ª Ley de Kirchhoff (nudos)**: Σ Ī_k = 0 (suma vectorial de fasores). **Nunca** Σ I_k ≠ 0 con
  valores eficaces.
- **2ª Ley de Kirchhoff (mallas)**: Σ Ū_k = 0, equivalente a Σ Ē = Σ Z̄·Ī (suma de f.e.m. complejas
  = suma de caídas de tensión complejas).
- Aplicación práctica en **circuitos serie**: la impedancia equivalente es la suma vectorial de las
  impedancias: Z̄_T = Σ Z̄_k (nunca suma algebraica de módulos Z_T ≠ ΣZ_k).
- Aplicación en **circuitos paralelo**: la admitancia equivalente es la suma vectorial de
  admitancias: Ȳ_T = Σ Ȳ_k.

## Ejemplo resuelto

Tres ramas conectadas a un mismo nudo con corrientes i₁ = 10·sen(ωt), i₂ = 10·sen(ωt−120°),
i₃ = 10·sen(ωt+120°) (sistema equilibrado trifásico, ver [[sistemas-trifasicos-estrella-triangulo]]).
Como fasores: Ī₁ = 10∠0°, Ī₂ = 10∠−120°, Ī₃ = 10∠120°. Su suma vectorial:
Ī₁+Ī₂+Ī₃ = 10(1+0j) + 10(−0,5−0,866j) + 10(−0,5+0,866j) = 10 − 5 − 5 + j(0 −8,66+8,66) = 0.
Se cumple la 1ª ley con fasores, aunque I₁=I₂=I₃=10 A eficaces cada una (no nulo si se sumaran
módulos).

## Conexión con otros conceptos

- [[circuitos-rlc-serie-paralelo]]: aplicación directa de estas leyes para reducir circuitos.
- [[metodo-boucherot]] (Patrón 1): mismo error conceptual de fondo — sumar magnitudes fasoriales
  como si fueran escalares.
- [[sistemas-trifasicos-estrella-triangulo]] (Patrón 3): en la conexión estrella con neutro, la
  corriente de neutro I_N es precisamente Ī₁+Ī₂+Ī₃ por la 1ª ley — si el receptor es equilibrado,
  I_N=0; si es desequilibrado, I_N≠0. Confundir cuándo se cumple una cosa u otra es la esencia del
  Patrón 3.

## Errores frecuentes de Marcos aquí

Documentado en memoria (`memory.json`) como concepto flojo: "teoría de circuitos DC (Kirchhoff,
nodos, mallas)". La causa raíz suele ser tratar las corrientes/tensiones como escalares con signo
en vez de como vectores (fasores) — hay que verificar siempre si la suma que se está haciendo es
de valores instantáneos/fasores (correcto) o de valores eficaces sueltos (incorrecto, salvo que
estén en fase).

## Relevancia en examen

Media — no suele preguntarse como teoría aislada, pero es el fundamento silencioso de cualquier
ejercicio de circuito mixto o de sistema trifásico desequilibrado con cálculo de I_N.
