---
titulo: "Crecimiento microbiano: curva de crecimiento y cinéticas"
asignatura: "microbiologia"
tema: "Tema 4 — Crecimiento microbiano"
tipo: "formula"
relacionado: ["nutricion-microbiana", "control-microbiano-muerte-termica", "bacterias-interes-alimentario"]
patrones_error: [3, 4, 7]
examen_relevancia: "alta"
fuente: ["Tema 4 crecimiento 25-26.pdf", "problemas crecimiento.pdf", "examenes/wuolah-free-Recuperación (2023-2024).pdf", "examenes/wuolah-free-Examen 2º Parcial (2024-2025).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El crecimiento microbiano es el aumento del número de células de una población (no del tamaño de una célula individual). En cultivo cerrado (batch), sigue una **curva de crecimiento** con 4 fases: latencia, exponencial (logarítmica), estacionaria y muerte. La cinética de crecimiento describe matemáticamente la fase exponencial, que es la única con crecimiento a velocidad constante y predecible.

## Por qué / de dónde viene

- **Fase de latencia**: el inóculo se adapta al nuevo medio (sintetiza enzimas, repone reservas) — no hay división neta todavía. Su duración depende de la "historia" del inóculo: si viene de fase exponencial y de un medio similar, la latencia es corta o nula.
- **Fase exponencial**: cada célula se divide en dos con un intervalo de tiempo constante (tiempo de generación, *g*). El número de células crece geométricamente porque cada división duplica la población entera, no solo suma una célula.
- **Fase estacionaria**: se agotan nutrientes o se acumulan productos tóxicos/metabolitos inhibidores; la tasa de división iguala a la tasa de muerte, así que el número neto de células viables se estabiliza.
- **Fase de muerte**: los recursos son insuficientes para mantener el metabolismo; la mortalidad supera a la división, y el descenso también es habitualmente exponencial (relevante para el control microbiano, ver [[control-microbiano-muerte-termica]]).

## Fórmula / procedimiento

Durante la fase exponencial, la velocidad específica de crecimiento (μ) se define a partir del logaritmo neperiano del número de células:

**μ = (ln N − ln N₀) / (t − t₀)**

donde:
- N₀ = número (o concentración) de células al tiempo t₀ (inicio del intervalo, normalmente el final de la latencia).
- N = número de células al tiempo t.
- μ = velocidad específica de crecimiento (unidades: h⁻¹ o min⁻¹).

El **tiempo de generación** (g), tiempo que tarda la población en duplicarse, se relaciona con μ mediante:

**g = ln 2 / μ ≈ 0,693 / μ**

Para calcular μ y g correctamente hay que **descontar la fase de latencia** del intervalo de tiempo total (usar t − t₀ donde t₀ es el final de la latencia, no el instante de la inoculación).

## Ejemplo resuelto

*(Adaptado del examen de recuperación 2023-2024, pregunta 3)*. Un caldo de cultivo parte de N₀ = 10² cél/mL y tras 7 horas alcanza N = 1,6·10³ cél/mL. La fase de latencia dura 1 hora, así que el intervalo de crecimiento exponencial real es (7 − 1) = 6 horas.

μ = (ln 1,6·10³ − ln 10²) / 6 = (7,377 − 4,605) / 6 = 2,772 / 6 ≈ **0,462 h⁻¹**

g = ln 2 / μ = 0,693 / 0,462 ≈ **1,5 horas**

La fase de latencia se puede eliminar o acortar inoculando con células que ya estén en fase exponencial y usando condiciones óptimas de cultivo (pH, temperatura, nutrientes, O₂) idénticas a las del cultivo de origen.

## Conexión con otros conceptos

- [[nutricion-microbiana]] — el tipo de metabolismo disponible (respiración vs fermentación) condiciona directamente el valor de μ: la respiración aerobia suele dar μ mayores que la fermentación por su mayor rendimiento energético.
- [[control-microbiano-muerte-termica]] — la fase de muerte por agotamiento de nutrientes sigue la misma lógica exponencial que la muerte térmica inducida por calor (ambas se describen con logaritmos y reducciones decimales), pero **no deben confundirse**: una es muerte natural por inanición, la otra es letalidad inducida y se mide con valores D.
- [[bacterias-interes-alimentario]] — los factores ambientales (temperatura, aw, pH, O₂) que aceleran o frenan μ son los mismos que definen los rangos de crecimiento de cada género bacteriano de interés alimentario (psicrótrofos, mesófilos, termófilos).

## Errores frecuentes de Marcos aquí

**Patrón 3 (aplicar fórmulas sin verificar antes las condiciones)**: usar el intervalo de tiempo total del experimento en vez de restar la fase de latencia antes de calcular μ, lo que da un μ artificialmente bajo. Siempre hay que identificar primero t₀ real (fin de latencia) antes de aplicar la fórmula.

**Patrón 4 (confundir cocientes relacionados)**: confundir μ (velocidad específica) con g (tiempo de generación) — son inversamente relacionados vía ln 2, no lo mismo. Verbalizar siempre "μ es una velocidad (unidades 1/tiempo), g es un tiempo" antes de sustituir.

**Patrón 7 (dar por bueno un número que "suena razonable")**: comprobar siempre que μ tenga signo positivo y unidades coherentes (h⁻¹), y que g sea del orden de minutos-horas para bacterias (no días), como chequeo de orden de magnitud.

## Relevancia en examen

Alta. Es un tipo de problema numérico que aparece en prácticamente todos los parciales/finales revisados: cálculo de μ y g a partir de N₀, N y tiempo (con o sin fase de latencia dada), y preguntas conceptuales sobre cómo eliminar/acortar la latencia. También se combina con preguntas sobre factores intrínsecos/extrínsecos que afectan al crecimiento de un alimento concreto (ej. carne picada en refrigeración, examen 2º parcial 2024-2025).
