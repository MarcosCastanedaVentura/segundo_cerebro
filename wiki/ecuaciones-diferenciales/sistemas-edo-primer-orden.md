---
titulo: "Transformación entre EDO de 2º orden y sistemas de 2 ecuaciones de 1er orden"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 4 - Introducción a los sistemas de ecuaciones diferenciales"
tipo: "procedimiento"
relacionado: ["edo-lineales-segundo-orden-homogeneas", "autovalores-autovectores-sistemas-lineales", "autovalores-complejos"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 4.1-4.2)", "PEP2 19-12-2025", "FINAL 2_JULIO_2025 - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Cualquier EDO de orden `n` se puede reescribir como un sistema equivalente de `n` ecuaciones de
primer orden, y viceversa: un sistema de 2 ecuaciones de primer orden se puede reducir a **una**
ecuación de segundo orden en una sola variable. Ambas representaciones describen exactamente lo
mismo — la elección de cuál usar es una cuestión de conveniencia según lo que pida el ejercicio
(resolver por raíces características o por autovalores/autovectores).

## Por qué / de dónde viene

Dada `x'' + px' + qx = 0`, si se define la nueva variable `y = x'` (la velocidad, si `x` es
posición), entonces `y' = x''= −qx − py`. El sistema resultante:

```
x' = y
y' = −qx − py
```

es equivalente a la ecuación original. Al revés: dado un sistema `x'=f(x,y)`, `y'=g(x,y)`, se
deriva la primera ecuación y se sustituye `y'` (o `y`) usando la segunda ecuación, hasta dejar
todo en función de `x`, `x'`, `x''` — eliminando `y`.

## Fórmula / procedimiento

**De ecuación a sistema:** con `x'=y`, la ecuación `x''+px'+qx=0` se convierte en el sistema de
arriba, cuya matriz es `[[0,1],[−q,−p]]`.

**De sistema a ecuación:** dado `x'=f(x,y)`, `y'=g(x,y)`:
1. Derivar la primera ecuación: `x'' = f_x·x' + f_y·y'` (o simplemente derivar si `f` es lineal).
2. Sustituir `y'` por la segunda ecuación del sistema.
3. Despejar `y` de la primera ecuación (si `x'` depende de `y` de forma sencilla) y sustituirla
   también, dejando una única ecuación en `x` (de 2º orden, coeficientes constantes si el sistema
   era lineal).
4. Resolver esa ecuación de 2º orden y luego recuperar `y(t)` a partir de la relación `y = ...`
   obtenida en el paso 3.

## Ejemplo resuelto

*Adaptado de Apuntes de ecuaciones diferenciales.pdf, secc. 4.1, Ejemplo 1.* Dado el sistema
`x' = −2y`, `y' = (1/2)x`, con `x(0)=2`, `y(0)=0`.

Derivando la primera ecuación y sustituyendo la segunda: `x'' = −2y' = −2·(1/2)x = −x` →
`x'' + x = 0`.

Ecuación característica `r²+1=0` → `r=±i` → `x(t) = A·cos t + B·sen t`.

De la primera ecuación del sistema, `y = −(1/2)x' = −(1/2)(−A sen t + B cos t)`.

Con `x(0)=2`: `A=2`. Con `y(0)=0`: `−(1/2)B=0` → `B=0`.

**`x(t) = 2·cos t`, `y(t) = sen t`.** Eliminando `t`: `(x/2)² + y² = 1` — la trayectoria es una
elipse en el plano fase.

## Conexión con otros conceptos

- [[edo-lineales-segundo-orden-homogeneas]] — resolver el sistema pasa siempre por resolver una
  ecuación de 2º orden con las mismas 3 casuísticas (raíces reales distintas/dobles/complejas).
- [[autovalores-autovectores-sistemas-lineales]] y [[autovalores-complejos]] — la vía alternativa
  (y la que más se usa en la práctica con matrices) es resolver el sistema directamente con
  autovalores/autovectores de la matriz de coeficientes, sin pasar por la ecuación de 2º orden.
- [[clasificacion-puntos-criticos-sistemas-lineales]] — una vez resuelto, el tipo de trayectoria
  (elipse, espiral, hipérbola...) se identifica con la clasificación de puntos críticos.

## Errores frecuentes de Marcos aquí

**Patrón 5** (orden incorrecto en procedimientos con norma estricta): al pasar de sistema a
ecuación de 2º orden es fácil equivocar el orden de sustitución — hay que derivar **primero** la
ecuación que define la variable que se quiere aislar, y solo **después** sustituir usando la otra
ecuación del sistema. Invertir el orden (sustituir antes de derivar) lleva a una ecuación
inconsistente. Verifica explícitamente qué ecuación derivas primero antes de escribir nada.

## Relevancia en examen

**Alta.** La transformación en ambas direcciones aparece en prácticamente todos los segundos
parciales y finales como parte de un ejercicio de sistemas (PEP2 19-12-2025, EDO_Primer_Control,
ejercicios tema 2, FINAL 2_JULIO_2025): normalmente el enunciado da un sistema de 2 ecuaciones y
pide "resolver transformándolo en una ecuación de 2º orden", verificar el tipo de trayectorias
(elipses, hipérbolas, circunferencias), y dibujar el plano fase. Vale típicamente 2-3 puntos.
