---
titulo: "Fundamentos de GNSS: segmentos y sistemas de referencia"
asignatura: "geomatica"
tema: "Tema 4 - GNSS"
tipo: "concepto"
relacionado: ["gnss-metodos-posicionamiento", "gnss-errores-precision", "practica-6-gnss"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Tema 4_GNSS.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

GNSS (Global Navigation Satellite System) es el término genérico que engloba todos los sistemas de navegación
por satélite (GPS de EEUU, GLONASS ruso, Galileo europeo, BeiDou chino). Permiten calcular la posición 3D de
un receptor en cualquier punto de la Tierra midiendo distancias a varios satélites cuya posición se conoce con
precisión en cada instante.

Todo sistema GNSS se organiza en tres segmentos:
- **Segmento espacial**: la constelación de satélites que emiten señales.
- **Segmento de control**: estaciones terrestres que vigilan la constelación, calculan las órbitas reales
  (efemérides) y suben al satélite las correcciones de reloj y navegación que el usuario necesitará.
- **Segmento de usuario**: los receptores (topográficos, smartphones, tractores con guiado automático, etc.).

## Por qué / de dónde viene

El posicionamiento por GNSS se basa en multilateración: el receptor mide su distancia (realmente una
"pseudodistancia", ver [[gnss-errores-precision]]) a varios satélites simultáneamente. Con 3 distancias se
obtendría una posición 3D si los relojes estuvieran perfectamente sincronizados, pero el reloj del receptor
(barato, de cuarzo) no lo está respecto al reloj atómico del satélite. Por eso se necesita un **cuarto
satélite**: 3 incógnitas de posición (X, Y, Z) + 1 incógnita de desfase de reloj del receptor = 4 incógnitas,
4 ecuaciones.

Para que la cartografía y las coordenadas tengan sentido en un territorio concreto, además del sistema GNSS
hace falta un **datum/sistema de referencia geodésico**:
- **WGS84**: el datum global que usan por defecto los satélites GPS y la mayoría de dispositivos.
- **ETRS89**: el marco de referencia oficial y obligatorio para cartografía en España y Europa (ligado a la
  placa euroasiática, por lo que no se ve afectado por la deriva continental como sí lo está WGS84 a nivel
  global).

## Fórmula / procedimiento

Multilateración con 4 satélites (esquema conceptual):

```
Para cada satélite i:  ρᵢ = c · (t_recepción - t_emisión)
```
donde ρᵢ es la pseudodistancia, c la velocidad de la luz, y el desfase de reloj del receptor (δt) aparece como
una incógnita más en el sistema de ecuaciones junto a X, Y, Z del receptor.

Estructura de la señal GNSS:
- **Portadoras**: ondas en banda L (GPS: L1 1575,42 MHz, L2 1227,60 MHz, L5 1176,23 MHz; Galileo: E1, E5a, E5b,
  E6; BeiDou: B1, B2, B3; GLONASS usa FDMA, frecuencia propia por satélite).
- **Códigos**: C/A (adquisición basta, civil), P (preciso, militar), códigos civiles modernos (L2C).
- **Mensaje de navegación**: efemérides, almanaque, correcciones de reloj.

## Ejemplo resuelto

Un receptor GPS mono-frecuencia de bajo coste capta 6 satélites GPS con máscara de elevación de 15° (se
descartan los que están muy bajos en el horizonte, donde el error atmosférico es mayor). Usa 4 de ellos para
resolver X, Y, Z y δt_receptor simultáneamente. Si el reloj del receptor tuviese un error de 1 ns sin corregir,
esto se traduciría en un error de posición de 30 cm (1 ns × velocidad de la luz), de ahí la necesidad de tratar
δt como incógnita en vez de asumirlo nulo.

## Conexión con otros conceptos

- [[gnss-metodos-posicionamiento]] — cómo se usa esta base (código/fase) para lograr distintas precisiones
  (absoluto, DGPS, RTK, PPP, estático).
- [[gnss-errores-precision]] — fuentes de error (ionosfera, troposfera, multipath) y cómo se cuantifican
  (DOP, UERE, CEP).
- [[practica-6-gnss]] — aplicación práctica con receptores Leica Zeno y Trimble en campo.
- [[../vegetales/MOC]] — el posicionamiento GNSS de precisión centimétrica (RTK) es la base del guiado
  automático de maquinaria agrícola y del muestreo georreferenciado en agricultura de precisión.

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmulas sin verificar las condiciones de uso)**: en Estadística confundió cuándo usar
tabla Z frente a t-Student según se conociera o no σ; aquí el riesgo análogo es mezclar WGS84 y ETRS89 como si
fueran intercambiables. Aunque muy parecidos, mezclarlos introduce errores métricos porque no son el mismo
datum (ETRS89 es el marco legal obligatorio en España; WGS84 es el que usan por defecto los satélites GPS).
Antes de dar una coordenada, verificar siempre en qué sistema de referencia está expresada.

## Relevancia en examen

Alta. Es contenido de examen tipo test recurrente: función del segmento de control (Tema 4, P2), sistema
geodésico de referencia global (P3: WGS84), por qué es crítico distinguir WGS84/ETRS89 en España (P6), y la
razón de que se necesiten 4 satélites (falta de sincronización de relojes, P10). También aparecen preguntas
sobre técnicas geodésicas de precisión como VLBI y SLR (P12, P15).
