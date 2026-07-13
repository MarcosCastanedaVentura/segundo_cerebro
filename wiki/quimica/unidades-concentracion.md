---
titulo: "Unidades de concentración y conversiones"
asignatura: "quimica"
tema: "Tema 1 - Bloque 1: Unidades de Concentración"
tipo: "formula"
relacionado: ["propiedades-coligativas", "equilibrio-acido-base-ph", "equilibrios-solubilidad-kps"]
patrones_error: [3, 6]
examen_relevancia: "media"
fuente: ["Tema 1. Bloque 1.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Conjunto de formas de expresar "cuánto soluto hay en una disolución". No es una única magnitud: hay
unidades que dependen del volumen de la disolución (Molaridad, Normalidad, %v/v, %p/v, ppm, ppb) y
unidades que dependen solo de masas (molalidad, fracción molar, %p/p), que por tanto **no cambian con
la temperatura**. Saber cuál usar según el contexto (estequiometría vs. propiedades coligativas vs.
trabajo de laboratorio) es la mitad del problema en los ejercicios de este bloque.

## Por qué / de dónde viene

El volumen de un líquido se dilata con el calor, así que cualquier concentración definida "por litro de
disolución" (M, N, %v/v, %p/v, ppm) varía ligeramente si cambia la temperatura, aunque la cantidad de
soluto sea la misma. Para evitar ese problema en medidas de precisión (como las propiedades coligativas,
que se miden calentando o enfriando la disolución) se usan magnitudes basadas en masas, que no varían:
molalidad (moles soluto / kg disolvente) y fracción molar (proporción real de partículas). La densidad
es la pieza que conecta ambos mundos: permite pasar de masa total de disolución a volumen y viceversa.

## Fórmula / procedimiento

- **Molaridad**: M = mol soluto / L disolución (depende de T)
- **Normalidad**: N = eq soluto / L disolución = M · ν, donde ν = nº de H⁺ transferidos (ácido-base) o
  electrones intercambiados (redox) por fórmula unidad. **Cuidado**: ν no es fijo por sustancia, depende
  de la reacción (ver Patrón 3 más abajo).
- **Molalidad**: m = mol soluto / kg disolvente (NO depende de T)
- **Fracción molar**: Xᵢ = mol componente i / mol totales. Siempre ΣXᵢ = 1.
- **%p/p** = (masa soluto / masa disolución)·100 ; **%v/v** = (vol soluto/vol disolución)·100 ;
  **%p/v** = (masa soluto en g / vol disolución en mL)·100
- **ppm** = mg soluto / kg (o L) disolución ; **ppb** = µg/kg ; **ppt** = ng/kg — para disoluciones muy diluidas.
- **Densidad**: ρ = m/V — puente entre masa y volumen de la disolución (no es unidad de concentración).

## Ejemplo resuelto

*(Tema 1. Bloque 1.pdf, Ejercicio 1)* Se disuelven 36 g de azúcar (Pm = 180 g/mol, no electrolito) en
360 g de agua. Densidad de la disolución = 1,05 g/mL. Calcular M y m.

1. Moles de soluto: n = 36/180 = 0,2 mol
2. Molalidad: kg disolvente = 0,36 kg → m = 0,2/0,36 = **0,55 m**
3. Para Molaridad hace falta el volumen de la disolución, no del disolvente:
   masa total = 36 + 360 = 396 g → V = 396/1,05 = 377,14 mL = 0,377 L
   M = 0,2/0,377 = **0,53 M**

El error típico aquí es dividir por el volumen de agua en vez de por el volumen de la disolución
completa (que incluye el soluto) — por eso hace falta la densidad de la disolución, no la del agua.

## Conexión con otros conceptos

- [[propiedades-coligativas]]: usa molalidad (m) y molaridad (M) como variables de entrada — sin dominar
  esta nota, no se puede calcular Δp, ΔTe, ΔTc ni π correctamente.
- [[equilibrio-acido-base-ph]]: la Normalidad y el concepto de equivalente reaparecen en valoraciones
  ácido-base.
- [[equilibrios-redox]]: la Normalidad en redox usa ν = electrones intercambiados, no protones — mismo
  nombre de magnitud, significado físico distinto (ver Patrón 3 abajo).
- Base de [[../bioquimica/MOC]]: en Bioquímica las concentraciones de sustrato/enzima en cinética
  enzimática se manejan casi siempre en Molaridad.

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): la fórmula N = M·ν parece única pero ν
cambia de significado según el tipo de reacción — en ácido-base es el nº de H⁺/OH⁻ intercambiados, en
redox es el nº de electrones transferidos. Antes de calcular N hay que preguntarse explícitamente "¿ν de
qué reacción?".

**Patrón 6** (copiar mal datos): en estos ejercicios es fácil confundir "masa de soluto" con "masa de
disolución" al leer el enunciado (p. ej. "9 g de KCl en 100 mL de disolución" no es lo mismo que "9 g de
KCl en 100 mL de agua"). Verificar siempre qué volumen/masa se da antes de plantear la fórmula.

## Relevancia en examen

Relevancia media: no suele ser la pregunta central de un examen, pero aparece como paso intermedio en
casi cualquier problema numérico (ácido-base, redox, solubilidad) porque primero hay que pasar los datos
del enunciado a Molaridad. En los exámenes de julio 2025 y PEP1 aparece siempre camuflado dentro de
enunciados de otros temas, casi nunca como pregunta aislada de "calcula la Molaridad de...".
