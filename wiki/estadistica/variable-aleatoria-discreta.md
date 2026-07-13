---
titulo: "Variable aleatoria discreta: función de cuantía y de distribución"
asignatura: "estadistica"
tema: "Tema 2.2 — Variable aleatoria"
tipo: "concepto"
relacionado: ["probabilidad-propiedades", "variable-aleatoria-continua", "distribucion-binomial", "distribucion-poisson", "estadistica-descriptiva-una-variable"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["VariableAleatoria_25_26-2.pdf", "Variable Aleatoria_J Ibañez.pdf (Tema 4)"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una **variable aleatoria (V.A.)** X es una función que asocia un número real a cada suceso elemental del espacio
muestral E de un experimento aleatorio: X: E → ℝ. Es discreta cuando su dominio de definición Dx = {x₁, x₂, ..., xᵢ,
...} es un conjunto de valores aislables y ordenados (finito o infinito numerable) — por ejemplo, número de caras al
lanzar dos monedas, número de heladas en mayo, número de artículos defectuosos en una muestra de 20.

## Por qué / de dónde viene

Muchos espacios muestrales no son numéricos de partida (caras/cruces, sano/enfermo). La variable aleatoria traduce
cualquier suceso a un subconjunto de ℝ (X≤x, x₁<X≤x₂, X>x), lo que permite razonar con desigualdades y funciones en
vez de con conjuntos abstractos, reutilizando todo el aparato de probabilidad ya visto en [[probabilidad-propiedades]].

## Fórmula / procedimiento

**Función de distribución** (sirve para discreta y continua): Fx(x) = P(X≤x), para todo x∈ℝ. Propiedades: Fx(-∞)=0,
Fx(∞)=1, no decreciente, acotada en [0,1], continua por la derecha.

**Función de probabilidad discreta (función de cuantía)**: fx(x) = P(X=x), para todo x∈ℝ. Cumple fx(xᵢ)≥0 y
Σᵢ fx(xᵢ) = 1 (probabilidad del suceso seguro). Fx(x) es una función **en escalera**: en cada xᵢ∈Dx da un salto
ascendente de magnitud exactamente fx(xᵢ):

Fx(xᵢ) − Fx(xᵢ₋₁) = P(X=xᵢ) = fx(xᵢ)

**Cálculo de probabilidades de sucesos** a partir de fx(x): la probabilidad de cualquier suceso es la suma de
fx(xᵢ) para los xᵢ∈Dx contenidos en ese suceso. Ojo con los extremos del intervalo — es aquí donde se decide si un
valor xᵢ concreto entra o no en la suma (ver "Errores frecuentes" más abajo):

- P(a < X ≤ b) = Σ fx(xᵢ) para a<xᵢ≤b
- P(X ≥ k) = Σ fx(xᵢ) para xᵢ≥k — **incluye** fx(k)
- P(X > k) = Σ fx(xᵢ) para xᵢ>k — **excluye** fx(k)

**Características** (mismo aparato que en descriptiva, pero con probabilidades en vez de frecuencias — ver
[[estadistica-descriptiva-una-variable]]):

- Media / esperanza: μ = E[X] = Σᵢ xᵢ·P(X=xᵢ)
- Varianza: σ² = E[(X−μ)²] = Σᵢ(xᵢ−μ)²·P(X=xᵢ) = E[X²] − (E[X])² (teorema de König, igual que en descriptiva)
- Desviación típica: σ = √σ²
- Moda: xᵢ∈Dx con mayor P(X=xᵢ)
- Cuantil xα: el valor que verifica α=Fx(xα); si Fx(xᵢ₋₁)<α<Fx(xᵢ) entonces xα=xᵢ; si α=Fx(xᵢ₋₁) entonces
  xα=(xᵢ₋₁+xᵢ)/2 (mismo criterio de [[cuartiles-boxplot]] pero con probabilidad teórica en vez de frecuencia empírica).

## Ejemplo resuelto

(Adaptado de Variable Aleatoria_J Ibañez.pdf, problema 4.2) X con Dx={1,2,3,4,5,6} y fx(x)=1/6 (lanzamiento de un
dado).

P(3 < X ≤ 5) = fx(4)+fx(5) = 1/6+1/6 = 1/3. P(X > 4) = fx(5)+fx(6) = 1/3. P(X ≤ 3) = fx(1)+fx(2)+fx(3) = 1/2.

Media: m = E[X] = (1+2+3+4+5+6)/6 = 3.5. E[X²] = (1+4+9+16+25+36)/6 = 15.17. Varianza: σ² = 15.17 − 3.5² = 2.92.

Primer cuartil: x₀.₂₅ = 2 (comprobando con Fx: Fx(1)=1/6, Fx(2)=1/3 — como 0.25 cae estrictamente entre Fx(1) y
Fx(2), x₀.₂₅=2). Mediana: x₀.₅=(3+4)/2=3.5 (0.5 coincide exactamente con Fx(3)=1/2, así que se promedia con el
siguiente valor).

## Conexión con otros conceptos

- [[probabilidad-propiedades]] — fx(x) hereda los 3 axiomas de probabilidad (no negatividad, suceso seguro,
  aditividad de sucesos incompatibles).
- [[variable-aleatoria-continua]] — la contrapartida continua sustituye la suma por una integral y fx(x) deja de
  ser una probabilidad para ser una densidad.
- [[distribucion-binomial]] y [[distribucion-poisson]] — son variables aleatorias discretas concretas, con una
  fx(x, parámetros) específica.
- [[estadistica-descriptiva-una-variable]] — mismo aparato de media/varianza/cuantil, pero aquí las probabilidades
  sustituyen a las frecuencias relativas observadas.

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmula sin verificar condiciones de uso), variante activa en binomial/Poisson**: al calcular
P(X≥k), Marcos tiende a restar P(X=k) en vez de incluirla, confundiéndolo con P(X>k). Antes de escribir la suma o el
complementario, verbaliza explícitamente si el límite k está incluido o excluido:
P(X≥k) = 1−P(X≤k−1) = 1−P(X<k) (incluye k), mientras que P(X>k) = 1−P(X≤k) (excluye k). Ver también
[[distribucion-binomial]] y [[distribucion-poisson]], donde este error está documentado con fecha en
`memory/memory.json`.

## Relevancia en examen

Alta — es la base teórica de todo ejercicio de variable aleatoria discreta, y reaparece encapsulada dentro de
prácticamente todos los ejercicios de Binomial y Poisson del examen (ver `examenes.md`).
