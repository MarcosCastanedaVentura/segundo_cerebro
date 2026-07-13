---
titulo: "Conceptos generales de EDOs: orden, solución, PVI, existencia y unicidad"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 1 - Ecuaciones diferenciales de primer orden"
tipo: "concepto"
relacionado: ["edo-separables", "edo-lineales-primer-orden", "edo-exactas", "sistemas-casi-lineales-estabilidad"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 1.1-1.4)", "ECUACIONES DI28octubre24 soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una **ecuación diferencial ordinaria (EDO)** relaciona una función desconocida de una sola
variable independiente con una o más de sus derivadas: `F(x, y, y', y'', ..., y^(n)) = 0`. El
**orden** de la ecuación es el de la derivada más alta que aparece. Si la función desconocida
dependiera de varias variables (derivadas parciales) sería una EDP, no una EDO — toda esta
asignatura trabaja solo con EDOs.

- **Solución general**: familia de soluciones que contiene una (o varias) constante(s)
  arbitraria(s) `C`.
- **Solución particular**: la que se obtiene fijando `C` mediante una condición inicial.
- **Solución singular**: solución que cumple la ecuación pero que NO se puede obtener dando
  ningún valor a `C` en la solución general (solo aparece en ecuaciones no lineales).
- **Problema de valor inicial (PVI)**: la EDO junto con una condición `y(x0) = y0`.

## Por qué / de dónde viene

Casi cualquier ley física expresada como "la tasa de cambio de algo depende del propio algo"
(enfriamiento, población, descarga de un depósito, muelles, circuitos) se traduce directamente
en una EDO. Antes de intentar resolver una, hay que saber **si tiene solución y si es única**,
porque si no lo es, cualquier método de resolución puede dar una respuesta incompleta o
engañosa — esto es exactamente lo que comprueba el teorema de existencia y unicidad.

## Fórmula / procedimiento

**Teorema de existencia y unicidad (EDO de 1er orden).** Dado el PVI `y' = f(x,y)`, `y(x0) = y0`:
si `f(x,y)` **y** `∂f/∂y` son continuas en un rectángulo que contiene a `(x0, y0)`, entonces
existe una única solución definida en algún intervalo abierto que contiene a `x0`.

Procedimiento antes de resolver cualquier PVI:
1. Escribir `f(x,y)` explícitamente.
2. Comprobar que `f` es continua en el punto de interés.
3. Calcular `∂f/∂y` y comprobar que también es continua ahí.
4. Solo si ambas condiciones se cumplen, el teorema garantiza solución única — si falla alguna,
   el teorema simplemente no dice nada (no significa que no haya solución, hay que mirar caso a
   caso).

## Ejemplo resuelto

*Adaptado de ECUACIONES DI28octubre24 soluciones.pdf, ejercicio 1.* Dada `y' = ∛y` (raíz
cúbica de `y`), estudiar existencia/unicidad en `y(0) = 0` y en `y(0) = 1`.

`f(x,y) = y^(1/3)` es continua en todo el plano, incluido `y = 0`. Pero
`∂f/∂y = (1/3)y^(-2/3)`, que **no** es continua en `y = 0` (se dispara a infinito).

- En `(0, 1)`: ambas `f` y `∂f/∂y` son continuas → solución única. Resolviendo por separación de
  variables, `∫y^(-1/3) dy = ∫dx` → `(3/2)y^(2/3) = x + C`; con `y(0)=1` sale `C = 3/2`, y la
  solución particular es `(3/2)∛(y²) − x = 3/2`.
- En `(0, 0)`: falla la continuidad de `∂f/∂y` → el teorema no garantiza nada. De hecho hay al
  menos dos soluciones que pasan por `(0,0)`: la solución singular `y = 0` y la que sale de la
  familia general — no hay unicidad.

## Conexión con otros conceptos

- [[edo-separables]], [[edo-lineales-primer-orden]], [[edo-exactas]] — antes de aplicar
  cualquiera de estos tres métodos conviene tener claro si el PVI tiene solución única.
- [[sistemas-casi-lineales-estabilidad]] — el teorema de existencia y unicidad se generaliza a
  sistemas autónomos y es la base de por qué las trayectorias en el plano fase nunca se cruzan.
- Base directa de Operaciones Unitarias I/II e Ingeniería del Calor/Frío (3º-4º curso): cualquier
  balance dinámico que planteéis allí (temperatura, concentración, caudal en función del tiempo)
  es un PVI y se debería verificar la misma existencia/unicidad antes de resolver, aunque en la
  práctica de ingeniería casi siempre se dé por hecho.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): el error típico es comprobar
solo que `f(x,y)` es continua y darse por satisfecho, olvidando comprobar también `∂f/∂y`. Son
dos condiciones independientes y ambas hacen falta para garantizar unicidad — antes de decir
"hay solución única", exige comprobar explícitamente las dos, no solo la primera.

## Relevancia en examen

**Media.** Aparece como primer apartado de un ejercicio (1-1.5 puntos) en varios primeros
parciales (ej. EDO_Primer_Control.pdf 2018-19, ECUACIONES DI28octubre24, FINAL 2_JULIO_2025):
casi siempre pide comprobar existencia/unicidad de un PVI concreto antes de resolverlo. Rara vez
es la parte central del ejercicio, pero perder ese primer apartado por no comprobar `∂f/∂y` es
un fallo barato y frecuente.
