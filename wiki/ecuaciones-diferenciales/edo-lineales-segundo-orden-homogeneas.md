---
titulo: "EDOs lineales de segundo orden homogéneas con coeficientes constantes"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 3 - Ecuaciones lineales de segundo orden"
tipo: "procedimiento"
relacionado: ["edo-lineales-segundo-orden-completas", "sistemas-edo-primer-orden", "autovalores-complejos"]
patrones_error: [3, 2]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 3.1)", "20_12_23_2parcial - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una ecuación `ay'' + by' + cy = 0` con `a,b,c` constantes es lineal, homogénea y de segundo
orden. Su solución general es siempre combinación lineal `y = c1·y1 + c2·y2` de dos soluciones
independientes entre sí (principio de superposición), y esas dos soluciones se obtienen a partir
de las raíces de la **ecuación característica** `ar² + br + c = 0`.

## Por qué / de dónde viene

Probar `y = e^(rx)` como solución candidata es natural porque la exponencial es la única función
cuya derivada es proporcional a sí misma. Sustituyendo `y=e^(rx)` en la ecuación y sacando
factor común `e^(rx)` (que nunca es cero), toda la ecuación diferencial colapsa en una ecuación
algebraica de segundo grado en `r`: la ecuación característica. El tipo de raíces que tenga esa
ecuación de segundo grado determina completamente la forma de la solución.

## Fórmula / procedimiento

1. Escribir la ecuación característica `ar² + br + c = 0` y resolverla.
2. Según el tipo de raíces:

| Tipo de raíces | Solución general |
|---|---|
| Reales distintas `r1 ≠ r2` | `y = c1·e^(r1·x) + c2·e^(r2·x)` |
| Real doble `r1 = r2 = r` | `y = (c1 + c2·x)·e^(rx)` |
| Complejas conjugadas `r = a ± bi` | `y = e^(ax)·(c1·cos(bx) + c2·sen(bx))` |

3. Si hay condiciones iniciales `y(x0)`, `y'(x0)`, sustituir en `y` y en `y'` para hallar `c1, c2`.

## Ejemplo resuelto

*Adaptado de Apuntes de ecuaciones diferenciales.pdf, sección 3.1.2 (raíz doble).* Resolver el
PVI `y'' + 2y' + y = 0`, `y(0)=5`, `y'(0)=−3`.

Ecuación característica: `r² + 2r + 1 = (r+1)² = 0` → raíz doble `r = −1`.

Solución general: `y(x) = (c1 + c2·x)·e^(−x)`.

`y(0) = c1 = 5`. Derivando: `y'(x) = (c2 − c1 − c2·x)·e^(−x)` → `y'(0) = c2 − c1 = −3` →
`c2 = c1 − 3 = 2`.

**Solución particular: `y(x) = (5 + 2x)·e^(−x)`.**

## Conexión con otros conceptos

- [[edo-lineales-segundo-orden-completas]] — cuando el lado derecho no es cero (ecuación
  "completa"), la solución de la homogénea de esta nota es la primera mitad del resultado.
- [[sistemas-edo-primer-orden]] — toda ecuación de 2º orden se puede transformar en un sistema
  de dos ecuaciones de primer orden (`x1=y, x2=y'`), y la ecuación característica de la matriz de
  ese sistema es exactamente la misma que la de aquí.
- [[autovalores-complejos]] — el caso de raíces complejas usa la misma fórmula de Euler que el
  caso de autovalores complejos en sistemas de 2 ecuaciones.
- Aplicación directa: vibraciones mecánicas (muelle-masa-amortiguador) y circuitos RLC — ambos
  dan ecuaciones de este tipo y son el contexto casi universal en los exámenes de esta
  asignatura (ver ejemplo de amortiguamiento en `Apuntes...pdf` secc. 3.4.2).

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmula sin verificar condiciones): usar la fórmula de raíces reales
  distintas cuando en realidad la raíz es doble (discriminante cero) da una solución con solo
  una constante libre — no se pueden imponer las dos condiciones iniciales. Comprueba siempre el
  signo del discriminante `b²−4ac` antes de elegir la fórmula.
- **Patrón 2** (confundir operadores/fórmulas parecidas): la fórmula de raíz doble
  `(c1+c2x)e^(rx)` y la de raíces complejas `e^(ax)(c1 cos bx + c2 sen bx)` se parecen en
  estructura (un factor exponencial multiplicando una combinación de dos funciones) y es fácil
  mezclarlas bajo presión de examen — verbaliza primero qué tipo de raíz tienes antes de escribir
  la fórmula.

## Relevancia en examen

**Alta.** Casi todo segundo parcial/PEP2 y final incluye un ejercicio de resolver una ecuación de
2º orden homogénea (a menudo interpretada como un sistema masa-muelle-amortiguador, ver
20_12_23_2parcial, Alimentaria_19_12_22, PEP2 19/12/2025): pide resolver el PVI, interpretar
físicamente los coeficientes, y clasificar el tipo de movimiento (sobreamortiguado, crítico,
subamortiguado, armónico simple) según el signo del discriminante. Vale típicamente 3 puntos.
