---
titulo: "Extracción líquido-líquido: coeficiente de reparto y ecuación de Nernst"
asignatura: "quimica"
tema: "Tema 2 - Bloque 2: Extracción Líquido-Líquido"
tipo: "formula"
relacionado: ["operaciones-basicas-separacion", "unidades-concentracion"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Tema 2. Bloque 2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Operación de separación en la que un soluto disuelto en una fase (normalmente acuosa) se transfiere a un
disolvente líquido inmiscible con ella (el "extractante", normalmente orgánico), aprovechando que el
soluto es más soluble en uno de los dos líquidos. Se usa para recuperar compuestos orgánicos de interés
(aromas, principios activos) o para eliminar contaminantes de una disolución acuosa.

## Por qué / de dónde viene

Cuando se ponen en contacto dos disolventes inmiscibles con un soluto presente, el soluto se reparte
entre ambas fases hasta alcanzar el equilibrio, y esa relación de reparto es **constante** a una
temperatura dada (Ley de Reparto de Nernst) — es una manifestación del equilibrio químico aplicado a un
reparto entre fases en vez de a una reacción. Cuanto más afín sea el soluto al disolvente orgánico
respecto al acuoso, mayor será esa constante y más eficaz la extracción.

## Fórmula / procedimiento

- **Coeficiente de distribución**: K_D = [A]_orgánica / [A]_acuosa
- **Ecuación de Nernst para n extracciones sucesivas**:

  aₙ = a₀ · [ V_ac / (K_D·V_org + V_ac) ]ⁿ

  donde: aₙ = cantidad de soluto que queda sin extraer en la fase acuosa tras n extracciones; a₀ =
  cantidad inicial de soluto; V_ac = volumen de la fase acuosa; V_org = volumen de disolvente orgánico
  usado **en cada etapa**; n = número de extracciones.

- **Regla de optimización clave**: para un mismo volumen total de disolvente orgánico disponible, es
  **más eficaz repartirlo en varias extracciones pequeñas sucesivas (n alto)** que usarlo todo de una vez
  (n=1) — porque aₙ decrece exponencialmente con n, mientras que aumentar solo V_org tiene un efecto
  mucho menor (relación no exponencial).

## Ejemplo resuelto

*(Adaptado del planteamiento del Tema 2. Bloque 2.pdf, con números limpios)* Se tienen 100 mL de una
disolución acuosa con a₀ = 10 g de un compuesto orgánico. K_D = 4 (el soluto es 4 veces más soluble en el
disolvente orgánico que en agua). Comparar: (a) una única extracción con 100 mL de disolvente orgánico
frente a (b) dos extracciones sucesivas de 50 mL cada una.

(a) Una extracción, V_org = 100 mL, n=1:
a₁ = 10 · [100/(4·100+100)] = 10 · (100/500) = 10 · 0,2 = **2 g** quedan en el agua (8 g extraídos)

(b) Dos extracciones, V_org = 50 mL cada una, n=2:
a₂ = 10 · [100/(4·50+100)]² = 10 · (100/300)² = 10 · (0,333)² = 10 · 0,111 = **1,11 g** quedan en el agua
(8,89 g extraídos)

Con el mismo volumen total de disolvente (100 mL), repartirlo en 2 extracciones deja menos soluto sin
extraer (1,11 g) que una sola extracción (2 g) — confirma la regla de optimización.

## Conexión con otros conceptos

- [[unidades-concentracion]]: K_D se define como cociente de concentraciones (Molaridad o concentración
  en g/L en ambas fases).
- [[operaciones-basicas-separacion]]: la extracción es una de las operaciones de transferencia de masa
  citadas en el mapa general de ese bloque.
- Precedente conceptual de técnicas analíticas usadas en Bioquímica y Análisis de Alimentos para purificar
  metabolitos o pigmentos — ver [[../bioquimica/MOC]].

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): fácil confundir el V_org "total disponible" con
el V_org "por etapa" al aplicar la fórmula de Nernst con n>1 — hay que dividir el volumen total entre el
número de extracciones antes de sustituir, no usar el volumen total en cada n.

**Patrón 4** (confundir cocientes relacionados): K_D = orgánica/acuosa, no al revés — invertir el
cociente cambia completamente el resultado. Conviene fijar mentalmente "arriba va donde el soluto se
disuelve mejor" antes de escribir la fracción.

## Relevancia en examen

Media. Bloque corto (1 página de teoría) pero con fórmula muy concreta y numérica — encaja bien como
problema de examen de "calcula cuánto queda sin extraer tras n repeticiones", en la línea de los
ejercicios numéricos de otros bloques de este temario.
