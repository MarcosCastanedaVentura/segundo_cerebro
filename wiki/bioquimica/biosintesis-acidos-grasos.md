---
titulo: "Biosíntesis de ácidos grasos: acetil-CoA carboxilasa y ácido graso sintasa"
asignatura: "bioquimica"
tema: "Tema 6 - Metabolismo de lípidos"
tipo: "procedimiento"
relacionado: ["metabolismo-lipidos-beta-oxidacion", "regulacion-enzimatica-alosterica", "gluconeogenesis"]
patrones_error: [3]
examen_relevancia: "media"
fuente: ["Tema 6.pdf", "examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

La biosíntesis de ácidos grasos (lipogénesis) ocurre en el citosol (en animales, sobre todo hígado, tejido
adiposo y glándula mamaria; en plantas, en el cloroplasto) y **no es la inversión de la β-oxidación**: usa
enzimas completamente distintos y un precursor de 3 carbonos (malonil-CoA) en vez de acetil-CoA directamente.

## Por qué / de dónde viene

Igual que la gluconeogénesis no es la glucólisis invertida (ver [[gluconeogenesis]]), la síntesis de ácidos
grasos evita usar las reacciones de la β-oxidación a la inversa porque termodinámicamente eso no sería
favorable de forma espontánea en ambos sentidos con los mismos enzimas. En su lugar, la célula "activa" el
acetil-CoA carboxilándolo a malonil-CoA (gasto de ATP) para dar a la reacción de condensación un empuje
termodinámico adicional (pérdida de CO2 en el paso de condensación), y usa NADPH en vez de NADH/FADH2 como
poder reductor (el NADPH proviene de la ruta de las pentosas fosfato o del enzima málico). Necesita además un
sistema de "lanzadera" para sacar el acetil-CoA de la matriz mitocondrial (donde se genera) al citosol (donde
se sintetizan los ácidos grasos), porque la membrana mitocondrial interna no es permeable al acetil-CoA.

## Fórmula / procedimiento

**Paso regulador clave — formación de malonil-CoA:**
Acetil-CoA + CO2 + ATP → Malonil-CoA + ADP + Pi, catalizada por **acetil-CoA carboxilasa (ACC)**, el enzima
regulador más importante de la ruta:
- Regulación alostérica: activada por citrato y acetil-CoA; inhibida por palmitoil-CoA (producto final).
- Regulación covalente (hormonal): glucagón/adrenalina (glucosa en sangre baja) → fosforilación → **inactiva**
  la ACC → favorece la β-oxidación. Insulina (glucosa alta) → desfosforilación → activa la ACC.

**Complejo ácido graso sintasa** (multienzimático, con dos sitios: KS y ACP):
1. Se carga el sitio KS con un grupo acetilo (desde acetil-CoA).
2. Se carga el sitio ACP con un grupo malonilo (desde malonil-CoA).
3. Condensación (con pérdida de CO2, gasto de ATP indirecto vía la carboxilación previa) → cadena C4.
4. Reducción (NADPH) → hidroxiacil.
5. Deshidratación (−H2O) → enoil.
6. Reducción (NADPH) → acil saturado.

El ciclo se repite añadiendo malonil-CoA cada vez (elongación de 2 en 2 carbonos) hasta llegar a **palmitato
(16:0)**, momento en el que se abandona el ciclo. Elongación posterior y desaturación (introducción de dobles
enlaces hasta el C9, nunca más allá — de ahí que linoleico y linolénico sean esenciales) ocurren en enzimas
del retículo endoplasmático.

**Balance de la síntesis de palmitato**: 8 Acetil-CoA + 14 NADPH + 7 ATP → Palmitato + 14 NADP⁺ + 8 CoA +
7 ADP + 7 Pi + 7 CO2.

## Ejemplo resuelto

*Adaptado de examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf, pregunta 3a.* Acetil-CoA carboxilasa:
sustratos = Acetil-CoA, ATP, bicarbonato (HCO3⁻); productos = Malonil-CoA, ADP, Pi; localización = citosol;
ruta = síntesis de ácidos grasos (lipogénesis). Es el enzima que "activa" el 2-carbonos acetilo a un
3-carbonos malonilo, gastando el equivalente de un ATP por cada 2 carbonos que se van a añadir a la cadena en
crecimiento — de ahí que sintetizar 1 palmitato (16C = 8 unidades de acetilo) cueste 7 ATP (7 carboxilaciones,
la primera unidad de acetilo no se carboxila, se carga directamente en el sitio KS).

## Conexión con otros conceptos

- [[metabolismo-lipidos-beta-oxidacion]]: ruta opuesta en compartimento (mitocondria vs citosol) y en
  regulación cruzada (malonil-CoA inhibe CAT-I).
- [[gluconeogenesis]]: mismo patrón conceptual — una ruta anabólica no es la simple inversión de la
  catabólica correspondiente, usa enzimas y reguladores propios.
- [[regulacion-enzimatica-alosterica]]: ACC es un buen ejemplo de doble regulación (alostérica + covalente).

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): asumir que la síntesis usa los mismos pasos
que la β-oxidación en sentido inverso (mismo NADH/FADH2, misma localización) es el error conceptual más
grave posible en este tema — la síntesis usa NADPH (no NADH/FADH2) y ocurre en el citosol (no en la
mitocondria). Antes de responder, verificar explícitamente si la pregunta es sobre síntesis o degradación.

## Relevancia en examen

**Media-alta.** La tabla de rutas metabólicas con "Biosíntesis de ácidos grasos" (anabólica, citosol,
sustratos acetil-CoA+NADPH, productos ácidos grasos) aparece en varios exámenes. Formular sustratos/productos
de acetil-CoA carboxilasa aparece explícitamente en examenes/wuolah-free-Ejercicios-examen-bioquimica.pdf y
en la recuperación 2023-2024. La pregunta "por qué no ocurren a la vez β-oxidación y síntesis" (regulación
por malonil-CoA sobre CAT-I) es recurrente.
