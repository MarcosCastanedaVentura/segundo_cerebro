---
titulo: "Circuitos RLC serie y paralelo en corriente alterna"
asignatura: "electrotecnia"
tema: "Tema 5-6 — Corrientes alternas I y II"
tipo: "concepto"
relacionado: ["corriente-alterna-fundamentos", "leyes-kirchhoff-ca", "triangulo-potencias", "metodo-boucherot"]
patrones_error: [6, 7]
examen_relevancia: "alta"
fuente: ["T5.pdf", "T6.pdf", "2E_Tema-5.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un circuito RLC es la combinación de una resistencia (R), una bobina o autoinducción (L) y un
condensador o capacidad (C). En corriente alterna cada elemento se comporta de forma distinta
frente al paso de la corriente, y esa combinación determina cuánta intensidad circula y con qué
desfase respecto a la tensión aplicada. Es el modelo base de cualquier receptor eléctrico real
(motor, línea, lámpara con balasto, etc.).

## Por qué / de dónde viene

En corriente continua solo existe resistencia (oposición por disipación de energía en calor). En
corriente alterna aparece además la **reactancia** (X), oposición asociada a los campos magnético
(L) y eléctrico (C) que no disipan energía sino que la almacenan y devuelven al circuito en cada
semiciclo. Combinando R (parte real) y X (parte imaginaria) se define la **impedancia compleja**
Z̄ = R + jX, que generaliza la Ley de Ohm a CA: Ū = Z̄·Ī.

- **Reactancia inductiva**: X_L = ωL (Ω). Crece con la frecuencia — una bobina "frena más" cuanto
  más rápido cambia la corriente (se opone a la variación de flujo, Ley de Faraday).
- **Reactancia capacitiva**: X_C = 1/(ωC) (Ω). Decrece con la frecuencia — un condensador se
  carga/descarga con más facilidad cuanto más rápido oscila la tensión.

## Fórmula / procedimiento

**Circuito serie** (misma intensidad I por todos los elementos):
- Impedancia total: Z̄_T = R + j(X_L − X_C) = R + jX ; Z = √(R² + X²)
- Desfase: φ = arctg(X/R) — triángulo de impedancias (R en el eje real, X en el imaginario)
- I = U/Z ; φ es el desfase entre Ū e Ī
- **Resonancia serie** (tensiones): cuando X_L = X_C → Z = R (mínima), I = U/R (máxima), φ=0.
  Ocurre a la pulsación ω_r = 1/√(LC). Factor de sobretensión Q = U_L/U_R = U_C/U_R (si Q>1
  aparecen sobretensiones peligrosas en L y C).

**Circuito paralelo** (misma tensión U en todos los elementos): se trabaja con **admitancia**
Ȳ = 1/Z̄ = G − jB, donde G = R/Z² (conductancia) y B = X/Z² (susceptancia).
- Admitancia total (en paralelo, suma vectorial): Ȳ_T = ΣȲ_k = G_T − jB_T
- I = Y·U
- **Resonancia paralelo** (corrientes): cuando B = 0 → Y mínima, I mínima, φ=0.

**Circuitos mixtos** (serie + paralelo combinados): regla de oro — nunca se pueden sumar
impedancias en serie y admitancias en paralelo en el mismo paso. Se resuelve por tramos:
1. Calcular Z̄ o Ȳ de cada receptor.
2. Reducir secuencialmente: sumar Z̄ solo donde hay elementos en serie sin ramas en paralelo
   por medio; sumar Ȳ solo donde hay elementos en paralelo sin nada en serie por medio.
3. Aplicar Ohm (Ū = Z̄·Ī) en cada tramo ya reducido.

## Ejemplo resuelto

Circuito serie con R = 30 Ω, X_L = 40 Ω, X_C = 0 (solo R y L), alimentado a U = 230 V, 50 Hz.
- Z̄ = 30 + j40 Ω → Z = √(30²+40²) = 50 Ω ; φ = arctg(40/30) = 53,13°
- I = U/Z = 230/50 = 4,6 A, retrasada 53,13° respecto a la tensión (circuito inductivo, la I "llega
  después" que la U).

Si en vez de L hubiera un condensador con X_C = 40 Ω: Z̄ = 30 − j40 Ω, mismo módulo Z=50 Ω pero
φ = −53,13° (I adelantada respecto a U, circuito capacitivo).

## Conexión con otros conceptos

- [[corriente-alterna-fundamentos]]: representación fasorial y ley de Ohm compleja de base.
- [[leyes-kirchhoff-ca]]: las leyes de Kirchhoff en régimen senoidal (con fasores, no con valores
  eficaces sumados directamente) son las que permiten reducir circuitos serie/paralelo/mixtos.
- [[triangulo-potencias]] y [[metodo-boucherot]]: una vez con Z̄ e Ī, se calculan P, Q, S.
- [[sistemas-trifasicos-estrella-triangulo]]: cada fase de un sistema trifásico equilibrado se
  resuelve como un circuito RLC monofásico independiente.
- Base directa de Instalaciones Eléctricas (3º curso) — ver [[../carrera/dependencias]].

## Errores frecuentes de Marcos aquí

No hay un patrón de error específico de RLC documentado con activación registrada, pero este es
terreno fértil para el **Patrón 6** (copiar mal un dato numérico de R, X_L o X_C del enunciado) y el
**Patrón 7** (dar por bueno un resultado de Z o I que "suena razonable" sin comprobar unidades ni
que Z ≥ R siempre). Verificar siempre: Z nunca puede ser menor que R o que |X| por separado.

## Relevancia en examen

Alta — aparece en casi todos los problemas de PEP1 como paso de cálculo de intensidad de línea
antes de aplicar Boucherot o el triángulo de potencias. Los "Enunciados problemas primer parcial"
incluyen varios ejercicios de circuito serie/paralelo/mixto con datos de R, L, C y frecuencia.
