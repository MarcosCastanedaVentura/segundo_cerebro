---
titulo: "El agua en los sistemas agrícolas (bases agronómicas, Tema 1)"
asignatura: "vegetales"
tema: "UT1 - Bases y técnicas agronómicas"
tipo: "concepto"
relacionado: ["semillas", "cereales", "cultivo-del-trigo", "cebada", "girasol", "colza", "patata", "remolacha-azucarera", "../geomatica/MOC"]
patrones_error: [3, 4, 6]
examen_relevancia: "alta"
fuente: ["raw/.../vegetales/Tema 1 2026 primera parte.pdf", "raw/.../vegetales/Tema 1 2026 segunda parte.pdf", "raw/.../vegetales/Tema 1.- El agua en los sistemas agrícolas (caso especial de los cereales) PMPOV2026-2.pdf", "raw/.../vegetales/apuntes_claude/vegetales_guia_v2.docx", "raw/.../vegetales/apuntes_claude/vegetales_guia_bloques.docx (veg_guide.js)"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un **sistema agrícola** es una población de plantas rodeada por el medio (suelo, atmósfera) e influida por condiciones externas (clima, plagas) y por las labores del agricultor. Es un **sistema abierto**: intercambia materia y energía con el exterior (entran agua, radiación, CO₂, abonos; salen cosechas, agua, O₂). El **rendimiento agrícola** es la cantidad de producto por unidad de superficie (kg/ha, t/ha).

El agua es uno de los **factores limitantes** del rendimiento (junto con los nutrientes): no fija el techo productivo (eso lo hacen los **factores determinantes** — radiación, temperatura, CO₂ — no controlables a campo abierto), pero si no se aporta al nivel adecuado, reduce el rendimiento por debajo de lo que permitirían los determinantes. Los **factores reductores** (heladas, salinidad, plagas, malas hierbas) restan rendimiento activamente cuando aparecen. Esta tríada (determinantes / limitantes / reductores) es el concepto más preguntado de la UT1.

## Por qué / de dónde viene

Las plantas en crecimiento activo tienen ~80% de humedad en su masa fresca; esa agua da **turgencia** a las células (presión contra la pared celular rígida) y permite el crecimiento de tejidos herbáceos. El estado hídrico se caracteriza con el **potencial hídrico (Ψ)**, energía del agua por unidad de volumen (unidades de presión: MPa). El agua siempre fluye de mayor a menor potencial hídrico: Ψ_atmósfera < Ψ_hoja < Ψ_raíz < Ψ_suelo. Este gradiente es lo que hace que el agua ascienda por la planta y se pierda finalmente a la atmósfera por **transpiración** en los estomas (mismo poro por el que entra el CO₂ para la fotosíntesis — de ahí el compromiso fisiológico entre fotosintetizar y no deshidratarse).

En la hoja: Ψh = Ψp + Ψo (potencial de presión, siempre ≥0, más el potencial osmótico, siempre ≤0). En el suelo: Ψs = Ψm + Ψo + Ψg (matricial + osmótico + gravitacional). Al secarse el suelo, el potencial matricial se hace más negativo (mayor tensión matricial) y la planta necesita más energía para extraer el agua.

## Fórmula / procedimiento

- **Balance hídrico del suelo**: entradas (lluvia P, riego) vs. salidas (evapotranspiración ETc, percolación, escorrentía). Si P > ETc el suelo almacena agua hasta la Capacidad de Campo (CC, tensión 10 kPa); si P < ETc se consume la reserva hasta el Punto de Marchitez (PM, 1500 kPa). **Agua Útil (AU) = CC − PM**.
- **Evapotranspiración del cultivo**: ETc = ETo × kc, donde ETo es la evapotranspiración de referencia (depende de radiación neta, humedad y viento) y kc el coeficiente de cultivo (crece con el LAI a lo largo del ciclo: kc bajo al inicio ~0,5-0,7, máximo ~1,0-1,2 en pleno desarrollo, baja al final por senescencia).
- **Déficit hídrico**: DH = ETmáx − ETc. En secano español, el déficit se concentra típicamente en los meses finales del ciclo (abril-junio), coincidiendo con maduración y llenado del grano — **no al principio del ciclo** (trampa de examen habitual).
- **Contenido de agua de la planta**: MF (materia fresca) = MS (materia seca) + H₂O; %MS + %H = 100%.
- **PAR y biomasa** (transversal a todos los cultivos): PARi = 0,45·Rg; Ei (fracción PAR interceptada) = 1 − e^(−k·LAI); PAR interceptada = Ei·PARi; EUR (eficiencia en el uso de la radiación) = Biomasa/PAR interceptada (g ms/MJ); Biomasa = PARi·(1−e^(−k·LAI))·EUR.

## Ejemplo resuelto

Un cultivo de cereal (fuente: Tema 1, segunda parte) tiene LAI = 3,5, k = 0,77, EUR = 2,75 g/MJ, y Rg = 26,1 MJ/m² día en junio:
1. PARi = 0,45 × 26,1 = 11,75 MJ/m² día
2. Ei = 1 − e^(−0,77×3,5) = 1 − e^(−2,695) = 1 − 0,068 = 0,93 (93%)
3. PAR interceptada = 0,93 × 11,75 = 10,9 MJ/m² día → en el mes (30 días): 327 MJ/m² mes
4. Biomasa = 327 × 2,75 = 899,3 g/m² mes

Otro ejemplo de potencial hídrico: si Ψp = 0,75 MPa y Ψo = −1,75 MPa a mediodía → Ψh = 0,75 − 1,75 = **−1,00 MPa**.

## Conexión con otros conceptos

- Es la base fisiológica que se repite en [[cereales]], [[cebada]], [[cultivo-del-trigo]], [[girasol]], [[colza]], [[patata]] y [[remolacha-azucarera]]: todos definen su fase más sensible al estrés hídrico (floración en cereales y girasol; inicio de tuberización en patata; llenado del grano en colza y cereales).
- El seguimiento del estado hídrico y nutricional de los cultivos por teledetección (NDVI, TCARI/OSAVI, imágenes de dron/satélite para estimar déficit de N o estrés hídrico) conecta directamente con [[../geomatica/MOC]] — es el mismo tipo de índices espectrales que se estudian en Geomática aplicados aquí a agricultura de precisión (ver ejemplo real de la plataforma "Layers" para remolacha en [[remolacha-azucarera]]).
- Relevante para ingeniería alimentaria: el estado hídrico del cultivo en campo determina directamente parámetros de calidad de la materia prima que llega a fábrica (contenido de proteína en cereales, VTIR en remolacha, calibre en patata, contenido de aceite en oleaginosas).

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmulas sin verificar el caso): confundir cuándo usar ETmáx vs ETc, o aplicar la fórmula de tiempo térmico sin fijar antes la temperatura base (Tb) de cada cultivo (cebada Tb=0°C, girasol Tb=6°C, etc.) — hay que identificar primero el cultivo y su Tb antes de calcular.
- **Patrón 4** (confundir cocientes relacionados): mezclar Ψp con Ψo al calcular Ψh — recordar que Ψp ≥ 0 (presión) y Ψo ≤ 0 (solutos), y que Ψh es la suma algebraica, no siempre positiva.
- **Patrón 6** (copiar mal datos): en ejercicios con LAI, k y Rg hay que anotar cada dato con su unidad antes de sustituir en la fórmula — es fácil intercambiar k y LAI en la fórmula de Ei.

## Relevancia en examen

Tema con alta frecuencia en UT1 (introducción): en los exámenes reales de 2024-25 y años anteriores aparece siempre un bloque de test V/F sobre factores determinantes/limitantes/reductores, PAR (con la trampa recurrente de poner "MJ/m²" en vez de "nm" como unidad), y balance hídrico; y un **ejercicio práctico obligatorio** de cálculo de PARi → Ei → PAR interceptada → biomasa/rendimiento con datos numéricos limpios (ver ejemplo arriba, tomado literalmente del examen de junio 2025). También cae con frecuencia el ejercicio de tiempo térmico (fórmula: tiempo térmico = temperatura × tiempo).
