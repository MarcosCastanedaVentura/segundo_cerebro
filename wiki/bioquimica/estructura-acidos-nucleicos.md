---
titulo: "Ácidos nucleicos: nucleótidos, doble hélice de ADN y propiedades físico-químicas"
asignatura: "bioquimica"
tema: "Tema 8 - Ácidos nucleicos: estructura, propiedades y función"
tipo: "concepto"
relacionado: ["replicacion-adn", "transcripcion-y-traduccion", "biomoleculas-glucidos-lipidos", "aminoacidos-y-estructura-proteica"]
patrones_error: [2, 6]
examen_relevancia: "alta"
fuente: ["Tema 8.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Examen ordinario (2023-2024).pdf", "examenes/wuolah-free-Recuperacion (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Los ácidos nucleicos (ADN y ARN) son polímeros de nucleótidos unidos por enlaces fosfodiéster. Cada
nucleótido tiene 3 componentes: una base nitrogenada (púrica: A, G; o pirimidínica: C, T/U), un azúcar
(ribosa en ARN, desoxirribosa en ADN) y uno o más grupos fosfato. El ADN es el material genético: forma una
doble hélice (modelo de Watson y Crick, 1953, a partir de los datos de difracción de rayos X de Rosalind
Franklin) con dos cadenas antiparalelas y complementarias unidas por puentes de hidrógeno entre bases (A-T:
2 puentes; G-C: 3 puentes).

## Por qué / de dónde viene

La complementariedad de bases (Chargaff: %A=%T y %G=%C) permite que cada hebra sirva de molde exacto para
reconstruir la otra — esto es la base física de la replicación semiconservativa (ver [[replicacion-adn]]). El
número de puentes de H entre G-C (3) frente a A-T (2) explica por qué las regiones ricas en G+C son más
estables térmicamente (mayor Tm, temperatura de fusión): hay que romper más enlaces para separar las hebras.
La estabilidad global del ADN de doble hebra frente a la desnaturalización se puede seguir midiendo su
absorbancia a 260 nm: las bases apiladas y emparejadas absorben menos luz UV que las bases libres y expuestas
al desnaturalizarse — este aumento de absorbancia al separar las hebras es el **efecto hipercrómico**.

## Fórmula / procedimiento

**Componentes y enlaces:**
- Nucleósido = azúcar + base nitrogenada (enlace N-glucosídico).
- Nucleótido = nucleósido + fosfato (enlace éster, entre el fosfato y el C5' del azúcar).
- Cadena de ácido nucleico: nucleótidos unidos por enlace **fosfodiéster** entre el 3'-OH de un nucleótido y
  el 5'-fosfato del siguiente. Toda secuencia se escribe convencionalmente 5'→3'.

**Doble hélice de ADN (forma B, la fisiológica):**
- Dos cadenas antiparalelas (una 5'→3', la otra 3'→5') enrolladas en hélice dextrógira, ~10,5 pb/vuelta.
- Azúcares y fosfatos por fuera (esqueleto), bases nitrogenadas por dentro (apareadas).
- Complementariedad: A=T (2 puentes H), G≡C (3 puentes H).
- Existen otras conformaciones (A-DNA, Z-DNA levógira en tramos ricos en CG) pero la B es la más común en
  condiciones fisiológicas.

**Propiedades físico-químicas:**
- Desnaturalización: ruptura de los puentes de H (no de los enlaces covalentes) → separación de hebras →
  aumenta la absorbancia a 260 nm (**efecto hipercrómico**).
- Temperatura de fusión (Tm): temperatura a la que el 50% de las moléculas están desnaturalizadas. **A mayor
  %G+C, mayor Tm** (más puentes de H que romper).
- Estabilidad frente a desnaturalización por calor: dúplex ARN > dúplex ARN-ADN > dúplex ADN (el ADN es el
  menos estable de los tres, aunque es el más estable químicamente frente a hidrólisis).
- Molécula de cadena simple digerible por exonucleasas → indica que es lineal (las exonucleasas atacan desde
  los extremos); si no es digerible por exonucleasas → es circular (sin extremos libres).

## Ejemplo resuelto

*Adaptado del examen final 2022-2023, pregunta 3.* Un ácido nucleico tiene dA=15%, dI=15%, dG=35%, dC=35%, y
es digerible por exonucleasas.
a) Es **ADN** (tiene desoxirribosa) y de **cadena simple**: si fuera de doble cadena, %A debería igualar a
%T (aquí no hay T, hay I=inosina) y %G a %C — pero la presencia de dI en vez de dT y el hecho de que las
proporciones no emparejan según Chargaff (dA=dI=15%≠dG=dC=35%, sería casualidad, no regla de doble cadena
real) apunta a cadena simple.
b) Es **lineal**: al ser digerible por exonucleasas (que atacan solo extremos libres), debe tener extremos —
si fuera circular no tendría extremos y sería resistente a exonucleasas.
c) El efecto hipercrómico observado al desnaturalizar indica que, pese a ser "simple", tenía regiones de
doble hélice intracatenaria (plegamiento sobre sí misma) cuyos puentes de H se rompen al calentar, liberando
las bases y aumentando la absorbancia a 260 nm.

## Conexión con otros conceptos

- [[replicacion-adn]]: la complementariedad de bases descrita aquí es el fundamento físico de la
  replicación semiconservativa.
- [[transcripcion-y-traduccion]]: el ARN transcrito usa las mismas reglas de complementariedad (con U en vez
  de T).
- [[aminoacidos-y-estructura-proteica]]: ambos son polímeros con "unidades monoméricas + enlace covalente
  repetitivo", útil como analogía pedagógica (enlace fosfodiéster ↔ enlace peptídico).
- Conexión con Microbiología Alimentaria: identificación de especies/patógenos por secuencia de ADN (ver
  [[tecnicas-biologia-molecular]] y [[../microbiologia/MOC]]).

## Errores frecuentes de Marcos aquí

**Patrón 2** (confundir términos parecidos): enantiómero, epímero, anómero y diastereoisómero de un azúcar (y
por extensión de un nucleósido) se confunden con facilidad porque todos son "variantes espaciales de la misma
molécula" — exige verbalizar la definición exacta de cada uno antes de aplicarlo (aparece explícitamente en
el examen de recuperación 2023-2024, pregunta 1).

**Patrón 6** (copiar mal los datos): en los ejercicios de composición de bases (%dA, %dG, etc.) es fácil
sumar mal los porcentajes o asumir Chargaff (%A=%T) sin comprobar primero si de verdad se cumple con los
datos del enunciado — verificar siempre la suma total (=100%) y la regla de Chargaff antes de concluir si es
cadena simple o doble.

## Relevancia en examen

**Alta.** Presente en los 3 exámenes oficiales completos revisados (final 2022-23, ordinario 2023-24,
recuperación 2023-24): composición de bases y deducción de ADN/ARN y simple/doble cadena, efecto
hipercrómico y Tm, representación de la estructura con enlaces fosfodiéster y N-glucosídico marcando extremos
5'/3'.
