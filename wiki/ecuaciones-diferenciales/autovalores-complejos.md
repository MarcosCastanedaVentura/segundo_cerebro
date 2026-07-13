---
titulo: "Autovalores complejos en sistemas lineales: espirales y centros"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 5 - Sistemas de ecuaciones diferenciales lineales"
tipo: "procedimiento"
relacionado: ["autovalores-autovectores-sistemas-lineales", "clasificacion-puntos-criticos-sistemas-lineales", "edo-lineales-segundo-orden-homogeneas"]
patrones_error: [3, 2]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 5.2)", "2025:12:19_PEP2 Alimentaria (solución).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Cuando la ecuación característica `λ² − tr(A)λ + |A| = 0` de un sistema `X'=AX` tiene
discriminante negativo, los autovalores son un par complejo conjugado `λ = a ± bi`. Las
soluciones ya no son exponenciales reales puras, sino que combinan una exponencial real `e^(at)`
(que hace crecer o decrecer el radio) con senos y cosenos de frecuencia `b` (que hacen girar la
trayectoria) — geométricamente, **espirales** (si `a≠0`) o **centros** (elipses, si `a=0`).

## Por qué / de dónde viene

El autovector asociado a un autovalor complejo `λ=a+bi` es también complejo: `v = u + i·w`. La
solución candidata `X1 = v·e^(λt)` es entonces una función compleja de `t`, pero como el sistema
original es real, tanto la parte real como la parte imaginaria de `X1` son, cada una por
separado, soluciones reales del sistema — y son linealmente independientes entre sí. Para
separarlas se usa la **fórmula de Euler** `e^(ibt) = cos(bt) + i·sen(bt)`, que sale de comparar
la serie de Taylor de `e^x` evaluada en `x=ibt` con las series de `cos` y `sen`.

## Fórmula / procedimiento

1. Hallar `λ = a ± bi` resolviendo la ecuación característica (discriminante negativo).
2. Hallar el autovector complejo `v` asociado a **uno** de los dos autovalores (el conjugado da
   la misma información, no hace falta repetir el cálculo).
3. Calcular `v·e^(λt) = v·e^(at)·(cos(bt) + i·sen(bt))` y separar en parte real `Re` e
   imaginaria `Im`.
4. La solución general real es `X(t) = c1·Re + c2·Im`.
5. Para saber el sentido de giro (horario/antihorario), evaluar `A·(1,0)` (el vector tangente en
   un punto de referencia como `(1,0)`) y ver hacia qué cuadrante apunta.
6. Clasificar: si `a=0` → **centro** (elipses, estable pero no asintóticamente); si `a<0` →
   **espiral sumidero** (asintóticamente estable); si `a>0` → **espiral fuente** (inestable).

## Ejemplo resuelto

*Adaptado de 2025:12:19_PEP2 Alimentaria (solución).pdf, ejercicio 1.* Un sensor responde a
`x'' + 2x' + 5x = 0`. Como sistema (`x1=x`, `x2=x'`): `X' = [[0,1],[−5,−2]]·X`.

Ecuación característica: `λ² + 2λ + 5 = 0` → `λ = −1 ± 2i`.

Autovector para `λ=−1+2i`: de `(1−2i)v1 + v2 = 0` → `v2=(−1+2i)v1` → `v = (1, −1+2i)`.

```
v·e^(λt) = e^(−t)·[(cos2t, −cos2t−2sen2t) + i·(sen2t, 2cos2t−sen2t)]
```

Solución general: `X(t) = e^(−t)·[c1·(cos2t, −cos2t−2sen2t) + c2·(sen2t, 2cos2t−sen2t)]`, y en
particular `x(t) = e^(−t)·(c1·cos2t + c2·sen2t)`.

Vector tangente en `(1,0)`: `A·(1,0) = (0,−5)`, apunta hacia abajo → giro **horario**.

Como `a=−1<0`: **espiral sumidero, asintóticamente estable.**

## Conexión con otros conceptos

- [[autovalores-autovectores-sistemas-lineales]] — mismo procedimiento general, pero aquí el
  discriminante es negativo y hace falta separar parte real/imaginaria en vez de usar
  autovectores reales directamente.
- [[edo-lineales-segundo-orden-homogeneas]] — la fórmula de Euler y la forma
  `e^(ax)(c1 cos bx + c2 sen bx)` son idénticas a las de raíces complejas de una ecuación de 2º
  orden; son el mismo cálculo visto desde dos formalismos distintos.
- [[clasificacion-puntos-criticos-sistemas-lineales]] — los autovalores complejos dan siempre
  espirales (parte real ≠0) o centros (parte real =0), nunca nodos ni sillas.

## Errores frecuentes de Marcos aquí

- **Patrón 2** (confundir operadores parecidos): confundir la parte real `a` (que decide
  estabilidad: sumidero si `a<0`, fuente si `a>0`) con la parte imaginaria `b` (que decide la
  velocidad angular de giro pero no la estabilidad). Antes de clasificar, verbaliza cuál de las
  dos partes decide qué.
- **Patrón 3** (aplicar fórmula sin verificar condiciones): calcular el sentido de giro sin
  evaluar realmente `A·v` en un punto de referencia, sino "a ojo" — siempre evalúa `A` sobre un
  vector concreto (típicamente `(1,0)`) para verificarlo, no lo intuyas.

## Relevancia en examen

**Alta.** Los autovalores complejos son, junto con los sistemas casi-lineales, el bloque más
preguntado en segundos parciales y finales: PEP2 19-12-2025, 20_12_23_2parcial,
Alimentaria_19_12_22, FINAL 2_JULIO_2025 (ejercicio 3), FInal17_1_25. El patrón casi fijo es:
resolver por autovalores, identificar tipo y sentido de giro del plano fase, y comprobar
consistencia con la solución obtenida transformando a ecuación de 2º orden. Vale típicamente 3
puntos.
