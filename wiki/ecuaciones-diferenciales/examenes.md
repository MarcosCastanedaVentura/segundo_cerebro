---
titulo: "Ecuaciones Diferenciales y Modelización — análisis de exámenes"
asignatura: "ecuaciones-diferenciales"
tema: "Meta-análisis de exámenes 2018-2025"
tipo: "concepto"
relacionado: ["../ecuaciones-diferenciales/MOC"]
patrones_error: [3, 5, 6, 7]
examen_relevancia: "alta"
fuente: ["~24 exámenes/parciales/finales 2018-2025 en raw/Estudio2carrera/1 cuatri/ecuaciones diferenciales/"]
ultima_actualizacion: "2026-07-12"
---

# Qué cae en examen y con qué frecuencia

Análisis basado en la lectura directa de 14 de los ~24 exámenes/parciales disponibles en `raw/`
(muestra representativa de todos los años 2018-2025, primeros y segundos parciales, finales de
enero y julio): 1parcial18_19, EDO_Primer_Control, Final enero 18_19, EDO_Examen_Julio,
20251030_EcuaDif_Solución, ECUACIONES DI28octubre24 soluciones, 2025:12:19_PEP2 Alimentaria,
20_12_23_2parcial, Alimentaria_19_12_22, Examen Ordinario IA solución, FINAL 2_JULIO_2025,
Ejercicios examnes segundo parcial. Los ~10 exámenes restantes (JULIO20_21, JULIO22_23,
JULIO23_24, NOVIEMBRE_2022, Pracial18_12_24, RESOLUCIÓNl 30_10_23, examen final 23724,
ffinal_28_6_22, FINAL 9_ENE_24, FInal17_1_25, juliol18.19, soluciones2parciall19.20) no se
abrieron individualmente, pero por títulos y fechas siguen el mismo patrón de convocatoria
(parcial de diciembre / final de enero / final de julio) que los ya analizados, y los exámenes sí
leídos muestran una repetición casi literal de los mismos enunciados año tras año (los mismos
números cambian de un curso a otro, la estructura no).

## Estructura fija del curso

La asignatura se examina en **dos pruebas parciales (PEP1 en octubre/noviembre, PEP2 en
diciembre)** más un **examen final** (enero, y recuperación en julio) que cubre toda la materia.
Casi todos los exámenes, sea parcial o final, siguen el mismo guion de 3-5 problemas:

### Bloque A — EDOs de primer orden y modelización simple (siempre en PEP1 y en la primera mitad de los finales)

1. **Existencia y unicidad** de un PVI concreto (comprobar `f` y `∂f/∂y` continuas) — ver
   [[edo-conceptos-generales]]. Aparece casi siempre como primer apartado, 1-1.5 puntos.
2. **Resolver una EDO de primer orden** clasificándola primero (separable / lineal / exacta) —
   ver [[edo-separables]], [[edo-lineales-primer-orden]], [[edo-exactas]]. A veces piden
   explícitamente identificar el tipo antes de resolver.
3. **Aplicación de enfriamiento de Newton** (café, helado, cadáver) — ver [[edo-separables]].
4. **Problema de mezclas** (tanque de sal, azúcar, alcohol, salmuera) — ver
   [[edo-lineales-primer-orden]].
5. **Modelo logístico de población** (peces, lagartos, conejos, insectos): identificar modelo,
   puntos críticos y estabilidad, resolver el PVI, evaluar en un instante — ver
   [[modelos-poblacion-logistica]]. Es, junto con enfriamiento y mezclas, el ejercicio más
   repetido de todo el temario.

### Bloque B — EDOs lineales de 2º orden y sistemas (siempre en PEP2 y en la segunda mitad de los finales)

1. **EDO de 2º orden homogénea con coeficientes constantes**, casi siempre interpretada como un
   sistema masa-muelle-amortiguador: resolver el PVI, interpretar los coeficientes físicamente, y
   clasificar el tipo de movimiento (sobreamortiguado/crítico/subamortiguado/armónico simple)
   según el discriminante — ver [[edo-lineales-segundo-orden-homogeneas]] y
   [[edo-lineales-segundo-orden-completas]].
2. **Sistema de 2 EDOs lineales**: resolver por el método de autovalores (reales o complejos),
   dibujar el plano fase, clasificar el punto crítico y describir el comportamiento a largo plazo
   — ver [[autovalores-autovectores-sistemas-lineales]], [[autovalores-complejos]],
   [[clasificacion-puntos-criticos-sistemas-lineales]]. Casi siempre se pide también resolver el
   mismo sistema transformándolo en una ecuación de 2º orden, para verificar consistencia — ver
   [[sistemas-edo-primer-orden]].
3. **Sistema casi-lineal** (2 ecuaciones no lineales): hallar todos los puntos críticos,
   linealizar con la matriz Jacobiana en cada uno, clasificar tipo y estabilidad, explicar si se
   conserva en el sistema no lineal, y dar una interpretación biológica/industrial — ver
   [[sistemas-casi-lineales-estabilidad]]. Suele ser el ejercicio de mayor peso (4-5 puntos) y el
   más recurrente en forma de **modelo ecológico** (depredador-presa o especies compitiendo,
   normalmente disfrazado de plaga agrícola o bacterias en un alimento) — ver
   [[modelos-ecologicos-depredador-presa-competencia]].

## Formato de las preguntas

- Casi nunca son preguntas de teoría "suelta" (definir, enunciar sin aplicar): la teoría se
  evalúa siempre incrustada en un ejercicio de aplicación (ej. "enunciar el teorema de existencia
  y unicidad y aplicarlo a...", o "¿qué tipo de amortiguamiento resulta para cada valor de β?").
- El patrón dominante es: **clasificar el tipo de problema primero, resolver después** —
  prácticamente todos los ejercicios piden explícitamente identificar de qué tipo es la ecuación/
  sistema antes de aplicar el método. Esto es coherente con el **Patrón 3** de Marcos (aplicar
  fórmulas sin verificar antes las condiciones/tipo): en esta asignatura casi todos los puntos se
  pierden por saltarse ese paso de clasificación.
- Los contextos narrativos son sistemáticamente de tipo alimentario/agrícola/industrial (leche,
  helado, cerveza, cultivos, plagas, bacterias, tanques de mezcla) — coherente con el grado de
  Ingeniería Alimentaria/Agrícola de la ETSIAAB, y una buena señal de qué tipo de "ropaje" usar en
  los simulacros.
- Casi todos los exámenes indican explícitamente "no se admite ningún resultado si no está
  debidamente justificado" y prohíben calculadora programable — hay que dominar el cálculo a mano
  de raíces de polinomios de 2º grado, autovalores 2×2, integrales por fracciones parciales, y
  factor integrante.

## Distribución aproximada de puntuación (sobre exámenes de 4-5 ejercicios)

| Bloque | Peso aproximado |
|---|---|
| EDOs 1er orden (existencia/unicidad, separables/lineales/exactas) | 15-20% |
| Aplicaciones de modelización simple (enfriamiento, mezclas) | 20-25% |
| Modelo logístico de población | 15-20% |
| EDO de 2º orden / muelle-amortiguador | 15-20% |
| Sistemas lineales (autovalores, plano fase) | 15-20% |
| Sistemas casi-lineales / modelos ecológicos | 20-25% (el ejercicio de mayor peso) |

## Ver también

- [[MOC]]
- [[../perfil/patrones_error]]
