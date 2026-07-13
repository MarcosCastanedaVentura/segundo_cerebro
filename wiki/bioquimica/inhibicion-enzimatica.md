---
titulo: "Inhibición enzimática: irreversible, competitiva y no competitiva"
asignatura: "bioquimica"
tema: "Tema 2 - Enzimas"
tipo: "concepto"
relacionado: ["cinetica-michaelis-menten", "enzimas-estructura-funcion", "regulacion-enzimatica-alosterica"]
patrones_error: [3, 4]
examen_relevancia: "alta"
fuente: ["Tema 2_Enzimas.pdf", "Problemas Enzimas resueltos.pdf", "Problemas Enzimas II resuelto.pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Recuperacion (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Un inhibidor es cualquier sustancia que reduce la actividad específica de un enzima, disminuyendo la
velocidad de reacción sin actuar como sustrato. Se clasifica en dos grandes grupos según cómo se une al
enzima: **irreversible** (unión covalente, sin equilibrio de disociación) y **reversible** (unión no
covalente, con equilibrio de disociación), y dentro de la reversible hay dos tipos principales: **competitiva**
y **no competitiva**, que se distinguen por su efecto sobre Km y Vmax.

## Por qué / de dónde viene

El efecto de un inhibidor reversible sobre Km y Vmax depende de si compite o no con el sustrato por el mismo
sitio (el centro activo):
- Si el inhibidor se parece estructuralmente al sustrato y compite por el centro activo (**competitiva**),
  basta con subir mucho [S] para desplazar al inhibidor → Vmax no cambia, pero se necesita más sustrato para
  llegar a ½Vmax → Km aparente sube.
- Si el inhibidor se une en un sitio distinto del centro activo (**no competitiva**), da igual cuánto suba
  [S], nunca se desplaza al inhibidor → Vmax baja. Como no compite por el mismo sitio que el sustrato, la
  afinidad del enzima libre por el sustrato no cambia → Km no varía.

## Fórmula / procedimiento

**Inhibición competitiva:**
- Km aparente (Km' o Km,ap) = Km · (1 + [I]/Ki) — **aumenta**
- Vmax no cambia
- Ki = [E][I]/[EI] (constante de disociación enzima-inhibidor)
- En Lineweaver-Burk: mismo corte en Y (1/Vmax), pero rectas con distinta pendiente → cortan el eje X en
  puntos distintos (más cerca de 0 con inhibidor).

**Inhibición no competitiva:**
- Km no cambia
- Vmax aparente (Vm') = Vmax / (1 + [I]/Ki) — **disminuye**
- En Lineweaver-Burk: mismo corte en X (-1/Km), pero distinto corte en Y → rectas que se cortan en el eje X
  (paralelas si es no competitiva "pura").

**Factor α** (forma práctica de resolver problemas con datos aparentes):
- α = 1 + [I]/Ki  →  Ki = [I] / (α − 1)
- Competitiva: Km,ap = α·Km, Vmax constante.
- No competitiva "pura": Vmax,ap = Vmax/α, Km constante.

**Procedimiento para clasificar un inhibidor a partir de datos experimentales** (orden obligatorio):
1. Calcular Km y Vmax sin inhibidor (Lineweaver-Burk).
2. Calcular Km,ap y Vmax,ap con inhibidor.
3. Comparar: ¿cambia Km? ¿cambia Vmax? Solo con esa comparación se decide el tipo de inhibición — nunca antes.
4. Solo entonces calcular α y Ki con la fórmula que corresponda al tipo identificado.

## Ejemplo resuelto

*Adaptado de Problemas Enzimas II resuelto.pdf (examen junio 2012).* Enzima con Km=0,5 mM y Vmax=5 mM·min⁻¹
sin inhibidor. Con inhibidor A a 1,5 mM: Km,ap(A)=1,25 mM, Vmax,ap(A)=5 mM·min⁻¹ (igual que sin inhibidor).
Con inhibidor B a 6 mM: Km,ap(B)=0,5 mM (igual que sin inhibidor), Vmax,ap(B)=2 mM·min⁻¹.

- Inhibidor A: Km sube, Vmax constante → **competitiva**. α(A) = Km,ap/Km = 1,25/0,5 = 2,5.
  Ki(A) = [I]/(α−1) = 1,5 mM/(2,5−1) = **1 mM**.
- Inhibidor B: Km constante, Vmax baja → **no competitiva**. α(B) = Vmax/Vmax,ap = 5/2 = 2,5.
  Ki(B) = [I]/(α−1) = 6 mM/(2,5−1) = **4 mM**.

Verificación de razonabilidad (Patrón 7): con el inhibidor A, V₀ a [S]=2 mM sin inhibidor da
V₀=(5×2)/(0,5+2)=4 mM·min⁻¹, un valor menor que Vmax como cabe esperar — chequeo rápido antes de dar el
resultado por bueno.

## Conexión con otros conceptos

- [[cinetica-michaelis-menten]]: toda esta clasificación se apoya en la ecuación de Michaelis-Menten y su
  linealización de Lineweaver-Burk.
- [[regulacion-enzimatica-alosterica]]: los inhibidores alostéricos (feedback) son un mecanismo fisiológico
  distinto, no farmacológico, pero comparten la idea de unión en un sitio regulador.
- Ejemplos fisiológicos concretos: malonil-CoA inhibe la carnitina-acil-transferasa I (ver
  [[metabolismo-lipidos-beta-oxidacion]]); ATP/NADH/acetil-CoA inhiben el complejo piruvato deshidrogenasa
  (ver [[ciclo-krebs]]).

## Errores frecuentes de Marcos aquí

**Patrón 3** (aplicar fórmulas sin verificar condiciones de uso): las fórmulas de Km,ap y Vmax,ap son
distintas según el tipo de inhibición — usar la fórmula de competitiva cuando los datos indican no
competitiva (o al revés) es el error más probable. **Antes de aplicar cualquier fórmula, identifica primero
qué parámetro cambia (Km, Vmax o ambos) mirando los datos experimentales.**

**Patrón 4** (confundir cocientes relacionados): α = 1+[I]/Ki y su despeje Ki=[I]/(α−1) se confunden
fácilmente con Km,ap=α·Km — verifica siempre qué variable estás despejando antes de sustituir.

## Relevancia en examen

**Alta.** Aparece como problema numérico completo en el examen final 2022-2023 (pregunta 7, clasificar
inhibidor Z) y en la recuperación 2023-2024 (pregunta 7d). También en las dos hojas de "Problemas Enzimas
resueltos" al completo. Es, junto con la cinética de Michaelis-Menten, el bloque de problema numérico más
repetido en todas las convocatorias revisadas.
