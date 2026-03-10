# Concrete Compressive Strength Dataset (CCS)

Este directorio contiene una versión adaptada del popular dataset "Concrete Compressive Strength" para estimar la resistencia del hormigón.

[📥 Descargar Dataset (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/ccs/datos_ccs.zip)

## Origen y Cita Recomendada

Este conjunto de datos fue donado originalmente al repositorio de UCI Machine Learning en 2007. Trata sobre la resistencia a la compresión del hormigón, la cual es una función altamente no lineal de la edad y los ingredientes utilizados en la mezcla.

**Cita recomendada:**
> *I.-C. Yeh, "Concrete Compressive Strength," UCI Machine Learning Repository, doi: 10.24432/C5PK67, 2007.*
> *Paper original: I. Yeh. "Modeling of strength of high-performance concrete using artificial neural networks," Cement and Concrete Research, Vol. 28, No. 12, 1998.*

## Descripción de los Datos

La resistencia a la compresión simple es la característica mecánica principal del concreto. Se define como la capacidad para soportar una carga por unidad de área, y se expresa en términos de esfuerzo [MPa]. El cemento es el material más activo de la mezcla, y su proporción tiene gran influencia. Además, existen varios “agregados” que afectan de manera no lineal las proporciones para una resistencia determinada.

### Diccionario de Datos

El dataset contiene **1030 muestras** con 9 variables en total (8 de entrada y 1 de salida). No contiene valores faltantes.

*   **`cement`**: (Numérica, Continua) Cantidad de cemento, medido en $kg/m^3$.
*   **`slag`**: (Numérica, Continua) Escoria de alto horno (Blast Furnace Slag), medido en $kg/m^3$.
*   **`flyash`**: (Numérica, Continua) Ceniza volante (Fly Ash), medido en $kg/m^3$.
*   **`water`**: (Numérica, Continua) Agua, medido en $kg/m^3$.
*   **`superplasticizer`**: (Numérica, Continua) Superplastificante, medido en $kg/m^3$.
*   **`coarseaggregate`**: (Numérica, Continua) Agregado grueso, medido en $kg/m^3$.
*   **`fineaggregate`**: (Numérica, Continua) Agregado fino, medido en $kg/m^3$.
*   **`age`**: (Numérica, Entero) Edad del concreto en días, desde 1 a 365 días.
*   **`csMPa` (Variable Objetivo / Target)**: (Numérica, Continua) Resistencia a la compresión del concreto, medida en Megapascales (MPa).

## Consideraciones para Ingeniería y Casos de Uso

Este dataset es el estándar ideal para plantear y resolver problemas de:
- **Regresión Múltiple No Lineal:** Predecir un valor continuo a partir de múltiples variables independientes cuyas relaciones no son triviales.
- **Importancia del Preprocesamiento:** Analizar cómo el escalado de variables (Estandarización, MinMax) afecta drásticamente a ciertos modelos de regresión y no a otros.
- **Métricas de Regresión:** Comprender e interpretar el Error Cuadrático Medio (RMSE), Error Absoluto Medio (MAE) y el Coeficiente de Determinación ($R^2$) en un caso físico real.
