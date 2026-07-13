---
titulo: "Disoluciones no ideales: desviaciones de Raoult y azeótropos"
asignatura: "quimica"
tema: "Tema 1 - Bloque 4: Mezclas Líquido-Líquido no ideales"
tipo: "concepto"
relacionado: ["disoluciones-binarias-raoult-dalton"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Tema 1. Bloque 4.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una disolución es **no ideal** cuando su presión de vapor real no coincide con la predicha por la Ley de
Raoult (ver [[disoluciones-binarias-raoult-dalton]]). En algunos casos la desviación es tan grande que
aparece un **azeótropo**: una composición concreta en la que líquido y vapor tienen exactamente la misma
composición, por lo que la mezcla hierve sin cambiar de proporción y **ya no se puede seguir separando
por destilación** (ni simple ni fraccionada) más allá de ese punto.

## Por qué / de dónde viene

Raoult asume que las fuerzas intermoleculares A-B son iguales a las A-A y B-B (mezcla "ideal"). En la
realidad esto casi nunca es exacto:

- Si las fuerzas A-B son **más débiles** que las A-A/B-B, las moléculas escapan más fácilmente de lo
  esperado → presión de vapor real **mayor** que la ideal (**desviación positiva**), proceso de mezcla
  endotérmico (ΔH>0), y puede aparecer un **azeótropo de ebullición mínima** (ej. etanol-agua).
- Si las fuerzas A-B son **más fuertes**, las moléculas quedan más retenidas → presión de vapor real
  **menor** que la ideal (**desviación negativa**), proceso exotérmico (ΔH<0), y puede aparecer un
  **azeótropo de ebullición máxima** (ej. ácido nítrico-agua, acetona-cloroformo).

En el punto azeotrópico, por definición, x_i = y_i para todos los componentes: no hay diferencia de
volatilidad relativa ahí, así que destilar no cambia nada la composición.

## Fórmula / procedimiento

No hay una fórmula única; es un procedimiento de lectura de diagramas T-x (temperatura vs. composición):

1. Localizar el punto azeotrópico en el diagrama (mínimo o máximo de la curva).
2. Determinar si la composición de partida está a la izquierda o a la derecha del azeótropo.
3. **Destilación simple**: el vapor se enriquece hacia el azeótropo (nunca lo cruza); el líquido residual
   se enriquece en el componente puro del lado en que se está.
4. **Destilación fraccionada**: el destilado final tiende exactamente a la composición del azeótropo (si
   se parte del lado donde el azeótropo es la fracción menos volátil relativa) o al componente puro (si
   se parte del lado donde ese componente puro es alcanzable); el residuo en el calderín tiende al
   componente puro contrario o a la mezcla azeotrópica, según el lado de partida.
   - Regla práctica: **nunca se puede cruzar el azeótropo por destilación** — separa hasta el azeótropo,
     no más allá.

## Ejemplo resuelto

*(Tema 1. Bloque 4.pdf, Ejercicios 5-7)* El ácido nítrico (Teb=83°C) y el agua (Teb=100°C) forman un
azeótropo que hierve a 122°C con 68,4% molar de HNO₃ (azeótropo de ebullición **máxima** → desviación
negativa, fuerzas HNO₃-H₂O más fuertes que las puras).

- Si se destila fraccionadamente una mezcla con 95% molar de HNO₃ (a la derecha del azeótropo, en la
  zona rica en ácido): el **destilado** tiende al componente puro de esa zona, **HNO₃ puro**; el
  **residuo** en el calderín tiende al punto de mayor Teb, que es el **azeótropo** (122°C, 68,4% HNO₃).
- Si se parte de una mezcla con 80% agua / 20% HNO₃ (a la izquierda del azeótropo): el destilado tiende
  a **agua pura** y el residuo tiende a la **mezcla azeotrópica**.

## Conexión con otros conceptos

- [[disoluciones-binarias-raoult-dalton]]: esta nota es la extensión "no ideal" de esa — primero hay que
  dominar Raoult/Dalton ideal antes de razonar sobre desviaciones.
- Aplicación real en Ingeniería Alimentaria: el azeótropo etanol-agua (95,6% etanol, hierve a 78,2°C) es
  la razón por la que el "alcohol de 96°" no se puede concentrar más por destilación simple/fraccionada
  convencional — hace falta otra técnica (destilación azeotrópica con un tercer componente, tamices
  moleculares, etc.), tema relevante en la industria de bebidas alcohólicas.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): el error típico es asumir que la destilación
fraccionada siempre da los dos componentes puros — solo es así en mezclas ideales sin azeótropo. Antes de
predecir el resultado de una destilación, hay que comprobar primero si el diagrama tiene un azeótropo y
en qué lado de él está la composición de partida.

## Relevancia en examen

Media. Aparece en el material de clase con muchos ejercicios de lectura de diagrama (identificar tipo de
azeótropo, predecir destilado/residuo), lo que sugiere que Mónica lo valora como pregunta de
"interpretación gráfica" más que de cálculo numérico puro — buen candidato a pregunta corta de examen.
