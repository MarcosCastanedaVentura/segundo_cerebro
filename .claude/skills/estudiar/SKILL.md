---
name: estudiar
description: Arranca una sesión de estudio con el tutor siguiendo el protocolo de inicio de sesión del BLOQUE 7 de CLAUDE.md — qué asignatura y tema, diagnóstico si falta, examen próximo, errores recientes de memory.json. Usa este skill al principio de cualquier sesión donde Marcos quiera estudiar, repasar, preparar un examen, o cuando diga cosas como "vamos a estudiar X", "quiero repasar Y", "tengo examen de Z", incluso si no invoca el comando explícitamente.
---

# Estudiar

Formaliza como pasos explícitos el protocolo de inicio de sesión que ya describe el BLOQUE 7 de
`CLAUDE.md`, para que no dependa de que se recuerde en prosa en una conversación larga. Este skill
no sustituye la metodología del tutor (BLOQUE 4) ni las restricciones — solo estructura el arranque.

## 1. Preguntar asignatura y tema

Si Marcos no lo ha dicho ya, pregunta qué asignatura y qué tema concreto se va a trabajar hoy. No
asumas la última asignatura de una sesión anterior — pregúntalo siempre de nuevo.

## 2. Comprobar el estado real, no lo que "recuerdes"

Lee `memory/memory.json` y busca la entrada de esa asignatura/tema:

- Si está marcada `SIN_DIAGNOSTICAR` o no existe todavía, haz un diagnóstico rápido de nivel (unas
  pocas preguntas de calibración, nunca un examen completo) antes de empezar a enseñar — Restricción 11
  de `CLAUDE.md` prohíbe saltarse esto.
- Revisa si hay errores recientes o Patrones de error (BLOQUE 3) activos en esa asignatura y ten
  presente que pueden repetirse hoy.

## 3. Preguntar por examen próximo

Si Marcos no lo ha mencionado, pregunta si tiene un examen próximo y su fecha. Adapta el modo según
el BLOQUE 4: menos de 24h → modo emergencia (solo lo esencial, solución completa permitida si la pide);
más margen → construir desde la base.

## 4. Comprobar si hay wiki para esa asignatura

Si `wiki/<asignatura>/` no existe todavía, créala siguiendo `wiki/_templates/` como indica el BLOQUE 6,
y trátala como diagnóstico pendiente.

## 5. A partir de aquí, el tutor de siempre

Con esto resuelto, sigue el resto de `CLAUDE.md` con normalidad: método socrático, prioridad de
búsqueda wiki → índice semántico (`query/retrieve.py`), nombrar los Patrones de error cuando se
activen, y verificar comprensión con ejercicios antes de avanzar — nunca con "¿lo has entendido?".
