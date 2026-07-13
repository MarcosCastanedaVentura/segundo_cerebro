---
titulo: "Errores GNSS y métricas de precisión (DOP, UERE, CEP)"
asignatura: "geomatica"
tema: "Tema 4 - GNSS"
tipo: "formula"
relacionado: ["fundamentos-gnss", "gnss-metodos-posicionamiento"]
patrones_error: [7]
examen_relevancia: "alta"
fuente: ["Tema 4_GNSS.pdf", "PREGUNTAS TIPO TEST GEOMATICA CLASE.docx"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La precisión final de una medida GNSS no depende de un único factor: es el producto de dos componentes
independientes que hay que multiplicar:

**Incertidumbre total = Calidad de la señal (UERE) × Geometría de los satélites (DOP)**

- **UERE (User Equivalent Range Error)**: agrega en un solo parámetro (en metros) todos los errores de
  "calidad de la medida": reloj del satélite, reloj del receptor, retardo ionosférico, retardo troposférico,
  multipath, ruido del receptor.
- **DOP (Dilution of Precision)**: un multiplicador puramente geométrico que depende de cómo estén repartidos
  en el cielo los satélites usados. No tiene unidades; es un factor por el que se multiplica el UERE.

## Por qué / de dónde viene

Cada satélite define una "esfera de incertidumbre" (no una esfera perfecta, sino una banda difusa por el
UERE) alrededor de su posición conocida. La posición del receptor es la intersección de esas esferas. Si los
satélites están muy agrupados en el cielo (ángulos de intersección agudos), esa intersección se "estira" y
el volumen de incertidumbre resultante crece mucho; si están bien repartidos (ángulos de intersección
próximos a 90°), el volumen de incertidumbre es mínimo. Por eso una **buena geometría** (DOP bajo) es tan
importante como una buena calidad de señal.

Las fuentes de error se agrupan en 4 "pilares":
1. **Satélite**: errores orbitales (efemérides) y de reloj del satélite.
2. **Propagación**: retardo ionosférico (2-50 m, el mayor de todos, variable e impredecible según el TEC —
   Total Electron Content) y retardo troposférico (2-10 m).
3. **Receptor**: reloj del receptor, ruido instrumental, centro de fase de antena.
4. **Estación**: multipath local, altura de antena, coordenadas de la base.

## Fórmula / procedimiento

Jerarquía del DOP:
```
GDOP (Geometric DOP) = √(PDOP² + TDOP²)      → incertidumbre total (posición 3D + tiempo)
PDOP (Position DOP)                           → incertidumbre puramente espacial (3D)
  ├── HDOP (Horizontal DOP)                   → incertidumbre en el plano (x, y)
  └── VDOP (Vertical DOP)                     → incertidumbre en el eje vertical (z), normalmente el
                                                  factor más débil por la falta de satélites bajo el horizonte
TDOP (Time DOP)                               → precisión transmitida en el tiempo
```
Configuración óptima de referencia: DOP < 6.

Métricas estadísticas de confianza:
- **CEP (Circular Error Probable)**: radio donde cae el 50% de las medidas.
- **1σ / RMS**: radio que contiene el 67% de las medidas.
- **2σ / R95**: error máximo en el 95% de los casos.
- **2drms**: dos veces el error medio cuadrático en distancia.

Mitigación de cada fuente de error:
| Fuente de error | Técnica de mitigación |
|---|---|
| Errores orbitales | Efemérides precisas a posteriori (estático) |
| Reloj del satélite | Mensaje de navegación / diferencial de bases cortas |
| Retardo ionosférico | Observables de doble frecuencia (L1/L2) |
| Multipath / atmósfera baja | Máscaras de elevación (>10°-15°) |

## Ejemplo resuelto

Un receptor mono-frecuencia (solo L1) tiene un límite de uso de 20 km respecto a la base porque no puede
modelar el error ionosférico por sí mismo (solo lo corrige ~50% con modelos genéricos). Un receptor
bi-frecuencia (L1+L2) mide el retardo diferencial entre ambas portadoras: como el retardo ionosférico depende
de la longitud de onda, L1 y L2 se frenan de forma distinta, y de esa diferencia se puede calcular la densidad
exacta del TEC en ese instante y neutralizar casi por completo el error — por eso los bi-frecuencia no tienen
límite de distancia a la base (el límite pasa a depender del programa de procesado).

## Conexión con otros conceptos

- [[fundamentos-gnss]] — el receptor mide pseudodistancias afectadas por estos errores.
- [[gnss-metodos-posicionamiento]] — por qué cada método tiene su techo de precisión: el RTK y el estático
  neutralizan el UERE mediante diferenciación y usan geometrías controladas (DOP).

## Errores frecuentes de Marcos aquí

**Patrón 7 (dar por bueno algo que "suena razonable")**: aquí es donde más cuidado hay que tener. Un DOP de,
por ejemplo, 15 "suena" a un número cualquiera, pero es una **mala** geometría (el umbral de referencia es
DOP < 6); igual que hay que verificar el orden de magnitud de un resultado de Física, aquí hay que verificar
si el DOP obtenido está por debajo del umbral antes de aceptar la sesión de observación como válida. También
aplica a no confundir GDOP con PDOP, HDOP o VDOP: son conceptualmente distintos (uno incluye tiempo, otro no).

## Relevancia en examen

Alta. Aparece con mucha frecuencia: relacionar siglas UERE/GDOP/PDOP/CEP/DOP con su definición (P8, ejercicio
de emparejar 5 términos), identificar la fuente de incertidumbre según su origen (satélite/propagación/
receptor/estación, P9 y P13), qué representa el DOP (P11: "multiplicador de error basado en la geometría de
la constelación"), y por qué se necesitan 4 satélites por la falta de sincronización de relojes (P10).
