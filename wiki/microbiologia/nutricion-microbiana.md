---
titulo: "Nutrición microbiana: clasificación nutricional y medios de cultivo"
asignatura: "microbiologia"
tema: "Tema 3 — Nutrición microbiana"
tipo: "concepto"
relacionado: ["crecimiento-microbiano", "bacterias-interes-alimentario", "control-microbiano-muerte-termica"]
patrones_error: [3, 4]
examen_relevancia: "alta"
fuente: ["tema 3-nutrición 25-26.pdf", "examenes/wuolah-free-RECOLECCION-PREGUNTAS-DESARROLLO-1o-PEP.pdf", "examenes/wuolah-free-Recuperación (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La nutrición microbiana clasifica a los microorganismos según **de dónde obtienen su carbono, su energía y sus electrones**. Esta clasificación no es decorativa: determina qué medio de cultivo hay que diseñar para aislar o seleccionar un grupo microbiano concreto, y qué vía metabólica (respiración aerobia, respiración anaerobia o fermentación) puede usar un microorganismo según el ambiente.

## Por qué / de dónde viene

Todo microorganismo necesita tres cosas para vivir: una fuente de **carbono** (para construir biomasa), una fuente de **energía** (para las reacciones), y un **aceptor final de electrones** (para reoxidar los transportadores reducidos, NADH → NAD⁺). La clasificación nutricional cruza estos tres ejes:

- Fuente de carbono: **autótrofo** (CO₂) vs **heterótrofo** (materia orgánica).
- Fuente de energía: **fotótrofo** (luz) vs **quimiótrofo** (reacciones químicas).
- Fuente de electrones: **litótrofo** (compuestos inorgánicos, ej. H₂S, Fe²⁺, NH₃) vs **organótrofo** (compuestos orgánicos).

La mayoría de bacterias de interés alimentario son **quimioheterótrofas** (energía y carbono de materia orgánica). El tipo de metabolismo depende de cuál sea el **aceptor final de electrones** disponible:
- **Respiración aerobia**: O₂ es el aceptor final → máximo rendimiento energético (ATP por fosforilación oxidativa completa).
- **Respiración anaerobia**: un aceptor inorgánico distinto del O₂ (NO₃⁻, SO₄²⁻, CO₂) → rendimiento intermedio.
- **Fermentación**: un intermediario orgánico de la propia ruta catabólica actúa como aceptor (ej. piruvato → lactato) → rendimiento energético bajo (solo fosforilación a nivel de sustrato), pero no depende de aceptores externos.

## Fórmula / procedimiento

Procedimiento para diseñar un medio de cultivo selectivo y diferencial (tal como se pide en examen):
1. **Fuente de carbono y energía** — un azúcar concreto (ej. lactosa para enterobacterias) que solo fermentan los microorganismos de interés.
2. **Fuente de nitrógeno** — peptona (medio complejo) o sales de amonio (medio definido).
3. **Factores de crecimiento** (si el microorganismo es auxótrofo para ellos) — vitaminas, aminoácidos que el microorganismo no puede sintetizar y debe recibir ya hechos (ej. vitamina B12).
4. **Agente selectivo** — inhibe el crecimiento de microorganismos no deseados (ej. sales biliares inhiben Gram positivas, dejando crecer enterobacterias Gram negativas).
5. **Indicador diferencial** — un colorante sensible a pH (rojo de fenol, rojo neutro) que cambia de color si el microorganismo fermenta el azúcar diferencial, distinguiendo subgrupos dentro de los que ya crecieron.
6. **Agente solidificante** — agar (no metabolizable por casi ningún microorganismo, por eso sirve de matriz inerte).

Un medio es **definido** si se conoce su composición cualitativa y cuantitativa exacta (todos los componentes son sustancias químicas puras) y **complejo** si incluye extractos no definidos (peptona, extracto de levadura, sangre).

## Ejemplo resuelto

*(Adaptado de la Recolección de preguntas de desarrollo del 1er parcial)*. Se pide diseñar un medio complejo, selectivo y diferencial para enterobacterias:

- Extracto de levadura → fuente de vitaminas/factores de crecimiento.
- Peptona → fuente de nitrógeno (medio complejo).
- Lactosa → fuente de carbono fermentable, diferencial.
- Sales biliares → selectivo, inhiben Gram positivas.
- Rojo de fenol → indicador de pH, vira si hay fermentación de lactosa (diferencial).
- Agar → solidificante.

Resultado: solo crecen bacterias Gram negativas tolerantes a sales biliares (selección), y entre ellas se distinguen visualmente (por el color) las que fermentan lactosa (ej. *E. coli*, colonias rojas/rosadas) de las que no (ej. *Salmonella*, colonias incoloras).

Segundo ejemplo (medio: Glucosa 5 g/L, K₂HPO₄ 2 g/L, (NH₄)₂SO₄ 1 g/L, FeSO₄ 0,5 g/L, vitamina B12): es un medio **definido** (composición exacta conocida); los microorganismos que crecen en él son **quimioheterótrofos** (glucosa como fuente de C y energía); en presencia de O₂ hacen respiración aerobia (aceptor final O₂), en ausencia pueden fermentar (aceptor un intermediario de la ruta) o hacer respiración anaerobia usando sulfato como aceptor externo; la vitamina B12 es el factor de crecimiento del medio.

## Conexión con otros conceptos

- [[crecimiento-microbiano]] — el tipo de metabolismo disponible (respiración vs fermentación) determina el rendimiento energético y por tanto la velocidad de crecimiento.
- [[bacterias-interes-alimentario]] — cada grupo bacteriano de interés alimentario se caracteriza precisamente por su categoría nutricional y tipo de metabolismo (ej. bacterias del ácido láctico = quimioheterótrofas, fermentadoras).
- [[control-microbiano-muerte-termica]] — el pH y aw del medio (relacionados con el diseño de medios) son los mismos factores que se usan para el control microbiano en alimentos.
- [[../bioquimica/MOC]] — la ruta catabólica de la glucosa (Embden-Meyerhof, pentosas fosfato, Entner-Doudoroff) es contenido de bioquímica que aquí se aplica a clasificar fermentaciones.

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmulas sin verificar condiciones)**: antes de decidir si un microorganismo respira o fermenta hay que comprobar primero qué aceptores de electrones están disponibles en el medio y si el organismo es aerobio estricto, anaerobio estricto o anaerobio facultativo — no asumir automáticamente "hay glucosa → fermenta".

**Patrón 4 (confundir cocientes/relaciones parecidas)**: fácil confundir aceptor de electrones con fuente de energía o con fuente de carbono cuando aparecen en la misma tabla del examen (ver tabla de clasificación nutricional del examen de recuperación 2023-2024) — conviene verbalizar los tres ejes por separado antes de rellenar cualquier tabla.

## Relevancia en examen

Alta. Aparece de forma recurrente tanto en el test (identificar categoría nutricional de un microorganismo a partir de su medio) como en desarrollo: diseño de medios de cultivo complejos/selectivos/diferenciales, completar tablas de clasificación nutricional-relación con O₂-tipo de metabolismo a partir de la composición de un medio (examen de recuperación 2023-2024, pregunta 8), y preguntas conceptuales sobre medio definido vs complejo y factores de crecimiento.
