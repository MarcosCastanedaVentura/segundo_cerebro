---
titulo: "Distribución de Poisson"
asignatura: "estadistica"
tema: "Tema 2.3 — Distribuciones de probabilidad de uso frecuente"
tipo: "concepto"
relacionado: ["distribucion-binomial", "variable-aleatoria-discreta"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["DISTRIBUCIONES DE PROBABILIDAD DE USO FRECUENTE.pdf (Tema 5 Ibáñez)", "Tema2.3_DistribProbFrec25-26-2.pdf", "wuolah-free-Solucion-Junio-2025-parte-2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La distribución de Poisson, X∼℘(λ), modela el número de incidencias aleatorias **independientes** que ocurren sobre
un medio continuo (tiempo, longitud, superficie, volumen), cuando existe una tasa media constante λ de incidencias
por unidad de medio. Es la "distribución de los sucesos raros": número de llamadas a una centralita por hora, número
de microorganismos por cc de agua, número de heladas en un mes.

## Por qué / de dónde viene

Matemáticamente, la Poisson es el **límite de la Binomial** cuando n→∞, p→0, manteniendo el producto np constante
e igual a λ. Intuitivamente: trocea el medio continuo (una hora, un cc) en n fragmentos minúsculos; cada fragmento
es un "ensayo de Bernoulli" (¿hay incidencia en este fragmento diminuto o no?) con p muy pequeño; al ser n muy
grande y los fragmentos muy pequeños, la falta de reemplazo/independencia deja de importar. Por eso hereda de la
Binomial la condición de que las incidencias deben distribuirse con homogeneidad (si se agrupasen en una zona
concreta, np ya no sería constante y el modelo dejaría de ser válido).

## Fórmula / procedimiento

X∼℘(λ): fx(x,λ) = e^(-λ)·λˣ/x!  para x∈{0,1,2,...}, con λ>0.

Media: m = λ.   Varianza: σ² = λ (media y varianza coinciden — rasgo distintivo de Poisson, útil para verificar si
el modelo es plausible con datos reales: si en un conteo la varianza muestral está muy lejos de la media muestral,
Poisson probablemente no es el modelo adecuado).

**Paso obligatorio antes de calcular**: λ está definido para una unidad de medio concreta (p.ej. "por hora"). Si el
enunciado pide la probabilidad en un intervalo distinto (p.ej. "en 25 minutos" cuando λ se dio "por hora"), **hay
que reescalar λ proporcionalmente al nuevo intervalo** antes de aplicar la fórmula:

λ_nuevo = λ_dado × (tamaño del intervalo nuevo / tamaño del intervalo del dato)

**Cálculo de acumuladas** (mismo cuidado con el extremo que en Binomial, ver [[distribucion-binomial]]):

P(X ≥ k) = 1 − P(X ≤ k−1) = 1 − Σ_{x=0}^{k-1} e^(-λ)λˣ/x!   — incluye x=k

P(X > k) = 1 − P(X ≤ k) = 1 − Σ_{x=0}^{k} e^(-λ)λˣ/x!   — excluye x=k

## Ejemplo resuelto

(Adaptado de wuolah-free-Solucion-Junio-2025-parte-2.pdf, ejercicio 2) Una empresa reporta en promedio 8 incidentes
menores cada 100 horas de revisión de maquinaria (Poisson).

**a) Probabilidad de un incidente en 25 horas**: reescalamos λ: λ₂₅ₕ = 25×8/100 = 2. X∼℘(2).

P(X=1) = e^(-2)·2¹/1! = 0.27067

**b) Probabilidad de como máximo 2 incidentes en 50 horas**: λ₅₀ₕ = 50×8/100 = 4. X∼℘(4).

P(X=0) = e^(-4)·4⁰/0! = 0.0183
P(X=1) = e^(-4)·4¹/1! = 0.0733
P(X=2) = e^(-4)·4²/2! = 0.1465

P(X≤2) = 0.0183+0.0733+0.1465 = 0.2381

## Conexión con otros conceptos

- [[distribucion-binomial]] — Poisson es su caso límite (n grande, p pequeño, np=λ); si un enunciado da n muy
  grande y p muy pequeño, ambos modelos dan resultados casi idénticos, pero Poisson es mucho más rápido de calcular.
- [[variable-aleatoria-discreta]] — Poisson hereda de ahí Fx(x), fx(x), media y varianza.

## Errores frecuentes de Marcos aquí

**Error activo (documentado en `memory/memory.json`, pre-2026-07-12), compartido con Binomial**: en P(X≥k) resta
solo P(X=k) en vez de todos los términos por debajo de k. Mismo remedio que en [[distribucion-binomial]]: escribir
explícitamente el complementario correcto antes de sustituir números.

**Patrón 3 (aplicar fórmula sin verificar condiciones)**: el paso de reescalar λ al intervalo de tiempo/espacio
pedido es exactamente "identificar el caso antes de abrir el formulario" — si Marcos usa directamente el λ del
enunciado sin comprobar que la unidad de tiempo/espacio coincide con la que pide la pregunta, el resultado es
erróneo aunque la fórmula esté bien aplicada. Pregunta siempre: "¿el λ que tengo es para el mismo intervalo que me
piden calcular?"

## Relevancia en examen

Alta. Aparece con regularidad junto a Binomial y Normal en la 2ª parte del examen, casi siempre con contexto de
control de calidad o microbiología alimentaria (microorganismos por volumen, defectos por lote) — ver
`examenes.md`.
