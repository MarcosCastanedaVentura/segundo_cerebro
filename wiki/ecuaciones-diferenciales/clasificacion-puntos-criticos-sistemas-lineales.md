---
titulo: "Clasificación de puntos críticos de sistemas lineales: nodos, sillas, espirales, centros"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 5 - Sistemas de ecuaciones diferenciales lineales"
tipo: "concepto"
relacionado: ["autovalores-autovectores-sistemas-lineales", "autovalores-complejos", "sistemas-casi-lineales-estabilidad"]
patrones_error: [3, 5]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 5.4-5.6)", "2025:12:19_PEP2 Alimentaria (solución).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Todo sistema lineal `X'=AX` de 2 ecuaciones tiene un único punto crítico aislado en el origen
(si `|A|≠0`), y el **tipo** de ese punto crítico (cómo se comportan las trayectorias cerca de
él) queda determinado completamente por los autovalores de `A`. Se puede leer directamente de la
**traza** `tr(A)` y el **determinante** `|A|`, sin necesidad de calcular los autovalores
explícitamente primero.

## Por qué / de dónde viene

La ecuación característica de una matriz `2×2` es siempre `λ² − tr(A)·λ + |A| = 0`, así que sus
raíces son `λ = [tr(A) ± √(tr(A)²−4|A|)] / 2`. Todo el comportamiento cualitativo depende del
signo del discriminante `tr(A)²−4|A|` y de los signos de `tr(A)` y `|A|` — por eso se puede
dibujar un mapa completo de tipos de punto crítico en un plano con `tr(A)` en el eje X y `|A|`
en el eje Y, con la parábola `|A| = tr(A)²/4` como frontera entre autovalores reales y complejos.

## Fórmula / procedimiento

| Autovalores | Tipo de punto crítico | Estabilidad |
|---|---|---|
| Reales, mismo signo, distintos | Nodo propio | Sumidero si `λ<0` (estable); fuente si `λ>0` (inestable) |
| Real doble, 1 autovector | Nodo impropio/degenerado | Igual que arriba según signo |
| Real doble, 2 autovectores (A diagonal) | Nodo estrella | Igual que arriba según signo |
| Reales, signos opuestos | Punto de silla | Siempre inestable |
| Complejos `a±bi`, `a≠0` | Espiral | Sumidero si `a<0`; fuente si `a>0` |
| Imaginarios puros `±bi` | Centro (elipses) | Estable, pero NO asintóticamente |
| Un autovalor cero | Rectas paralelas (infinitos puntos críticos) | Según el signo del otro autovalor |

**Atajo con traza y determinante** (sin resolver la ecuación característica):
- `|A| < 0` → autovalores reales de signo opuesto → **siempre punto de silla**.
- `0 < |A| < tr(A)²/4` → autovalores reales del mismo signo → **nodo**, con el signo de `tr(A)`.
- `|A| > tr(A)²/4` → autovalores complejos → **espiral** (o centro si `tr(A)=0`).
- `|A| = tr(A)²/4` → autovalor doble → nodo impropio o estrella.

## Ejemplo resuelto

*Adaptado de 2025:12:19_PEP2 Alimentaria (solución).pdf, ejercicio 2.* Sistema
`X' = [[−3,1],[1,−3]]·X`.

`tr(A) = −6`, `|A| = 9−1 = 8`. Como `0 < 8 < (−6)²/4 = 9`: autovalores reales, mismo signo
(negativo, porque `tr(A)<0`) → **nodo propio sumidero, asintóticamente estable.**

Resolviendo la ecuación característica para confirmar: `λ²+6λ+8=0` → `λ=−2,−4`.
Autovector para `λ=−4`: `v=(1,−1)`. Autovector para `λ=−2`: `v=(1,1)`.

Las trayectorias en etapas tempranas (`t→−∞`) tienden a la dirección del autovalor menor en
valor absoluto invertido; a largo plazo (`t→∞`) se alinean con el autovector del autovalor
dominante (el más cercano a cero en valor absoluto, `λ=−2`, dirección `(1,1)`).

## Conexión con otros conceptos

- [[autovalores-autovectores-sistemas-lineales]] — el cálculo de traza y determinante es un
  atajo sobre este método, útil para clasificar rápido sin resolver la ecuación característica.
- [[autovalores-complejos]] — el caso de discriminante negativo (espirales, centros) se
  desarrolla con detalle en esa nota.
- [[sistemas-casi-lineales-estabilidad]] — esta clasificación es exactamente lo que se aplica
  después de linealizar un sistema no lineal alrededor de cada punto crítico con la matriz
  Jacobiana.

## Errores frecuentes de Marcos aquí

- **Patrón 5** (orden incorrecto en procedimientos con norma estricta): clasificar el punto
  crítico ANTES de haber calculado correctamente `tr(A)` y `|A|` (o calcularlos con un signo
  equivocado) invalida toda la clasificación posterior — siempre calcula primero traza y
  determinante explícitamente, verifícalos, y solo entonces consulta la tabla.
- **Patrón 3** (aplicar fórmula sin verificar condiciones): la tabla de clasificación por
  traza/determinante asume que el punto crítico está en el origen — para sistemas casi-lineales
  hay que trasladar primero al punto crítico de interés (`u=x−x0`, `v=y−y0`) antes de aplicar
  esta tabla directamente al Jacobiano evaluado ahí.

## Relevancia en examen

**Alta.** Clasificar el punto crítico de un sistema lineal (nodo/silla/espiral/centro y su
estabilidad) es un apartado casi obligatorio en cualquier ejercicio de sistemas: aparece en
prácticamente todos los segundos parciales, PEP2 y finales revisados. Suele combinarse con dibujar
el plano fase y describir el comportamiento a largo plazo. Vale típicamente 1-2 puntos dentro de
un ejercicio mayor de 3-5 puntos.
