---
titulo: "Técnicas de biología molecular en la industria alimentaria: electroforesis, PCR y ELISA"
asignatura: "bioquimica"
tema: "Tema 10 - Técnicas de Biología Molecular aplicadas a la Industria Alimentaria"
tipo: "procedimiento"
relacionado: ["estructura-acidos-nucleicos", "replicacion-adn", "aminoacidos-y-estructura-proteica", "enzimas-estructura-funcion"]
patrones_error: [5]
examen_relevancia: "baja"
fuente: ["Tema 10.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Conjunto de técnicas de laboratorio para aislar, separar, identificar y cuantificar biomoléculas (proteínas,
ácidos nucleicos), con aplicación directa en la industria alimentaria: trazabilidad, autenticidad de origen,
detección de fraudes (ej. atún claro vendido como bonito del norte), alérgenos, patógenos y organismos
modificados genéticamente.

## Por qué / de dónde viene

Separar un componente celular explota sus propiedades físico-químicas diferenciales (tamaño, carga,
solubilidad, reactividad, actividad biológica). La electroforesis usa el movimiento de partículas cargadas en
un campo eléctrico; la PCR explota la propia lógica de la replicación del ADN (ver [[replicacion-adn]]) para
amplificar exponencialmente una región concreta; el ELISA explota la especificidad antígeno-anticuerpo. El
ADN es especialmente útil como herramienta de bioseguridad alimentaria porque aporta más información que las
proteínas, es más estable frente a condiciones ambientales y al procesado, y se puede amplificar por PCR
incluso partiendo de cantidades mínimas.

## Fórmula / procedimiento

**Electroforesis:**
- Movilidad electroforética: v = (Q·V/d)/f (Q=carga, V/d=campo eléctrico, f=coeficiente de fricción).
- Ácidos nucleicos: relación carga/masa igual para todas las moléculas → la separación depende solo del
  tamaño (tamiz molecular del gel de agarosa); menor tamaño = mayor movilidad. Detección con bromuro de
  etidio o GelRed (intercalantes fluorescentes) bajo luz UV.
- Proteínas: relación carga/masa NO es igual entre proteínas distintas → sin tratamiento, la separación
  depende de carga, forma y tamaño. Con SDS (SDS-PAGE, geles de poliacrilamida): el detergente cubre la
  proteína con carga negativa uniforme → separación solo por peso molecular. Permite estimar el PM aparente
  por comparación con un marcador de peso molecular (ojo: el PM de una banda intermedia NO es la media
  aritmética simple de las bandas vecinas).

**PCR (reacción en cadena de la polimerasa, Kary Mullis, Nobel 1993):**
- Materiales: ADN molde, ADN polimerasa termorresistente, dNTPs, cebadores (primers), tampón con Mg²⁺.
- Ciclo (25-40 veces): desnaturalización (94°C) → hibridación de cebadores (50-60°C, 3-5°C por debajo de la
  Tm de los primers) → extensión (72°C).
- Amplificación exponencial: nº de moléculas tras n ciclos = nº inicial × 2ⁿ.
- Diseño de cebadores: deben flanquear la región a amplificar, uno en cada hebra, orientados el uno hacia el
  otro (5'→3' apuntando hacia el fragmento de interés) — error de diseño típico: elegir un cebador que
  apunte "hacia fuera" del fragmento en vez de hacia dentro.
- Variantes: qPCR (cuantificación relativa, en tiempo real, asume amplificación exponencial); dPCR
  (cuantificación absoluta, más robusta frente a inhibidores, ideal para muestras de baja concentración).

**ELISA (Enzyme-Linked Immunosorbent Assay)**: detección basada en anticuerpos marcados con un enzima;
existen variantes directa, indirecta y sandwich (la más específica, requiere 2 anticuerpos contra epítopos
distintos del antígeno, no necesita purificar el antígeno).

## Ejemplo resuelto

*Ejercicio del Tema 10 (diseño de cebadores).* Dada la secuencia de doble cadena:
5'-AACCCCGGCATTGAATGTAGCTCAAAGCAATGATAGTCTTCATGGTTACGAAAACC-3'
3'-TTGGGGCCGTAACTTACATCGAGTTTCGTTACTATCAGAAGTACCAATGCTTTTGG-5'

Se pide elegir la pareja de cebadores correcta entre varias opciones. Procedimiento: el cebador "forward"
debe ser idéntico (5'→3') al extremo 5' de la hebra superior; el cebador "reverse" debe ser complementario e
idéntico (5'→3') al extremo 3' de la hebra superior (equivalente al extremo 5' de la hebra inferior leída en
su propio sentido). La pareja correcta en este ejercicio es la opción 1 (5'-CCCCGGCATTGAA-3', que coincide
con el inicio de la hebra superior) + la opción D (5'-TTTTCGTAACCATGAA-3', que es complementaria y
antiparalela al final de la hebra superior) — comprobar siempre que ambos cebadores "miran hacia dentro" del
fragmento a amplificar.

## Conexión con otros conceptos

- [[replicacion-adn]]: la PCR reproduce artificialmente la lógica de la ADN polimerasa (molde, cebador,
  dNTPs, síntesis 5'→3').
- [[estructura-acidos-nucleicos]]: la separación por electroforesis y la hibridación de cebadores dependen
  de las propiedades físico-químicas descritas ahí.
- [[aminoacidos-y-estructura-proteica]] y [[enzimas-estructura-funcion]]: SDS-PAGE y ELISA se aplican a
  proteínas/enzimas (ej. detección de alérgenos, enzimas recombinantes de uso industrial).
- Conexión directa con Microbiología Alimentaria: detección de patógenos, autenticidad de especies y
  trazabilidad usan estas mismas técnicas — ver [[../microbiologia/MOC]], relación señalada en
  [[../carrera/dependencias]].

## Errores frecuentes de Marcos aquí

**Patrón 5** (orden/secuencia estricta no intuitiva): en PCR, el orden de las 3 fases del ciclo
(desnaturalización → hibridación → extensión) y sus temperaturas decrecientes-crecientes no es intuitivo; y
en el diseño de cebadores, confundir cuál cebador corresponde a cada hebra (y en qué sentido debe leerse) es
el error más probable de este tema. Verificar explícitamente, antes de responder, sobre qué hebra y en qué
sentido (5'→3') actúa cada cebador.

## Relevancia en examen

**Baja** en los exámenes finales oficiales revisados (no aparece ningún ejercicio de PCR o electroforesis en
los 4 exámenes completos analizados) — parece un tema más orientado a la práctica de laboratorio (Práctica 3)
que a examen teórico escrito, aunque Marcos debería confirmarlo con el profesor antes de descartarlo del todo
para el examen.
