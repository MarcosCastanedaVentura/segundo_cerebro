---
titulo: "Glucólisis: etapas, rendimiento energético y destino del piruvato"
asignatura: "bioquimica"
tema: "Tema 4 - Metabolismo de glúcidos"
tipo: "procedimiento"
relacionado: ["gluconeogenesis", "ciclo-krebs", "regulacion-enzimatica-alosterica", "atp-compuestos-alta-energia", "ciclo-alanina-glucosa-cahill"]
patrones_error: [3, 6]
examen_relevancia: "alta"
fuente: ["Tema 4 -Met de Glucidos.pdf", "Preguntas metabolismo glucidos y oxidativo 1.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Examen final (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La glucólisis (glykos=dulce, lysis=rotura) es la ruta central y universal (presente en todas las células) de
degradación de la glucosa: en 10 reacciones enzimáticas transforma una molécula de glucosa (6C) en dos de
piruvato (3C), ocurre siempre en el citosol, y funciona tanto en presencia como en ausencia de oxígeno. Es la
puerta de entrada de la glucosa al metabolismo energético y a la vez fuente de precursores biosintéticos.

## Por qué / de dónde viene

Es una ruta muy antigua evolutivamente (anterior a la fotosíntesis y por tanto al oxígeno atmosférico), lo
que explica por qué no necesita O2 para funcionar. Se organiza en dos fases con lógica opuesta: una **fase
preparativa** (reacciones 1-5) que consume 2 ATP para "activar" la glucosa por fosforilación y romperla en
dos triosas fosfato, y una **fase de generación de energía** (reacciones 6-10) que oxida esas triosas y
recupera esa inversión con creces, generando 4 ATP y 2 NADH. El NADH generado debe reoxidarse a NAD⁺ para que
la ruta no se bloquee (el sustrato de la reacción 6 se agotaría); en condiciones aeróbicas eso ocurre en la
cadena respiratoria, y en anaerobiosis mediante fermentación — de ahí que el destino del piruvato dependa
directamente de la disponibilidad de oxígeno.

## Fórmula / procedimiento

**Fase I (preparativa, 5 reacciones, consume 2 ATP):**
1. Glucosa → Glucosa-6-P (hexoquinasa/glucoquinasa, ATP-dependiente, irreversible, ΔG0'=−16,7 kJ/mol)
2. Glucosa-6-P ⇌ Fructosa-6-P (fosfoglucoisomerasa, reversible)
3. Fructosa-6-P → Fructosa-1,6-bisP (PFK-1, ATP-dependiente, irreversible, ΔG0'=−22,2 kJ/mol — **principal
   punto de regulación de la ruta**, enzima alostérico)
4. Fructosa-1,6-bisP → Gliceraldehído-3-P (G3P) + Dihidroxiacetona-P (aldolasa)
5. Dihidroxiacetona-P ⇌ G3P (triosa fosfato isomerasa) — de aquí en adelante todo × 2

**Fase II (de generación de energía, 5 reacciones, × 2 porque hay 2 triosas):**
6. G3P → 1,3-bisfosfoglicerato (G3P deshidrogenasa; oxidación + fosforilación; genera NADH)
7. 1,3-bisfosfoglicerato → 3-fosfoglicerato + **ATP** (fosfoglicerato quinasa — 1ª fosforilación a nivel de
   sustrato)
8. 3-fosfoglicerato ⇌ 2-fosfoglicerato (fosfoglicerato mutasa)
9. 2-fosfoglicerato → fosfoenolpiruvato (enolasa, deshidratación)
10. Fosfoenolpiruvato → Piruvato + **ATP** (piruvato quinasa, irreversible, enzima alostérico — 2ª
    fosforilación a nivel de sustrato)

**Balance global**: Glucosa + 2 ADP + 2 Pi + 2 NAD⁺ → 2 Piruvato + **2 ATP netos** + 2 NADH + 2 H⁺ + 2 H₂O
(se gastan 2 ATP en fase I y se generan 4 en fase II).

**Destino del piruvato:**
- Aeróbico (respiración): descarboxilación oxidativa a acetil-CoA → ciclo de Krebs → alto rendimiento
  energético (ver [[ciclo-krebs]]).
- Anaeróbico (fermentación): sin oxidación neta, rendimiento bajo (2 ATP/glucosa).
  - Fermentación láctica: piruvato → lactato (lactato deshidrogenasa), regenera NAD⁺. Importante en
    eritrocitos y músculo en ejercicio intenso; base industrial de yogur, queso, kéfir.
  - Fermentación alcohólica: piruvato → acetaldehído (descarboxilación) → etanol (reducción por NADH); base
    de bebidas alcohólicas y panificación.

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-Examen final (2023-2024).pdf, pregunta 4.* Oxidación completa de una
molécula de glucosa, con NADH=3 ATP y FADH2=2 ATP (factores de conversión clásicos usados en el examen, ver
nota en [[cadena-transporte-electrones-fosforilacion-oxidativa]] sobre el valor más moderno 2,5/1,5):

- Glucólisis: 2 ATP netos + 2 NADH (2×3=6 ATP) = 8 ATP "equivalentes"
- Piruvato → Acetil-CoA (×2): 2 NADH (2×3=6 ATP)
- Ciclo de Krebs (×2 vueltas): 2 GTP (2 ATP) + 6 NADH (6×3=18 ATP) + 2 FADH2 (2×2=4 ATP)
- **Total: 2+6+6+2+18+4 = 38 ATP**

## Conexión con otros conceptos

- [[gluconeogenesis]]: ruta inversa (no literalmente, usa 3 enzimas distintos en los pasos irreversibles),
  regulada de forma recíproca.
- [[ciclo-krebs]] y [[cadena-transporte-electrones-fosforilacion-oxidativa]]: destino aeróbico del piruvato y
  del NADH generado.
- [[regulacion-enzimatica-alosterica]]: PFK-1 y piruvato quinasa son los enzimas alostéricos clave de esta
  ruta (PFK-1 activada por AMP y fructosa-2,6-bisfosfato, inhibida por ATP y citrato).
- [[ciclo-alanina-glucosa-cahill]]: conecta el piruvato de la glucólisis muscular con el metabolismo hepático
  del nitrógeno.
- Conexión con Microbiología Alimentaria: fermentación láctica y alcohólica industrial (yogur, queso, vino,
  cerveza, pan) — ver [[../microbiologia/MOC]], relación directa según [[../carrera/dependencias]].

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones): los 3 pasos irreversibles de la glucólisis
(hexoquinasa, PFK-1, piruvato quinasa) son precisamente los que cambian de enzima en la gluconeogénesis — si
no se identifica primero cuál de los 10 pasos se está preguntando, es fácil aplicar el enzima o el ΔG0' de la
ruta equivocada.

**Patrón 6** (copiar mal los datos): en el balance de ATP es fácil olvidar que la fase I "gasta" 2 ATP antes
de que la fase II empiece a "generar" — copiar solo el resultado neto sin verificar el desglose lleva a
errores al preguntar por el ATP generado en una fase concreta.

## Relevancia en examen

**Alta.** La tabla de rutas metabólicas (tipo de ruta, localización, sustratos, productos) que incluye
Glucólisis aparece en los 4 exámenes/hojas de ejercicios revisados. El esquema completo de oxidación de
glucosa con el balance de 38 ATP aparece también en los 4. Formular sustratos/productos/localización de
enzimas concretos de la glucólisis (hexoquinasa, PFK-1, GAPDH, piruvato quinasa) es recurrente.
