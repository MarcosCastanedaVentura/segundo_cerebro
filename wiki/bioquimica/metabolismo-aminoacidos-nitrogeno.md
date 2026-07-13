---
titulo: "Metabolismo de aminoácidos: transaminación, desaminación y destino del nitrógeno"
asignatura: "bioquimica"
tema: "Tema 7 - Metabolismo de aminoácidos y ácidos nucleicos"
tipo: "concepto"
relacionado: ["aminoacidos-y-estructura-proteica", "ciclo-alanina-glucosa-cahill", "ciclo-krebs", "gluconeogenesis", "cuerpos-cetonicos"]
patrones_error: [2]
examen_relevancia: "alta"
fuente: ["Tema 7.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Recuperacion (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

A diferencia de la glucosa o los ácidos grasos, los aminoácidos no se pueden almacenar ni excretar
directamente: el exceso que no se usa en biosíntesis se degrada separando el grupo α-amino (que sigue una
ruta de eliminación como nitrógeno) del esqueleto carbonado (que se oxida en el ciclo de Krebs o se usa como
precursor).

## Por qué / de dónde viene

Cada aminoácido tiene su propia ruta de degradación, pero todas comparten la misma lógica de dos pasos: (1)
separar el grupo amino del esqueleto carbonado y (2) enviar cada uno por su ruta. El grupo amino es tóxico en
forma de amoníaco/amonio libre (neurotóxico), así que el organismo lo "canaliza" primero hacia un único
aminoácido (glutamato) antes de eliminarlo, en vez de tener una vía de excreción distinta para cada
aminoácido — una solución mucho más eficiente evolutivamente.

## Fórmula / procedimiento

**Destino del grupo amino — dos mecanismos:**
1. **Transaminación** (citosol de hepatocitos, la mayoría de aminoácidos siguen esta vía): catalizada por
   aminotransferasas (grupo prostético piridoxal-fosfato = vitamina B6 activa). NO es una desaminación neta
   (no se libera amonio): el aminoácido cede su -NH2 a un α-cetoácido (habitualmente α-cetoglutarato) para
   formar el correspondiente α-cetoácido del aminoácido original + L-glutamato.
   - Ejemplo clave de examen: Ala + α-KG ⇌ Piruvato + Glu (ALT/GPT — marcador de daño hepático).
   - Ejemplo clave de examen: Asp + α-KG ⇌ Oxalacetato + Glu (AST/GOT — menos específica de hígado, se eleva
     también por infarto o ejercicio intenso).
2. **Desaminación oxidativa** (mitocondria): la más importante es la del L-glutamato, catalizada por
   glutamato deshidrogenasa (enzima alostérico: activado por ADP, inhibido por GTP — inhibición feedback),
   que sí libera NH4+ neto: Glutamato + NAD⁺ → α-cetoglutarato + NADH + NH4⁺.

**Destino del ión NH4⁺:**
- Reutilización en biosíntesis de compuestos nitrogenados (nucleótidos, aminas biogénicas).
- Excreción, en forma que depende del hábitat: NH3 directo (amoniotélicos: peces óseos), ácido úrico
  (uricotélicos: aves, reptiles), **urea (ureotélicos: mamíferos)** — vía ciclo de la urea, hepatocito
  (mitocondria + citosol), con gasto de ATP.
- Transporte seguro por la sangre: como glutamina (mayoría de tejidos) o como **alanina** (desde el músculo,
  ver [[ciclo-alanina-glucosa-cahill]]).

**Destino del esqueleto carbonado** — clasificación de los aminoácidos:
- **Glucogénicos**: se degradan a piruvato o intermediarios del ciclo de Krebs → pueden generar glucosa por
  gluconeogénesis.
- **Cetogénicos**: se degradan a acetil-CoA o acetoacetil-CoA → pueden generar cuerpos cetónicos (ver
  [[cuerpos-cetonicos]]). Leu y Lys son cetogénicos puros; varios aminoácidos son mixtos.

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-Examen final (2022-2023) y ordinario 2023-2024, pregunta sobre V/F.*
"El amonio producido por desaminación oxidativa se elimina en mamíferos como ácido úrico" — **FALSA**. En
mamíferos el NH4⁺ se elimina principalmente como **urea** a través del ciclo de la urea; el ácido úrico es el
producto de excreción de las bases púricas (degradación de ácidos nucleicos), no de los aminoácidos — una
confusión muy explotada en los exámenes revisados.

## Conexión con otros conceptos

- [[aminoacidos-y-estructura-proteica]]: estructura de los aminoácidos cuyo catabolismo se describe aquí.
- [[ciclo-alanina-glucosa-cahill]]: mecanismo concreto de transporte del nitrógeno muscular al hígado.
- [[ciclo-krebs]]: destino final de los esqueletos carbonados glucogénicos.
- [[cuerpos-cetonicos]]: destino de los esqueletos carbonados cetogénicos.
- [[gluconeogenesis]]: los aminoácidos glucogénicos son precursores directos.
- Conexión con Microbiología Alimentaria: ciclo del nitrógeno en suelo/bacterias fijadoras (contexto amplio
  del tema) — ver [[../microbiologia/MOC]].

## Errores frecuentes de Marcos aquí

**Patrón 2** (confundir términos/procesos parecidos): "transaminación" (no libera amonio, transfiere el grupo
NH2 de un aminoácido a otro) y "desaminación oxidativa" (sí libera NH4⁺ neto) se confunden con facilidad
porque ambas "quitan" el grupo amino del aminoácido original. Exige verbalizar si el proceso libera o no
amonio libre antes de identificarlo, y qué coenzima/cofactor interviene en cada uno (PLP en
transaminación vs NAD⁺ en la desaminación de Glu).

## Relevancia en examen

**Alta.** "Explique la diferencia entre aminoácidos glucogénicos y cetogénicos" aparece **literalmente en
los 4 exámenes/hojas de ejercicios revisados**. La pregunta V/F sobre excreción de amonio como ácido úrico
(falsa, es urea) es una trampa recurrente. Formular sustratos/productos de transaminasas (ALT/GPT, AST/GOT)
también es material de examen.
