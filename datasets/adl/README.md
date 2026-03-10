# Air Quality Dataset for ADL Classification

Este directorio contiene una versión adaptada del conjunto de datos de calidad del aire utilizado para la clasificación de Actividades de la Vida Diaria (ADL, por sus siglas en inglés).

[📥 Descargar Dataset (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/adl/datos_adl.zip)

## Origen y Cita Recomendada

Este conjunto de datos se basa en mediciones reales de una matriz de sensores de bajo costo para detectar la variación en la concentración de gases en interiores a lo largo del tiempo. Se evitó un enfoque cuantitativo (que requeriría calibración precisa) en favor del uso de algoritmos de inteligencia artificial.

**Cita recomendada:**
> *E. Gambi, "Air Quality dataset for ADL classification," Mendeley Data, V1, doi: 10.17632/kn3x9rz3kd.1, 2020.*

## Descripción de los Datos

El conjunto de sensores consta de dos categorías principales:
- **Sensores MQ (MQ2, MQ9, MQ135, MQ137, MQ138):** Ofrecen alta sensibilidad, baja latencia y bajo costo; cada sensor responde a diferentes tipos de gases.
- **Sensor analógico de CO2 (MG-811):** Excelente sensibilidad al dióxido de carbono y apenas afectado por las variaciones de temperatura y humedad del aire.

Cualquier actividad produce sustancias químicas en el aire (respiración humana, exhalaciones de procesos metabólicos, liberación de volátiles por combustión u oxidación, y evaporación de detergentes domésticos, etc.). Esto permite identificar la actividad basándose en la composición del aire.

### Diccionario de Datos

El dataset contiene **1845 muestras** con 7 columnas:

*   **`MQ2`, `MQ9`, `MQ135`, `MQ137`, `MQ138`**: (Numéricas) Salidas de los diferentes sensores de gas MQ.
*   **`MG-811`**: (Numérica) Salida del sensor analógico de CO2.
*   **`Situacion` (Variable Objetivo / Target)**: (Categórica/Numérica) Índice que identifica la actividad realizada en la habitación. Toma 4 posibles valores:
    *   `1`: **Situación normal:** Aire limpio, una persona durmiendo, estudiando o descansando. (595 muestras).
    *   `2`: **Preparación de comidas:** Cocinar carne, pasta, o verduras fritas. Una o dos personas en la habitación, con circulación de aire forzado. (515 muestras).
    *   `3`: **Presencia de humo:** Quemar papel y madera por un período corto en una habitación con puertas y ventanas cerradas. (195 muestras).
    *   `4`: **Limpieza:** Uso de detergentes en aerosol y líquidos con amoníaco y/o alcohol. (540 muestras).

## Consideraciones para Ingeniería y Casos de Uso

Este dataset es ideal para plantear y resolver problemas relacionados a:
- **Clasificación Multiclase:** Construcción y evaluación de modelos predictivos capaces de discernir entre 4 estados diferentes.
- **Evaluación de Desempeño y Costos:** Análisis de la relación entre el rendimiento del modelo (exactitud, tiempos de entrenamiento y latencia de inferencia) y las necesidades de un sistema en tiempo real.
- **Análisis de Importancia de Características (Feature Selection):** Determinar si es estrictamente necesario mantener encendidos (o comprar) los 6 sensores para que el sistema funcione adecuadamente, un aspecto crítico en el diseño de hardware IoT (Internet de las Cosas).
- **Desbalance de Clases Leve:** La clase `3` (presencia de humo) es minoritaria frente a las demás.
