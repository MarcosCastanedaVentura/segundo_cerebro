---
titulo: "Impuesto específico, incidencia fiscal y pérdida irrecuperable de eficiencia"
asignatura: "economia"
tema: "Tema 3 — Mercados: regulación"
tipo: "concepto"
relacionado: ["equilibrio-mercado", "excedente-consumidor-productor", "elasticidad-precio-demanda"]
patrones_error: [3]
examen_relevancia: "alta"
fuente: ["Diapositivas Tema 3.pdf", "Diapositivas Tema 4.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un **impuesto indirecto específico** es una cantidad fija de dinero (T €/unidad) que el Estado cobra por cada unidad
vendida de un bien (a diferencia del *ad valorem*, que es un % del precio). Introduce una **brecha (cuña fiscal)**
entre el precio que paga el consumidor (P_C) y el precio que recibe el productor (P_P): `P_C − P_P = T`.

## Por qué / de dónde viene

Da igual si el impuesto se cobra "al vendedor" o "al comprador" en la ley: el mercado reacciona igual, desplazando la
curva de oferta (si se cobra al vendedor) o la de demanda (si se cobra al comprador) verticalmente en la cuantía T.
El resultado final —precios y cantidad de equilibrio— es el mismo en ambos casos. Un impuesto reduce la cantidad de
equilibrio transactada (de Q_E a Q_T < Q_E), porque encarece la transacción para al menos una de las partes, y por
tanto algunas operaciones mutuamente beneficiosas dejan de realizarse.

## Fórmula / procedimiento

1. El impuesto desplaza la curva de oferta hacia arriba en T (o la de demanda hacia abajo en T): en el nuevo
   equilibrio, `P_C = P_P + T`.
2. **Recaudación del impuesto** = `T × Q_T` (rectángulo entre P_C y P_P, con base Q_T).
3. **Incidencia (reparto de la carga entre consumidor y productor)** depende de las **elasticidades relativas**:
   - Si la demanda es **más inelástica** que la oferta → el consumidor soporta la mayor parte de la carga (el precio
     al consumidor sube casi todo el impuesto).
   - Si la oferta es **más inelástica** que la demanda → el productor soporta la mayor parte (el lado inelástico es
     el que "no puede escapar" ajustando cantidad, así que absorbe más del impuesto).
   - Regla mnemotécnica: **"el lado más rígido (inelástico) paga más"**.
4. **Pérdida irrecuperable de eficiencia (o exceso de gravamen)**: triángulo entre Q_T y Q_E, delimitado por las
   curvas de oferta y demanda. Representa las ganancias del comercio que ya no se producen porque esas unidades
   (entre Q_T y Q_E) ya no se compran/venden. Cuanto **más elásticas** sean oferta y/o demanda, mayor es esta
   pérdida (más transacciones se abandonan ante el mismo impuesto).

## Ejemplo resuelto

(Adaptado de Diapositivas Tema 3, mercado de taxis) Sin impuesto: equilibrio en P=5€, Q=10 millones de viajes/año.
Se introduce un impuesto específico de 2€/viaje.

- Nueva oferta desplazada 2€ hacia arriba → nuevo equilibrio con `P_C = 6€` (lo que paga el pasajero) y
  `P_P = 4€` (lo que recibe el taxista), y `Q_T = 8` millones de viajes (comprobando: `P_C − P_P = 6 − 4 = 2€ = T`
  ✓).
- Recaudación = `2€ × 8 millones = 16 millones €`.
- Como en este ejemplo el precio subió 1€ (de 5 a 6) y bajó 1€ (de 5 a 4), la carga se reparte a partes iguales:
  elasticidades de oferta y demanda similares en ese punto.
- En el ejemplo de la gasolina (demanda muy inelástica, oferta casi plana): un impuesto de 1€ hace subir el precio
  al consumidor de 2,00€ a 2,95€ (el consumidor asume 0,95€ de los 1€) y el productor solo pierde 0,05€ — la
  demanda inelástica absorbe casi todo el impuesto.

## Conexión con otros conceptos

- [[equilibrio-mercado]]: el impuesto crea un nuevo equilibrio con menor cantidad.
- [[excedente-consumidor-productor]]: el impuesto reduce el excedente del consumidor y del productor; parte de esa
  pérdida se convierte en recaudación fiscal (transferencia al Estado) y otra parte es pérdida irrecuperable pura
  (no la recibe nadie).
- [[elasticidad-precio-demanda]]: determina el reparto de la incidencia y el tamaño de la pérdida de eficiencia.

## Errores frecuentes de Marcos aquí

Riesgo del **Patrón 3** (aplicar fórmulas sin verificar el caso): confundir "quién paga legalmente el impuesto" (el
que lo ingresa en Hacienda) con "quién soporta la carga económica" (que depende solo de elasticidades, no de quién
firma el papel). También, al dibujar el desplazamiento, olvidar que la distancia vertical entre las dos curvas de
oferta (antigua y nueva) debe ser exactamente T en todo punto, no solo en el de equilibrio.

## Relevancia en examen

Alta. Ejercicio 3.2 de Diapositivas Tema 3 (mercado de cerveza con impuesto de 0,6 um/ud, preguntando efectos y quién
soporta más carga) es representativo del tipo de pregunta típica: dadas funciones de oferta y demanda y un impuesto
T, calcular P_C, P_P, Q_T, recaudación y razonar la incidencia según elasticidades.
