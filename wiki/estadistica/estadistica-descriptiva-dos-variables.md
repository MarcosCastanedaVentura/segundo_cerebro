---
titulo: "Estadística descriptiva de dos variables (correlación)"
asignatura: "estadistica"
tema: "Tema 1.2 — Distribuciones de dos caracteres"
tipo: "concepto"
relacionado: ["estadistica-descriptiva-una-variable", "probabilidad-propiedades"]
patrones_error: []
examen_relevancia: "media"
fuente: ["Tema1.2_Distribucion2caracteres25-26_moodle-2.pdf", "EstadisticaDescriptiva_2caracteres-2.pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Cuando se miden **dos caracteres A y B** sobre los mismos individuos (ej. valor energético y contenido en azúcar de
un alimento), la información se organiza en una **tabla de doble entrada**: filas = modalidades de A, columnas =
modalidades de B, y cada celda Nᵢⱼ = número de individuos que caen en la modalidad Iᵢ de A **y** Jⱼ de B a la vez.
De esta tabla conjunta se derivan tres tipos de distribuciones de una sola variable: marginales, condicionadas, y
las medidas de relación entre ambas (covarianza y correlación).

## Por qué / de dónde viene

Estudiar A y B por separado (marginales) pierde la información de cómo se relacionan. Estudiar A solo dentro de un
subgrupo fijado de B (condicionada) permite ver si esa relación existe. Y reducir esa relación a un único número
(correlación) permite cuantificar si es lineal, y en qué sentido.

## Fórmula / procedimiento

**Distribución marginal de A** (colapsando B): Nᵢ. = Σⱼ Nᵢⱼ, fᵢ. = Nᵢ./N — es la tabla de frecuencias de A ignorando
B por completo, ya vista en [[estadistica-descriptiva-una-variable]].

**Distribución condicionada de A a B=Jⱼ**: se toma solo la columna Jⱼ y se recalculan las frecuencias relativas
dentro de esa columna: fᵢⱼ_condicionada = Nᵢⱼ/N.ⱼ (respecto al total de esa columna, no del total N).

**Independencia entre A y B**: se da si y solo si fᵢⱼ = fᵢ.×f.ⱼ para todo i,j (equivalente a Nᵢⱼ = Nᵢ.×N.ⱼ/N).
Si se cumple, todas las distribuciones condicionadas de A coinciden entre sí y con la marginal de A.

**Covarianza entre X e Y** (variables cuantitativas):

σ_XY = (1/N)·Σ(xₖ−m_X)(yₖ−m_Y) = (1/N)·Σxₖyₖ − m_X·m_Y

- σ_XY > 0 → relación lineal directa (cuando sube X, sube Y)
- σ_XY = 0 → no hay relación **lineal** (pero puede haber relación no lineal, ej. Y=X²)
- σ_XY < 0 → relación lineal inversa

**Coeficiente de correlación**: ρ_XY = σ_XY/(σ_X·σ_Y) — adimensional, siempre entre −1 y 1. |ρ|=1 significa relación
lineal perfecta; ρ=0 significa incorrelación (no necesariamente independencia: la independencia SÍ implica ρ=0, pero
ρ=0 NO implica independencia — ejemplo canónico Y=X²).

## Ejemplo resuelto

(Adaptado de Tema1.2_Distribucion2caracteres25-26_moodle-2.pdf, diapositiva 23) Valor energético X y contenido en
azúcar Y de 10 muestras de un alimento:

X: 85, 45, 38, 50, 100, 65, 60, 75, 58, 55
Y: 93, 112, 109, 128, 110, 135, 98, 103, 111, 101

m_X = 63.1, m_Y = 110.0 (calculados como media simple, N=10). Covarianza:
σ_XY = (1/10)·Σxₖyₖ − m_X·m_Y. Con Σxₖyₖ = 68990 (suma de productos), σ_XY = 6899 − 63.1×110.0 ≈ 6899 − 6941 ≈ −42.
Como σ_XY < 0, hay indicio de relación lineal **inversa**: a mayor valor energético, menor contenido en azúcar en
esta muestra. El coeficiente ρ_XY se obtiene dividiendo por σ_X·σ_Y (calculados como en
[[estadistica-descriptiva-una-variable]]), dando un valor entre −1 y 0, coherente con la relación inversa observada.

## Conexión con otros conceptos

- [[estadistica-descriptiva-una-variable]] — las marginales y condicionadas son distribuciones de una sola variable
  ya trabajadas ahí; solo cambia de dónde sale la tabla de frecuencias.
- [[probabilidad-propiedades]] — el concepto de independencia entre caracteres (fᵢⱼ=fᵢ.×f.ⱼ) es el análogo
  descriptivo de la independencia de sucesos P(A∩B)=P(A)P(B).

## Errores frecuentes de Marcos aquí

Ninguno activo documentado — Marcos domina dos variables (correlación, tabla conjunta, distribución condicionada)
según `memory/memory.json`. Punto de vigilancia general: no confundir "incorrelación" (ρ=0) con "independencia" —
independencia es una condición más fuerte.

## Relevancia en examen

Media — aparece con regularidad como ejercicio propio dentro de la 1ª parte del examen (construcción de tabla
conjunta a partir de datos brutos, marginales, condicionada y coeficiente de correlación), normalmente con un
contexto de industria alimentaria (valor energético/azúcar, producción/superficie, etc.).
