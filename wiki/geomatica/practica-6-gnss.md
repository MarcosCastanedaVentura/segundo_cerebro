---
titulo: "Práctica 6 - GNSS: captura de datos en campo"
asignatura: "geomatica"
tema: "Tema 4 - GNSS"
tipo: "practica"
relacionado: ["fundamentos-gnss", "gnss-metodos-posicionamiento", "gnss-errores-precision"]
patrones_error: [3, 7]
examen_relevancia: "media"
fuente: ["Practicas geomatica/Práctica_6.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Práctica de campo en el entorno de la ETSIAAB (UPM) consistente en tomar observaciones de distintas entidades
espaciales (puntos, líneas y polígonos) con dos receptores GNSS de gama distinta, comparando su comportamiento
real.

## Por qué / de dónde viene

El objetivo es aplicar en campo los fundamentos teóricos de [[fundamentos-gnss]] y
[[gnss-metodos-posicionamiento]]: planificar la observación según la geometría de satélites prevista (DOP),
capturar puntos/líneas/polígonos con la app SW Maps, y comparar la precisión real de un receptor de gama media
(Trimble TDC100, basado en SBAS/EGNOS) frente a uno de gama profesional (Leica Zeno FLX100, RTK).

## Fórmula / procedimiento

1. **Planificación** de la observación con GNSS Planning de Trimble: previsualizar el número de satélites
   visibles y la evolución del DOP a lo largo del día para elegir la mejor ventana horaria.
2. **Captura de datos en campo** con apps móviles (SW Maps + Zeno Connect):
   - Crear un proyecto nuevo, capas por tipo de geometría.
   - Tipo punto (p. ej. papeleras), tipo línea (Record Track, un bordillo o seto, posiciones cada 1-3 segundos),
     tipo polígono (una parcela, para calcular superficie).
   - Averaging entre 10-15 segundos por punto para mejorar la precisión.
3. **Exportación**: Share/Export Project en formatos .shp, .kmz, .kml.
4. **Elaboración de mapa** en ArcGIS Pro/ArcMap con los shapefiles resultantes.

## Ejemplo resuelto

Comparación de precisión entre receptores sobre el mismo punto ("Pilar"):
- Trimble TDC100 (SBAS, accuracy real-time <1,5 m típico): X=438249,075 Y=4477006,985
- Leica Zeno FLX100 (RTK, 2-3 cm real-time): X=438249,080 Y=4477006,99
- Diferencia: ΔX=-0,005 m, ΔY=-0,006 m

Esta diferencia milimétrica entre ambos, pese a que el Trimble tiene una especificación nominal de metro, se
explica porque en esa sesión concreta el fix obtenido fue DGPS (no SBAS puro) con buena geometría — el DOP más
favorable del día se dio a las 13h y a las 22h. La superficie del estanque medida con el Zeno fue de 335,66 m²
(perímetro 88,74 m).

## Conexión con otros conceptos

- [[gnss-metodos-posicionamiento]] — el Zeno usa RTK/corrección diferencial; el Trimble usa SBAS/EGNOS,
  disponible en Europa (el material distingue WAAS en Norteamérica, EGNOS en Europa, MSAS en Japón).
- [[gnss-errores-precision]] — el DOP de cada sesión (visible en GNSS Planning) condiciona directamente la
  precisión final obtenida en campo.
- [[../vegetales/MOC]] — este flujo de trabajo (captura de puntos/líneas/polígonos georreferenciados en campo)
  es la base de cualquier inventario agrícola georreferenciado o mapa de parcela.

## Errores frecuentes de Marcos aquí

**Patrón 3**: antes de comparar dos receptores hay que identificar qué método de corrección usa cada uno
(SBAS vs RTK no son comparables directamente en su "categoría" de precisión aunque ambos sean "GNSS
diferencial").

**Patrón 7**: el informe de la práctica valora negativamente que "factores externos pueden limitar la
precisión si no se elige la hora adecuada" y que "la dependencia de una buena conexión de datos para las
correcciones diferenciales puede dar dificultades en zonas con poca cobertura" — es decir, un fix "SINGLE"
(sin corrección) puede dar una posición que parezca razonable pero tenga metros de error; siempre hay que
comprobar el tipo de fix (DGPS/RTK Fixed/Single) antes de validar una medida.

## Relevancia en examen

Media. No hay preguntas de test literales sobre esta práctica, pero refuerza directamente conceptos de examen
de Tema 4: tipos de receptor (mono/bi-frecuencia), DOP como criterio de planificación, y diferencia de
precisión entre corrección SBAS y RTK.
