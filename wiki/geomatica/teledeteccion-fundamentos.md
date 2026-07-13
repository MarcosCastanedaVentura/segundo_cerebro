---
titulo: "Teledetección: fundamentos radiométricos y resolución"
asignatura: "geomatica"
tema: "Tema 6 - Teledetección"
tipo: "concepto"
relacionado: ["indice-ndvi", "practica-8-teledeteccion", "sig-fundamentos"]
patrones_error: [4]
examen_relevancia: "alta"
fuente: ["Teledetección_Fundamentos_Geomática26_GIAg_M.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La teledetección es la técnica de obtener información de la superficie terrestre sin contacto físico,
mediante sensores (normalmente satelitales) que captan la radiación electromagnética reflejada o emitida por
los objetos. Cada tipo de superficie (agua, vegetación, suelo desnudo) tiene una **firma espectral**
característica: cómo refleja la energía en cada longitud de onda.

## Por qué / de dónde viene

Toda la teledetección óptica se basa en un balance de energía: la radiación que incide sobre una superficie se
reparte entre reflejada, absorbida y transmitida. Las magnitudes radiométricas clave son:

- **Energía radiante**: cantidad total de energía transportada por la radiación.
- **Flujo radiante**: tasa de transferencia de esa energía por unidad de tiempo.
- **Reflectividad**: proporción de radiación incidente que es reflejada.
- **Absortividad**: fracción absorbida por el material.
- **Transmisividad**: cuánta radiación atraviesa el material sin ser absorbida ni reflejada.
- **Emitancia (M)**: potencia radiante emitida por unidad de área de una superficie.

El **cuerpo negro** es el objeto teórico ideal que absorbe toda la energía incidente sin reflejar nada (y por
tanto emite el máximo posible según su temperatura, base de los sensores térmicos). Las **superficies
lambertianas** reflejan la energía por igual en todas direcciones, de forma que la radiancia captada por el
sensor no depende del ángulo de observación — al contrario que las superficies especulares.

La energía de un fotón depende de su longitud de onda según `Q = h·c/λ`: a mayor longitud de onda, menos
energía transporta cada fotón. Esto explica por qué los sensores térmicos (longitudes de onda largas, 8-14 μm)
necesitan un IFOV (campo de visión instantáneo) más grande que los ópticos para captar una señal detectable, y
por eso tienen peor resolución espacial.

## Fórmula / procedimiento

Cuatro tipos de resolución en un sensor (fáciles de confundir entre sí):
- **Espacial**: tamaño del píxel en el terreno (cuánto detalle geométrico).
- **Espectral**: número y anchura de las bandas del espectro que capta.
- **Radiométrica**: número de niveles de intensidad que puede distinguir (bits por píxel).
- **Temporal**: intervalo de tiempo entre dos adquisiciones sucesivas del mismo punto (frecuencia de revisita).

Espectro visible (única parte perceptible por el ojo humano, máxima radiación solar): 0,4 a 0,7 μm.

Comparativa de satélites según escala:
| Escala | Ejemplo | Resolución |
|---|---|---|
| Reconocimiento (baja) | NOAA-AVHRR | Muy baja, cobertura global diaria |
| Semidetalle (media) | Landsat TM | 30 m |
| Detalle (alta) | IKONOS, Sentinel-2 | 10 m (Sentinel-2 en NIR/rojo) |
| Alto detalle (muy alta) | Cámaras fotogramétricas / WorldView | <1 m |

## Ejemplo resuelto

Para monitorizar variabilidad intra-parcelaria en una finca de frutales con marcos de plantación estrechos, la
combinación más adecuada es Sentinel-2 (10 m en bandas visibles y NIR, alta frecuencia de revisita), frente a
MODIS o Meteosat (mejor resolución temporal pero espacial demasiado basta para distinguir árboles individuales)
o Landsat (30 m, insuficiente para marcos de plantación estrechos).

Composición en "falso color estándar" (NIR, Rojo, Verde): una zona con vegetación muy densa y activa se ve de
color rojo intenso, porque el NIR (alta reflectividad de la vegetación sana) se asigna al canal rojo de
visualización.

## Conexión con otros conceptos

- [[indice-ndvi]] — el NDVI y otros índices se calculan a partir de estas magnitudes de reflectividad en
  bandas concretas (rojo y NIR).
- [[practica-8-teledeteccion]] — aplicación real con imágenes Sentinel-2 y combinación de bandas en QGIS.
- [[../vegetales/MOC]] — la elección de satélite/resolución según el cultivo y la escala de manejo es
  directamente aplicable a agricultura de precisión.

## Errores frecuentes de Marcos aquí

**Patrón 4 (confundir cocientes/magnitudes relacionadas)**: reflectividad, absortividad y transmisividad sumn
1 (ρ+α+τ=1) y se confunden fácilmente entre sí, igual que tgφ y cosφ en el triángulo de potencias de
Electrotecnia. También los 4 tipos de resolución (espacial/espectral/radiométrica/temporal) se prestan a
confusión porque los nombres suenan parecido: antes de responder cuál es cuál, verbalizar la definición
completa de cada uno.

## Relevancia en examen

Alta. Superficies lambertianas (Tema 6, P1), definición de cuerpo negro (P2), relacionar magnitudes
radiométricas con su definición (P6, ejercicio de emparejar 6 términos), rango del espectro visible (P10),
dispersión atmosférica (P11), razón física de la peor resolución espacial de sensores térmicos vía Q=hc/λ
(P13), relación banda espectral-aplicación (P16), resolución temporal (P18), clasificación de satélites por
escala de detalle (P19).
