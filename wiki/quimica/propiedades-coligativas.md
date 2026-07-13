---
titulo: "Propiedades coligativas (electrolitos y no electrolitos)"
asignatura: "quimica"
tema: "Tema 1 - Bloque 2: Propiedades Coligativas"
tipo: "formula"
relacionado: ["unidades-concentracion", "equilibrio-acido-base-ph"]
patrones_error: [3, 4]
examen_relevancia: "alta"
fuente: ["Tema 1. Bloque 2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Son propiedades físicas de una disolución (presión de vapor, punto de ebullición, punto de congelación,
presión osmótica) que dependen **únicamente del número de partículas de soluto disueltas**, no de qué
sustancia sea ese soluto. Por eso 1 mol de sal (que se separa en 2 iones) afecta el doble que 1 mol de
azúcar (que no se separa en absoluto) a estas propiedades.

## Por qué / de dónde viene

Cuantas más partículas de soluto hay disueltas, más "estorban" a las moléculas de disolvente para
escapar a vapor, para congelarse ordenadamente, o generan más flujo osmótico a través de una membrana.
El factor que corrige por el número real de partículas es el **factor de Van't Hoff (i)**:

- No electrolito (no se disocia, ej. glucosa, sacarosa, urea): i = 1 (1 molécula = 1 partícula).
- Electrolito fuerte (se disocia al 100%, ej. NaCl, CaCl₂): i = n + m, el nº total de iones que salen de
  la fórmula unidad (AₙBₘ → nA + mB).
- Electrolito débil (se disocia solo parcialmente, ej. ácido acético): i = 1 + α(ν − 1), donde α es el
  grado de disociación (dato del enunciado, entre 0 y 1) y ν es el nº de iones que generaría si se
  disociara completamente.

## Fórmula / procedimiento

| Propiedad | No electrolito | Electrolito | Símbolos |
|---|---|---|---|
| Descenso presión de vapor | ΔP = [nₛ/(nₛ+n_d)]·P° | ΔP = [nₛ·i/(nₛ·i+n_d)]·P° | nₛ=mol soluto, n_d=mol disolvente, P°=presión vapor disolvente puro |
| Ascenso ebulloscópico | ΔTe = Ke·m | ΔTe = Ke·m·i | Ke=cte ebulloscópica, m=molalidad |
| Descenso crioscópico | ΔTc = −Kc·m | ΔTc = −Kc·m·i | Kc=cte crioscópica |
| Presión osmótica | π = M·R·T | π = M·i·R·T | M=molaridad, R=0,082 atm·L·mol⁻¹·K⁻¹, T=temperatura absoluta (K) |

**Procedimiento**: (1) identificar si el soluto es electrolito fuerte, débil o no electrolito → (2)
calcular i → (3) calcular m o M según la propiedad pedida → (4) aplicar la fórmula correspondiente.

## Ejemplo resuelto

*(Tema 1. Bloque 2.pdf, Ejercicio 2)* Se disuelven 5,85 g de NaCl (Pm=58,5 g/mol) en 100 g de agua a
25 °C. Ke=0,52, Kc=1,86, P°=23,8 mmHg, R=0,082. Calcular ascenso ebulloscópico y presión osmótica.

1. Moles de soluto: n = 5,85/58,5 = 0,1 mol
2. Factor i: NaCl → Na⁺ + Cl⁻ (2 partículas, disociación completa) → i = 2
3. Molalidad: m = 0,1 mol / 0,1 kg agua = 1 mol/kg
4. ΔTe = Ke·m·i = 0,52·1·2 = **1,04 °C** (hierve a 101,04 °C)
5. Molaridad (aprox., disolución diluida): M ≈ 0,1 mol/0,1 L = 1 M
6. π = M·i·R·T = 1·2·0,082·298 = **48,9 atm**

## Conexión con otros conceptos

- [[unidades-concentracion]]: sin dominar molalidad, molaridad y fracción molar no se puede aplicar
  ninguna de estas fórmulas.
- [[equilibrio-acido-base-ph]]: el grado de disociación α reaparece igual en ácidos/bases débiles al
  calcular pH — es el mismo concepto físico (fracción de moléculas que se separan en iones).
- Conecta con presión osmótica en [[../bioquimica/MOC]]: el transporte a través de membranas celulares
  (ósmosis) es la misma física que aquí, aplicada a células en vez de a un tubo de laboratorio.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): las cuatro fórmulas cambian según si el soluto
es electrolito o no — usar la fórmula "simple" (sin i) para una sal es el error más común. Antes de
calcular, hay que clasificar explícitamente: ¿el soluto se disocia en agua? ¿totalmente o parcialmente?

**Patrón 4** (confundir cocientes relacionados): los cuatro numeradores/denominadores de i = 1 + α(ν−1)
son fáciles de trasponer bajo presión (confundir ν con i, o el "−1" con "+1"). Conviene escribir siempre
la ecuación de disociación completa antes de sustituir números.

## Relevancia en examen

Alta. Aparece de forma recurrente en los exámenes de julio 2025 y en el PEP1 como problema numérico
completo (calcular las 4 propiedades a partir de una masa disuelta), casi siempre combinando el cálculo
de i con al menos dos de las cuatro propiedades coligativas en el mismo enunciado.
