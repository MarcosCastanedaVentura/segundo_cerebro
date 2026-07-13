---
titulo: "Fotogrametría: principios y toma de datos"
asignatura: "geomatica"
tema: "Tema 5 - Fotogrametría"
tipo: "concepto"
relacionado: ["fotogrametria-productos-mdt-mds", "practica-7-fotogrametria", "sig-fundamentos"]
patrones_error: [5]
examen_relevancia: "alta"
fuente: ["Tema 5_Fotogrametría_indus.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Según la definición de la ASPRS (American Society for Photogrammetry and Remote Sensing), la fotogrametría es
"el arte, ciencia y tecnología para la obtención de medidas fiables de objetos físicos y su entorno a través
de procesos de grabación, medida e interpretación de imágenes y patrones de energía electromagnética radiante
y otros fenómenos". En la práctica: reconstruir la geometría 3D real del terreno o un objeto a partir de
fotografías solapadas.

Se clasifica según la posición de la cámara:
- **Aérea vertical**: eje óptico perpendicular al suelo, perspectiva cónica, base de la cartografía y
  ortofotos.
- **Aérea oblicua**: eje inclinado, útil para visualizar fachadas o zonas urbanas, no para medir con precisión
  homogénea.
- **Terrestre de corto alcance**: objetos pequeños, precisión milimétrica (arqueología, ingeniería inversa).
- **Terrestre de largo alcance**: objetos de mayor tamaño (fachadas, taludes), menor precisión relativa.

## Por qué / de dónde viene

El principio físico es la **estereoscopia**: dos fotografías tomadas desde puntos distintos del mismo objeto
contienen la información de profundidad, igual que la visión binocular humana. Al solapar dos imágenes con
suficiente recubrimiento se puede triangular la posición 3D de cualquier punto que aparezca en ambas.

Para que la triangulación sea posible y robusta se exige un recubrimiento mínimo entre fotogramas consecutivos:
- **Recubrimiento longitudinal (frontal)**: 80% (es la zona de solape entre fotos de una misma pasada).
- **Recubrimiento transversal (lateral)**: 60% (solape entre pasadas paralelas).

La técnica moderna que automatiza esta triangulación con cientos de imágenes es **Structure from Motion
(SfM)**: un algoritmo de visión por computador que reconstruye la posición 3D y la orientación de la cámara
en cada foto y genera una nube de puntos densa (mediante Multi-View Stereo, MVS) sin necesidad de instrumentos
analíticos clásicos.

## Fórmula / procedimiento

Flujo de trabajo fotogramétrico típico (arquitectura de un proyecto geomático):
1. **Planificación de la misión** (UAV): definir área de estudio, altura de vuelo, recubrimientos
   longitudinal/transversal, tipo de sensor. La altura de vuelo determina el GSD (Ground Sample Distance,
   tamaño real del píxel proyectado en el suelo): a mayor altura, mayor GSD (menos detalle); a más
   megapíxeles de la cámara, mejor GSD a igual altura.
2. **Captura**: vuelo real o toma terrestre.
3. **Orientación interior y exterior**: la orientación exterior elimina el paralaje y calcula los parámetros
   angulares (giro acimutal, longitudinal, transversal) usando puntos de coordenadas conocidas (GCP - Ground
   Control Points, medidos con GNSS RTK).
4. **Procesado (SfM/MVS)**: genera nube de puntos, MDS y MDT (ver [[fotogrametria-productos-mdt-mds]]).
5. **Productos finales**: ortofoto, modelos digitales, índices espectrales.
6. **Análisis SIG**: integración de los productos en capas georreferenciadas.

Precisión típica en Z para fotogrametría con dron: 2-5 × GSD (peor que en planimetría XY).

## Ejemplo resuelto

En un vuelo con Phantom 4 Pro sobre una cantera en Caudete (Albacete), con una altura de 80 m y solapamientos
del 75%/75%, el software de planificación (Maps Made Easy) estimó 567 imágenes, 2,2 cm/pixel de GSD y 21
pasadas. Para conseguir un GSD por encima de 3,0 cm/píxel (peor resolución) bastaría con **aumentar la altura
de vuelo** (en ese caso concreto, a 108 m); si se quisiera más detalle (menor GSD) habría que **disminuir la
altura de vuelo**, a costa de necesitar más imágenes y más tiempo de vuelo.

## Conexión con otros conceptos

- [[fotogrametria-productos-mdt-mds]] — los productos que resultan de este procesado (MDT, MDS, ortofoto).
- [[practica-7-fotogrametria]] — aplicación real de GSD y análisis temporal con PNOA.
- [[sig-fundamentos]] — el producto final (ortofoto, MDT) se integra como capa raster en un SIG.
- [[../vegetales/MOC]] — la fotogrametría con dron es la base de la agricultura de precisión: recuento de
  cepas/árboles, mapas de vigor por NDVI, estimación de volumen de copa.

## Errores frecuentes de Marcos aquí

**Patrón 5 (orden incorrecto en procedimientos con normas estrictas)**: el flujo fotogramétrico tiene un orden
obligatorio (planificación → captura → orientación interior → orientación exterior → procesado → productos)
que no se puede alterar: no se puede calcular la orientación exterior sin los GCP medidos en campo, ni generar
el MDT sin haber densificado antes la nube de puntos. Es análogo a usar el código Gray en Karnaugh: un orden no
intuitivo pero obligatorio para que el resultado sea válido.

## Relevancia en examen

Alta. Definición de fotogrametría según ASPRS (Tema 5, P9), tipo de fotogrametría con precisión milimétrica
(P4: terrestre de corto alcance), solapamiento mínimo frontal (P5: 80%, es fácil equivocarse con el 60% que es
el transversal — trampa típica), qué se tiene en cuenta al planificar un vuelo UAV (P6), tipo de perspectiva de
la foto aérea vertical (P7: cónica, no ortogonal), primer vuelo con cobertura nacional en España (P8: Vuelo
Americano), relación GSD-megapíxeles (P17), y SfM como técnica de reconstrucción 3D por visión artificial
(P19).
