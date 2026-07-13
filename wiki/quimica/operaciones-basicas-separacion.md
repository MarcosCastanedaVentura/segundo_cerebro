---
titulo: "Operaciones básicas de separación en Ingeniería Alimentaria"
asignatura: "quimica"
tema: "Tema 2 - Bloque 1: Introducción a las operaciones básicas"
tipo: "concepto"
relacionado: ["disoluciones-binarias-raoult-dalton", "extraccion-liquido-liquido", "azeotropos-desviaciones-raoult"]
patrones_error: []
examen_relevancia: "baja"
fuente: ["Tema 2. Bloque 1.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Panorama general (mapa conceptual) de las operaciones básicas ("Operaciones Unitarias") que se estudian
en Ingeniería de procesos alimentarios, clasificadas en tres grandes grupos según el tipo de fenómeno de
transporte implicado:

1. **Transferencia de masa**: destilación, extracción, adsorción/absorción-desorción.
2. **Transferencia de calor y operaciones mixtas**: cristalización, liofilización, secado.
3. **Cantidad de movimiento (fluidos y sólidos)**: conducción de fluidos, sedimentación/centrifugación,
   ósmosis inversa; y acondicionamiento de materias primas: trituración/molienda, tamizado, mezclado.

Este bloque es más un mapa de vocabulario y criterio de decisión ("¿qué operación uso para separar X de
Y?") que teoría matemática — sienta las bases de lo que en cursos posteriores será Operaciones Unitarias
I y II.

## Por qué / de dónde viene

El criterio general para elegir la operación de separación es identificar **qué tienen en común y en qué
se diferencian** las fases o componentes a separar:

- Dos líquidos miscibles con distinto punto de ebullición → **destilación** (simple si Teb muy distintos,
  fraccionada si Teb cercanos).
- Dos líquidos inmiscibles → **decantación**.
- Sólido + líquido, sólido soluble → **evaporación/cristalización**.
- Sólido + líquido, sólido insoluble → **filtración/centrifugación**.
- Dos sólidos, uno soluble en un disolvente y el otro no → **extracción sólido-líquido + filtración**.
- Dos sólidos con distinto tamaño de partícula → **tamizado**.
- El principal "motor" (potencial impulsor) de cualquier proceso de transporte es la **tendencia del
  sistema a alcanzar el equilibrio** (de concentración, temperatura o presión).

## Fórmula / procedimiento

Guía rápida de decisión (según el material):

| Se quiere separar... | Condición | Operación |
|---|---|---|
| Dos líquidos | Miscibles, Teb distinto | Destilación (simple/fraccionada) |
| Dos líquidos | Inmiscibles | Decantación |
| Sólido + líquido | Sólido soluble | Evaporación / Cristalización |
| Sólido + líquido | Sólido insoluble | Filtración / Centrifugación |
| Dos sólidos | Uno soluble en agua, el otro no | Extracción + Filtración |
| Aceites esenciales / aromas volátiles | Se degradan con calor directo | Destilación por arrastre de vapor |
| Soluto termolábil (se descompone con calor) | Necesita quitar agua sin calentar | Liofilización (sublimación a vacío) o destilación a presión reducida |
| Iones de dureza del agua (Ca²⁺, Mg²⁺) | — | Intercambio iónico |

## Ejemplo resuelto

*(Tema 2. Bloque 1.pdf, ejercicio de relacionar)* "Preparación de café soluble conservando aromas" →
como el calor destruiría los compuestos aromáticos volátiles, se usa **liofilización**: se congela el
extracto de café y se sublima el hielo a vacío, eliminando el agua sin pasar por temperaturas altas.
Contraste: "Separación de los componentes del petróleo crudo (gasolina, queroseno...)" → estos tienen
puntos de ebullición relativamente cercanos entre fracciones → **destilación fraccionada**.

## Conexión con otros conceptos

- [[disoluciones-binarias-raoult-dalton]] y [[azeotropos-desviaciones-raoult]]: son la base teórica que
  justifica por qué funciona (o falla) la destilación como operación de este bloque.
- [[extraccion-liquido-liquido]]: desarrolla en detalle una de las operaciones citadas aquí
  (extracción), con su propia fórmula.
- Precede directamente a Operaciones Unitarias I y II (3º curso) — ver [[../carrera/dependencias]].

## Errores frecuentes de Marcos aquí

No se ha detectado ningún patrón de error específico de Marcos en este bloque todavía (es más memorístico
que procedimental). Vigilar si en la práctica confunde "adsorción" (retención en superficie de un sólido)
con "absorción" (disolución en el seno de un líquido) — son términos con Patrón 2 (operadores/términos
parecidos) potencial si se activa en sesión.

## Relevancia en examen

Baja como pregunta de cálculo, pero puede aparecer como pregunta tipo test o de relacionar conceptos con
ejemplos de aplicación industrial (formato visto en el propio material: "¿qué operación usarías para
extraer aceites esenciales?").
