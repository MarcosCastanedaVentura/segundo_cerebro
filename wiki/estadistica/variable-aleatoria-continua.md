---
titulo: "Variable aleatoria continua: función de densidad y de distribución"
asignatura: "estadistica"
tema: "Tema 2.2 — Variable aleatoria"
tipo: "concepto"
relacionado: ["variable-aleatoria-discreta", "distribucion-normal-tipificacion", "cuartiles-boxplot"]
patrones_error: []
examen_relevancia: "alta"
fuente: ["VariableAleatoria_25_26-2.pdf", "Variable Aleatoria_J Ibañez.pdf (Tema 4)", "Examen_marzo_2025_solucion.pdf", "wuolah-free-Solucion-julio-2025.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una variable aleatoria es **continua** cuando su función de distribución Fx(x) es continua en todo ℝ (por la
derecha y por la izquierda), y su dominio de definición es la recta real o un intervalo — por ejemplo, tiempo de
espera, rendimiento de un cultivo (t/ha), peso de un lote de huevos. A diferencia de la discreta, aquí no tiene
sentido preguntar P(X=x) punto a punto: siempre vale 0 (el área bajo una curva sobre un único punto es nula).

## Por qué / de dónde viene

Como P(X=x)=0 para todo x, se necesita otra función que sí "informe" localmente: la **función de densidad** fx(x),
definida como fx(x) = dFx(x)/dx. No es una probabilidad (puede valer más de 1), sino una **verosimilitud**: indica
qué tan fácil es que la variable tome valores cerca de x, no la probabilidad de ese valor exacto. La probabilidad de
un intervalo se recupera integrando esa densidad (sumando infinitos rectángulos infinitesimales fx(x)·dx).

## Fórmula / procedimiento

**Función de densidad** fx(x), propiedades:
- fx(x) ≥ 0 para todo x
- fx(x) = 0 fuera del dominio Dx
- ∫₋∞^∞ fx(x) dx = 1 (el área total bajo la curva es 1 — primer paso casi siempre pedido en examen: hallar la
  constante k que hace esto cierto)

**Relación entre densidad y distribución**:

Fx(x) = P(X≤x) = ∫₋∞^x fx(t) dt        fx(x) = dFx(x)/dx

**Probabilidad de un intervalo**: P(a≤X≤b) = ∫ₐᵇ fx(x) dx = Fx(b) − Fx(a). Como P(X=a)=P(X=b)=0, da igual que el
intervalo sea abierto o cerrado en los extremos: P(a<X<b) = P(a≤X≤b) = P(a<X≤b) = P(a≤X<b) — **a diferencia de la
discreta**, donde sí importa el extremo (ver [[variable-aleatoria-discreta]]).

**Características** (mismas fórmulas que en discreta pero sustituyendo Σ por ∫):
- Esperanza: E[X] = ∫ x·fx(x) dx
- Varianza: σ² = ∫(x−μ)²·fx(x) dx = E[X²] − (E[X])² (teorema de König)
- Moda: el x que maximiza fx(x) (máximo de la curva de densidad, no de probabilidad)
- Mediana / cuantil xα: el valor que cumple Fx(xα) = α

## Ejemplo resuelto

(Adaptado de wuolah-free-Solucion-julio-2025.pdf, ejercicio 2) Densidad fx(x) = k(x+2) para 0≤x≤4, 0 en el resto.

**a) Hallar k**: ∫₀⁴ k(x+2) dx = k[x²/2+2x]₀⁴ = k(8+8) = 16k = 1 → k = 1/16.

**b) Función de distribución**: para 0≤x≤4, Fx(x) = ∫₀ˣ (1/16)(t+2) dt = (x²+4x)/32. Fx(x)=0 si x<0, Fx(x)=1 si x>4.

**c) Esperanza**: E[X] = ∫₀⁴ x·(1/16)(x+2) dx = (1/16)[x³/3+x²]₀⁴ = (1/16)(64/3+16) = 112/48 ≈ 2.33.

**d) P(2≤X≤3)** = Fx(3)−Fx(2) = (9+12)/32 − (4+8)/32 = 21/32 − 12/32 = 9/32 ≈ 0.281.

## Conexión con otros conceptos

- [[variable-aleatoria-discreta]] — misma estructura conceptual (Fx, media, varianza, cuantil), cambiando suma por
  integral; el punto de contraste clave es que aquí P(X=x)=0 siempre.
- [[distribucion-normal-tipificacion]] — la Normal es la variable aleatoria continua de uso más frecuente; su
  cálculo de probabilidades reutiliza exactamente Fx(x)=P(X≤x) pero con tablas en vez de integración directa.
- [[cuartiles-boxplot]] — el concepto de cuantil xα (α=Fx(xα)) es el mismo, sólo cambia si F es empírica (datos) o
  teórica (modelo de probabilidad).

## Errores frecuentes de Marcos aquí

Ninguno activo documentado específicamente aquí. Punto de vigilancia general (Patrón 7, validar sin verificar):
comprobar siempre que ∫fx(x)dx=1 en el dominio dado antes de seguir calculando — si la constante k sale mal, todo
el resto del ejercicio arrastra el error. También comprobar signo y límites de integración al hallar Fx(x) por
tramos: es fácil "perder" un tramo cuando el dominio no empieza en 0 (Patrón 6, transcripción/montaje de la
integral).

## Relevancia en examen

Alta. Aparece en casi todos los exámenes como ejercicio propio de "variable aleatoria continua": hallar k, obtener
Fx(x), calcular E[X], una probabilidad de intervalo y a veces la mediana (ver Examen_marzo_2025_solucion,
wuolah-free-Solucion-julio-2025, ambos con estructura idéntica de 4-5 apartados encadenados).
