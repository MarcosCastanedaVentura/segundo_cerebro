# Segundo cerebro — Ingeniería Alimentaria

Un "segundo cerebro" académico construido siguiendo el patrón **LLM Wiki** (Karpathy): un wiki en markdown
interconectado por wikilinks, mantenido de forma incremental sesión a sesión por un agente de Claude Code, sobre el
que se apoya un **índice de búsqueda semántica (RAG) transversal a toda la carrera**.

La idea de fondo: en vez de que el conocimiento de cada asignatura muera en una carpeta al aprobar el examen,
construir un archivo vivo de toda la carrera — apuntes, exámenes, diapositivas — indexado y consultable, de forma
que un concepto de 2º curso pueda recuperarse sin fricción cuando hace falta en una asignatura de 4º.

## Arquitectura

**Principio de diseño no negociable: un único agente, un único índice.** La asignatura, el tema y la página son
metadata de cada fragmento de texto (chunk), nunca una partición del sistema — nada de un agente o una base de datos
distinta por asignatura. Es lo que permite que una pregunta de una asignatura recupere, sin fricción, contenido
de otra completamente distinta.

```
segundo_cerebro/
├── CLAUDE.md          # system prompt del tutor: identidad, metodología socrática, arquitectura
├── ingest/            # pipeline de ingesta agnóstico a asignatura
│   ├── extract.py     # PDF/imagen → texto, OCR de fórmulas vía MinerU (fórmulas/química a LaTeX)
│   ├── chunk.py        # chunking semántico por párrafo + metadata (asignatura, tema, curso, página)
│   ├── embed.py          # embeddings (OpenAI) + upsert incremental a la colección única de Chroma
│   └── run.py              # orquestación con manifest.json (hash SHA-256) — solo procesa lo nuevo/modificado
├── query/
│   └── retrieve.py       # búsqueda semántica con filtro opcional de metadata; solo recupera, no genera
├── wiki/               # conocimiento sintetizado, atómico, interconectado por wikilinks
│   ├── carrera/         # plan de estudios y dependencias entre asignaturas
│   └── <asignatura>/     # notas curadas por asignatura, una por concepto/fórmula/procedimiento
└── .claude/skills/     # /indexar (dispara la ingesta) y /estudiar (protocolo de inicio de sesión)
```

## Stack

- **Vector DB**: [Chroma](https://www.trychroma.com/), embebida y local — sin servidor, una única colección
  filtrable por metadata.
- **Embeddings**: OpenAI `text-embedding-3-small`.
- **OCR de fórmulas**: [MinerU](https://github.com/opendatalab/mineru) — local y gratis, conversión a LaTeX de
  notación matemática/química, sin depender de una API de pago. [Mathpix Convert API](https://mathpix.com/) queda
  documentada como upgrade opcional si en alguna asignatura la calidad de OCR se queda corta.
- **Interfaz**: Claude Code — sin backend ni frontend propios; el agente lee `wiki/` y consulta el índice
  directamente en la sesión.

## Sobre este repositorio

Este repo público incluye la arquitectura, el pipeline completo y las notas de contenido académico del wiki.
**No incluye** el perfil de aprendizaje personal ni el histórico de errores del estudiante (`wiki/perfil/`,
`memory/`) ni el material fuente (`raw/`, PDFs/apuntes escaneados) — esas partes existen y son las que hacen el
sistema realmente personal, pero se mantienen privadas fuera de este repositorio.
