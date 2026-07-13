---
titulo: "Control microbiano y muerte térmica: valores D, Z y F"
asignatura: "microbiologia"
tema: "Tema 3-control — Control microbiano"
tipo: "formula"
relacionado: ["crecimiento-microbiano", "nutricion-microbiana", "toxi-infecciones-alimentarias", "micotoxinas-biotoxinas-priones"]
patrones_error: [3, 4, 6, 7]
examen_relevancia: "alta"
fuente: ["tema 3-control 25-26.pdf", "Problemas muerte térmica MicAli25.pdf", "examenes/wuolah-free-Examen 2º Parcial (2024-2025).pdf", "examenes/wuolah-free-Recuperación (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

El control microbiano por calor (esterilización/pasteurización) se diseña para reducir la población de un microorganismo de referencia (habitualmente *Clostridium botulinum* en enlatados de baja acidez) hasta un nivel de riesgo aceptable. La muerte térmica microbiana sigue una **cinética logarítmica** (no lineal): en cada intervalo de tiempo fijo se destruye la misma **fracción** de la población superviviente, no un número fijo de células. Los valores D, Z y F cuantifican esta cinética y permiten diseñar y comparar tratamientos térmicos.

## Por qué / de dónde viene

Igual que en el crecimiento exponencial (ver [[crecimiento-microbiano]]), la muerte térmica es un proceso de primer orden: la velocidad de destrucción es proporcional al número de supervivientes en cada instante. Por eso, representando el logaritmo del número de supervivientes frente al tiempo a temperatura constante, se obtiene una recta — la pendiente de esa recta define el valor D.

- **Valor D** (tiempo de reducción decimal): tiempo, a una temperatura dada, necesario para reducir la población microbiana al 10% de la inicial (una reducción logarítmica, 1 log). Depende de la temperatura: a mayor T, menor D (destrucción más rápida).
- **Valor Z**: incremento de temperatura necesario para que el valor D se reduzca a la décima parte (o, equivalentemente, cuánto hay que subir la temperatura para conseguir el mismo efecto letal en una décima parte del tiempo). Es una medida de la **sensibilidad térmica** del microorganismo/enzima/toxina a los cambios de temperatura.
- **Valor F** (o tiempo de proceso): tiempo total de tratamiento térmico a una temperatura de referencia (habitualmente 121,1 °C = 250 °F) necesario para conseguir el número de reducciones decimales (n) que se busca. F = n · D.

## Fórmula / procedimiento

1. **Número de reducciones decimales conseguidas** por un tratamiento de duración t a una temperatura con valor D conocido:

   **n = t / D**

   (n es el número de ciclos logarítmicos de reducción de la población).

2. **Relación entre dos temperaturas de tratamiento equivalentes** (mismo efecto letal), usando el valor Z:

   **T₂ = T₁ + Z · log(t₁ / t₂)**

   donde T₁, t₁ es un tratamiento de referencia conocido y T₂, t₂ el tratamiento equivalente que se busca (a mayor T₂, menor t₂ para el mismo efecto).

3. **Procedimiento general de diseño de un tratamiento de esterilización**:
   - Identificar el microorganismo de referencia según el tipo de alimento (ej. *C. botulinum* para pH > 4,5; hongos/levaduras para pH < 4,5).
   - Obtener su valor D a la temperatura de proceso.
   - Fijar el número de reducciones decimales objetivo (tratamiento **12D** es el estándar de la industria para enlatados de baja acidez, referido a *C. botulinum*).
   - Calcular F = 12 · D y verificar que el tiempo/temperatura reales del proceso alcanzan ese F.

## Ejemplo resuelto

*(Adaptado del examen 2º parcial 2024-2025, pregunta 4)*. Un alimento recibe un tratamiento de 5 minutos a 110 °C. Dato: Z = 10 °C.

a) ¿A qué temperatura se necesitaría un tratamiento de solo 1,5 minutos para el mismo efecto letal?

T₂ = 110 + 10 · log(5 / 1,5) = 110 + 10 · log(3,33) = 110 + 10 · 0,523 ≈ **115,2 °C**

b) Si D₁₁₀ = 0,4 minutos, ¿cuántas reducciones decimales se consiguen con el tratamiento de 5 min a 110 °C?

n = t / D = 5 / 0,4 = **12,5 reducciones logarítmicas**

Para un enlatado de pH 4,8 (favorable a *C. botulinum*, pH > 4,5) se exige un tratamiento **12D**; como n = 12,5 > 12, el tratamiento **es adecuado**.

Segundo ejemplo *(adaptado del examen de recuperación 2023-2024, pregunta 9)*: esporas con D₁₀₀ = 2 minutos. Para eliminar una suspensión de 10⁶ células/mL hasta 0 (7 reducciones decimales, de 10⁶ a 10⁰):

Tratamiento = 7 · D = 7 · 2 = **14 minutos**. Este tratamiento **no es suficiente** para un enlatado a pH 5,3 (> 4,5, favorable a *C. botulinum*), porque la referencia exige 12D = 12 · 2 = 24 minutos, no 7D.

## Conexión con otros conceptos

- [[crecimiento-microbiano]] — misma lógica matemática (cinética logarítmica/exponencial), pero en sentido contrario (destrucción en vez de multiplicación).
- [[toxi-infecciones-alimentarias]] — el *C. botulinum* como referencia de 12D conecta directamente con el botulismo como intoxicación por enlatados mal esterilizados.
- [[micotoxinas-biotoxinas-priones]] — las micotoxinas son termoestables (a diferencia de las toxinas bacterianas, que suelen ser termolábiles); esta diferencia de valores D/Z entre tipos de toxina es clave para no generalizar "el calor destruye toda toxina".
- [[nutricion-microbiana]] — el pH y aw del alimento (que también definen el medio de cultivo) son las variables que determinan qué microorganismo de referencia usar en el diseño del tratamiento térmico.

## Errores frecuentes de Marcos aquí

**Patrón 4 (confundir cocientes/relaciones relacionadas)** — activación documentada: confundir D con Z (uno es un tiempo a una T fija, el otro es un incremento de T) o confundir n = t/D con F = n·D. Antes de sustituir, verbalizar qué representa cada letra: "D es tiempo para 1 reducción; Z es grados para reducir D a la décima parte; F es el tiempo total del proceso".

**Patrón 3 (aplicar fórmulas sin verificar el caso)**: aplicar automáticamente el criterio 12D de *C. botulinum* sin comprobar antes el pH del alimento — por debajo de pH 4,5 *C. botulinum* no crece y el microorganismo de referencia cambia (hongos/levaduras, con valores D mucho menores). Siempre identificar primero el pH y el microorganismo de referencia antes de calcular n o F.

**Patrón 6 (copiar mal los datos del enunciado)**: en estos problemas es fácil intercambiar T₁↔T₂ o t₁↔t₂ en la fórmula de Z. Escribir explícitamente qué tratamiento es el "conocido" y cuál el "buscado" antes de sustituir.

**Patrón 7 (dar por bueno un resultado que "suena razonable")**: comprobar siempre si n calculado es mayor o menor que el n exigido (12D u otro) antes de concluir si el tratamiento es adecuado — no basta con calcular n, hay que compararlo.

## Relevancia en examen

Alta — es el tipo de problema numérico más recurrente de la asignatura. Aparece en casi todos los parciales/finales/recuperaciones revisados, siempre con la misma estructura: dado D (y a veces Z), calcular n o F, y razonar si el tratamiento es suficiente para un pH de alimento dado, indicando el microorganismo de referencia, su Gram, relación con el oxígeno y tipo de metabolismo.
