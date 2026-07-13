---
titulo: "Distribución de Bernoulli y Binomial"
asignatura: "estadistica"
tema: "Tema 2.3 — Distribuciones de probabilidad de uso frecuente"
tipo: "concepto"
relacionado: ["variable-aleatoria-discreta", "probabilidad-propiedades", "distribucion-poisson"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Tema2.3_DistribProbFrec25-26-2.pdf", "DISTRIBUCIONES DE PROBABILIDAD DE USO FRECUENTE.pdf (Tema 5 Ibáñez)", "wuolah-free-Solucion-julio-2025.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un **experimento de Bernoulli** es aquel con solo dos resultados posibles: A (éxito) o Ā (fracaso), con P(A)=p. La
**variable de Bernoulli** X∼β(p) vale 1 si ocurre A y 0 si ocurre Ā en un único experimento. La **variable binomial**
X∼B(n,p) generaliza esto a n repeticiones **independientes** del mismo experimento de Bernoulli: X cuenta cuántas
veces se obtiene A en total (el número de éxitos), Dx={0,1,...,n}.

## Por qué / de dónde viene

Que las repeticiones sean independientes es lo que garantiza que p se mantenga constante en cada una (por eso el
muestreo "con reemplazamiento" es el caso típico de aplicación — ver ejemplo de las vacas en
[[probabilidad-propiedades]]). La probabilidad de obtener **una** secuencia concreta con x éxitos y n−x fracasos es
pˣq^(n-x) (regla del producto por independencia). Pero como el orden interno no importa (X solo cuenta el total de
éxitos), hay que multiplicar por el número de secuencias distintas posibles con x éxitos: n!/(x!(n−x)!) —
combinaciones, no permutaciones simples, porque los x éxitos son indistinguibles entre sí.

## Fórmula / procedimiento

**Bernoulli** X∼β(p): fx(x,p) = pˣq^(1-x) para x∈{0,1}. Media: m=p. Varianza: σ²=pq.

**Binomial** X∼B(n,p): fx(x,n,p) = [n!/(x!(n−x)!)]·pˣ·q^(n-x) para x∈{0,1,...,n}, con q=1−p.

Media: m = np.   Varianza: σ² = npq.

**Condiciones que hay que verificar antes de aplicar la fórmula (clasificar el caso, Patrón 3)**:
1. Solo dos resultados posibles por ensayo (éxito/fracaso).
2. p constante en todos los ensayos (con reemplazamiento, o población "infinita"/muy grande respecto a la muestra).
3. Ensayos independientes entre sí.

Si el muestreo es **sin reemplazamiento** de una población finita pequeña, no es Binomial — sería hipergeométrica
(p cambia en cada extracción). Antes de escribir n, p, verifica explícitamente estas 3 condiciones.

**Cálculo de probabilidades acumuladas** (aquí es donde se activa el error de incluir/excluir el extremo, ver
[[variable-aleatoria-discreta]]):

- P(X ≥ k) = 1 − P(X ≤ k−1) = 1 − Σ_{x=0}^{k-1} fx(x) — **incluye** x=k
- P(X > k) = 1 − P(X ≤ k) = 1 − Σ_{x=0}^{k} fx(x) — **excluye** x=k

## Ejemplo resuelto

(Adaptado de wuolah-free-Solucion-julio-2025.pdf, ejercicio 3c) Se clasifican como "XL" el 10% de huevos más
pesados de una granja: p=0.10. Se recogen 12 huevos al azar, Y≡número de huevos XL, Y∼B(12, 0.10). Se pide
P(Y≥2):

P(Y≥2) = 1 − P(Y=0) − P(Y=1)

P(Y=0) = [12!/(0!12!)]·0.10⁰·0.90¹² = 0.2824
P(Y=1) = [12!/(1!11!)]·0.10¹·0.90¹¹ = 0.3765

P(Y≥2) = 1 − 0.2824 − 0.3765 = 0.3411

Nótese que para calcular P(Y≥2) hay que restar P(Y=0) **y** P(Y=1) (los dos valores estrictamente menores que 2),
no P(Y=2): el 2 sí está incluido en el suceso pedido.

## Conexión con otros conceptos

- [[variable-aleatoria-discreta]] — Binomial es un caso concreto de variable aleatoria discreta; hereda toda su
  maquinaria de Fx(x), fx(x), media y varianza.
- [[probabilidad-propiedades]] — la deducción de la fórmula usa directamente independencia y regla del producto.
- [[distribucion-poisson]] — la Poisson es el límite de la Binomial cuando n→∞, p→0 y np=λ constante (sucesos
  raros); útil para decidir cuál usar cuando n es muy grande y p muy pequeño.

## Errores frecuentes de Marcos aquí

**Error activo (documentado en `memory/memory.json`, pre-2026-07-12)**: en P(X≥k), Marcos resta solo P(X=k) en vez
de sumar/restar todos los términos estrictamente por debajo de k. La causa raíz es no distinguir "mayor o igual"
(incluye el propio k) de "estrictamente mayor" (lo excluye). **Antes de escribir la resta, verbaliza en voz alta
qué valores concretos de Dx quedan fuera del suceso pedido** y compleméntalos explícitamente, no de memoria.

**Patrón 3 (aplicar fórmula sin verificar condiciones)**: comprobar siempre "¿hay reemplazo/población grande
(→Binomial) o extracción sin reemplazo de una población pequeña (→hipergeométrica, fuera de este curso pero hay que
saber que Binomial no aplicaría tal cual)?" antes de identificar n y p.

## Relevancia en examen

Alta. Aparece en casi todos los exámenes, normalmente encadenado tras un ejercicio de Normal (clasificar un
resultado con probabilidad p y luego preguntar por el número de "éxitos" en varias repeticiones — ver
wuolah-free-Solucion-julio-2025.pdf ejercicio 3, Solucion-Junio-2025 problema 3.1 tipo Bayes+Binomial).
