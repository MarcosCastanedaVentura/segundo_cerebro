---
titulo: "Práctica 7 - Fotogrametría: planificación de vuelo y análisis temporal PNOA"
asignatura: "geomatica"
tema: "Tema 5 - Fotogrametría"
tipo: "practica"
relacionado: ["fotogrametria-principios", "fotogrametria-productos-mdt-mds"]
patrones_error: []
examen_relevancia: "media"
fuente: ["Practicas geomatica/Practica_7_Fotogrametria.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Práctica con dos partes: (1) planificación de una misión de vuelo fotogramétrico con UAV usando el software
Maps Made Easy sobre una cantera en Caudete (Albacete); (2) exploración del PNOA (Plan Nacional de
Ortofotografía Aérea, repositorio del IGN) y análisis temporal comparando el Vuelo Americano de 1956 con la
ortofotografía actual, en SIG.

## Por qué / de dónde viene

Objetivo: familiarizarse con el flujo de trabajo real de producción fotogramétrica en ingeniería —desde la
planificación del vuelo (parámetros de GSD, altura, solapamiento) hasta la integración de productos
históricos y actuales en un SIG para evaluación territorial (ver [[fotogrametria-principios]] y
[[fotogrametria-productos-mdt-mds]]).

## Fórmula / procedimiento

1. **Planificación de vuelo** (Maps Made Easy): definir área (400×400 m), solapamiento frontal/lateral (75%),
   altura de vuelo (80 m con cámara Phantom 4 Pro/Adv, sensor 9,64×7,23 mm, focal 8,8 mm) → GSD resultante
   2,2 cm/píxel, 567 imágenes, 21 pasadas, 16,71 min de vuelo.
   - Para GSD > 3,0 cm/píxel: aumentar la altura de vuelo (a 108 m en este caso).
2. **Descarga PNOA**: identificar la hoja MTN50 correspondiente (por las 3 últimas cifras del DNI) y descargar
   el Vuelo Americano de 1956 en formato ECW, con sistema de coordenadas ETRS89 UTM Zona 30N (EPSG:25830).
3. **Análisis temporal**: comparar ortofotos de distintas épocas (visor PLANEA de la Comunidad de Madrid,
   Comparador PNOA del IGN) para observar cambios de uso del suelo.
4. **Salida cartográfica**: mapa DIN-A3 horizontal con localización, vuelo histórico y ortofoto actual.

## Ejemplo resuelto

Comparación en Villaverde Alto (Madrid): el Vuelo Americano de 1956 muestra suelo mayoritariamente agrícola
con núcleos de población dispersos; la ortofotografía PNOA actual (25 cm de resolución) muestra urbanización
completa del área. La imagen de 1956 se ve "deformada" respecto a un mapa porque son fotografías sin corregir
geométricamente (proyección cónica con efectos de relieve e inclinación de cámara); el PNOA actual está
ortorrectificado, corrigiendo esas deformaciones y permitiendo medir directamente sobre la imagen.

Reto de planificación resuelto en la práctica: "¿Cuándo usarías fotogrametría aérea vertical y cuándo
oblicua?" → vertical para medir (cartografía, ortofoto), oblicua para visualizar (fachadas, zonas urbanas en
3D). "¿Diferencia entre corto y largo alcance?" → corto alcance para objetos pequeños con precisión milimétrica
(mayor resolución de imagen); largo alcance para objetivos de mayor tamaño.

## Conexión con otros conceptos

- [[fotogrametria-principios]] — GSD, solapamiento, tipos de fotogrametría (vertical/oblicua, corto/largo
  alcance) aplicados en esta práctica.
- [[fotogrametria-productos-mdt-mds]] — la ortorrectificación como proceso que distingue foto aérea bruta de
  ortofoto.
- [[../vegetales/MOC]] — el PNOA y los vuelos UAV son la fuente de datos habitual para análisis temporal de
  parcelas agrícolas (cambios de uso del suelo, evolución de cultivos).

## Errores frecuentes de Marcos aquí

Ninguno activado explícitamente en esta práctica, pero conviene vigilar el Patrón 4 (confundir MDT/MDS,
documentado en [[fotogrametria-productos-mdt-mds]]) al interpretar los "resultados clave" de fotogrametría:
relieve sombreado sin edificios (MDT), relieve con árboles y casas (MDS), foto con escala uniforme
(ortofoto) — tres productos que se parecen visualmente pero representan cosas distintas.

## Relevancia en examen

Media. Refuerza directamente varias preguntas de Tema 5 sobre GSD, solapamiento y tipos de fotogrametría, y
sirve de ejemplo aplicado para la pregunta sobre el primer vuelo con cobertura nacional en España (Vuelo
Americano, Tema 5 P8).
