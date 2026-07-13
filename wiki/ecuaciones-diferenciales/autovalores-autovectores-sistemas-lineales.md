---
titulo: "Método de autovalores y autovectores para sistemas lineales X'=AX"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 5 - Sistemas de ecuaciones diferenciales lineales"
tipo: "procedimiento"
relacionado: ["sistemas-edo-primer-orden", "autovalores-complejos", "clasificacion-puntos-criticos-sistemas-lineales", "sistemas-casi-lineales-estabilidad"]
patrones_error: [3, 4]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 5, 5.1)", "20_12_23_2parcial - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Dado un sistema lineal de EDOs con coeficientes constantes `X' = A·X` (donde `X` es un vector de
2 funciones y `A` una matriz `2×2`), las soluciones tienen la forma `X(t) = v·e^(λt)`, donde `λ`
es un **autovalor** de `A` y `v` su **autovector** asociado. Si `A` tiene dos autovalores reales
distintos `λ1, λ2` con autovectores `v1, v2`, la solución general es
`X(t) = c1·v1·e^(λ1 t) + c2·v2·e^(λ2 t)`.

## Por qué / de dónde viene

Si se propone `X = v·e^(λt)` como solución candidata (igual que se probaba `y=e^(rx)` en la
ecuación de 2º orden), sustituyendo en `X'=AX` sale `λv·e^(λt) = Av·e^(λt)`, y como `e^(λt)`
nunca es cero, se reduce a `Av = λv`, es decir, `(A−λI)v = 0`. Esto es un sistema homogéneo que
solo tiene solución no nula (`v≠0`) si el determinante `|A−λI| = 0` — esa ecuación (el polinomio
característico de `A`) da los autovalores.

## Fórmula / procedimiento

1. Plantear la ecuación característica `|A−λI| = 0`. Para una matriz `2×2` se puede calcular
   directamente como `λ² − tr(A)·λ + |A| = 0`, donde `tr(A)` es la traza (suma de la diagonal) y
   `|A|` el determinante — no hace falta expandir el determinante simbólico cada vez.
2. Resolver la ecuación de 2º grado en `λ` → autovalores `λ1, λ2`.
3. Para cada `λi`, resolver el sistema homogéneo `(A−λi·I)v = 0` para hallar el autovector `vi`
   (basta una ecuación, ya que el sistema es siempre indeterminado por construcción).
4. La solución general es `X(t) = c1·v1·e^(λ1t) + c2·v2·e^(λ2t)`.
5. Con condiciones iniciales `X(0) = X0`, sustituir `t=0` y resolver el sistema lineal en
   `c1, c2`.

## Ejemplo resuelto

*Adaptado de Apuntes de ecuaciones diferenciales.pdf, secc. 5, Ejemplo 5.* Sistema
`X' = [[4,2],[3,−1]]·X`.

`tr(A) = 4−1 = 3`, `|A| = 4·(−1) − 2·3 = −10`. Ecuación característica:
`λ² − 3λ − 10 = (λ+2)(λ−5) = 0` → `λ1=−2`, `λ2=5`.

Para `λ1=−2`: `(A+2I)v=0` → `[[6,2],[3,1]]v=0` → `3a+b=0` → `v1=(1,−3)`.

Para `λ2=5`: `(A−5I)v=0` → `[[−1,2],[3,−6]]v=0` → `−a+2b=0` → `v2=(2,1)`.

**Solución general:** `X(t) = c1·(1,−3)·e^(−2t) + c2·(2,1)·e^(5t)`.

Los autovalores son reales de signos opuestos → punto crítico de tipo silla (ver
[[clasificacion-puntos-criticos-sistemas-lineales]]): las trayectorias se acercan al origen por
la dirección `(1,−3)` (autovalor negativo) y se alejan por `(2,1)` (autovalor positivo).

## Conexión con otros conceptos

- [[sistemas-edo-primer-orden]] — vía alternativa a resolver pasando por una ecuación de 2º
  orden; ambos métodos dan el mismo resultado.
- [[autovalores-complejos]] — cuando el discriminante `tr(A)²−4|A|` es negativo, los autovalores
  son complejos conjugados y hace falta la fórmula de Euler (nota separada).
- [[clasificacion-puntos-criticos-sistemas-lineales]] — el signo y tipo de los autovalores
  determina directamente el tipo de punto crítico (nodo, silla, espiral, centro...) y su
  estabilidad.
- [[sistemas-casi-lineales-estabilidad]] — este método lineal es la base de la linealización de
  sistemas no lineales cerca de un punto crítico (vía matriz Jacobiana).

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmula sin verificar condiciones): la fórmula rápida `λ²−tr(A)λ+|A|=0`
  solo vale para matrices `2×2` — no generaliza directamente a sistemas de 3 o más ecuaciones sin
  matices adicionales.
- **Patrón 4** (confundir cocientes/relaciones parecidas): es fácil trastocar qué autovector
  corresponde a qué autovalor al escribir la solución final, sobre todo bajo presión de examen.
  Verifica siempre sustituyendo `Av = λv` con los valores concretos antes de dar la solución por
  buena (Patrón 7: no valides un resultado solo porque "parece razonable").

## Relevancia en examen

**Alta.** El método de autovalores para resolver sistemas `X'=AX` con autovalores reales
distintos es la base de casi todos los ejercicios de sistemas lineales en segundos parciales y
finales (PEP2 19-12-2025 ejercicio 2, ejercicios tema 2, Problemas Tema 3): se pide resolver el
sistema, dibujar el plano fase, y describir el comportamiento a largo plazo y en etapas
tempranas. Vale típicamente 2-3 puntos.
