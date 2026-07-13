---
titulo: "Cadena de transporte electrónico y fosforilación oxidativa"
asignatura: "bioquimica"
tema: "Tema 5 - Metabolismo oxidativo"
tipo: "concepto"
relacionado: ["ciclo-krebs", "termodinamica-bioenergetica", "atp-compuestos-alta-energia", "glucolisis"]
patrones_error: [3, 7]
examen_relevancia: "alta"
fuente: ["05-Met oxidativo.pdf", "Problemas de Metabolismo 2.pdf", "examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La cadena de transporte electrónico (cadena respiratoria) reoxida el NADH y el FADH2 generados en glucólisis,
descarboxilación del piruvato, ciclo de Krebs y β-oxidación, cediendo sus electrones en última instancia al
O2 (que se reduce a H2O). Este transporte de electrones está acoplado a la síntesis de ATP (fosforilación
oxidativa) mediante el gradiente de protones que genera a través de la membrana mitocondrial interna (teoría
quimiosmótica).

## Por qué / de dónde viene

Los electrones no pasan directamente de NADH/FADH2 al O2: lo hacen a través de una serie de transportadores
(4 complejos transmembrana + 2 transportadores móviles) ordenados por afinidad creciente por los electrones
(potencial de reducción E0' creciente). Cada salto de electrones entre complejos libera energía libre
(ΔG'=−nFΔE0', ver [[termodinamica-bioenergetica]]), que en 3 de los 4 complejos (I, III, IV) se usa para
bombear protones desde la matriz al espacio intermembrana, creando un gradiente electroquímico (fuerza
protón-motriz, con componente químico ΔpH y componente eléctrico ΔΨ). El retorno de esos protones a la matriz
a través del canal de la ATP sintasa (complejo F0F1) es lo que impulsa la síntesis de ATP a partir de ADP+Pi
— es decir, la energía "de electrones" se convierte primero en un gradiente de protones y después en energía
del enlace fosfoanhidro del ATP.

## Fórmula / procedimiento

**Los 4 complejos transmembrana + 2 transportadores móviles:**
- Complejo I (NADH-coenzima Q reductasa): recibe electrones del NADH, bombea protones.
- Complejo II (succinato-coenzima Q reductasa): recibe electrones del FADH2 (succinato deshidrogenasa, del
  ciclo de Krebs) — **no bombea protones**, por eso el FADH2 rinde menos ATP que el NADH.
- Ubiquinona (CoQ): transportador móvil liposoluble, recibe electrones de los complejos I y II.
- Complejo III (citocromo reductasa): bombea protones.
- Citocromo c: transportador móvil, en el espacio intermembrana.
- Complejo IV (citocromo oxidasa): reduce el O2 a H2O, bombea protones.

**ATP sintasa (F0F1):**
- F1 (periférico, matriz): 5 subunidades (3α3βγδε), sintetiza ATP a partir de ADP+Pi usando la energía del
  flujo de protones.
- F0 (transmembrana): canal de protones.

**Rendimiento energético aproximado** (valores clásicos usados en los exámenes de esta asignatura, aunque la
bioquímica moderna usa 2,5 y 1,5 respectivamente por la estequiometría real de bombeo de H⁺): **NADH ≈ 3
ATP**, **FADH2 ≈ 2 ATP** — la diferencia se debe exactamente a que el FADH2 entra por el complejo II,
saltándose el bombeo de protones del complejo I.

## Ejemplo resuelto

*Adaptado de Problemas de Metabolismo 2.pdf, pregunta 10.* El amital y la rotenona bloquean el Complejo I. Si
se añade succinato a una suspensión de mitocondrias:
- **Producción de H2O**: continúa con normalidad, porque los electrones del succinato entran por el Complejo
  II (que no está bloqueado), siguen por III y IV, y el O2 se sigue reduciendo a H2O.
- **Producción de ATP**: disminuye (pero no se detiene del todo), porque el Complejo II no bombea protones —
  se pierde una fracción del gradiente de protones que normalmente aportaría el Complejo I, pero los
  Complejos III y IV siguen bombeando.

*Ejemplo del desacoplante (adaptado de la misma hoja, pregunta sobre el 2,4-dinitrofenol):* el DNP hace
permeable la membrana mitocondrial interna a los protones, de forma que estos vuelven a la matriz sin pasar
por la ATP sintasa. El transporte de electrones (y el consumo de O2) sigue funcionando, pero la energía del
gradiente se disipa como **calor** en vez de sintetizar ATP — por eso se usó (peligrosamente) como
"adelgazante": el organismo sigue quemando sustrato pero no obtiene ATP de ello.

## Conexión con otros conceptos

- [[ciclo-krebs]]: fuente principal de NADH y FADH2 que alimentan esta cadena.
- [[termodinamica-bioenergetica]]: la relación ΔG0'=−nFΔE0' es la que explica por qué los electrones fluyen
  en el orden de los complejos (de menor a mayor afinidad por los electrones).
- [[atp-compuestos-alta-energia]]: la fosforilación oxidativa es uno de los 3 mecanismos de síntesis de ATP.
- [[glucolisis]] y [[metabolismo-lipidos-beta-oxidacion]]: también generan NADH/FADH2 que se reoxidan aquí.
- Conexión con Microbiología Alimentaria: en procariotas la cadena está en la membrana plasmática, no en
  mitocondrias (ver [[../microbiologia/MOC]]) — bombea protones hacia el espacio periplásmico.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): el rendimiento en ATP del NADH es distinto según
de dónde venga — el NADH citosólico de la glucólisis necesita un sistema de lanzadera para entrar en la
mitocondria y puede rendir menos ATP que el NADH mitocondrial, dependiendo del tejido. Verificar siempre si
el NADH en cuestión es citosólico o mitocondrial antes de aplicar el factor de conversión a ATP.

**Patrón 7** (validar sin verificar): comprobar que un inhibidor de un complejo concreto (ej. Complejo I)
sigue permitiendo la reoxidación de FADH2 (que entra por el Complejo II) es un chequeo de razonabilidad
habitual en estos ejercicios — no asumir que bloquear un complejo detiene toda la cadena.

## Relevancia en examen

**Alta.** La tabla de rutas metabólicas con "Cadena de transporte e-" (localización: membrana mitocondrial
interna; sustratos: NADH, FADH2; productos: ATP, agua) aparece en los 4 exámenes revisados. Preguntas de
razonamiento sobre inhibidores de complejos específicos (rotenona, amital, cianuro, antimicina) y sobre
desacoplantes (2,4-dinitrofenol) aparecen en Problemas de Metabolismo 2 y en las hojas de ejercicios de
examen. La teoría quimiosmótica en procariotas también se pregunta explícitamente.
