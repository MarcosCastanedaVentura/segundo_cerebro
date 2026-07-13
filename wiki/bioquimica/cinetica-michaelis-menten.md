---
titulo: "Cinética enzimática: ecuación de Michaelis-Menten, Km y Vmax"
asignatura: "bioquimica"
tema: "Tema 2 - Enzimas"
tipo: "formula"
relacionado: ["enzimas-estructura-funcion", "inhibicion-enzimatica", "regulacion-enzimatica-alosterica"]
patrones_error: [4, 6, 7]
examen_relevancia: "alta"
fuente: ["Tema 2_Enzimas.pdf", "Clase de problemas de cinética.pdf", "Problemas Enzimas resueltos.pdf", "Problemas Enzimas II resuelto.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Recuperacion (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La ecuación de Michaelis-Menten (1913) describe cómo varía la velocidad inicial (V₀) de una reacción
catalizada por un enzima en función de la concentración de sustrato [S], cuando la concentración de enzima
es constante y baja frente a [S]. Es la herramienta central para caracterizar cuantitativamente cualquier
enzima y para detectar y clasificar inhibidores (ver [[inhibicion-enzimatica]]).

## Por qué / de dónde viene

El mecanismo asumido es E + S ⇌ ES → E + P, con una primera etapa reversible y rápida (equilibrio de unión)
y una segunda etapa (ruptura de ES a E + P) irreversible y lenta, que es la que limita la velocidad global:
V₀ = k₂[ES]. Cuando [S] es muy baja, casi todo el enzima está libre y V₀ crece linealmente con [S]; cuando
[S] es muy alta, todo el enzima está saturado en forma ES y V₀ tiende a un máximo (Vmax) que ya no depende de
[S]. Esta transición de comportamiento lineal a comportamiento saturado (curva hiperbólica) es la firma de la
cinética michaeliana.

## Fórmula / procedimiento

**Ecuación de Michaelis-Menten:**

V₀ = (Vmax · [S]) / (Km + [S])

- V₀: velocidad inicial de la reacción (unidades de concentración/tiempo, ej. mM/min).
- Vmax: velocidad máxima, alcanzada cuando el enzima está saturado de sustrato. Varía proporcionalmente con
  [E] y con las condiciones de reacción (T, pH, fuerza iónica) — **no** es una constante universal del
  enzima, depende de cuánto enzima hay en el ensayo.
- Km (constante de Michaelis): concentración de sustrato a la que V₀ = ½ Vmax. Es característica de cada
  pareja enzima-sustrato (no depende de [E]). Refleja la afinidad: **Km baja = mayor afinidad** (con poco
  sustrato ya se satura la mitad del enzima).
- [S]: concentración de sustrato.

**Representación doble recíproca de Lineweaver-Burk** (linealiza la hipérbola para poder leer Km y Vmax en
una recta):

1/V₀ = (Km/Vmax) · (1/[S]) + 1/Vmax

Es una recta y = mx + b con:
- pendiente = Km/Vmax
- corte con el eje Y (1/V₀, cuando 1/[S]→0) = 1/Vmax
- corte con el eje X (1/[S], cuando 1/V₀=0) = -1/Km

**Procedimiento para resolver un problema de cinética** (orden obligatorio, Patrón 3/4 de Marcos si se
salta):
1. Comprobar si los datos ya están en forma doble recíproca (1/V vs 1/[S]) o hay que invertirlos primero.
2. Ajustar la recta y leer los dos cortes con los ejes.
3. De la ordenada en el origen obtener Vmax; del corte con el eje X obtener Km.
4. Solo entonces, si hay inhibidor, comparar Km y Vmax con y sin inhibidor (ver [[inhibicion-enzimatica]]).

## Ejemplo resuelto

*Adaptado de Problemas Enzimas resueltos.pdf.* De una gráfica V₀ vs [S] se lee: la recta doble recíproca da
corte en Y = 1/Vmax = 50 min/mM → **Vmax = 0,02 mM/min**; corte en X (pendiente de la recta) da 1/Km = 0,2
mM⁻¹ → **Km = 5 mM**.

Pregunta: ¿cuánto sustrato se ha transformado en 10 minutos si [S]=5 mM (sin inhibidor)?

V₀ = (Vmax · [S])/(Km + [S]) = (0,02 mM/min · 5 mM)/(5 mM + 5 mM) = (0,1 mM²/min)/(10 mM) = 0,01 mM/min

Cantidad transformada en 10 min = 0,01 mM/min × 10 min = **0,1 mM**.

Nota de verificación (Patrón 7): como [S]=Km en este caso, V₀ debe ser exactamente ½ Vmax = 0,01 mM/min — la
propia definición de Km sirve para comprobar el resultado sin rehacer la cuenta.

## Conexión con otros conceptos

- [[inhibicion-enzimatica]]: se detecta y clasifica comparando Km y Vmax con y sin inhibidor sobre esta misma
  ecuación.
- [[regulacion-enzimatica-alosterica]]: los enzimas alostéricos NO siguen esta cinética (curva sigmoidal, no
  hiperbólica; se habla de K0,5 en vez de Km).
- [[enzimas-estructura-funcion]]: Vmax y Km se miden sobre la reacción E+S→ES→E+P descrita ahí.
- Conexión con Estadística/Matemáticas: ajuste de una recta por mínimos cuadrados a los datos dobles
  recíprocos (ver [[../estadistica/MOC]]).

## Errores frecuentes de Marcos aquí

**Patrón 4** (confundir cocientes relacionados): en Lineweaver-Burk hay tres cocientes parecidos —
pendiente=Km/Vmax, corte en Y=1/Vmax, corte en X=-1/Km — y es fácil asignar el valor numérico al parámetro
equivocado (ej. leer el corte en Y como si fuera 1/Km). Antes de sustituir números, haz que dibuje la recta y
etiquete explícitamente qué eje y qué corte corresponde a qué magnitud.

**Patrón 6** (copiar mal los datos): estos problemas casi siempre dan los datos ya invertidos (1/[S] y 1/V₀)
en vez de [S] y V₀ directos — leer "0,25 mM⁻¹" como si fuera "0,25 mM" invalida todo el cálculo posterior.
Pide que escriba explícitamente las unidades de cada dato leído antes de operar.

**Patrón 7** (validar sin verificar): siempre se puede comprobar Km calculando si V₀ = ½Vmax cuando [S]=Km —
usarlo como check automático antes de dar un resultado por bueno.

## Relevancia en examen

**Alta — el bloque más seguro de puntos del examen.** Aparece como problema numérico completo (con gráfica de
Lineweaver-Burk, cálculo de Km/Vmax con y sin inhibidor, cálculo de Ki, y V₀ a una [S] dada) en el examen
final 2022-2023 (pregunta 7) y en la recuperación 2023-2024 (pregunta 7), además de en las dos hojas de
problemas de enzimas resueltos y en la clase de problemas de cinética. Es prácticamente seguro que cae un
problema de este tipo en cada convocatoria.
