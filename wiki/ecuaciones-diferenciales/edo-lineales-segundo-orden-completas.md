---
titulo: "EDOs lineales de segundo orden completas: coeficientes indeterminados y aplicaciones (muelle, RLC)"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 3 - Ecuaciones lineales de segundo orden"
tipo: "procedimiento"
relacionado: ["edo-lineales-segundo-orden-homogeneas", "sistemas-edo-primer-orden"]
patrones_error: [3, 6]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 3.2, 3.4)", "20_12_23_2parcial - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una ecuación `ay'' + by' + cy = f(x)` con `f(x) ≠ 0` es la versión "completa" (no homogénea) de
[[edo-lineales-segundo-orden-homogeneas]]. Su solución general es siempre
`y = yh + yp`: la solución de la homogénea (`yh`, con las dos constantes libres) más **una**
solución particular cualquiera de la completa (`yp`, sin constantes).

## Por qué / de dónde viene

Si `yp` es una solución de la completa y `z` es cualquier otra, entonces `z − yp` cumple la
ecuación homogénea (los términos con `f(x)` se cancelan al restar). Por tanto `z − yp` se puede
escribir como combinación lineal de las soluciones de la homogénea, y despejando queda
`z = yh + yp`. Encontrar `yp` es un problema de "adivinar la forma": si `f(x)` es un polinomio,
exponencial, seno/coseno o producto de estos, existe una tabla de formas candidatas
(**método de coeficientes indeterminados**).

## Fórmula / procedimiento

1. Resolver primero la homogénea asociada (`f(x)=0`) → `yh` (ver [[edo-lineales-segundo-orden-homogeneas]]).
2. Proponer `yp` según la forma de `f(x)`:

| `f(x)` | Candidato `yp` |
|---|---|
| Polinomio de grado `n` | Polinomio de grado `n` |
| `e^(kx)` | `A·e^(kx)` |
| `sen(kx)`, `cos(kx)` | `A·sen(kx) + B·cos(kx)` |
| `e^(kx)·cos(βx)` | `e^(kx)·(A·cos(βx) + B·sen(βx))` |

   **Si el candidato ya forma parte de `yh`, multiplicarlo por `x` (o por `x²` si hiciera falta)
   hasta que deje de coincidir** — este es el paso que más se olvida.
3. Sustituir `yp` (y sus derivadas) en la ecuación completa y resolver los coeficientes
   indeterminados igualando término a término.
4. La solución general es `y = yh + yp`; aplicar condiciones iniciales al final, sobre la suma
   completa, nunca solo sobre `yh`.

## Ejemplo resuelto

*Adaptado de Apuntes de ecuaciones diferenciales.pdf, secc. 3.4.2 — muelle sobreamortiguado.*
Un muelle con masa `m=2 kg` y constante `k=128 N/m` está sumergido en un fluido con constante de
amortiguación `c=40`. Parte del equilibrio con velocidad inicial `0.6 m/s`. Ecuación:

```
2x'' + 40x' + 128x = 0  →  x'' + 20x' + 64x = 0
```

Ecuación característica: `r² + 20r + 64 = 0` → raíces `r = −4, −16` (reales negativas distintas,
sobreamortiguado — sin oscilación). `x(t) = c1·e^(−4t) + c2·e^(−16t)`.

Con `x(0)=0`: `c1+c2=0` → `c2=−c1`. Con `x'(0)=0.6`: `−4c1−16c2=0.6` → `−4c1+16c1=12c1=0.6` →
`c1=0.05`, `c2=−0.05`.

**Solución: `x(t) = 0.05·(e^(−4t) − e^(−16t))`.**

*Ejemplo de coeficientes indeterminados (Apuntes, secc. 3.2).* `y'' − 3y' + 2y = e^x`: raíces de
la homogénea `r=1,2`, así que `yh = c1e^x + c2e^(2x)`. Como `e^x` ya está en `yh`, se prueba con
`yp = A·x·e^x` (no `A·e^x`), y sustituyendo se obtiene `A=−1`:
`y = c1e^x + c2e^(2x) − x·e^x`.

## Conexión con otros conceptos

- [[edo-lineales-segundo-orden-homogeneas]] — paso previo obligatorio: sin `yh` no se puede ni
  comprobar si `yp` colisiona con ella ni completar la solución general.
- [[sistemas-edo-primer-orden]] — la interpretación física (masa-muelle-amortiguador,
  circuito RLC) es la misma tanto si se resuelve como ecuación de 2º orden como si se transforma
  en sistema de 2 ecuaciones de 1er orden.
- Base directa de Ingeniería del Calor/Frío y Operaciones Unitarias (vibraciones en maquinaria,
  golpe de ariete en tuberías — ver aplicación hidráulica en Apuntes secc. 3.4.5) y de
  Electrotecnia (circuitos RLC en corriente alterna, ver [[../electrotecnia/MOC]]).

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmula sin verificar condiciones): el fallo más común es proponer
  `yp = A·e^(kx)` sin comprobar antes si `e^(kx)` ya es parte de `yh` — si lo es, el método falla
  silenciosamente (los coeficientes indeterminados dan `0=f(x)`, una contradicción) y hay que
  multiplicar por `x`.
- **Patrón 6** (copiar mal datos): en los problemas de muelle es fácil confundir la posición
  inicial con la velocidad inicial, o el signo de la velocidad (hacia arriba/abajo respecto a la
  posición de equilibrio) — leer en voz alta qué representa cada condición inicial antes de
  sustituir.

## Relevancia en examen

**Alta.** Presente en casi todos los segundos parciales/PEP2 y finales en forma de sistema
masa-muelle-amortiguador (Alimentaria_19_12_22, 20_12_23_2parcial, JULIO23_24, FInal17_1_25):
pide plantear la ecuación, resolver el PVI, interpretar el resultado físicamente, y clasificar el
tipo de amortiguamiento según los valores del coeficiente `β`/`c`. El coeficiente indeterminados
puro (sin contexto físico) aparece con más frecuencia en los primeros finales de julio
(FINAL 2_JULIO_2025, JULIO23_24). Vale típicamente 3 puntos.
