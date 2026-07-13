---
titulo: "Frontera de posibilidades de producción (FPP) y coste de oportunidad"
asignatura: "economia"
tema: "Tema 1 — Introducción a la economía"
tipo: "concepto"
relacionado: ["ventaja-comparativa", "pib-tres-metodos"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["Diapositivas Tema 1.pdf", "EcoProblemas_01_con_solucion.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La **Frontera de Posibilidades de Producción (FPP)** es un modelo que representa, para una economía que solo puede
producir dos bienes, todas las combinaciones máximas de ambos bienes que se pueden obtener utilizando **todos** los
recursos disponibles de forma eficiente y con la tecnología existente.

## Por qué / de dónde viene

Es la forma más simple de representar el principio básico de la economía: **los recursos son escasos y hay que
elegir**. Como los recursos (tierra, trabajo, capital) son limitados, producir más de un bien obliga a renunciar a
producir otro. La FPP traduce esa disyuntiva en una curva.

- **Puntos sobre la curva**: factibles y eficientes (se usan todos los recursos al máximo).
- **Puntos por debajo/dentro de la curva**: factibles pero ineficientes (sobran recursos sin usar, o se usan mal).
- **Puntos fuera de la curva**: no factibles con los recursos y tecnología actuales.
- La FPP suele ser **cóncava** (combada hacia afuera) porque el coste de oportunidad es **creciente**: los primeros
  recursos que se trasladan de un bien a otro son los más productivos en el segundo bien; a medida que se sigue
  trasladando, se usan recursos cada vez menos adecuados, así que cuesta cada vez más del primer bien producir la
  misma cantidad adicional del segundo.
- Un **desplazamiento hacia afuera de toda la FPP** representa crecimiento económico (más recursos o mejor
  tecnología). Una mejora tecnológica que solo afecta a un bien desplaza la FPP de forma asimétrica (gira sobre el
  eje del bien no afectado).

## Fórmula / procedimiento

Si la FPP es lineal, del tipo `Y = a − b·X`:
- **Coste de oportunidad de una unidad más de X** = cuántas unidades de Y hay que sacrificar = la pendiente en valor
  absoluto, `b` (constante si la FPP es una recta; creciente si es cóncava).
- Procedimiento para evaluar un punto (X₀, Y₀):
  1. Sustituir X₀ en la ecuación de la FPP y obtener el Y máximo posible, `Y_max`.
  2. Si `Y₀ = Y_max` → el punto está **sobre la FPP** → factible y eficiente.
  3. Si `Y₀ < Y_max` → el punto está **por debajo** → factible pero ineficiente (sobran recursos).
  4. Si `Y₀ > Y_max` → el punto está **por encima** → no factible con los recursos actuales.

## Ejemplo resuelto

(Adaptado de EcoProblemas_01, Problema 1) Una economía con un solo factor (trabajo) produce bienes X e Y según
`Y = 600 − 3X`.

- Punto A: X=150, Y=150 → con X=150, `Y_max = 600 − 3(150) = 150`. Como Y₀=150=Y_max → **A es eficiente** (está
  sobre la FPP).
- Punto B: X=100, Y=400 → `Y_max = 600 − 3(100) = 300`. Como Y₀=400 > 300 → **B es inalcanzable** (fuera de la FPP).
- Punto C: X=50, Y=300 → `Y_max = 600 − 3(50) = 450`. Como Y₀=300 < 450 → **C es ineficiente** (dentro de la FPP,
  sobran recursos).
- Coste de oportunidad de una unidad adicional de X: la pendiente de la recta es 3, luego producir 1 X más cuesta
  **3 unidades de Y**.
- Si la productividad del trabajo en X sube un 50%, con los mismos recursos se puede producir un 50% más de X para
  cada nivel de Y: la nueva FPP es `Y = 600 − 2X` (el máximo de X pasa de 200 a 300), y el coste de oportunidad de
  una unidad de X baja a **2 unidades de Y** (ahora hace falta menos Y para "liberar" el trabajo necesario para 1 X,
  porque cada trabajador produce más X que antes).

## Conexión con otros conceptos

- [[ventaja-comparativa]]: la FPP de dos individuos/países distintos, comparada, revela quién tiene menor coste de
  oportunidad en qué bien — la base de las ganancias del comercio.
- [[pib-tres-metodos]]: el crecimiento económico (desplazamiento de la FPP hacia afuera) es lo que mide el
  crecimiento del PIB real en macroeconomía.

## Errores frecuentes de Marcos aquí

Ninguno activo documentado en `memory/memory.json` para este concepto. Vigilar el **Patrón 7** (dar por bueno un
resultado que "suena razonable"): al leer combinaciones (X, Y) de un enunciado, verificar siempre sustituyendo en la
ecuación de la FPP antes de clasificar el punto como eficiente/ineficiente/inalcanzable, no "a ojo" sobre un dibujo.

## Relevancia en examen

Alta. Aparece en casi todos los exámenes y PEP como pregunta de teoría (dibujar FPP, señalar puntos A/B/C eficiente-
ineficiente-inalcanzable) y como problema numérico con FPP lineal tipo `Y = a − bX`, pidiendo coste de oportunidad y
efecto de un cambio tecnológico sobre la frontera (ver Ejercicios 1.2, 1.3, 1.4, 1.5 de Diapositivas Tema 1 y
Problema 1 de EcoProblemas_01).
