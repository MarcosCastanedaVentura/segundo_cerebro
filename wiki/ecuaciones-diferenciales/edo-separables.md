---
titulo: "EDOs separables y aplicaciones (enfriamiento, crecimiento/decaimiento)"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 1 - Ecuaciones diferenciales de primer orden"
tipo: "procedimiento"
relacionado: ["edo-conceptos-generales", "edo-lineales-primer-orden", "modelos-poblacion-logistica"]
patrones_error: [3, 6]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 1.5)", "EDO_Examen_Julio.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una EDO de primer orden `dy/dx = H(x,y)` es **separable** si se puede reescribir como
`dy/dx = g(x)·f(y)`, es decir, si el lado derecho se puede factorizar en una parte que solo
depende de `x` y otra que solo depende de `y`. Entonces todas las `y` se pasan a un lado y todas
las `x` al otro, y se integra cada lado por separado.

## Por qué / de dónde viene

Un enorme número de leyes físicas y biológicas tienen la forma "la tasa de cambio de una
magnitud es proporcional a (una función de) ella misma o a una diferencia con un valor de
referencia": desintegración radiactiva, interés compuesto, enfriamiento de Newton, ley de
Torricelli, crecimiento poblacional simple. En todos estos casos la ecuación resultante es
separable casi por construcción, porque el modelo dice literalmente "la derivada es una
constante por una función de la variable dependiente".

## Fórmula / procedimiento

1. Escribir la ecuación como `dy/f(y) = g(x) dx` (dividir por `f(y)`, cuidado con los valores
   donde `f(y) = 0`: pueden dar soluciones singulares, ver [[edo-conceptos-generales]]).
2. Integrar ambos lados por separado: `∫ dy/f(y) = ∫ g(x) dx + C`.
3. Si hay condición inicial, sustituir para hallar `C` y obtener la solución particular.
4. Despejar `y` explícitamente si es posible (no siempre lo es: queda a veces en forma
   implícita).

## Ejemplo resuelto

*Adaptado de EDO_Examen_Julio.pdf (Prueba Global 2 de julio de 2019), ejercicio 2 — ley de
enfriamiento de Newton aplicada a la elaboración de helado.* Una mezcla láctea a 40 °C se
introduce en un congelador a −20 °C. El helado está listo para la venta al alcanzar −4 °C, lo
que ocurre al cabo de 1 hora. ¿Cuánto tardará en llegar a la temperatura de conservación de
−18 °C?

La ley de Newton: `dT/dt = k(A − T)`, con `A = −20`. Separando variables:
`dT/(A−T) = k dt` → `−ln|A−T| = kt + C` → `T(t) = A + (T0 − A)e^(−kt)`, con `T0 = 40`:

```
T(t) = −20 + 60·e^(−kt)
```

Con `T(1) = −4`: `−4 = −20 + 60e^(−k)` → `e^(−k) = 16/60` → `k = ln(60/16) ≈ 1.322`.

Para `T = −18`: `−18 = −20 + 60e^(−1.322t)` → `e^(−1.322t) = 2/60 = 1/30` →
`t = ln(30)/1.322 ≈ 2.57 h` (≈ 2 h 34 min).

## Conexión con otros conceptos

- [[edo-conceptos-generales]] — comprobar existencia/unicidad antes de separar variables.
- [[edo-lineales-primer-orden]] — muchas ecuaciones de mezclas son lineales, no separables;
  clasificar bien es el primer paso (ver Patrón 3 abajo).
- [[modelos-poblacion-logistica]] — la ecuación logística también se resuelve por separación de
  variables, con fracciones parciales en vez de una integral directa.
- Base directa de Ingeniería del Calor/Frío (cinética de enfriamiento/congelación de alimentos)
  y Operaciones Unitarias I/II (transferencia de calor, secado): el mismo modelo `dT/dt = k(A−T)`
  reaparece allí con nombre de "ley de enfriamiento" o "aproximación de primer orden".

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmulas sin verificar condiciones): antes de separar variables hay que
  comprobar que la ecuación realmente se factoriza como `g(x)·f(y)` — si no se puede separar
  (por ejemplo si aparece una suma `x+y` dentro de una raíz o un logaritmo mezclando ambas
  variables), no es aplicable este método y hay que clasificarla como lineal o exacta primero.
- **Patrón 6** (copiar mal datos del enunciado): en problemas de enfriamiento es fácil confundir
  la temperatura ambiente `A` con la inicial `T0`, o invertir el signo de `k`. Verifica siempre
  cuál de los dos números dados es la temperatura del entorno (constante) y cuál la del objeto en
  `t=0` antes de sustituir.

## Relevancia en examen

**Alta.** Presente en casi todos los primeros parciales/PEP1 (noviembre/octubre): 1parcial18_19,
EDO_Examen_Julio, ECUACIONES DI28octubre24, 20251030_EcuaDif_Solución. Los contextos típicos son
enfriamiento de un producto alimentario (café, helado, cadáver en criminología — sí, aparece
literalmente como "determinar la hora de la muerte"), desintegración/eliminación de fármacos, y
crecimiento exponencial simple de poblaciones. Vale típicamente 1.5-2 puntos sobre 10.
