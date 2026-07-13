---
name: indexar
description: Dispara la ingesta incremental del pipeline RAG (extract → chunk → embed) sobre raw/ y reporta qué se indexó. Usa este skill siempre que Marcos diga que ha añadido apuntes, PDFs, fotos o exámenes nuevos a raw/, o pida explícitamente indexar, reindexar, actualizar el índice, o "meter esto al segundo cerebro" — incluso si no usa la palabra exacta "indexar". No sintetiza contenido ni responde preguntas de la carrera: solo mueve datos de raw/ al índice vectorial.
---

# Indexar

Este skill ejecuta `ingest/run.py`, el pipeline que convierte PDFs/imágenes/docx de `raw/` en chunks
embebidos dentro de la colección única de Chroma (`index/`). Es mantenimiento de datos, no tutoría:
no genera respuestas de contenido ni crea notas en `wiki/` por sí mismo.

## 1. Comprobar credenciales antes de nada

Lee `.env` en la raíz del proyecto. Si no existe, o le faltan `MATHPIX_APP_ID`, `MATHPIX_APP_KEY` u
`OPENAI_API_KEY`, dilo explícitamente a Marcos y para aquí — copia `.env.example` a `.env` como
sugerencia, pero no inventes claves ni sigas sin ellas. Sin esto el pipeline falla fichero a fichero
de forma confusa; mejor cortar antes.

## 2. Decidir el alcance

Si Marcos ya ha dicho qué quiere indexar (una asignatura, una carpeta, "todo"), usa eso. Si no lo ha
dicho, pregúntaselo.

Comprueba si `index/manifest.json` existe todavía. Si **no existe** (primera ingesta real), recomienda
explícitamente empezar por una carpeta pequeña de una sola asignatura como piloto, en vez de lanzar los
261 PDFs de golpe — así se valida calidad de OCR/chunking y coste real antes de comprometer todo el
corpus. Si el manifest ya existe, no hace falta insistir en el piloto; puedes proceder con lo que pida.

## 3. Ejecutar el pipeline

Usa siempre el intérprete del entorno virtual del proyecto, nunca el Python del sistema:

```bash
.venv/bin/python ingest/run.py                                    # todo raw/
.venv/bin/python ingest/run.py --path "Estudio2carrera/1 cuatri/electrotecnia"   # una carpeta
.venv/bin/python ingest/run.py --force                            # reprocesa aunque no haya cambiado
```

La ruta de `--path` es relativa a `raw/`. El script ya es incremental por sí mismo — solo procesa
ficheros nuevos o modificados según el hash guardado en el manifest — así que no hace falta que tú
filtres manualmente qué ha cambiado.

## 4. Reportar el resultado

El script imprime un resumen final con nuevos / actualizados / sin cambios / fallos. Resume esto a
Marcos en una frase clara. Si hay fallos, indica cuáles ficheros fallaron y por qué (la causa suele
estar en la propia salida de consola: fichero corrupto, timeout de Mathpix, extensión no soportada).
No los reintentes automáticamente ni los ocultes.

## 5. Después de indexar

Si se indexó material nuevo de una asignatura que todavía no tiene carpeta en `wiki/`, menciónaselo a
Marcos y recuerda que se puede diagnosticar y empezar a poblar esa asignatura siguiendo el protocolo del
BLOQUE 7 de `CLAUDE.md` — pero no la crees tú automáticamente aquí; eso es trabajo del tutor en una
sesión de estudio, no de este skill.
