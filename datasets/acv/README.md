# Stroke Prediction Dataset (ACV)

Este directorio contiene una versión modificada y adaptada al español del dataset popularmente conocido como *"Stroke Prediction Dataset"* en Kaggle.

[📥 Descargar Dataset (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/acv/datos_acv.zip)

## Origen y Cita Recomendada

**Importante:** La mejor evidencia disponible indica que este dataset no tiene una fuente clínica o institucional claramente identificable. Su origen primario trazable es la plataforma Kaggle; no hay referencia verificable a un hospital, institución de salud pública o estudio concreto del que se haya extraído. Versiones del archivo aparecen alojadas en GitHub y otros sitios como simples copias, sin ninguna información adicional sobre procedencia clínica. 

Por lo tanto, la forma más honesta de citarlo en trabajos o artículos es como un dataset de autor desconocido:

> *“Healthcare Dataset Stroke Data (Stroke Prediction Dataset). Kaggle, dataset no oficial de predicción de accidente cerebrovascular a partir de datos clínicos simulados o desidentificados; fuente clínica original no especificada. Disponible en: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset”*

## Contexto del Dataset

Este conjunto de datos reúne características (features) clínicas y demográficas de más de 5100 pacientes, las cuales se creen son relevantes para la predicción de accidentes cerebrovasculares (ACV). 

El archivo ha sido modificado para que los nombres de las columnas y sus categorías estén en **español**, facilitando su uso en el material de estudio de este repositorio.

## Diccionario de Datos

El dataset presenta la siguiente estructura de variables (12 columnas):

*   **`id`**: (Numérica) Identificador único del paciente.
*   **`género`**: (Categórica) Género del paciente: *"hombre"*, *"mujer"* u *"otro"*.
*   **`edad`**: (Numérica) Edad del paciente en años.
*   **`hipertensión`**: (Categórica/Binaria) Indica si el paciente padece hipertensión: `"0"` (no tiene), `"1"` (sí tiene).
*   **`enfermedad_corazón`**: (Categórica/Binaria) Indica si el paciente padece alguna enfermedad cardíaca: `"0"` (no tiene ninguna), `"1"` (tiene al menos una).
*   **`casado_alguna_vez`**: (Categórica/Binaria) Estado civil histórico: `"0"` (nunca estuvo ni está casado), `"1"` (estuvo o está casado).
*   **`tipo_trabajo`**: (Categórica) Tipo de empleo del paciente. Se incluyen 5 categorías diferentes y descriptivas.
*   **`tipo_residencia`**: (Categórica) Entorno donde reside el paciente: *"urbano"* o *"rural"*.
*   **`nivel_glucosa`**: (Numérica) Nivel promedio de glucosa en sangre.
*   **`imc`**: (Numérica) Índice de Masa Corporal. *(Nota: Esta columna puede contener datos faltantes que requieren tratamiento).*
*   **`estado_fumador`**: (Categórica) Historial de tabaquismo. Se incluyen 4 categorías: *"fumaba"*, *"fuma"*, *"nunca"* y *"desconocido"*. La categoría "desconocido" se utilizó para completar la información no disponible para esos pacientes.
*   **`apoplejía` (Variable Objetivo / Target)**: (Categórica/Binaria) Indica si el paciente sufrió un accidente cerebrovascular (ACV): `"1"` (sí tuvo un ACV), `"0"` (no lo tuvo).

## Consideraciones para Ingeniería

Al trabajar con este dataset, el estudiante o profesional debe enfrentarse a problemas reales del Análisis Exploratorio de Datos (EDA) y preprocesamiento:
- Presencia de datos faltantes (especialmente en la columna `imc`).
- Un fuerte desbalance de clases en la variable objetivo (`apoplejía`), lo cual requerirá estrategias específicas de muestreo o evaluación métrica.
- Presencia de categorías raras o inconsistentes (ej. la categoría *"otro"* en `género` o el estado *"desconocido"* en `estado_fumador`).
