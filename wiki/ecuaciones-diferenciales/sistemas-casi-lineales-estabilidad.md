---
titulo: "Sistemas casi-lineales: linealización, matriz Jacobiana y estabilidad"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 6 - Sistemas casi lineales"
tipo: "procedimiento"
relacionado: ["clasificacion-puntos-criticos-sistemas-lineales", "autovalores-autovectores-sistemas-lineales", "modelos-ecologicos-depredador-presa-competencia", "modelos-poblacion-logistica"]
patrones_error: [3, 5, 7]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 6.1-6.2)", "Alimentaria_19_12_22 - soluciones.pdf", "FINAL 2_JULIO_2025 - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un sistema **casi-lineal** (o "cuasi-lineal") es un sistema autónomo no lineal
`x'=f(x,y)`, `y'=g(x,y)` que, cerca de un punto crítico aislado, se comporta como un sistema
lineal — el aproximado por la **matriz Jacobiana** de `f, g` evaluada en ese punto. Esto permite
clasificar y estudiar la estabilidad de sistemas no lineales usando exactamente la misma
maquinaria de autovalores que en sistemas lineales, punto crítico a punto crítico.

## Por qué / de dónde viene

Por el desarrollo de Taylor de `f` y `g` alrededor de un punto crítico `(x0,y0)` (donde
`f(x0,y0)=g(x0,y0)=0`), los términos de primer orden dominan sobre el resto cuando `(u,v)` (el
desplazamiento respecto al punto crítico) es pequeño — los términos de orden superior son
despreciables cerca del punto. Esos términos de primer orden forman precisamente la matriz
Jacobiana `J`, y el sistema linealizado resultante `u'=J·u` se comporta cualitativamente igual
que el sistema original **cerca de ese punto**, siempre que los autovalores de `J` no tengan
parte real nula (si la tienen —centro o autovalor cero—, los términos no lineales sí importan y
la linealización no basta para concluir).

## Fórmula / procedimiento

1. Encontrar todos los puntos críticos resolviendo `f(x,y)=0`, `g(x,y)=0` simultáneamente.
2. Calcular la matriz Jacobiana general: `J(x,y) = [[fx, fy], [gx, gy]]`.
3. Para cada punto crítico, evaluar `J` en ese punto → matriz de coeficientes constantes.
4. Clasificar ese punto con autovalores/traza-determinante (ver
   [[clasificacion-puntos-criticos-sistemas-lineales]]).
5. **Teorema de transferencia de estabilidad:** si los autovalores de `J` tienen parte real
   distinta de cero (no son un centro ni cero), el tipo y la estabilidad del sistema linealizado
   se conservan en el sistema no lineal original. Si son imaginarios puros (centro) o hay un
   autovalor cero, la linealización NO permite concluir — los términos no lineales deciden y
   haría falta un análisis aparte (energía, función de Lyapunov, etc., fuera de esta asignatura).

## Ejemplo resuelto

*Adaptado de Apuntes de ecuaciones diferenciales.pdf, secc. 6.2.* Determinar el tipo y
estabilidad del punto crítico `(0,0)` del sistema:

```
dx/dt = 4x + 2y + 2x² − 3y²
dy/dt = 4x − 3y + 7xy
```

Jacobiano general: `J(x,y) = [[4+4x, 2−6y], [4+7y, −3+7x]]`. En `(0,0)`:

```
J(0,0) = [[4, 2], [4, −3]]
```

`tr(J) = 1`, `|J| = 4·(−3) − 2·4 = −20`. Como `|J| < 0`: autovalores reales de signo opuesto.
Confirmando: `λ² − λ − 20 = (λ−5)(λ+4)=0` → `λ=5, −4`.

**El punto `(0,0)` es un punto de silla, inestable** — y como los autovalores no son ni cero ni
imaginarios puros, esta clasificación se transfiere íntegra al sistema no lineal original.

## Conexión con otros conceptos

- [[clasificacion-puntos-criticos-sistemas-lineales]] — la tabla de tipos se aplica idéntica,
  pero al Jacobiano evaluado en cada punto crítico, no a una matriz de coeficientes constantes
  dada directamente.
- [[modelos-ecologicos-depredador-presa-competencia]] — el modelo depredador-presa y el de
  especies compitiendo son los ejemplos casi-lineales más recurrentes en examen; ahí el punto de
  coexistencia de ambas especies es siempre un punto crítico casi-lineal a linealizar.
- [[modelos-poblacion-logistica]] — la logística es la versión en 1 sola ecuación de este mismo
  análisis de estabilidad (allí basta con el signo de `f'(x)` en vez de autovalores de matriz).

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmulas sin verificar condiciones): usar la clasificación lineal
  directamente sin comprobar primero que los autovalores del Jacobiano NO son imaginarios puros
  ni cero — si lo son, la conclusión sobre el sistema no lineal simplemente no está garantizada
  y hay que decirlo explícitamente en vez de dar una respuesta falsa por analogía.
- **Patrón 5** (orden incorrecto en procedimientos con norma estricta): el orden correcto es
  siempre (1) hallar todos los puntos críticos del sistema no lineal completo, (2) calcular el
  Jacobiano **general** (en función de x,y), y solo (3) evaluarlo en cada punto — evaluar antes
  de derivar, o derivar solo parcialmente, es un error de secuencia muy similar al de aplicar
  binario en vez de Gray en Karnaugh: el procedimiento tiene un orden estricto que hay que
  respetar aunque no sea intuitivo.
- **Patrón 7** (dar por bueno un resultado porque "suena razonable"): no asumas que la
  estabilidad de un punto crítico "cerca del origen" es igual a la de otro punto crítico del
  mismo sistema sin evaluar el Jacobiano en cada uno por separado — cada punto crítico tiene su
  propia linealización y puede tener un comportamiento completamente distinto.

## Relevancia en examen

**Alta — junto con autovalores complejos, el bloque más preguntado de toda la asignatura.**
Aparece en casi todos los segundos parciales y finales (PEP2 19-12-2025 ejercicio 3,
Alimentaria_19_12_22 ejercicio 3, 20_12_23_2parcial ejercicio 3, FINAL 2_JULIO_2025 ejercicio 4,
Examen Ordinario IA solución): el patrón fijo es hallar todos los puntos críticos, linealizar en
cada uno, clasificar tipo y estabilidad, dibujar el plano fase local, y explicar si la
clasificación se conserva en el sistema no lineal — a menudo con una interpretación biológica o
industrial del resultado. Vale típicamente 4-5 puntos, el ejercicio de mayor peso del examen.
