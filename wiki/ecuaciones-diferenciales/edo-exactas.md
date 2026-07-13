---
titulo: "EDOs exactas y criterio de exactitud"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 1 - Ecuaciones diferenciales de primer orden"
tipo: "procedimiento"
relacionado: ["edo-conceptos-generales", "edo-separables", "edo-lineales-primer-orden"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 1.7)", "20251030_EcuaDif_Solución.pdf", "EC DIF 1_6.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una ecuación escrita en forma diferencial `M(x,y)dx + N(x,y)dy = 0` es **exacta** si existe una
función `F(x,y)` tal que `∂F/∂x = M` y `∂F/∂y = N`. En ese caso la solución general es
simplemente `F(x,y) = C` (la ecuación es la diferencial total `dF = 0` de una función que ya
existe, solo hay que "reconstruirla").

## Por qué / de dónde viene

Si `y(x)` está definida implícitamente por `F(x,y) = C`, derivando ambos lados respecto de `x`
sale automáticamente `Fx + Fy·y' = 0`, que es la forma `M dx + N dy = 0` con `M = Fx`, `N = Fy`.
El criterio para saber si una `M dx + N dy = 0` dada viene de una `F` así es que las derivadas
cruzadas coincidan: `∂M/∂y = ∂²F/∂y∂x = ∂²F/∂x∂y = ∂N/∂x`. Esto es solo el teorema de Schwarz
(igualdad de derivadas parciales mixtas) aplicado al revés: si las cruzadas no coinciden, no
puede existir tal `F`.

## Fórmula / procedimiento

1. Identificar `M(x,y)` y `N(x,y)` en `M dx + N dy = 0`.
2. Comprobar el criterio de exactitud: `∂M/∂y = ∂N/∂x`. Si no se cumple, la ecuación **no** es
   exacta (a veces se puede convertir con un factor integrante, pero eso queda fuera de lo
   habitual en esta asignatura).
3. Integrar `M` respecto de `x`: `F(x,y) = ∫M dx + g(y)`, donde `g(y)` es una "constante" de
   integración que puede depender de `y`.
4. Derivar ese `F` respecto de `y`, igualar a `N`, y despejar `g'(y)` — el resultado solo debe
   depender de `y` (si depende de `x` también, algo se calculó mal).
5. Integrar `g'(y)` para obtener `g(y)`, sustituir en `F`, y la solución general es `F(x,y) = C`.

## Ejemplo resuelto

*Adaptado de 20251030_EcuaDif_Solución.pdf, ejercicio 1.* Resolver `(x+y)y' = x−y`.

Reescrita en forma diferencial: `(y−x)dx + (x+y)dy = 0`, con `M = y−x`, `N = x+y`.

Criterio: `∂M/∂y = 1 = ∂N/∂x` ✓ exacta.

`F(x,y) = ∫(y−x)dx + g(y) = xy − x²/2 + g(y)`.

Derivando respecto de `y` e igualando a `N`: `x + g'(y) = x + y` → `g'(y) = y` → `g(y) = y²/2`.

Solución general: **`xy − x²/2 + y²/2 = C`**.

## Conexión con otros conceptos

- [[edo-separables]] y [[edo-lineales-primer-orden]] — clasificar el tipo de EDO es siempre el
  primer paso; una misma ecuación puede a veces resolverse por más de un método (separando
  variables o viéndola como exacta), y en examen a veces piden explícitamente decir de qué tipo
  o tipos es antes de resolver.
- [[edo-conceptos-generales]] — el criterio de exactitud usa el mismo tipo de razonamiento con
  derivadas parciales que el teorema de existencia y unicidad (continuidad de derivadas
  parciales en un rectángulo).

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): es muy tentador lanzarse a
integrar `M` respecto de `x` sin comprobar antes `∂M/∂y = ∂N/∂x`. Si la ecuación no es exacta y
se aplica el procedimiento igualmente, se obtiene una `g(y)` que en realidad depende también de
`x` — eso es la señal de alarma de que el criterio falló y hay que parar y reclasificar la
ecuación (probar si es lineal o separable en su lugar).

## Relevancia en examen

**Media.** Aparece en la mayoría de primeros parciales como un apartado de "resolver aplicando
alguno de los métodos posibles" donde se pide identificar el tipo de ecuación (separable, lineal
o exacta) antes de resolver — ver 20251030_EcuaDif_Solución y FINAL 2_JULIO_2025 (ejercicio 1,
donde una misma ecuación resulta ser a la vez exacta y lineal). Vale típicamente 1.5-2 puntos.
