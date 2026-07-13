---
titulo: "Bioquímica"
slug: "bioquimica"
semestre: "3º"
creditos: 6
tipo: "Básica"
estado: "EN_PROGRESO"
ultima_actualizacion: "2026-07-12"
---

# Bioquímica — Mapa de contenidos

Ver estado dinámico y % de dominio real de Marcos en [`memory/memory.json`](../../memory/memory.json).

## Dependencias

Requiere Química General y Aplicada ([[../quimica/MOC]]) — enlace de aminoácidos, ionización ácido-base,
enlace glicosídico y termodinámica química. Es base directa de Microbiología Alimentaria
([[../microbiologia/MOC]]) — fermentación láctica/alcohólica, técnicas de biología molecular para detección de
patógenos y trazabilidad —, y de Análisis de Alimentos y de la tecnología de industrias específicas (láctea,
cárnica, cereales, enológica). Ver [[../carrera/dependencias]].

## Temario y notas

- **Tema 1 — Introducción a la bioquímica y repaso de las moléculas**
  - [[biomoleculas-glucidos-lipidos]]
  - [[aminoacidos-y-estructura-proteica]]
- **Tema 2 — Enzimas**
  - [[enzimas-estructura-funcion]]
  - [[cinetica-michaelis-menten]]
  - [[inhibicion-enzimatica]]
  - [[regulacion-enzimatica-alosterica]]
- **Tema 3 — Bioenergética. Panorámica del metabolismo**
  - [[termodinamica-bioenergetica]]
  - [[atp-compuestos-alta-energia]]
- **Tema 4 — Metabolismo de glúcidos**
  - [[glucolisis]]
  - [[gluconeogenesis]]
  - [[ruta-pentosas-fosfato]]
- **Tema 5 — Metabolismo oxidativo**
  - [[ciclo-krebs]]
  - [[cadena-transporte-electrones-fosforilacion-oxidativa]]
- **Tema 6 — Metabolismo de lípidos**
  - [[metabolismo-lipidos-beta-oxidacion]]
  - [[biosintesis-acidos-grasos]]
  - [[cuerpos-cetonicos]]
- **Tema 7 — Metabolismo de aminoácidos y ácidos nucleicos**
  - [[metabolismo-aminoacidos-nitrogeno]]
  - [[ciclo-alanina-glucosa-cahill]]
- **Tema 8 — Ácidos nucleicos: estructura, propiedades y función**
  - [[estructura-acidos-nucleicos]]
- **Tema 9 — Ácidos nucleicos: flujo de la información genética**
  - [[replicacion-adn]]
  - [[transcripcion-y-traduccion]]
- **Tema 10 — Técnicas de Biología Molecular aplicadas a la Industria Alimentaria**
  - [[tecnicas-biologia-molecular]]

## Prácticas

No hay carpeta de prácticas de laboratorio separada en `raw/`; las clases de problemas están integradas como
fuente de ejemplos dentro de las notas de teoría correspondientes:
- Clase de problemas de cinética → ejemplos en [[cinetica-michaelis-menten]] e [[inhibicion-enzimatica]].
- Problemas Enzimas resueltos / Problemas Enzimas II resuelto → ejemplos numéricos completos en
  [[cinetica-michaelis-menten]] e [[inhibicion-enzimatica]].
- Problemas de Metabolismo 2 y Preguntas metabolismo glúcidos y oxidativo 1 → ejemplos distribuidos en
  [[ciclo-krebs]], [[cadena-transporte-electrones-fosforilacion-oxidativa]], [[glucolisis]],
  [[gluconeogenesis]] y [[ruta-pentosas-fosfato]].
- El Tema 10 menciona explícitamente una "Práctica 3" de electroforesis y PCR cuyo guion no está en `raw/`
  todavía (ver más abajo).

## Exámenes

Ver [`examenes.md`](examenes.md) para el análisis completo de qué cae y con qué frecuencia. Resumen: la
cinética enzimática con inhibición, el ciclo de la alanina-glucosa (Cahill), la hidrólisis ortofosfatolítica
del ATP y la tabla de rutas metabólicas (Krebs/gluconeogénesis/glucólisis/cadena de transporte/β-oxidación)
aparecen prácticamente en todas las convocatorias revisadas (2022-23 a 2023-24). El Tema 10 (técnicas
moleculares) no ha aparecido en ningún examen teórico completo revisado.

## Material sin procesar todavía

Todo el contenido textual de `raw/Estudio2carrera/1 cuatri/bioquimica/` ha sido leído y sintetizado en las
notas de arriba. Quedan sin sintetizar como notas propias (por ser material de ejercicios ya usado como
fuente de ejemplos dentro de otras notas, no por no haberse leído):

- `Clase de problemas de cinética.pdf` — leído completo (solo 1 ejercicio corto); ejemplo incorporado en
  [[cinetica-michaelis-menten]].
- `Problemas Enzimas resueltos.pdf` y `Problemas Enzimas II resuelto.pdf` (esta última es un documento
  escaneado a mano, examen de junio 2012) — leídos completos; ejemplos numéricos incorporados en
  [[cinetica-michaelis-menten]] e [[inhibicion-enzimatica]].
- `Problemas de Metabolismo 2.pdf` y `Preguntas metabolismo glucidos y oxidativo 1.pdf` — leídos completos;
  ejercicios distribuidos como ejemplos en las notas de metabolismo correspondientes (no se ha creado una
  nota "problemas.md" aparte para no duplicar contenido ya integrado).
- Los 6 documentos de `examenes/` están analizados en [[examenes.md]]; no se han creado notas 1:1 por examen
  porque su contenido (mismas preguntas repetidas) ya está distribuido en las notas de concepto y en el
  análisis agregado de exámenes.

No hay en esta carpeta de `raw/` apuntes manuscritos, fotos ni vídeo aparte de los enlaces a YouTube
incrustados en los PDFs de teoría (no descargados ni transcritos) — si Marcos pregunta por el contenido de
alguno de esos vídeos, decirlo explícitamente y ofrecer verlo/transcribirlo bajo demanda en vez de inventar
su contenido.
