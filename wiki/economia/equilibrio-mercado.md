---
titulo: "Equilibrio de mercado, escasez y excedente de producto"
asignatura: "economia"
tema: "Tema 2 — Mercados: demanda y oferta"
tipo: "concepto"
relacionado: ["elasticidad-precio-demanda", "excedente-consumidor-productor", "impuesto-especifico-incidencia"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Diapositivas Tema 2.pdf", "Diapositivas Tema 3.pdf", "EcoProblemas_02_con_solucion.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El **equilibrio de mercado** es el punto (P*, Q*) en el que la curva de oferta y la curva de demanda se cortan: la
cantidad que los compradores quieren comprar a ese precio coincide exactamente con la que los vendedores quieren
vender. P* se llama **precio de equilibrio** (o "precio de vaciado del mercado") y Q* **cantidad de equilibrio**.

## Por qué / de dónde viene

La curva de demanda es decreciente (ley de la demanda: a mayor precio, menor cantidad demandada) y la de oferta es
creciente (ley de la oferta: a mayor precio, mayor cantidad ofertada). Solo hay un precio en el que ambos planes
coinciden; a cualquier otro precio, uno de los dos lados del mercado se queda con un plan que no puede cumplir, lo
que genera presión para que el precio se mueva hacia el equilibrio:

- **Precio por encima del de equilibrio** → la cantidad ofertada supera a la demandada → **excedente (exceso de
  oferta)** → los vendedores no consiguen vender todo, bajan el precio.
- **Precio por debajo del de equilibrio** → la cantidad demandada supera a la ofertada → **escasez (exceso de
  demanda)** → los compradores compiten por el bien escaso, empujan el precio al alza.

Este ajuste hace que el mercado **tienda al equilibrio** por sí solo, sin que nadie lo planifique.

## Fórmula / procedimiento

1. Igualar `Q_demandada(P) = Q_ofertada(P)` y despejar P* (precio de equilibrio).
2. Sustituir P* en cualquiera de las dos funciones para obtener Q*.
3. Para analizar un **desplazamiento de curva** (cambio en gustos, renta, precios de bienes relacionados, número de
   productores, costes de los factores, tecnología, expectativas — ver [[frontera-posibilidades-produccion]] para la
   distinción movimiento-a-lo-largo vs desplazamiento): dibujar la curva nueva y encontrar el nuevo corte.
   - Aumento de demanda (D se desplaza a la derecha) → sube P* y sube Q*.
   - Aumento de oferta (O se desplaza a la derecha) → baja P* y sube Q*.
   - Si ambas se desplazan a la vez, el efecto sobre P* o Q* depende de cuál desplazamiento es mayor (ver combinación
     de "gran incremento en demanda + pequeña disminución de oferta" en las diapositivas).
4. Para un **control de precios**:
   - **Precio máximo** por debajo del de equilibrio → genera **escasez**.
   - **Precio mínimo** por encima del de equilibrio → genera **excedente**.
   - Un control de precios que no cruza el equilibrio (ej. precio máximo por encima del de equilibrio) no tiene
     ningún efecto real.

## Ejemplo resuelto

(Adaptado de EcoProblemas_02, Problema 3) Mercado de cacao: demanda de mercado `Q_D = 1000 × (20 − 0,01P) = 20000 −
10P`; oferta de mercado `Q_S = 100 × (0,3P) = 30P`.

- Equilibrio: `20000 − 10P = 30P → 20000 = 40P → P* = 500`; `Q* = 30(500) = 15.000`.
- Si la demanda sube a `Q_D = 25.000 − 10P` (más renta): nuevo equilibrio `25000 − 10P = 30P → P* = 625`,
  `Q* = 18.750`. Sube el precio y sube la cantidad, coherente con un desplazamiento de la demanda hacia la derecha.

## Conexión con otros conceptos

- [[elasticidad-precio-demanda]]: se calcula habitualmente en el punto de equilibrio.
- [[excedente-consumidor-productor]]: el excedente total (bienestar) se maximiza precisamente en el equilibrio de
  mercado.
- [[impuesto-especifico-incidencia]]: un impuesto desplaza la curva de oferta (o demanda) y crea un nuevo equilibrio
  con menor cantidad transactada.

## Errores frecuentes de Marcos aquí

Riesgo del **Patrón 3** (aplicar fórmulas sin verificar el caso): antes de igualar oferta y demanda hay que
comprobar que ambas están expresadas como **funciones de mercado** (sumando las funciones individuales × número de
consumidores/productores) y no como funciones individuales sueltas — mezclar ambas da un equilibrio incorrecto. Otro
riesgo es confundir "excedente" (exceso de oferta) con "excedente del consumidor/productor" (ganancia de bienestar,
ver [[excedente-consumidor-productor]]): son conceptos distintos con el mismo nombre.

## Relevancia en examen

Alta. Es la base de casi todos los problemas de microeconomía del examen: hallar equilibrio a partir de funciones de
oferta/demanda, analizar desplazamientos de curvas, y calcular efectos de precios máximos/mínimos (control de
precios, Tema 3 de las diapositivas: mercado de alquileres con precio máximo, mercado de mantequilla con precio
mínimo).
