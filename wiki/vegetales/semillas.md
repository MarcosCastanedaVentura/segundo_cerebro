---
titulo: "Semillas: estructura, producción certificada y germinación"
asignatura: "vegetales"
tema: "UT1 - Bases y técnicas agronómicas"
tipo: "concepto"
relacionado: ["agua-en-sistemas-agricolas", "cereales", "cebada", "cultivo-del-trigo"]
patrones_error: [2, 5]
examen_relevancia: "alta"
fuente: ["raw/.../vegetales/Tema 1.- Semillas PMPOV 2026.pdf", "raw/.../vegetales/apuntes_claude/vegetales_guia_v2.docx", "raw/.../vegetales/apuntes_claude/vegetales_guia_bloques.docx (veg_guide.js)"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Las semillas proceden de la fecundación de los óvulos por el polen en las flores (angiospermas). Constan de tres elementos básicos: un **embrión** (futura planta), un **tejido de reserva** (alimenta al embrión durante la germinación) y una **cubierta** protectora. Su función es multiplicar la especie: son un elemento de dispersión en el espacio (nuevos individuos) y en el tiempo (resisten condiciones desfavorables hasta que germinan).

En la doble fecundación de las monocotiledóneas (cereales): un núcleo espermático fecunda la oósfera → embrión (con su cotiledón transformado en **escutelo**); el otro fecunda los núcleos polares → **endospermo** (tejido de reserva); los tegumentos del óvulo → **testa**; la pared del ovario → **pericarpio**; las envueltas de la flor (glumas/glumillas) → envueltas del grano.

## Por qué / de dónde viene

**Granos vestidos vs. desnudos**: si las glumillas (pálea y lemma) quedan soldadas al grano tras la trilla, es un grano vestido (**cebada, avena, arroz**); si se desprenden, es desnudo (**trigo, centeno, triticale, maíz**). Regla mnemotécnica: *cebada vestida, trigo desnudo*.

Debajo de la testa está la **aleurona**, capa de células vivas que segrega enzimas (amilasas, proteasas, betaglucanasas) durante la germinación para degradar las reservas del endospermo (almidón, proteínas) y alimentar al embrión. El **escutelo** comunica el embrión con la aleurona y segrega giberelinas que estimulan esa secreción enzimática — este mecanismo hormonal (escutelo→giberelinas→aleurona→enzimas) es la base del **malteado de la cebada** para cerveza.

**Producción de semilla comercial**: se parte de material parental (G-0) y se multiplica varios años bajo control oficial hasta llegar a semilla certificada. Categorías y colores de etiqueta (muy preguntado): Prebase y Base (etiqueta blanca) → **R-1 (etiqueta azul)** → **R-2 (etiqueta roja)** → semilla estándar (etiqueta amarilla/naranja, sin control oficial de campo, solo control interno del obtentor).

## Fórmula / procedimiento

**Fases de la germinación**: (1) Hidratación/imbibición — absorción rápida de agua, al final aparece la radícula; (2) Activación metabólica — el escutelo segrega giberelinas, la aleurona produce enzimas, no cambia apenas el peso; (3) Crecimiento del embrión — la radícula crece y absorbe agua, aumenta el peso de la plántula pero *disminuye* el peso de la semilla porque el embrión consume las reservas.

**Análisis de calidad de semillas de cebada** (relevante para malterías/cerveceras — conexión con ingeniería alimentaria):
- **Pureza (%)** = (peso semillas puras / peso muestra) × 100; impurezas = 100 − pureza.
- **Peso de mil granos (g)**: indica reservas; varía con la pluviometría de la zona (secano árido ~40 g, húmedo ~52 g).
- **Peso específico (kg/hL)**: mayor densidad = más reservas; mínimo exigido >65 kg/hL.
- **Calibre**: cribado a 2,8/2,5/2,2 mm; para malta se exige fracción >2,5 mm >65% y <2,2 mm <10%.
- **Energía germinativa (EG)**: test con 100 semillas, 4 mL agua, 20°C, 3 días; EG (%) = 100×(germinadas/sembradas); exigido >90%.
- **Sensibilidad al agua (SA)**: SA = %germinación(4 mL) − %germinación(8 mL); exigido <15% — un exceso de agua limita la difusión de O₂ al embrión.
- **Viabilidad (test de tetrazolio)**: tiñe de **rojo los tejidos vivos**; los necrosados no se tiñen (trampa habitual: invertir esto).
- **Proteína**: método Kjeldahl, %N × 6,25; óptimo cebada cervecera 10,0-11,0%.

## Ejemplo resuelto

Test de germinación de cebada: 93 semillas germinadas de 100 con 4 mL, y 87 de 100 con 8 mL.
- Energía germinativa = 93% (cumple, >90%)
- Sensibilidad al agua = 93 − 87 = 6% (cumple, <15%)

Cálculo de humedad: una muestra de cebada de 5,00 g fresca da 4,48 g tras desecar en estufa a 105°C → agua = 5,00 − 4,48 = 0,52 g → %H = 100×(0,52/5,00) = 10,4%.

## Conexión con otros conceptos

- Base directa de [[cebada]] (todo el proceso de malteado/cervecería parte de la germinación controlada de la semilla) y de [[cultivo-del-trigo]] (gluten = gliadinas+gluteninas, análogas a las hordeínas/glutelinas de cebada).
- El concepto de potencial hídrico y humedad de [[agua-en-sistemas-agricolas]] es el que rige la fase de hidratación de la germinación.
- Relevancia para ingeniería alimentaria: los criterios de calidad de semilla (pureza, calibre, energía germinativa, proteína, beta-glucanos) son literalmente los parámetros de recepción de materia prima en una maltería/cervecera — puente directo entre producción agrícola y tecnología alimentaria.

## Errores frecuentes de Marcos aquí

- **Patrón 2** (confundir operadores/términos parecidos): confundir **testa** (cubierta de la semilla, del tegumento del óvulo) con **pericarpio** (pared del ovario) — son capas distintas y superpuestas. También confundir **hordeínas** (proteínas de reserva de alto peso molecular del endospermo) con **albúminas/globulinas** (proteínas de bajo peso molecular de la aleurona/embrión, no de reserva).
- **Patrón 5** (orden en procedimientos estrictos): en el cálculo de energía germinativa/sensibilidad al agua, el orden de la resta importa (siempre %4mL − %8mL, nunca al revés) y las condiciones del test (4 mL vs 8 mL, 20°C, 3 días) son fijas — no improvisar el protocolo.

## Relevancia en examen

Muy alta en UT1/UT2: en los exámenes reales aparecen preguntas V/F sobre el color de etiqueta de semilla certificada (R-1 azul, no verde — trampa repetida), sobre qué se tiñe de rojo en el test de tetrazolio (vivos, no necrosados), sobre en qué fase de la germinación aparece la radícula (al final de la hidratación) y ejercicios numéricos de pureza/humedad/energía germinativa con datos limpios.
