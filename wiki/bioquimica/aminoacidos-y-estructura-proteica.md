---
titulo: "Aminoácidos y estructura de las proteínas (repaso)"
asignatura: "bioquimica"
tema: "Tema 1 - Repaso de las moléculas"
tipo: "concepto"
relacionado: ["biomoleculas-glucidos-lipidos", "enzimas-estructura-funcion", "metabolismo-aminoacidos-nitrogeno"]
patrones_error: [6]
examen_relevancia: "alta"
fuente: ["Tema 1. Repaso de las moleculas .pdf", "examenes/wuolah-free-Examen final (2022-2023).pdf", "examenes/wuolah-free-Examen ordinario (2023-2024).pdf", "examenes/wuolah-free-Recuperacion (2023-2024).pdf"]
ultima_actualizacion: "2026-07-12"
---

## Qué es

Los aminoácidos son las unidades estructurales de las proteínas: 20 aminoácidos primarios, cada uno con un
grupo amino, un grupo carboxilo y una cadena lateral R que determina sus propiedades (apolar/hidrofóbico,
polar sin carga, polar con carga positiva o negativa a pH fisiológico 7,4). Unidos por enlace peptídico
(covalente, entre el -COOH de uno y el -NH2 del siguiente, con pérdida de agua) forman péptidos y proteínas,
que se organizan en 4 niveles estructurales (primaria = secuencia; secundaria = hélice α/lámina β; terciaria
= plegamiento 3D; cuaternaria = asociación de varias cadenas).

## Por qué / de dónde viene

Cada aminoácido tiene al menos dos grupos ionizables (α-carboxilo y α-amino) y algunos tienen un tercero en
la cadena lateral (Asp, Glu, His, Cys, Tyr, Lys, Arg). Cada grupo tiene su propio pKa. La carga neta de un
péptido a un pH dado es la suma de las cargas de todos sus grupos ionizables en ese pH, y depende de si el pH
está por encima o por debajo del pKa de cada grupo (por debajo del pKa, el grupo ácido está protonado/neutro
o el grupo básico está protonado/positivo). El punto isoeléctrico (pI) es el pH al que la carga neta es cero.

## Fórmula / procedimiento

**Cálculo de carga neta y punto isoeléctrico** (procedimiento, hay que seguir el orden):
1. Listar todos los grupos ionizables del péptido con su pKa: el α-amino N-terminal, el α-carboxilo
   C-terminal, y las cadenas laterales ionizables de los residuos internos (los α-amino/carboxilo internos
   ya están en el enlace peptídico y no cuentan).
2. Ordenar los pKa de menor a mayor.
3. Para un pH dado, cada grupo ácido (COOH) está cargado -1 si pH > pKa, neutro si pH < pKa; cada grupo
   básico (NH3+) está cargado +1 si pH < pKa, neutro si pH > pKa.
4. El pI es el promedio de los dos pKa que flanquean el punto en el que la carga neta pasa de +1 a -1 (el
   "0" de la tabla de cargas).

**Niveles de estructura proteica**
- Primaria: secuencia de aminoácidos (enlace peptídico, covalente).
- Secundaria: hélice α y lámina β (puentes de H entre grupos C=O y N-H del esqueleto).
- Terciaria: plegamiento 3D completo (interacciones hidrofóbicas, puentes de H, iónicas, puentes disulfuro
  S-S entre cisteínas).
- Cuaternaria: asociación de varias cadenas (subunidades) — solo si la proteína es oligomérica.
- Desnaturalización: pérdida de estructura secundaria, terciaria y cuaternaria (nunca de la primaria) por
  calor, pH extremo, agentes caotrópicos (urea, guanidina) o detergentes (SDS) → pérdida de función.

## Ejemplo resuelto

*Adaptado de recuperación 2023-2024, pregunta 3 y 5b.* Péptido A = Fenilalanina-Prolina-Glicina (obtenido
tras digerir un péptido mayor con quimotripsina y luego carboxipeptidasa). Datos: Phe pK1(COOH)=1,83,
pK2(NH3+)=9,13; Pro pK1=1,99, pK2=10,96; Gly no tiene cadena lateral ionizable.

Grupos ionizables del péptido completo: α-COOH del C-terminal (Gly, pKa≈2,3), α-NH3+ del N-terminal (Phe,
pKa≈9,1). Ninguno de los tres tiene cadena lateral cargada. A pH=7 (entre los dos pKa): el COOH está
desprotonado (-1) y el NH3+ está protonado (+1) → carga neta = 0. El pI sería el promedio de esos dos pKa:
pI = (2,3 + 9,1) / 2 ≈ 5,7.

## Conexión con otros conceptos

- [[enzimas-estructura-funcion]]: el centro activo de un enzima está formado por aminoácidos concretos de la
  estructura terciaria.
- [[metabolismo-aminoacidos-nitrogeno]]: destino catabólico de estos mismos aminoácidos.
- [[biomoleculas-glucidos-lipidos]]: la otra familia de biomoléculas repasadas en el Tema 1.
- Conexión con Química General (ionización ácido-base, pKa, ecuación de Henderson-Hasselbalch — ver
  [[../quimica/MOC]]).

## Errores frecuentes de Marcos aquí

**Patrón 6** (copiar mal los datos del enunciado): estos ejercicios dan tablas de pKa con 3 valores por
aminoácido (pK1, pK2, pKR) y es fácil coger el pKa de la cadena lateral equivocado o aplicarlo a un
aminoácido que no lo tiene libre (porque está en medio de la cadena y no es ni N-terminal ni C-terminal).
Antes de calcular, haz que Marcos escriba en voz alta qué grupos están realmente libres en el péptido y con
qué pKa exacto de la tabla, antes de sumar cargas.

## Relevancia en examen

**Alta.** En todos los exámenes de recuperación/ordinario revisados aparece un ejercicio de secuenciación de
péptidos con proteasas (quimotripsina + carboxipeptidasa + aminopeptidasa) y cálculo de punto isoeléctrico /
carga neta a un pH dado. También aparecen preguntas V/F sobre desnaturalización, puentes disulfuro,
L-aminoácidos vs D-aminoácidos, y glicina como único aminoácido no quiral.
