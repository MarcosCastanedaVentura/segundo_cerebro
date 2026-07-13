---
titulo: "Productos fotogramétricos: MDT, MDS y ortofoto"
asignatura: "geomatica"
tema: "Tema 5 - Fotogrametría"
tipo: "concepto"
relacionado: ["fotogrametria-principios", "practica-7-fotogrametria", "sig-fundamentos"]
patrones_error: [4]
examen_relevancia: "alta"
fuente: ["Tema 5_Fotogrametría_indus.pdf", "Practicas geomatica/Practica_7_Fotogrametria.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Tras el procesado fotogramétrico (SfM/MVS, ver [[fotogrametria-principios]]) se obtienen tres productos
fundamentales, fáciles de confundir entre sí:

- **MDT (Modelo Digital del Terreno)**: representación numérica del **suelo desnudo**, sin vegetación ni
  construcciones. Coordenadas X, Y, Z de la superficie topográfica pura.
- **MDS (Modelo Digital de Superficie)**: incluye **todo lo que cubre el suelo** (vegetación, edificios,
  vehículos). Es lo que "ve" directamente la cámara o el sensor sin filtrar.
- **Ortofotografía**: fotografía aérea corregida geométricamente (ortorrectificada) para que tenga las
  propiedades de un plano — escala uniforme en toda su superficie, medible como un mapa.

## Por qué / de dónde viene

Una fotografía aérea sin corregir es una **proyección cónica** (como el ojo humano o cualquier cámara): los
objetos altos se desplazan radialmente desde el centro de la imagen (efecto de relieve o "desplazamiento por
relieve"), y la escala no es uniforme porque depende de la distancia real al objetivo en cada punto. Un mapa,
en cambio, es una **proyección ortogonal**: escala constante en toda su superficie. La **ortorrectificación**
es el proceso matemático que corrige esas deformaciones (relieve, inclinación de la cámara, perspectiva cónica)
usando el MDT y los parámetros de orientación de la cámara, transformando la fotografía en una ortoimagen que
sí se puede medir como un mapa.

La diferencia MDS − MDT en cada punto da directamente la **altura de lo que hay sobre el terreno** (vegetación,
edificios): por eso el MDS es la base para calcular volumen de copa de árboles o altura de dosel forestal.

## Fórmula / procedimiento

```
Altura de la cubierta vegetal o construida = MDS − MDT (en cada celda)
```

Obtención de un MDT: por métodos fotogramétricos (SfM con filtrado de puntos no-suelo) o por sensor LiDAR
(que penetra mejor la vegetación mediante múltiples retornos del pulso láser). Bajo dosel vegetal denso, el
SfM no puede "ver" el suelo (no penetra la vegetación), por lo que se necesita LiDAR o un MDT de referencia
externo para esa comparación.

## Ejemplo resuelto

En la Práctica 7 se comparó el Vuelo Americano de 1956 (fotografía analógica sin ortorrectificar, blanco y
negro, resolución media) con la ortofotografía PNOA actual (RGB + infrarrojo, resolución <0,5 m,
ortorrectificada). La imagen de 1956 se ve "deformada" respecto a un mapa porque son fotografías aéreas sin
corregir geométricamente, con efectos de relieve, inclinación de cámara y perspectiva cónica; el PNOA actual sí
está ortorrectificado, por lo que "mide igual que un mapa" en cualquier punto de la imagen.

En agricultura, el MDS − MDT de un viñedo permite estimar el volumen 3D de copa correlacionado con la
producción, y comparando MDT pre/post-poda se puede cuantificar el volumen de vegetación eliminado.

## Conexión con otros conceptos

- [[fotogrametria-principios]] — el proceso SfM/MVS que genera estos productos.
- [[practica-7-fotogrametria]] — comparación práctica Vuelo Americano vs PNOA.
- [[sig-fundamentos]] — MDT y MDS son datos raster, base del modelo de datos SIG.
- [[../vegetales/MOC]] — inventario forestal (altura de dosel, volumen maderable), control de poda, movimiento
  de tierras en obras de ingeniería rural.

## Errores frecuentes de Marcos aquí

**Patrón 4 (confundir cocientes/magnitudes relacionadas)**: MDT y MDS se confunden fácilmente porque suenan
casi igual y ambos son "modelos digitales de altura". La regla mnemotécnica: MDT = Terreno (suelo puro),
MDS = Superficie (todo incluido). Antes de responder cuál usar para un cálculo, identificar primero si el
objetivo es el relieve puro (MDT, para pendientes, hidrología) o la altura de lo que hay encima (MDS, para
volumen de copa, altura de edificios).

## Relevancia en examen

Alta. MDT es la respuesta directa a "representación numérica de las características topográficas... acrónimo"
(Tema 5, P1); métodos de elaboración de un MDT (P3: fotogramétricos y LiDAR); si el resultado principal tras
restitución es una ortofoto (P13: verdadero); definición de ortofotografía (P15); diferencia entre fotografía
vertical (perspectiva cónica) y ortofotografía (escala uniforme, P20).
