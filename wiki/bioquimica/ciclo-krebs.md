---
titulo: "Ciclo de Krebs (ciclo del ácido cítrico): fases, rendimiento y naturaleza anfibólica"
asignatura: "bioquimica"
tema: "Tema 5 - Metabolismo oxidativo"
tipo: "procedimiento"
relacionado: ["glucolisis", "cadena-transporte-electrones-fosforilacion-oxidativa", "regulacion-enzimatica-alosterica", "metabolismo-lipidos-beta-oxidacion", "metabolismo-aminoacidos-nitrogeno"]
patrones_error: [3, 7]
examen_relevancia: "alta"
fuente: ["05-Met oxidativo.pdf", "Problemas de Metabolismo 2.pdf", "Preguntas metabolismo glucidos y oxidativo 1.pdf", "examenes/wuolah-free-Examen final (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El ciclo del ácido cítrico (ciclo de Krebs o de los ácidos tricarboxílicos) es la vía final común de oxidación
aeróbica de los tres tipos de combustibles metabólicos (glúcidos, lípidos y proteínas), todos ellos
convertidos previamente en acetil-CoA (o directamente en intermediarios del ciclo). Ocurre en la matriz
mitocondrial (excepto la reacción de la succinato deshidrogenasa, en la membrana mitocondrial interna).

## Por qué / de dónde viene

El ciclo oxida el grupo acetilo (2C) del acetil-CoA hasta 2 CO2, y transfiere los electrones liberados a
NAD⁺ y FAD, reduciéndolos a NADH y FADH2. Estos coenzimas reducidos son los que después ceden electrones a la
cadena de transporte electrónico para generar ATP (ver
[[cadena-transporte-electrones-fosforilacion-oxidativa]]) — el ciclo en sí solo genera 1 GTP por vuelta
mediante fosforilación a nivel de sustrato, su función principal es "cosechar" electrones de alta energía.
Además es una ruta **anfibólica** (catabólica y anabólica a la vez): sus intermediarios (oxalacetato,
α-cetoglutarato, succinil-CoA, citrato) son también precursores de aminoácidos, glucosa (gluconeogénesis) y
grupo hemo. Por eso necesita reacciones anapleróticas ("de relleno", sobre todo piruvato carboxilasa) que
reponen los intermediarios que se desvían hacia biosíntesis.

## Fórmula / procedimiento

**Formación de acetil-CoA a partir de piruvato** (paso previo, no forma parte del ciclo en sí):
Piruvato + NAD⁺ + CoA-SH → Acetil-CoA + NADH + CO2, catalizada por el complejo piruvato deshidrogenasa
(matriz mitocondrial, 3 actividades enzimáticas E1-E2-E3, 5 coenzimas). Regulado alostéricamente (inhibido
por ATP, NADH, acetil-CoA; activado por AMP, NAD⁺, CoA) y por fosforilación covalente (ver
[[regulacion-enzimatica-alosterica]]).

**Las 8 reacciones del ciclo** (organizadas en 2 fases):
- *Fase 1 (reacciones 1-4, oxidación de los 2 carbonos a CO2):*
  1. Acetil-CoA (2C) + Oxalacetato (4C) → Citrato (6C) — condensación.
  2. Citrato → Isocitrato (isomerización vía cis-aconitato).
  3. Isocitrato → α-cetoglutarato (5C) + CO2 + NADH — descarboxilación oxidativa (isocitrato
     deshidrogenasa, enzima alostérico activado por ADP).
  4. α-cetoglutarato → Succinil-CoA (4C) + CO2 + NADH — descarboxilación oxidativa.
- *Fase 2 (reacciones 5-8, regeneración del oxalacetato):*
  5. Succinil-CoA → Succinato + **GTP** (fosforilación a nivel de sustrato, por la energía del enlace
     tioéster).
  6. Succinato → Fumarato + FADH2 (succinato deshidrogenasa, en la membrana mitocondrial interna).
  7. Fumarato → Malato (hidratación).
  8. Malato → Oxalacetato + NADH (regenera el oxalacetato de partida).

**Balance por vuelta**: Acetil-CoA + 3 NAD⁺ + FAD + GDP + Pi + H₂O → CoA + 2 CO2 + 3 NADH + FADH2 + GTP + 2 H⁺

**Regulación**: fundamentalmente alostérica, sensible a (1) estado redox — se activa cuando NAD⁺/NADH es
alto—, (2) carga energética — se activa cuando ADP(AMP)/ATP es alto—, y (3) disponibilidad de intermediarios
de alta energía (acetil-CoA y succinil-CoA inhiben algunos enzimas del ciclo). Los puntos clave son isocitrato
deshidrogenasa (activada por ADP) y α-cetoglutarato deshidrogenasa.

## Ejemplo resuelto

*Adaptado de Problemas de Metabolismo 2.pdf, pregunta 4.* SDH (succinato deshidrogenasa) de corazón de buey:
la adición de ácido fumárico, oxalacético o malónico hace decrecer la formación de FADH2 → actúan como
**inhibidores** (el malonato es el inhibidor competitivo clásico de la SDH, por ser un análogo estructural
del succinato). El ácido málico aumenta ligeramente el FADH2 pero disminuye el fumarato → el málico desplaza
el equilibrio de la reacción 7 (fumarato⇌malato) hacia atrás (hacia fumarato), lo que "arrastra" indirectamente
más flujo hacia la reacción 6 (succinato→fumarato+FADH2) por efecto de masas; el metabolito adicional que se
forma es **oxalacetato** (producto de la reacción 8, malato→oxalacetato).

## Conexión con otros conceptos

- [[glucolisis]]: el piruvato generado ahí es el sustrato de entrada al ciclo (vía acetil-CoA).
- [[cadena-transporte-electrones-fosforilacion-oxidativa]]: destino de todo el NADH y FADH2 generados aquí.
- [[metabolismo-lipidos-beta-oxidacion]] y [[metabolismo-aminoacidos-nitrogeno]]: ambas rutas alimentan el
  ciclo con acetil-CoA o con intermediarios directos (oxalacetato, α-cetoglutarato, succinil-CoA, fumarato).
- [[gluconeogenesis]]: usa el oxalacetato del ciclo como precursor — de ahí la necesidad de reacciones
  anapleróticas.
- [[regulacion-enzimatica-alosterica]]: isocitrato deshidrogenasa es el ejemplo alostérico de examen más
  citado.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar el caso): confundir "reacciones anapleróticas" (reponen
intermediarios) con las reacciones normales del ciclo — antes de responder sobre balance de intermediarios,
identificar si la pregunta habla del ciclo en sí o de su función anfibólica/anaplerótica.

**Patrón 7** (validar sin verificar): no es posible obtener síntesis neta de oxalacetato a partir de
acetil-CoA usando solo las enzimas del ciclo sin retirar intermediarios — es un ciclo, no una vía de síntesis
neta. Verificar siempre esta lógica antes de responder preguntas sobre "de dónde sale" un intermediario.

## Relevancia en examen

**Alta.** La tabla de rutas metabólicas con Ciclo de Krebs (tipo, localización, sustratos: acetil-CoA +
oxalacetato, productos: CO2+NADH+FADH2+ATP) aparece en los 4 exámenes revisados. Preguntas de razonamiento
sobre inhibidores de la SDH, sobre por qué el ciclo requiere O2 indirectamente (aunque no participa
directamente en ninguna reacción del ciclo), y sobre reacciones anapleróticas aparecen repetidamente en las
hojas de problemas y ejercicios de examen.
