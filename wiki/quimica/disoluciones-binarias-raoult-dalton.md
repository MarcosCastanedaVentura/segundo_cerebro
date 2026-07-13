---
titulo: "Disoluciones binarias ideales: Ley de Raoult, Ley de Dalton y destilación"
asignatura: "quimica"
tema: "Tema 1 - Bloque 3: Mezclas Líquido-Líquido"
tipo: "formula"
relacionado: ["unidades-concentracion", "propiedades-coligativas"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Tema 1. Bloque 3.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Descripción del equilibrio líquido-vapor en una mezcla de dos líquidos volátiles (disolución ideal: las
fuerzas A-B son casi iguales a las A-A y B-B). Permite predecir la composición del vapor que se forma al
calentar la mezcla, y es la base teórica de la destilación (separación de alcohol, aromas, disolventes).

## Por qué / de dónde viene

Cada componente de la mezcla líquida contribuye a la presión de vapor total en proporción a su cantidad
en el líquido (Ley de Raoult) y luego, en la fase vapor, cada componente pesa según su fracción en esa
fase (Ley de Dalton). Como el componente más volátil (mayor P° puro) escapa más fácilmente hacia el
vapor, el vapor siempre queda **enriquecido en el componente más volátil** respecto al líquido de
partida — este es el principio físico que hace posible separar líquidos por destilación.

## Fórmula / procedimiento

- **Ley de Raoult** (fase líquida): Pᵢ = xᵢ · Pᵢ°, donde xᵢ = fracción molar en el líquido, Pᵢ° = presión
  de vapor del componente puro i a esa temperatura.
- **Ley de Dalton** (fase vapor): P_T = P_A + P_B ; yᵢ = Pᵢ/P_T, donde yᵢ = fracción molar en el vapor.
- Procedimiento típico: (1) hallar x_B = 1 − x_A → (2) calcular P_A y P_B con Raoult → (3) sumar para
  P_T → (4) calcular y_A, y_B con Dalton → (5) comparar P° de cada componente para decir cuál es más
  volátil (mayor P° puro = más volátil = y > x en el vapor).
- **Destilación simple**: una sola vaporización-condensación. Enriquece el vapor en el más volátil pero
  NO separa completamente los componentes.
- **Destilación fraccionada**: múltiples vaporizaciones-condensaciones sucesivas (columna de
  fraccionamiento) — en el límite se obtiene el componente más volátil puro en el destilado y el menos
  volátil puro en el residuo (calderín).

## Ejemplo resuelto

*(Tema 1. Bloque 3.pdf, Ejercicio 2)* A 20 °C, P°(benceno) = 74,7 mmHg, P°(tolueno) = 22,3 mmHg. La
cantidad de benceno en el líquido es 4 veces la de tolueno. Calcular presión total y composición del
vapor.

1. Fracciones molares en el líquido: X_benceno = 4/5 = 0,8 ; X_tolueno = 1/5 = 0,2
2. Presiones parciales (Raoult): P_benceno = 0,8·74,7 = 59,76 mmHg ; P_tolueno = 0,2·22,3 = 4,46 mmHg
3. Presión total: P_T = 59,76 + 4,46 = **64,22 mmHg**
4. Composición del vapor (Dalton): Y_benceno = 59,76/64,22 = **0,93** ; Y_tolueno = **0,07**

El vapor (93% benceno) está mucho más enriquecido en benceno que el líquido (80%) porque el benceno es
el más volátil (mayor P°).

## Conexión con otros conceptos

- [[unidades-concentracion]]: la fracción molar (X) usada aquí es la misma magnitud que en las unidades
  de concentración.
- [[propiedades-coligativas]]: ambos bloques comparten la idea de "presión de vapor del disolvente" (P°),
  aunque aquí se aplica a mezclas de dos volátiles y allí a un soluto no volátil disuelto en un
  disolvente.
- Aplicación directa en tecnología de alimentos: destilación de alcohol en bebidas fermentadas,
  recuperación de aromas, tratamiento de aguas — mencionado explícitamente en el propio apunte como
  contexto de Ingeniería Alimentaria.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): Raoult (P = x·P°) es para la fase líquida,
Dalton (y = P/P_T) es para la fase vapor — mezclar cuál x/y corresponde a cuál fase es el error típico.
Antes de sustituir, identificar explícitamente "¿esto es composición de líquido o de vapor?".

## Relevancia en examen

Media. Es un bloque más aislado dentro del Tema 1; en los exámenes de julio 2025 y PEP1 revisados no
aparece como pregunta central tan a menudo como propiedades coligativas o cinética/ácido-base/redox, pero
puede aparecer como pregunta corta de interpretación de diagrama T-x o P-x (identificar qué línea es
burbuja/rocío, cuál es más volátil).
