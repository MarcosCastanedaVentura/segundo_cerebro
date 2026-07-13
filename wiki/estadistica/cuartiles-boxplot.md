---
titulo: "Cuantiles, cuartiles y diagrama de caja (boxplot)"
asignatura: "estadistica"
tema: "Tema 1.1 — Distribuciones de un solo carácter"
tipo: "procedimiento"
relacionado: ["estadistica-descriptiva-una-variable", "variable-aleatoria-continua"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Tema1.1_EstadisticaDescriptiva_25-26-2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El **cuantil de orden α** (x_α) es el valor de la variable que separa a la población en dos grupos: el α×100% con
valores más bajos, y el (1−α)×100% con valores más altos (0≤α≤1). Los cuartiles son los cuantiles de orden
0.25, 0.5 y 0.75 (Q₁, Q₂=mediana, Q₃) y dividen la distribución en 4 partes iguales. El **diagrama de caja y
bigotes (boxplot)** es la representación gráfica de esos cuartiles junto con los valores atípicos.

## Por qué / de dónde viene

La media y la varianza resumen la distribución con dos números, pero no dicen nada sobre la forma ni sobre valores
extremos. Los cuantiles cortan la distribución acumulada F(x) en puntos concretos, dando una foto más robusta frente
a valores atípicos (la mediana no se mueve si cambias el máximo, la media sí).

## Fórmula / procedimiento

El procedimiento **depende del tipo de dato y de si h=α×N es entero o no** — este es el punto donde hay que
clasificar el caso antes de calcular (Patrón 3, ver más abajo).

**A) Datos individuales** (ordenados de menor a mayor), sea h = α×N:

- Si h **no** es entero: se toma el entero inmediatamente superior hᵉ, y x_α = x_(hᵉ).
- Si h **es** entero:
  - si x_h = x_(h+1) → x_α = x_h
  - si x_h ≠ x_(h+1) → x_α es el intervalo-cuantil [x_h, x_(h+1)] (discreta) o su punto medio (x_h+x_(h+1))/2 (continua)

**B) Datos agrupados en tabla** (a partir de la función acumulada F(x)):

- V.E. discreta: si F_(i-1) < α < F_i → x_α = x_i; si α = F_i → x_α es el intervalo [x_i, x_(i+1)].
- V.E. continua: si α coincide con un extremo de clase, x_α = l_i directamente; si no, se **interpola linealmente**
  dentro de la clase:

  x_α = l_(i-1) + (α − F_(i-1)) × (l_i − l_(i-1))/(F_i − F_(i-1))

**Diagrama de caja y bigotes**:

- Rango intercuartílico: RIC = Q₃ − Q₁ (mide dispersión del 50% central, robusta a atípicos).
- Bigote superior: L_s = mín(Q₃ + 1.5×RIC, máximo del dato).
- Bigote inferior: L_i = máx(Q₁ − 1.5×RIC, mínimo del dato).
- **Atípicos**: cualquier valor fuera de [L_i, L_s] se marca como punto aparte en el gráfico.

## Ejemplo resuelto

Datos individuales (adaptado de Tema1.1_EstadisticaDescriptiva_25-26-2.pdf, diapositiva 35): variable continua Y con
n=10 valores ordenados: 93, 98, 101, 103, 109, 110, 111, 112, 128, 135.

Tercer cuartil Q₃ (α=0.75): h = 0.75×10 = 7.5, **no** es entero → hᵉ = 8 → Q₃ = x₈ = 112.

Con los mismos datos, calculando también Q₁ (h=0.75×10=2.5→hᵉ=3→Q₁=x₃=101) y usando RIC=112−101=11:
L_s = mín(112+16.5, 135) = 128.5→ se queda en 128.5 pero el máximo real es 135, así que el bigote superior real de
los datos llega hasta 135 solo si 135 ≤ 128.5 (no lo es) → 135 se marcaría como **atípico** en el boxplot.

## Conexión con otros conceptos

- [[estadistica-descriptiva-una-variable]] — la mediana es el cuantil 0.5, ya introducida ahí como medida de
  tendencia central.
- [[variable-aleatoria-continua]] — el mismo concepto de cuantil (x_α tal que F(x_α)=α) reaparece con F(x) teórica en
  lugar de empírica.
- [[distribucion-normal-tipificacion]] — buscar un percentil en la tabla Z es exactamente hallar un cuantil de la
  Normal tipificada.

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmula sin verificar condiciones de uso)**: el error típico es aplicar directamente la fórmula
de "h no entero" o la de interpolación continua sin comprobar primero (a) si los datos son individuales o agrupados,
y (b) si h=α×N sale entero o no. Son 4 fórmulas distintas y hay que **clasificar el caso explícitamente antes de
calcular**, igual que en electrotecnia hay que identificar el tipo de conexión antes de abrir el formulario de
triángulo/estrella. Antes de calcular un cuantil, pregúntate en voz alta: "¿tengo datos sueltos o una tabla
agrupada? ¿h=α×N me da entero?" — solo después abre la fórmula correspondiente.

## Relevancia en examen

Alta. Cuartiles y boxplot aparecen en casi todos los exámenes de la 1ª parte, normalmente como subapartado de un
ejercicio de descriptiva de una variable (ej. Examen_marzo_2024, Examen_marzo_2025). A veces piden explícitamente
identificar si hay atípicos.
