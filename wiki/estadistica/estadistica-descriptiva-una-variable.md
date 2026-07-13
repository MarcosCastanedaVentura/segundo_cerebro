---
titulo: "Estadística descriptiva de una variable"
asignatura: "estadistica"
tema: "Tema 1.1 — Distribuciones de un solo carácter"
tipo: "concepto"
relacionado: ["cuartiles-boxplot", "estadistica-descriptiva-dos-variables", "variable-aleatoria-discreta", "variable-aleatoria-continua"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["Tema1.1_EstadisticaDescriptiva_25-26-2.pdf", "E Descriptiva_Tema 1.1-2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La estadística descriptiva de una variable resume, con unos pocos números o gráficos, cómo se reparten los valores
de un carácter (cualitativo o cuantitativo) medido sobre los individuos de una población o muestra. Antes de calcular
nada hay que clasificar el carácter:

- **Cualitativo**: nominal (sin orden: estado civil) u ordinal (con orden: clase social).
- **Cuantitativo o variable estadística**: discreta (valores aislados y contables: nº de hijos) o continua (cualquier
  valor de un intervalo: peso, superficie).

Esta clasificación no es un detalle burocrático: determina qué tabla y qué gráfico usar (diagrama de barras vs.
histograma) y cómo se calculan luego media, mediana y cuantiles.

## Por qué / de dónde viene

Con N individuos no tiene sentido manejar el dato en bruto uno a uno: se agrupan en **modalidades** (I₁,...,Iₛ) y se
cuenta cuántos individuos caen en cada una (frecuencia absoluta Nᵢ), o qué proporción representan (frecuencia
relativa fᵢ = Nᵢ/N). Cuando la variable es continua, las modalidades son intervalos semiabiertos [lᵢ₋₁, lᵢ) y se
introduce la **marca de clase** xᵢ = (lᵢ₋₁+lᵢ)/2 como representante del intervalo para poder calcular después media y
varianza.

## Fórmula / procedimiento

**Tabla de frecuencias** (discreta o continua):

| Modalidad | F. Absoluta Nᵢ | F. Relativa fᵢ=Nᵢ/N | F. Acumulada Fᵢ=Σfⱼ (j≤i) |

con ΣNᵢ=N, Σfᵢ=1, Fₛ=1.

**Medidas de tendencia central**

- **Moda**: valor (o clase) con mayor frecuencia. Discreta: xᵢ con mayor fᵢ. Continua: la clase modal.
- **Mediana**: cuantil de orden 0.5 — separa el 50% inferior del 50% superior (ver [[cuartiles-boxplot]]).
- **Media** m (datos individuales): m = (1/N)·Σxₖ. Media (datos agrupados): m = Σfᵢ·xᵢ.

**Medidas de dispersión**

- **Varianza** σ²: mide cuánto se alejan los datos de la media, en unidades al cuadrado.
  - Datos individuales: σ² = (1/N)·Σ(xₖ−m)²
  - Teorema de König (más práctico de calcular): σ² = (1/N)·Σxₖ² − m²
  - Datos agrupados: σ² = Σfᵢ·xᵢ² − m²
- **Desviación típica** σ = √σ² — mismas unidades que la variable, por eso es la que se interpreta ("la variable se
  desvía en promedio σ unidades de la media").
- **Coeficiente de variación** cv = σ/m — adimensional, sirve para comparar dispersión entre poblaciones con medias
  distintas (ej. comparar la dispersión del peso de pollos con la del peso de huevos).

## Ejemplo resuelto

Nº de asalariados fijos en 24 explotaciones agrarias (adaptado de Tema1.1_EstadisticaDescriptiva_25-26-2.pdf,
diapositivas 26-27): variable discreta con tabla

| xᵢ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| Nᵢ | 3 | 3 | 5 | 7 | 2 | 2 | 1 | 1 |
| fᵢ | 0.125 | 0.125 | 0.208 | 0.292 | 0.083 | 0.083 | 0.042 | 0.042 |

N = 24. Media: m = Σfᵢxᵢ = 0×0.125+1×0.125+2×0.208+3×0.292+4×0.083+5×0.083+6×0.042+7×0.042 ≈ 2.83 asalariados.
Moda: xᵢ=3 (fᵢ=0.292, la mayor). Varianza por König: σ² = Σfᵢxᵢ² − m² ≈ 11.375 − 2.83² ≈ 3.36 → σ ≈ 1.83.
Coeficiente de variación: cv = σ/m ≈ 1.83/2.83 ≈ 0.65 (65% de dispersión relativa a la media — bastante alta).

## Conexión con otros conceptos

- [[cuartiles-boxplot]] — cuantiles, rango intercuartílico y diagrama de caja, calculados sobre esta misma tabla.
- [[estadistica-descriptiva-dos-variables]] — cuando se estudian dos caracteres a la vez sobre los mismos individuos.
- [[variable-aleatoria-discreta]] y [[variable-aleatoria-continua]] — el salto conceptual de "frecuencia observada en
  una muestra" a "probabilidad teórica de un modelo" reutiliza exactamente el mismo aparato (media=esperanza,
  varianza, teorema de König).

## Errores frecuentes de Marcos aquí

Ninguno activo documentado en este bloque concreto — Marcos domina descriptiva de una variable (ver
`memory/memory.json`). Cuidado solo con no confundir σ (desviación típica) con σ² (varianza) al leer un enunciado:
este error sí está activo más adelante en tipificación e IC — ver [[distribucion-normal-tipificacion]] e
[[intervalo-confianza-sigma-desconocida]].

## Relevancia en examen

Alta. Aparece en casi todos los exámenes como primer ejercicio o subapartado: tabla de frecuencias a partir de datos
brutos, cálculo de media/moda/mediana, varianza y coeficiente de variación. Suele ir encadenado con cuartiles y
boxplot en el mismo ejercicio (ver `examenes.md`).
