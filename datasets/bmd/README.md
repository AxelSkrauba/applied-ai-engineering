# Body Measurements Dataset (BMD)

Este directorio contiene una versión adaptada y traducida al español del "Body Measurements Datasets", que recoge mediciones corporales de diversas personas reales.

[📥 Descargar Dataset (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/bmd/datos_bmd.zip)

## Origen y Cita Recomendada

Este conjunto de datos fue recopilado originalmente por investigadores en Malasia debido a la falta de bases de datos públicas de libre acceso sobre mediciones del cuerpo humano. Los datos fueron recolectados utilizando cintas métricas en individuos desde 1 año de edad en adelante.

**Cita recomendada:**
> *M. Kiru, "Body Measurements Datasets," Mendeley Data, V1, doi: 10.17632/bjv6c9pmp4.1, 2021.*
> *Referencia de artículo: https://ieeexplore.ieee.org/document/9293673*

## Descripción de los Datos

El conjunto contiene información referente a diferentes variables que, en un entorno de producción, podrían ser extraídas mediante análisis de visión por computadora (longitud de extremidades, tamaño de la cabeza, etc.). A estas medidas se les incorpora información adicional de contexto como la edad y el género del sujeto. En nuestra versión adaptada, **todas las medidas han sido convertidas a centímetros** (el original estaba en pulgadas) para adherirse al sistema métrico internacional, y las columnas traducidas al español.

### Diccionario de Datos

El dataset contiene muestras de **716 individuos** (posterior a limpieza de encabezados en el CSV). 

*   **`Genero`**: (Categórica/Numérica) Masculino (`1`) y Femenino (`2`).
*   **`Edad`**: (Numérica) Edad en años (desde 1 año en adelante).
*   **`CircunferenciaCabeza`**: (Numérica) En centímetros.
*   **`AnchoHombro`**: (Numérica) En centímetros.
*   **`AnchoPecho`**: (Numérica) En centímetros.
*   **`Abdomen`**: (Numérica) En centímetros.
*   **`Cintura`**: (Numérica) En centímetros.
*   **`Cadera`**: (Numérica) En centímetros.
*   **`LongitudBrazo`**: (Numérica) En centímetros.
*   **`LongitudHombroCintura`**: (Numérica) En centímetros.
*   **`LongitudCinturaRodilla`**: (Numérica) En centímetros.
*   **`LongitudPierna`**: (Numérica) En centímetros.
*   **`AlturaTotal`**: (Numérica) De la cabeza a los pies, en centímetros.

## Consideraciones para Ingeniería y Casos de Uso

Este dataset presenta un excelente escenario "*cross domain*" (puede usarse tanto para regresión como para clasificación):
- **Clasificación en Entornos Reales:** Creación de un sistema para distinguir entre niños y adultos (estableciendo un umbral de edad objetivo) a partir de las medidas corporales. Ideal para simular sistemas de control de acceso automatizados mediante visión artificial.
- **Identificación de Rangos de Confianza:** Analizar y definir operativamente para qué rangos etarios el modelo es confiable y para cuáles no, una tarea vital al momento de certificar un sistema en la industria.
- **Análisis de Métricas Críticas:** Determinar, según el contexto del problema (ej. seguridad infantil vs. comodidad de adultos), qué tipo de error (Falso Positivo o Falso Negativo) es aceptable y cuál es crítico.
