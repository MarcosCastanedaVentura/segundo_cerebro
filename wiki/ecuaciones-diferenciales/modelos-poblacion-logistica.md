---
titulo: "Modelos de población: crecimiento exponencial, ecuación logística y estabilidad de equilibrios"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 2 - Modelos matemáticos y estabilidad de EDOs autónomas de primer orden"
tipo: "concepto"
relacionado: ["edo-separables", "edo-conceptos-generales", "sistemas-casi-lineales-estabilidad", "modelos-ecologicos-depredador-presa-competencia"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 2.1-2.3)", "ECUACIONES DI28octubre24 soluciones.pdf", "FINAL 2_JULIO_2025 - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El modelo general de población es `dP/dt = (β−δ)P`, donde `β` es la tasa de natalidad y `δ` la
de mortalidad (ambas por individuo y por unidad de tiempo). Si ambas son constantes, se obtiene
crecimiento exponencial simple `P = P0·e^(kt)`. Si la natalidad decrece linealmente con la
población (`β = β0 − β1·P`, recursos limitados), se obtiene la **ecuación logística**:

```
dP/dt = kP(M − P)
```

donde `M` es la **capacidad de carga** o nivel de saturación del entorno.

## Por qué / de dónde viene

En una población real la tasa de crecimiento no puede mantenerse constante indefinidamente
porque los recursos (alimento, espacio) son limitados: cuantos más individuos hay, menos
recursos por individuo y menor la tasa neta de crecimiento. Escribir la tasa de nacimientos como
una función que decrece linealmente con `P` es la forma más simple de capturar ese freno, y da
lugar de forma natural al término `−P²` que hace que la ecuación deje de ser separable de forma
trivial (crecimiento puro) y pase a tener dos puntos de equilibrio.

## Fórmula / procedimiento

**Puntos críticos y estabilidad de una EDO autónoma `dx/dt = f(x)`:**
1. Los puntos críticos son las raíces de `f(x) = 0` (soluciones de equilibrio: si `x(t0)=c`
   entonces `x(t)=c` para todo `t`).
2. Para saber si un punto crítico `x=c` es estable o inestable, estudiar el signo de `f(x)` a
   ambos lados de `c`: si las trayectorias vecinas se acercan a `c` cuando `t→∞`, es estable
   (sumidero); si se alejan, inestable (fuente).
3. En la ecuación logística `dP/dt = kP(M−P)` con `k>0`: `P=0` es inestable (fuente) y `P=M` es
   estable (sumidero) — cualquier población que empiece por debajo de `M` crece hacia `M`, y
   cualquiera por encima decrece hacia `M`.

**Solución de la ecuación logística** (por separación de variables + fracciones parciales):

```
P(t) = M·P0 / (P0 + (M−P0)·e^(−kMt))
```

## Ejemplo resuelto

*Adaptado de ECUACIONES DI28octubre24 soluciones.pdf, ejercicio 4.* Una población de conejos
crece según `P' = P − 0.001P²`, con `P(0) = 50` (tiempo en meses).

Sacando factor común: `P' = 0.001·P·(1000 − P)` → modelo logístico con `k = 0.001`, `M = 1000`.

Resolviendo por fracciones parciales (`1/[P(1000−P)] = (1/1000)[1/P + 1/(1000−P)]`) se llega a:

```
P(t) = 1000 / (1 + 19·e^(−t))
```

(la constante `19` sale de imponer `P(0)=50`). Comprobación: `P(0)=1000/20=50` ✓.
`P(3) = 1000/(1+19e^-3) ≈ 514` conejos. `P(12) ≈ 999.9 ≈ 1000` — la población se aproxima a la
capacidad de carga en aproximadamente un año.

## Conexión con otros conceptos

- [[edo-separables]] — la ecuación logística se resuelve con la misma técnica de separación de
  variables, solo que la integral en `P` requiere descomponer en fracciones parciales.
- [[sistemas-casi-lineales-estabilidad]] — el análisis de estabilidad de un punto crítico aquí
  (mirar el signo de `f` a ambos lados) es la versión en 1 dimensión de lo que en sistemas de 2
  ecuaciones se hace con la matriz Jacobiana y sus autovalores.
- [[modelos-ecologicos-depredador-presa-competencia]] — el término logístico `kx(M−x)` reaparece
  como la parte de "crecimiento acotado por separado" en los modelos de especies compitiendo.
- Conexión con Bioquímica/Microbiología Alimentaria: la curva de crecimiento microbiano en un
  alimento (fase exponencial → fase estacionaria) es exactamente una curva logística — mismo
  modelo matemático, distinto nombre de las constantes.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): antes de aplicar la fórmula cerrada de
la logística hay que comprobar que la ecuación realmente tiene la forma `kP(M−P)` — a veces el
enunciado da la ecuación ya en la forma `aP − bP²` y hay que sacar `k=b` y `M=a/b` factorizando
primero, no directamente por comparación visual apresurada.

## Relevancia en examen

**Alta.** El modelo logístico (población de peces, lagartos, conejos, insectos, bacterias) es
uno de los ejercicios más recurrentes de toda la asignatura: aparece en 1parcial18_19,
ECUACIONES DI28octubre24, Examen Ordinario IA solución, FINAL 2_JULIO_2025,
PROBLEMAS_TEMA1_COMPLEMENTARIOS, y varios más. El patrón de preguntas es casi siempre el mismo:
(a) identificar el modelo y sus parámetros `k`, `M`; (b) puntos críticos y estabilidad/diagrama
de fase; (c) resolver el PVI completo; (d) evaluar en un instante concreto o hallar cuándo se
alcanza cierta población. Vale típicamente 2-3 puntos.
