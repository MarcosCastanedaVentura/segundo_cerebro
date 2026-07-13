---
titulo: "EDOs lineales de primer orden y factor integrante (problemas de mezclas)"
asignatura: "ecuaciones-diferenciales"
tema: "Tema 1 - Ecuaciones diferenciales de primer orden"
tipo: "procedimiento"
relacionado: ["edo-conceptos-generales", "edo-separables", "edo-exactas"]
patrones_error: [3, 6]
examen_relevancia: "alta"
fuente: ["Apuntes de ecuaciones diferenciales.pdf (secc. 1.6)", "FINAL 2_JULIO_2025 - soluciones.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Una EDO lineal de primer orden tiene la forma `dy/dx + P(x)y = Q(x)`: la incógnita `y` y su
derivada aparecen solo elevadas a la primera potencia (no hay `y²`, `y·y'`, `sen(y)`, etc.). Se
resuelve multiplicando toda la ecuación por un **factor integrante** `ρ(x) = e^(∫P(x)dx)` que
convierte el lado izquierdo en la derivada de un producto.

## Por qué / de dónde viene

El truco funciona porque si multiplicamos por `ρ(x) = e^(∫P dx)`, se cumple
`d/dx[ρ(x)·y] = ρ(x)·y' + ρ(x)·P(x)·y`, que es exactamente el lado izquierdo de la ecuación ya
multiplicada. Es decir, `ρ(x)` está construido a propósito para que la regla del producto
"deshaga" la suma `y' + P(x)y` en una sola derivada, dejando una ecuación directamente
integrable. Este método aparece constantemente en problemas de mezclas (tanques con entrada y
salida de soluto) porque el balance de materia de un tanque agitado siempre da una ecuación
lineal de primer orden en la cantidad de soluto.

## Fórmula / procedimiento

1. Escribir la ecuación en la forma estándar `y' + P(x)y = Q(x)` (dividir si hace falta).
2. Calcular el factor integrante `ρ(x) = e^(∫P(x)dx)` (sin constante de integración aquí).
3. Multiplicar toda la ecuación por `ρ(x)`; el lado izquierdo es `d/dx[ρ(x)·y]`.
4. Integrar ambos lados: `ρ(x)·y = ∫ρ(x)Q(x)dx + C`.
5. Despejar `y(x)` y aplicar la condición inicial si la hay.

**Problemas de mezclas.** Si un tanque tiene entrada a caudal `ri` con concentración `ci` y
salida a caudal `r0`, la cantidad de soluto `x(t)` cumple:
`dx/dt = ri·ci − r0·(x/V(t))`, con `V(t) = V0 + (ri−r0)t`. Reordenando queda lineal de primer
orden en `x(t)` con `P(t) = r0/V(t)` y `Q(t) = ri·ci`.

## Ejemplo resuelto

*Adaptado de FINAL 2_JULIO_2025 - soluciones.pdf, ejercicio 2.* Un tanque de 1000 L contiene
inicialmente 500 L de leche con 250 g de azúcar disuelto. Entra leche azucarada a 1 g/L a razón
de 3 L/min, y sale mezcla homogénea a 2 L/min. ¿Cuánta azúcar hay cuando el tanque está lleno?

`V(t) = 500 + (3−2)t = 500 + t`. Balance: `dx/dt = 3·1 − 2·x/(500+t)` →

```
dx/dt + 2/(500+t)·x = 3
```

Factor integrante: `ρ(t) = e^(∫2/(500+t)dt) = (500+t)²`. Multiplicando e integrando:
`x·(500+t)² = ∫3(500+t)²dt = (500+t)³ + C` → `x(t) = (500+t) + C/(500+t)²`.

Con `x(0) = 250`: `250 = 500 + C/500²` → `C = −250·500² = −6.25×10⁷`.

El tanque se llena cuando `V = 1000`, es decir `t = 500` min. Sustituyendo:
`x(500) = 1000 − 6.25×10⁷/1000² = 1000 − 62.5 = 937.5 g` de azúcar.

## Conexión con otros conceptos

- [[edo-separables]] y [[edo-exactas]] — clasificar correctamente antes de elegir el método: una
  misma ecuación a veces admite dos vías (separable **y** lineal), pero solo una suele ser
  practicable según cómo esté escrita.
- Es la base directa de los balances de materia dinámicos en Operaciones Unitarias I/II
  (tanques agitados, disolución de sólidos, dilución continua) — el mismo esquema de
  "entra-sale-se acumula" reaparece allí con el nombre de balance de masa no estacionario.

## Errores frecuentes de Marcos aquí

- **Patrón 3** (aplicar fórmula sin verificar condiciones): antes de calcular el factor
  integrante hay que comprobar que la ecuación es realmente lineal (¿aparece `y²` o `y·y'`
  escondido tras reordenar?) — si no lo es, el factor integrante no sirve.
- **Patrón 6** (copiar mal datos): en problemas de mezclas es fácil intercambiar `ri` con `r0`, o
  la concentración de entrada `ci` con la concentración inicial del tanque. Escribe explícitamente
  las cuatro cantidades (`V0`, `ri`, `ci`, `r0`) antes de montar la ecuación.

## Relevancia en examen

**Alta.** Los problemas de mezclas (tanques de sal, azúcar, alcohol, salmuera) aparecen en casi
todos los primeros parciales y en varios finales: 1parcial18_19, 20251030_EcuaDif_Solución
(cuba de cerveza con alcohol), FINAL 2_JULIO_2025 (tanque de azúcar), PROBLEMAS_TEMA1_COMPLEMENTARIOS
(tanque de sal). Suelen valer 2-3 puntos y casi siempre piden: plantear el PVI, resolver la
ecuación lineal completa, y evaluar en un instante concreto (normalmente cuando el tanque se
llena o vacía).
