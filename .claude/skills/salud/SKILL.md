---
name: salud
description: Auditoría de higiene del wiki — wikilinks sin resolver, notas sin fuente, posibles duplicados, carpetas sobrecargadas y contradicciones entre notas. Usa este skill cuando Marcos pida revisar, auditar o hacer un chequeo de salud del wiki/segundo cerebro, cuando pregunte si hay huecos o temas pendientes, o periódicamente por iniciativa propia si ha pasado mucho tiempo desde la última vez y se han añadido muchas notas nuevas. Es de solo lectura: detecta y reporta, nunca corrige ni borra nada automáticamente.
---

# Salud del wiki

Existe un riesgo real en un sistema donde el propio LLM escribe su memoria de largo plazo: si en algún
momento se genera contenido incorrecto y se guarda, las siguientes sesiones construyen sobre ese error
como si fuera verdad — el wiki deja de ser fuente de verdad fiable. Este skill es la auditoría que evita
que eso pase desapercibido. Es explícitamente a demanda, sin cron ni watcher (ver BLOQUE 8 de
`CLAUDE.md`): lo disparas tú cuando quieras, no corre solo en background.

## 1. Chequeos mecánicos — ejecuta el script

```bash
.venv/bin/python tools/wiki_health.py
```

Este script es determinista (no usa LLM) y comprueba:
- **Wikilinks sin resolver**: `[[nombre]]` que no apunta a ninguna nota existente.
- **Notas sin `fuente`**: notas de tipo concepto/fórmula/procedimiento/práctica sin origen verificable.
- **Posibles duplicados**: notas de la misma asignatura con alta similitud de texto.
- **Carpetas sobrecargadas**: asignaturas con muchas más notas que la mediana del resto.

## 2. Interpreta los wikilinks sin resolver con criterio, no como una lista de errores

No todos son bugs. En este wiki hay dos casos distintos y hay que distinguirlos:
- **Huecos legítimos**: un concepto mencionado desde varias notas que todavía no tiene nota propia (ej.
  `triangulo-potencias`, `distribucion-normal-tipificacion`) — esto es exactamente la señal útil: qué
  nota crear a continuación. Repórtalo a Marcos como sugerencia de próxima nota, no como error.
- **Referencias adelantadas a asignaturas futuras**: enlaces tipo `[[../instalaciones-electricas/MOC|...]]`
  que apuntan a una asignatura de un curso que aún no se ha empezado a trabajar — son intencionados
  (BLOQUE 6 de `CLAUDE.md`), no los señales como problema.
- **Errores de formato reales**: por ejemplo un wikilink que incluye `.md` en el nombre (`[[examenes.md]]`
  en vez de `[[examenes]]`) — esto sí es un bug de transcripción, corrígelo tú mismo en el fichero
  (Restricción 7: es una corrección, no un borrado destructivo de contenido).

## 3. Contradicciones — esto no lo hace el script, lo haces tú

El script no puede juzgar si dos notas se contradicen — requiere lectura real. No hace falta releer las
~90 notas cada vez: prioriza así:
1. Lee los `MOC.md` de las asignaturas tocadas recientemente (mira `ultima_actualizacion` en el
   frontmatter) — es donde es más probable que se haya colado algo a medio verificar.
2. Si el script marcó posibles duplicados o una carpeta sobrecargada, lee esas notas concretas primero —
   es donde más probablemente haya contenido solapado o inconsistente.
3. Si Marcos pide una auditoría completa explícitamente, entonces sí, lee todo el wiki de la asignatura
   en cuestión.

## 4. Reporta con esta estructura

- **Huecos** (temas por crear, priorizados por cuántas notas los mencionan).
- **Bugs reales** (formato, `fuente` ausente) — y si los corriges, dilo explícitamente.
- **Duplicados/carpetas sobrecargadas** — con una recomendación concreta (fusionar, dividir en sub-temas).
- **Contradicciones encontradas** (si las hay) — cita las dos notas exactas y la fecha de cada una.

No hace falta actuar sobre todo en la misma sesión. Termina preguntando a Marcos qué quiere abordar
primero — esto es una auditoría, no una reescritura automática del wiki.
