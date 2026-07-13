---
titulo: "Bioenergética: leyes de la termodinámica y energía libre de Gibbs"
asignatura: "bioquimica"
tema: "Tema 3 - Bioenergética"
tipo: "concepto"
relacionado: ["atp-compuestos-alta-energia", "enzimas-estructura-funcion", "cadena-transporte-electrones-fosforilacion-oxidativa"]
patrones_error: [3, 7]
examen_relevancia: "media"
fuente: ["Tema 3 Bioenergetica.pdf", "Problemas de Metabolismo 2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La bioenergética estudia cómo los seres vivos usan la energía para producir trabajo biológico (mecánico,
osmótico, metabólico). Se rige por las mismas leyes físicas que cualquier sistema: la 1ª ley (la energía no
se crea ni se destruye, solo se transforma) y la 2ª ley (todo proceso real disipa energía como calor y
aumenta el desorden del universo). La magnitud clave para saber si una reacción bioquímica ocurre
espontáneamente es la **variación de energía libre de Gibbs (ΔG)**.

## Por qué / de dónde viene

Un organismo es un sistema abierto muy ordenado comparado con su entorno: mantener ese orden (baja entropía
local) cuesta energía continuamente, incluso en reposo — nunca alcanza el equilibrio termodinámico (el
equilibrio sería, literalmente, la muerte celular). La energía libre G = H − TS combina el contenido calórico
(entalpía H) y el desorden (entropía S) a una temperatura T; su variación ΔG = ΔH − TΔS es la que determina si
una reacción libera energía útil (exergónica, ΔG<0, espontánea) o la requiere (endergónica, ΔG>0, no
espontánea). Las reacciones endergónicas del metabolismo (anabolismo) se hacen posibles acoplándolas a
reacciones exergónicas (catabolismo, sobre todo la hidrólisis del ATP) de forma que la suma de ambos ΔG sea
negativa.

## Fórmula / procedimiento

- ΔG = ΔH − TΔS (T en Kelvin)
- ΔG negativo → reacción **espontánea/exergónica**; ΔG positivo → **no espontánea/endergónica**.
- Energía libre estándar (ΔG0'): valor de ΔG en condiciones estándar bioquímicas (pH=7, T=25°C=298K, P=1 atm,
  [sustratos]=[productos]=1M). Es una constante característica de cada reacción.
- Energía libre real: ΔG = ΔG0' + RT·ln(K'eq) = ΔG0' + 2,303·RT·log([C][D]/[A][B]), donde R=1,987 cal/mol·K.
  ΔG (real) depende de las concentraciones reales presentes en la célula; ΔG0' no.
- Relación con la constante de equilibrio: si Keq=1 → ΔG0'=0 (equilibrio); si Keq>1 → ΔG0'<0 (espontánea);
  si Keq<1 → ΔG0'>0 (no espontánea).
- ΔG real siempre es ≤0 en una reacción que avanza espontáneamente hacia el equilibrio (se hace menos
  negativo a medida que se acerca al equilibrio, y es 0 exactamente en el equilibrio).
- Potenciales redox: ΔG0' = −nFΔE0' (F = constante de Faraday = 96485 C/mol; n = nº electrones transferidos).
  Un par redox con E0' más negativo tiene mayor tendencia a **ceder** electrones (más reductor); el par con
  E0' más positivo tiende a **aceptarlos** (más oxidante). La reacción global va del par más reductor
  (dador) al par más oxidante (aceptor).

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf.* Pares redox conjugados NAD⁺/NADH
(E0'=−0,32 V) y piruvato/lactato (E0'=−0,19 V). Reacción: piruvato + NADH + H⁺ → lactato + NAD⁺.

- El par con E0' más negativo (NAD⁺/NADH, −0,32 V) tiene mayor tendencia a ceder electrones → NADH es el
  reductor, se oxidará.
- El par con E0' más positivo (piruvato/lactato, −0,19 V) es el aceptor de electrones (agente oxidante más
  fuerte de los dos) → el piruvato se reducirá a lactato.
- ΔE0' = E0'(aceptor) − E0'(dador) = −0,19 − (−0,32) = +0,13 V
- ΔG0' = −nFΔE0' = −2 × 96485 C/mol × 0,13 V ≈ −25 086 J/mol ≈ **−25,1 kJ/mol**
- ΔG0' negativo → con concentraciones estándar (1M) la reacción avanza espontáneamente hacia la formación de
  lactato (esto es exactamente lo que hace la fermentación láctica, ver [[glucolisis]]).

## Conexión con otros conceptos

- [[atp-compuestos-alta-energia]]: el ATP es el intermediario que "transporta" la energía libre entre
  reacciones acopladas.
- [[cadena-transporte-electrones-fosforilacion-oxidativa]]: aplica directamente ΔG0'=−nFΔE0' para calcular
  cuánta energía libera cada salto de electrones entre complejos.
- [[glucolisis]]: la reacción fosfofructoquinasa-1 tiene ΔG0' muy negativo (−22,2 kJ/mol) y por eso es
  prácticamente irreversible en la célula — clave para entender por qué la gluconeogénesis necesita un
  enzima distinto (fructosa-1,6-bisfosfatasa) en ese paso.
- Conexión con Química (termodinámica química, entropía, entalpía — ver [[../quimica/MOC]], base directa
  según [[../carrera/dependencias]]) y con Física (conceptos de energía y trabajo).

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): ΔG0' es un valor fijo tabulado por reacción, pero
ΔG real cambia con las concentraciones celulares reales — confundir ambos y usar ΔG0' para decidir la
dirección real de una reacción en la célula es un error típico. Antes de decidir espontaneidad, verifica si
el enunciado da concentraciones reales (hay que calcular ΔG real) o pide el valor estándar (ΔG0').

**Patrón 7** (validar sin verificar unidades): en el cálculo de ΔG0'=−nFΔE0', comprobar que el resultado en
J/mol tiene el signo coherente con qué especie se reduce y cuál se oxida — un signo cambiado es fácil de
pasar por alto si no se verifica al final.

## Relevancia en examen

**Media.** No suele aparecer como bloque de problema aislado en los 4 exámenes oficiales revisados, pero sí
como base conceptual de preguntas de "explique por qué" (ej. dirección del ciclo de Cori, por qué la
glucólisis y la gluconeogénesis no son la simple reacción inversa) y en el material de "Problemas de
Metabolismo 2" con ejercicios completos de ΔG0' y potenciales redox.
