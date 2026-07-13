---
titulo: "Degradación de ácidos grasos: activación, transporte por carnitina y β-oxidación"
asignatura: "bioquimica"
tema: "Tema 6 - Metabolismo de lípidos"
tipo: "procedimiento"
relacionado: ["biosintesis-acidos-grasos", "cuerpos-cetonicos", "ciclo-krebs", "biomoleculas-glucidos-lipidos", "inhibicion-enzimatica"]
patrones_error: [3, 5]
examen_relevancia: "alta"
fuente: ["Tema 6.pdf", "examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La β-oxidación es la ruta de degradación de los ácidos grasos hasta acetil-CoA, ocurre en la matriz
mitocondrial (también en peroxisomas para ácidos grasos muy largos, y en glioxisomas en plantas), y es la
ruta central del metabolismo energético en animales, protistas y algunas bacterias. Antes de poder oxidarse,
el ácido graso citosólico debe activarse y ser transportado a la matriz mitocondrial en 3 pasos que
constituyen, junto con las 4 reacciones cíclicas de la β-oxidación en sí, el bloque de examen más repetido de
este tema.

## Por qué / de dónde viene

Los ácidos grasos libres no pueden atravesar las membranas mitocondriales directamente. La célula resuelve
esto con un sistema de "relevo" en 3 pasos obligatorios en ese orden (Patrón 5: el orden es estricto, no
intuitivo): (1) activación en la membrana mitocondrial externa formando acil-CoA (gasto de 2 ATP
equivalentes, vía ruptura pirofosfatolítica), (2) transferencia del grupo acilo del CoA a la carnitina para
cruzar la membrana mitocondrial interna (paso limitante de toda la ruta), y (3) transferencia de vuelta al
CoA ya en la matriz mitocondrial. Este relevo mantiene además dos depósitos separados de CoA: uno en la
matriz (para catabolismo) y otro en el citosol (para biosíntesis, ver [[biosintesis-acidos-grasos]]) — la
separación física es la base de por qué degradación y síntesis de ácidos grasos no pueden ocurrir a la vez en
el mismo compartimento.

## Fórmula / procedimiento

**Movilización del ácido graso a la matriz mitocondrial (orden obligatorio):**
1. Activación (membrana mitocondrial externa): Ácido graso + CoA-SH + ATP → Acil-CoA + AMP + PPi
   (acil-CoA sintetasa). Coste ≈ 2 ATP (por la ruptura pirofosfatolítica, ver [[atp-compuestos-alta-energia]]).
2. Transferencia a la carnitina (cara citosólica de la membrana mitocondrial interna): Acil-CoA + carnitina →
   Acil-carnitina + CoA-SH (carnitina-acil-transferasa I, **CAT-I**, inhibida por malonil-CoA — así se evita
   que β-oxidación y síntesis de ácidos grasos ocurran a la vez).
3. Transferencia de vuelta al CoA (matriz mitocondrial): Acil-carnitina + CoA-SH → Acil-CoA + carnitina
   (carnitina-acil-transferasa II, CAT-II); la carnitina se recicla al citosol.

**Ciclo de β-oxidación (4 reacciones que se repiten, ruta "en espiral"):**
1. Oxidación (deshidrogenación) → FADH2
2. Hidratación (+H2O)
3. Oxidación (deshidrogenación) → NADH
4. Hidrólisis + unión de CoA → libera **1 Acetil-CoA** y un acil-CoA acortado en 2 carbonos

Número de ciclos = (nº C / 2) − 1. Para ácidos grasos de número impar de C, el último ciclo genera
acetil-CoA + **propionil-CoA**, que se carboxila y se convierte en succinil-CoA (entra directo al ciclo de
Krebs). Para ácidos grasos insaturados se necesitan además una isomerasa y una reductasa para eliminar los
dobles enlaces cis antes de continuar el ciclo estándar.

**Rendimiento del palmitato (16:0)**: 7 ciclos → 8 acetil-CoA + 7 FADH2 + 7 NADH − 2 ATP (coste de
activación) ≈ **106 ATP** en total tras pasar los acetil-CoA por el ciclo de Krebs y la cadena respiratoria.

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf, pregunta 10.* "Explique la importancia de
la carnitina en la oxidación de los ácidos grasos": la carnitina es imprescindible porque el acil-CoA no
puede atravesar la membrana mitocondrial interna directamente. El ácido graso se transfiere del CoA a la
carnitina (CAT-I, citosólica), la acil-carnitina cruza mediante un transportador específico (translocasa), y
en la matriz mitocondrial el ácido graso se transfiere de vuelta al CoA (CAT-II). Esto permite mantener dos
depósitos separados de CoA (matriz: catabolismo; citosol: biosíntesis) y es además el punto de regulación
clave: CAT-I está inhibida por malonil-CoA, el primer intermediario de la síntesis de ácidos grasos —
mecanismo que impide la β-oxidación mientras la célula está sintetizando ácidos grasos activamente.

## Conexión con otros conceptos

- [[biosintesis-acidos-grasos]]: ruta inversa en localización y regulación (el malonil-CoA de una ruta
  inhibe el paso limitante de la otra).
- [[cuerpos-cetonicos]]: destino alternativo del acetil-CoA generado aquí cuando el oxalacetato escasea
  (ayuno prolongado).
- [[ciclo-krebs]]: destino final del acetil-CoA (y del succinil-CoA en ácidos grasos de número impar de C).
- [[inhibicion-enzimatica]]: malonil-CoA sobre CAT-I es un ejemplo fisiológico de inhibición.
- [[gluconeogenesis]]: el glicerol liberado en la lipólisis sí es precursor, pero los ácidos grasos no.

## Errores frecuentes de Marcos aquí

**Patrón 5** (orden incorrecto en procedimientos con secuencia obligatoria): los 3 pasos de
activación-transporte-transferencia tienen un orden estricto y una localización distinta cada uno (membrana
externa → transporte → matriz) — invertir el orden o mezclar dónde actúa CAT-I vs CAT-II es el error más
probable. Verifica explícitamente la localización de cada paso antes de escribirlo.

**Patrón 3** (aplicar fórmulas sin verificar el caso): el número de ciclos y los productos del último ciclo
dependen de si el ácido graso tiene número par o impar de carbonos, y de si está saturado o insaturado —
identificar el tipo de ácido graso antes de aplicar la fórmula de "(nº C/2)−1" ciclos.

## Relevancia en examen

**Alta.** "Explique la importancia de la carnitina" aparece en los 4 exámenes/hojas revisados. La tabla de
rutas metabólicas con β-oxidación (localización: matriz o membrana interna mitocondrial; sustratos: ácidos
grasos; productos: acetil-CoA, NADH, FADH2) aparece en todos. La pregunta V/F sobre "la degradación y
biosíntesis ocurren en el mismo compartimento" (falsa) y sobre "CAT-I se activa por malonil-CoA" (falsa, la
inhibe) son trampas recurrentes en el bloque V/F.
