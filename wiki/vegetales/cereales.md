---
titulo: "Cereales: morfología, ciclo, componentes del rendimiento y nutrición (Tema 2)"
asignatura: "vegetales"
tema: "UT2 - Cereales"
tipo: "concepto"
relacionado: ["agua-en-sistemas-agricolas", "semillas", "cebada", "cultivo-del-trigo", "../geomatica/MOC"]
patrones_error: [3, 4, 6]
examen_relevancia: "alta"
fuente: ["raw/.../vegetales/Tema 2 Cereales (1) Introducción y morfología de la planta PMPOV 2026.pdf", "raw/.../vegetales/Tema 2 Cereales (2) Crecimiento y rendimiento PMPOV 2026.pdf", "raw/.../vegetales/Tema 2 Cereales (3) Exigencias nutricionales y abonado PMPOV2026.pdf", "raw/.../vegetales/apuntes_claude/vegetales_guia_v2.docx", "raw/.../vegetales/apuntes_claude/vegetales_guia_bloques.docx (veg_guide.js)"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Los cereales son monocotiledóneas de la familia **Poáceas/Gramíneas** (trigo y cebada: subfamilia Pooideae; maíz, sorgo, mijo: Panicoideae; arroz: Bambusoideae). Son la base de la alimentación humana desde el Neolítico: ricos en glúcidos (energía), con proteína apreciable pero pobre en lisina, y con fibra (celulosa, beta-glucanos). Ocupan el **52% de la superficie agrícola mundial** (730 Mha) y producen ~3.000 Mt/año de grano (63% de la producción agrícola vegetal mundial en materia seca). En España ocupan 6 Mha (34% de las tierras de cultivo), siendo cebada y trigo los mayoritarios; la alternativa tradicional en secano es barbecho/cereal (43% de la superficie cultivada total).

## Por qué / de dónde viene

**Morfología**: sistema radicular **fasciculado** (raíces seminales de la semilla, funcionales hasta el ahijado, más raíces adventicias/nodales que nacen del nudo de ahijamiento — puede alcanzar 10-25 km de raíces por m² de suelo y hasta 2 m de profundidad). Tallo en **caña hueca** con 6-8 entrenudos, porte bajo en variedades modernas (<1 m). Hojas alternas con vaina + limbo + lígula + aurículas (la forma de estas últimas identifica la especie: cebada con aurículas grandes y con cilios, trigo con aurículas pequeñas sin pelos, avena sin aurículas). Inflorescencia en **espiga** (espiguillas insertadas directamente en el raquis: trigo, cebada, centeno) o **panícula** (espiguillas unidas por un pedúnculo: avena, arroz, maíz). El grano es un fruto en **cariópside** (pericarpio soldado a la testa) — ver [[semillas]] para la anatomía completa del grano.

**Ciclo de cultivo**: Germinación-nascencia → Ahijado (emisión de tallos hijos desde el nudo de ahijamiento; define el número potencial de espigas) → Encañado (elongación de entrenudos; en su transición con el ahijado ocurre la diferenciación floral, estado "doble arruga") → Espigado (emergencia de la espiga tras la fase "espiga en zurrón") → Maduración del grano (estados acuoso → lechoso → pastoso → grano duro, con tres fases: proliferación celular del endospermo ~10 días, expansión/acumulación de reservas ~30 días, cese del crecimiento ~5 días).

**Componentes del rendimiento** — se fijan en fases sucesivas y no compensables entre sí una vez pasada su ventana:
- **Nº espigas/m² (NE)**: se define en el ahijado; depende de densidad de siembra y de que el tallo hijo alcance >1/3 de la longitud del principal para desarrollar espiga fértil. Es el componente con **mayor correlación con el rendimiento final** (el más preguntado).
- **Nº granos/espiga (NG)**: se define entre ahijado y espigado; sensible a competencia entre órganos, temperatura, estrés hídrico y N.
- **Peso del grano (PG)**: se fija en la maduración; PG = Pi + R·D (peso inicial + velocidad de crecimiento del grano × duración de la fase de expansión). En el llenado, el 70% de los fotoasimilados provienen de aristas/pedúnculo, el 20% de la hoja bandera y el 10% de retranslocación de reservas (que puede llegar al 50% bajo estrés).

RTO (kg/ha) = NE × NG × PG.

**Nutrición**: absorción en forma iónica de la solución del suelo. Macronutrientes primarios N-P-K, secundarios Ca-Mg-S, micronutrientes Fe-Cu-B etc. El N del suelo está mayoritariamente en forma **orgánica** (no disponible directamente); se mineraliza a amonio (NH₄⁺) y se nitrifica a nitrato (NO₃⁻, la forma que absorbe mayoritariamente la raíz, ligada al flujo de agua) — trampa de examen: el N del suelo NO está solo en amonio+nitrato, el reservorio mayor es orgánico. La absorción de N por el cultivo sigue el patrón de acumulación de biomasa: ~15% en siembra-ahijado, ~75% en ahijado-espigado, ~10% en maduración.

## Fórmula / procedimiento

- RTO = NE × NG × PG (componentes del rendimiento).
- Tiempo térmico = temperatura media × tiempo (constante para cada fase fenológica; Tb cebada = 0°C).
- Absorción de nutrientes por tonelada de grano (cebada, kg/t): N 24-28, P₂O₅ 10-12, K₂O 19-35, CaO 10, MgO 5,2, S 4,1.
- Función de producción-nitrógeno: relación curvilínea entre dosis de N y rendimiento (parábola con máximo); ej. y = −0,0709x² + 21,856x + 3557 (cebada) — el máximo se halla igualando a 0 la derivada.
- Fertilización: dosis en fondo (P, K y parte del N con urea/sulfato amónico) + cobertera (N en ahijado-espigado, período de mayor demanda, con nitrato amónico).

## Ejemplo resuelto

Rendimiento máximo con la función y = −0,0709x² + 21,856x + 3557: derivada y' = −0,1418x + 21,856 = 0 → x = 154 kg N/ha; sustituyendo, y = 5.241 kg/ha. Es decir, para maximizar el rendimiento de este cultivo de cebada hace falta abonar con 154 kg N/ha, y sin abonar (x=0) se obtendrían 3.557 kg/ha (procedentes del N residual del suelo y de la mineralización).

Cálculo de absorción de N: si el rendimiento es 4.000 kg/ha (4 t/ha) y la absorción es 25 kg N/t → N absorbido = 4 × 25 = 100 kg N/ha.

## Conexión con otros conceptos

- Aplica directamente a [[cebada]] y [[cultivo-del-trigo]], que comparten esta morfología y ciclo pero difieren en número de espiguillas/nudo (trigo: 1 espiguilla con 3+ flores; cebada: 3 espiguillas con 1 flor cada una) y en destino industrial (malta/pienso vs. harina/pasta).
- El balance hídrico y PAR de [[agua-en-sistemas-agricolas]] es la base física del crecimiento y del cálculo de biomasa/rendimiento aquí.
- La estimación de N absorbido y del estado nutricional mediante NDVI/sensores remotos (mencionada en la práctica de remolacha) conecta con [[../geomatica/MOC]].

## Errores frecuentes de Marcos aquí

- **Patrón 3**: aplicar la fórmula del componente de rendimiento sin identificar antes en qué fase del ciclo se determina cada uno (NE en ahijado, NG en espigado, PG en maduración) — sin ese anclaje temporal es fácil atribuir un factor de estrés al componente equivocado.
- **Patrón 4**: confundir "espiga" con "espiguilla" con "flor" — son tres niveles jerárquicos distintos (espiga > espiguilla > flor) y el examen pregunta explícitamente cuántas espiguillas hay por nudo y cuántas flores por espiguilla en cada cereal.
- **Patrón 6**: en ejercicios de función de producción-nitrógeno, copiar mal el signo de los coeficientes de la parábola (el coeficiente de x² es negativo) invalida todo el cálculo del máximo.

## Relevancia en examen

Bloque troncal de UT2, con presencia constante: preguntas V/F sobre estadísticas mundiales (mayor superficie = trigo, mayor producción = maíz, mayor rendimiento medio = maíz, principal productor = China, principal exportador = EEUU — China NO exporta, es importador neto), sobre morfología (aurículas, tipos de inflorescencia) y un **ejercicio práctico** casi siempre presente con PAR/EUR/rendimiento por componentes y densidad de siembra (semillas/m² × %germinación × %nascencia = plantas/m²).
