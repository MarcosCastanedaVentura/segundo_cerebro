---
titulo: "Modelos ecológicos: depredador-presa (Lotka-Volterra) y especies compitiendo"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 7 - Modelos ecológicos"
tipo: "concepto"
relacionado: ["sistemas-casi-lineales-estabilidad", "modelos-poblacion-logistica", "clasificacion-puntos-criticos-sistemas-lineales"]
patrones_error: [3, 6]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 7, 7.1)", "FINAL 2_JULIO_2025 - soluciones.pdf", "2025:12:19_PEP2 Alimentaria (solución).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Son sistemas casi-lineales de 2 ecuaciones que modelan la interacción entre dos especies o
poblaciones `x(t)`, `y(t)`:

- **Depredador-presa (Lotka-Volterra)**: `dx/dt = ax − pxy`, `dy/dt = −by + qxy` — la presa
  crece sola, el depredador decae solo, y el término `xy` captura los encuentros entre ambos.
- **Especies compitiendo**: `dx/dt = x(a1−b1x−c1y)`, `dy/dt = y(a2−b2y−c2x)` — cada especie por
  separado sigue una logística, y la competencia añade un término `−cxy` de interferencia mutua.

## Por qué / de dónde viene

En depredador-presa, sin depredadores la presa crece exponencialmente (`ax`) y sin presas el
depredador decae exponencialmente (`−by`); cuando ambos coexisten, cada encuentro casual
(proporcional al producto `xy`, como en cualquier modelo de "tasa de encuentros") reduce la
presa y alimenta al depredador. En especies compitiendo, cada población por separado seguiría
una logística (ver [[modelos-poblacion-logistica]]), pero la presencia de la otra especie
consume los mismos recursos, restando un término proporcional a `xy` a la tasa de crecimiento de
cada una — es el mismo razonamiento de "tasa de encuentros" aplicado a la competencia por comida
en vez de a la depredación.

## Fórmula / procedimiento

1. Hallar los puntos críticos (siempre incluyen `(0,0)` y, en depredador-presa, el punto de
   coexistencia `(b/q, a/p)`; en competencia, hasta 4 puntos: extinción total, dos de exclusión
   de una especie, y uno de coexistencia).
2. Calcular el Jacobiano y evaluarlo en cada punto crítico (ver
   [[sistemas-casi-lineales-estabilidad]]).
3. En depredador-presa, el origen `(0,0)` es siempre un **punto de silla** (autovalores `a, −b`,
   de signos opuestos) y el punto de coexistencia es siempre un **centro** (autovalores `±i√(ab)`,
   imaginarios puros) — las poblaciones oscilan de forma acoplada sin converger a un equilibrio.
4. En especies compitiendo, la estabilidad del punto de coexistencia depende del signo de
   `c1·c2 − b1·b2`: si `c1c2 < b1b2` (competencia débil frente a la autolimitación de cada
   especie) el punto es un nodo sumidero estable → **coexistencia**; si `c1c2 > b1b2` (competencia
   fuerte) el punto es un punto de silla inestable → **una especie termina extinguiéndose**.

## Ejemplo resuelto

*Adaptado de FINAL 2_JULIO_2025 - soluciones.pdf, ejercicio 4.* Dos especies de insectos en un
cultivo de maíz compiten por alimento (poblaciones en miles de individuos):

```
dx/dt = x(1.5 − x − 0.5y)
dy/dt = y(2 − y − 0.75x)
```

Puntos críticos: `(0,0)`, `(1.5,0)`, `(0,2)`, y coexistencia resolviendo
`1.5=x+0.5y`, `2=y+0.75x` → `x=0.8`, `y=1.4`.

Jacobiano en `(0.8, 1.4)`: `J = [[−0.8,−0.4],[−1.05,−1.4]]`. `tr(J)=−2.2<0`,
`|J| = 1.12−0.42 = 0.7 > 0` → autovalores reales, mismo signo (negativo) →
**nodo propio sumidero, asintóticamente estable.**

Con `b1=1, c1=0.5, b2=1, c2=0.75`: `c1·c2 = 0.375 < b1·b2 = 1` — confirma la coexistencia
predicha por el criterio general. Interpretación: ambas especies conviven de forma estable en el
cultivo, estabilizándose en 800 y 1400 individuos respectivamente.

## Conexión con otros conceptos

- [[sistemas-casi-lineales-estabilidad]] — procedimiento base: linealizar en cada punto crítico
  y clasificar con autovalores/traza-determinante.
- [[modelos-poblacion-logistica]] — cada ecuación por separado (sin el término de interacción) es
  una logística; la interacción es lo único nuevo.
- [[clasificacion-puntos-criticos-sistemas-lineales]] — el origen en depredador-presa es siempre
  silla, y el punto de coexistencia siempre centro — vale la pena memorizar estos dos resultados
  generales, no solo saber recalcularlos.
- Conexión directa con Microbiología Alimentaria y Producción Vegetal: control biológico de
  plagas (insectos beneficiosos vs. dañinos), competencia microbiana en fermentaciones, y
  dinámica de poblaciones en general — el mismo esquema matemático aparece ahí con otro nombre.

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmulas sin verificar condiciones): el resultado "el origen es siempre
  silla" en depredador-presa solo vale si el sistema tiene exactamente esa forma
  (`ax−pxy`, `−by+qxy`) — si el enunciado modifica el modelo (por ejemplo añadiendo un término
  logístico a la presa), hay que recalcular el Jacobiano desde cero, no asumir el resultado
  general de memoria.
- **Patrón 6** (copiar mal datos del enunciado): en especies compitiendo hay 6 parámetros
  (`a1,b1,c1,a2,b2,c2`) fácilmente intercambiables entre sí al leer el enunciado — escribe
  explícitamente la tabla de qué coeficiente corresponde a qué especie y qué efecto antes de
  montar el Jacobiano.

## Relevancia en examen

**Alta.** Los modelos ecológicos son el ejercicio de mayor peso en varios finales y segundos
parciales, casi siempre en un contexto de plagas agrícolas o bacterias en un alimento
(FINAL 2_JULIO_2025 ejercicio 4, PEP2 19-12-2025 ejercicio 3 —bacterias depredando entre sí—,
JULIO23_24, Examen Ordinario IA solución): piden hallar todos los puntos críticos, linealizar y
clasificar cada uno, dibujar el plano fase global combinando los locales, y dar una
interpretación ecológica/biológica del resultado con datos iniciales concretos. Vale típicamente
4-5 puntos, y suele ser el último y más largo ejercicio del examen.
