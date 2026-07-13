---
titulo: "Corriente alterna monofásica: fundamentos y fasores"
asignatura: "electrotecnia"
tema: "Tema 5 — Corrientes alternas I: fundamentos"
tipo: "concepto"
relacionado: ["circuitos-rlc-serie-paralelo", "triangulo-potencias", "leyes-kirchhoff-ca", "transformador-potencia"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["T5.pdf", "2E_Tema-5.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La corriente alterna (CA) es la que cambia periódicamente de sentido (a diferencia de la continua,
que siempre circula en el mismo sentido). En España la red doméstica es monofásica senoidal de
230 V y 50 Hz. Para poder operar con tensiones e intensidades que varían en el tiempo sin arrastrar
ecuaciones diferenciales en cada cálculo, se usa la representación **fasorial**: cada onda senoidal se
resume en un vector fijo (módulo = valor eficaz, ángulo = fase en t=0).

## Por qué / de dónde viene

Una espira que gira a velocidad angular constante ω dentro de un campo magnético uniforme B ve
variar el flujo que la atraviesa: Φ = B·A·cos(θ). Por la **Ley de Faraday** (e = −dΦ/dt), esa variación
de flujo induce una f.e.m. que resulta senoidal: e = E₀·sen(ωt + φ). Este es el principio de
funcionamiento del alternador (máquina que genera CA a partir de energía mecánica) — ver
[[transformador-potencia]] para el recordatorio completo de electromagnetismo (Biot-Savart,
Hopkinson, Faraday).

Si a un circuito con R, L, C se le aplica esa tensión senoidal, la ecuación diferencial que rige el
circuito (Ri + L·di/dt + (1/C)∫i·dt = u) tiene como solución en régimen permanente otra senoidal de
**la misma pulsación ω** pero con distinta amplitud y desfase φ respecto a la tensión. Operar con
senos y cosenos en cada problema sería muy lento — de ahí la representación fasorial (vectores fijos
en el plano complejo de Gauss, congelando el tiempo en t=0).

## Fórmula / procedimiento

**Valores característicos de una onda senoidal** e = E₀·sen(ωt + φ):
- E₀: valor máximo o amplitud (V)
- ω = 2πf = 2π/T: pulsación (rad/s); f: frecuencia (Hz); T: periodo (s)
- φ: fase inicial (ángulo en t=0)
- Valor medio en semiperiodo: Eₘ = (2/π)·E₀ ≈ 0,6366·E₀
- **Valor eficaz** (el que se usa en la práctica, sin subíndice): E = E₀/√2 ≈ 0,7071·E₀. Es el que
  produce el mismo efecto Joule que una continua del mismo valor.
- Factor de amplitud = E₀/E = √2 ; factor de forma = E/Eₘ = π/(2√2) ≈ 1,11

**Representación fasorial** (para tensión U y corriente I, ambas eficaces):
- Notación binómica/rectangular: Z̄ = R + jX (para sumar/restar)
- Notación polar: Z̄ = Z∠φ (para multiplicar/dividir), con Z = √(R²+X²), φ = arctg(X/R)
- Conversión: R = Z·cosφ, X = Z·senφ

**Ley de Ohm generalizada en CA**: Ū = Z̄·Ī, donde Z̄ es la impedancia compleja del receptor.

## Ejemplo resuelto

Tensión de red española: u = 325·sen(100πt) V (fuente: T5.pdf).
- U₀ = 325 V (amplitud) → U = 325/√2 = 230 V (valor eficaz, el que se mide con un voltímetro)
- ω = 100π rad/s → f = ω/2π = 50 Hz → T = 1/f = 0,02 s

Si esta tensión se aplica a una resistencia pura R = 7,5 Ω: I₀ = U₀/R = 325/7,5 ≈ 43,3 A (amplitud),
por tanto I = 43,3/√2 ≈ 30,6 A (eficaz), en fase con la tensión (φ=0, receptor resistivo puro).

## Conexión con otros conceptos

- [[circuitos-rlc-serie-paralelo]]: qué pasa cuando en vez de una R sola hay R, L y C combinadas.
- [[transformador-potencia]]: la Ley de Faraday y el resto de electromagnetismo básico (Biot-Savart,
  Hopkinson) que sustenta tanto el alternador como el transformador.
- [[triangulo-potencias]]: una vez con fasores de U e I, se define la potencia compleja.
- Es la base de [[../instalaciones-electricas/MOC|Instalaciones Eléctricas]] y Automatización de 3º
  curso (ver [[../carrera/dependencias]]).

## Errores frecuentes de Marcos aquí

Sin patrón específico documentado en esta nota, pero la base fasorial es la que luego dispara el
**Patrón 3** (aplicar fórmulas sin identificar antes el tipo de conexión/receptor) en temas
posteriores como trifásicos — repasar aquí si ese patrón se reactiva.

## Relevancia en examen

Tema base que rara vez se pregunta aislado, pero toda operación con fasores (suma, resta,
conversión polar↔rectangular, cálculo de valor eficaz) aparece en prácticamente todos los
problemas de parciales (PEP1 y PEP2) como paso intermedio.
