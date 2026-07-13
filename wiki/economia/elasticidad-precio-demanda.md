---
titulo: "Elasticidad precio de la demanda (y otras elasticidades)"
asignatura: "economia"
tema: "Tema 2 — Mercados: demanda y oferta"
tipo: "formula"
relacionado: ["equilibrio-mercado", "impuesto-especifico-incidencia"]
patrones_error: [4]
examen_relevancia: "alta"
fuente: ["Diapositivas Tema 2.pdf", "EcoProblemas_02_con_solucion.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La **elasticidad** mide cuánto responde una variable (en %) ante un cambio del 1% en otra variable, manteniendo todo
lo demás constante (*ceteris paribus*). La **elasticidad precio de la demanda** mide cuánto varía porcentualmente la
cantidad demandada de un bien cuando su precio varía un 1%.

## Por qué / de dónde viene

Saber que "si sube el precio baja la cantidad demandada" (ley de la demanda) no basta para tomar decisiones: hace
falta saber **cuánto** baja. Una empresa que sube precios necesita saber si perderá pocas o muchas ventas para decidir
si le conviene. La elasticidad convierte esa sensibilidad en un número comparable entre bienes distintos, porque es
**adimensional** (no depende de las unidades de medida de precio o cantidad).

## Fórmula / procedimiento

**Elasticidad precio de la demanda (método del punto medio/inicial, entre dos puntos):**

```
E_D = [ (Q₂ − Q₁)/Q₁ × 100 ] / [ (P₂ − P₁)/P₁ × 100 ]
```

**En un punto** (si Q = f(P) es derivable): `E_D = (P/Q) · (∂Q/∂P)`

- El signo de E_D en un bien normal es **negativo** (P y Q se mueven en sentido contrario), pero por convención se
  suele dar **en valor absoluto**.
- Interpretación (en valor absoluto):
  - `|E_D| > 1` → demanda **elástica** (la cantidad reacciona más que proporcionalmente al precio).
  - `|E_D| < 1` → demanda **inelástica** (reacciona menos que proporcionalmente).
  - `|E_D| = 1` → **elasticidad unitaria**.
  - `|E_D| = 0` → **perfectamente inelástica** (recta vertical, la cantidad no cambia nunca).
  - `|E_D| = ∞` → **perfectamente elástica** (recta horizontal).
- Factores que la determinan: existencia de sustitutivos cercanos, si es bien de primera necesidad o de lujo, el
  horizonte temporal (a más plazo, más elástica: hay tiempo para adaptarse).

**Relación con el ingreso total** (I = P × Q):
- Demanda **elástica**: subir el precio **reduce** el ingreso total (el efecto cantidad domina).
- Demanda **inelástica**: subir el precio **aumenta** el ingreso total (el efecto precio domina).
- Elasticidad **unitaria**: el ingreso total no cambia.

**Otras elasticidades relacionadas** (misma lógica, "% cambio en cantidad demandada de i" en el numerador):
- **Elasticidad precio cruzada** `E_ij = (%ΔQ_i)/(%ΔP_j)`: si `E_ij > 0` → bienes **sustitutivos**; si `E_ij < 0` →
  bienes **complementarios**.
- **Elasticidad renta** `E_iM = (%ΔQ_i)/(%ΔM)`: si `E_iM > 0` → bien **normal** (de lujo si >1, necesario si <1); si
  `E_iM < 0` → bien **inferior**.
- **Elasticidad precio de la oferta**: misma fórmula pero con cantidad ofertada; determinada sobre todo por la
  disponibilidad de factores de producción y el tiempo.

## Ejemplo resuelto

(Adaptado de EcoProblemas_02, Problema 2) Mercado de helados: demanda `Q = 30 − P`, oferta `Q = 20 + 4P`.

1. Equilibrio: `30 − P = 20 + 4P → 10 = 5P → P = 2`; `Q = 30 − 2 = 28`.
2. Elasticidad precio de la demanda en el punto (P=2, Q=28), usando la derivada: `∂Q/∂P = −1` (pendiente de la
   demanda). `E_D = (P/Q)·(∂Q/∂P) = (2/28)·(−1) = −0,07` → en valor absoluto, **0,07**: demanda muy inelástica.
3. Elasticidad precio de la oferta: `∂Q/∂P = 4`. `E_S = (2/28)·4 = 0,28`: oferta también inelástica (aunque más
   elástica que la demanda).

## Conexión con otros conceptos

- [[equilibrio-mercado]]: la elasticidad se calcula típicamente en el punto de equilibrio.
- [[impuesto-especifico-incidencia]]: la elasticidad relativa de oferta y demanda determina quién soporta la mayor
  parte de la carga de un impuesto, y el tamaño de la pérdida irrecuperable de eficiencia.

## Errores frecuentes de Marcos aquí

Riesgo del **Patrón 4** (confundir cocientes relacionados): mezclar `%ΔQ/%ΔP` con `%ΔP/%ΔQ` (invertir numerador y
denominador), o usar la pendiente de la recta directamente como si fuera la elasticidad (la pendiente es constante a
lo largo de una recta de demanda lineal, pero **la elasticidad no** — cambia en cada punto porque depende del
cociente P/Q en ese punto, no solo de la pendiente). Verificar siempre qué variable es "la que cambia" (numerador) y
cuál es "la causa" (denominador) antes de sustituir.

## Relevancia en examen

Alta. Aparece en casi todas las hojas de problemas (EcoProblemas_02) y en exámenes/PEP como cálculo directo a partir
de funciones de oferta/demanda, y como pregunta conceptual (interpretar si un bien es elástico/inelástico y su efecto
sobre el ingreso total).
