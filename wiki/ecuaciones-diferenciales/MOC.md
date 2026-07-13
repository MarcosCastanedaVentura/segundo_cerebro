---
titulo: "Ecuaciones Diferenciales y Modelización"
slug: "ecuaciones-diferenciales"
semestre: "3º"
creditos: 4
tipo: "Básica"
estado: "EN_PROGRESO"
ultima_actualizacion: "2026-07-12"
---

# Ecuaciones Diferenciales y Modelización — Mapa de contenidos

Ver estado dinámico y % de dominio real de Marcos en [`memory/memory.json`](../../memory/memory.json).

## Dependencias

Requiere Matemáticas I y II. Es base de Operaciones Unitarias I/II, Ingeniería del Calor e Ingeniería del Frío
(3º-4º curso). Ver [[../carrera/dependencias]].

## Temario y notas

- **Tema 1 — Ecuaciones diferenciales de primer orden**
  - [[edo-conceptos-generales]] — orden, EDO vs EDP, solución general/particular/singular, PVI,
    teorema de existencia y unicidad
  - [[edo-separables]] — separación de variables + aplicaciones (enfriamiento de Newton,
    crecimiento/decaimiento exponencial)
  - [[edo-lineales-primer-orden]] — factor integrante + problemas de mezclas
  - [[edo-exactas]] — criterio de exactitud `∂M/∂y = ∂N/∂x`
- **Tema 2 — Modelos matemáticos y estabilidad de EDOs autónomas de 1er orden**
  - [[modelos-poblacion-logistica]] — crecimiento exponencial, ecuación logística, puntos
    críticos y estabilidad en 1 dimensión
- **Tema 3 — Ecuaciones lineales de segundo orden**
  - [[edo-lineales-segundo-orden-homogeneas]] — ecuación característica: raíces reales
    distintas/dobles/complejas
  - [[edo-lineales-segundo-orden-completas]] — coeficientes indeterminados + aplicaciones
    (muelle-amortiguador, circuito RLC)
- **Tema 4 — Introducción a los sistemas de ecuaciones diferenciales**
  - [[sistemas-edo-primer-orden]] — transformación entre EDO de 2º orden y sistema de 2
    ecuaciones de 1er orden (en ambas direcciones)
- **Tema 5 — Sistemas de ecuaciones diferenciales lineales**
  - [[autovalores-autovectores-sistemas-lineales]] — método de autovalores/autovectores para
    `X'=AX`, atajo traza-determinante
  - [[autovalores-complejos]] — fórmula de Euler, espirales y centros
  - [[clasificacion-puntos-criticos-sistemas-lineales]] — nodo propio/impropio/estrella, silla,
    espiral, centro; mapa traza-determinante
- **Tema 6 — Sistemas casi lineales**
  - [[sistemas-casi-lineales-estabilidad]] — linealización, matriz Jacobiana, teorema de
    transferencia de estabilidad
- **Tema 7 — Modelos ecológicos**
  - [[modelos-ecologicos-depredador-presa-competencia]] — Lotka-Volterra depredador-presa y
    especies compitiendo

## Prácticas

No hay prácticas de laboratorio en esta asignatura (es íntegramente teórico-numérica). Las
"hojas de problemas" de `raw/` (PROBLEMAS_TEMA1_COMPLEMENTARIOS, ejercicios tema 2, Problemas
Tema 3/4y5/6) se han usado como fuente de ejemplos dentro de las notas atómicas de arriba, no
como notas propias — ver cada nota para los ejemplos concretos extraídos de ellas.

## Exámenes

Ver [`examenes.md`](examenes.md) para el análisis completo de qué cae, con qué frecuencia y en
qué formato. Resumen: dos parciales (PEP1 octubre/noviembre sobre Temas 1-2, PEP2 diciembre sobre
Temas 3-7) más final en enero y recuperación en julio cubriendo todo. El ejercicio de mayor peso
en casi todos los exámenes es el de sistemas casi-lineales/modelos ecológicos (4-5 puntos).

## Material sin procesar todavía

- `EC DIF 1_1y2 (2).pdf`, `EC DIF 1_3.pdf`, `EC DIF 1_4.pdf`, `EC DIF 1_5 Lineales.pdf`,
  `EC DIF 1_6.pdf`, `EC DIF 2_1.pdf`, `EC DIF 2_2.pdf` — son páginas escaneadas del libro de
  texto fuente (Edwards & Penney, *Ecuaciones diferenciales y problemas con valores de la
  frontera*). Se ha comprobado que su contenido está ya sintetizado casi al detalle en
  `Apuntes de ecuaciones diferenciales.pdf` (el documento maestro de 105 páginas usado como fuente
  principal de todas las notas de este MOC), así que no se han vuelto a procesar por separado
  para evitar duplicar trabajo — si en algún momento hace falta un ejemplo adicional del libro
  original, están aquí sin abrir todavía.
- `Ejemplo Autovalores complejos.pdf` (1 página) — no se pudo extraer texto ni se abrió en
  detalle; por el nombre coincide con el ejemplo ya cubierto en [[autovalores-complejos]].
- `Problemas Tema 6_SIST CASI LIN_Fdo.pdf` y `Problemas Temas 4 y 5_SISTEMAS_Fdo.pdf` — hojas de
  problemas de sistemas y sistemas casi-lineales, escaneadas como imágenes (15 MB cada una, sin
  texto extraíble); no se han revisado página a página. Es la fuente más probable de ejercicios
  adicionales para practicar [[autovalores-autovectores-sistemas-lineales]] y
  [[sistemas-casi-lineales-estabilidad]] si Marcos pide más ejemplos de esos temas.
- De los ~24 exámenes/parciales/finales sueltos (2018-2025), se abrieron y analizaron 14 en
  detalle para `examenes.md` (ver esa nota para la lista exacta). Los ~10 restantes
  (`JULIO20_21soluciones.pdf`, `JULIO22_23 SOLUCION.pdf`, `JULIO23_24 SOLUCIONES.pdf`,
  `NOVIEMBRE _2022 _SOLUCIONES.pdf`, `Pracial18_12_24.pdf`, `RESOLUCIÓNl 30_10_23.pdf`,
  `examen final 23724.pdf`, `ffinal_28_6_22 _ soluciones - copia.pdf`,
  `FINAL 9_ENE_24-1soluciones.pdf`, `FInal17_1_25 - solucionesz.pdf`, `juliol18.19..pdf`,
  `soluciones2parciall19.20.pdf`) no se han abierto todavía; por título y fecha siguen el mismo
  patrón de convocatoria que los ya analizados, pero si Marcos quiere ejemplos concretos de un año
  concreto de esa lista, hay que abrirlos primero — no asumir su contenido.
