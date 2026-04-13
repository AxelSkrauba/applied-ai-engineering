# Credit Card Fraud Detection Dataset (CCF)

Este directorio contiene dos muestras estratificadas del clásico dataset de detección de fraude en transacciones con tarjeta de crédito, ampliamente utilizado como benchmark en tareas de **detección de anomalías**.

[📥 Descargar `creditcard_sample.csv` (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/ccf/creditcard_sample.zip)
[📥 Descargar `creditcard_sample_2.csv` (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/ccf/creditcard_sample_2.zip)

## Origen y Cita Recomendada

Los datos originales fueron recopilados y analizados en el marco de una colaboración entre **Worldline** y el **Machine Learning Group (MLG)** de la Université Libre de Bruxelles (ULB), como parte de investigaciones sobre minería de grandes datos y detección de fraude.

**Fuente primaria:**
> *Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. "Calibrating Probability with Undersampling for Unbalanced Classification." In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015.*

**Dataset original disponible en:**
> *"Credit Card Fraud Detection." Kaggle / MLG-ULB. Disponible en: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud*


## Descripción del Dataset Original

El conjunto de datos original reúne transacciones realizadas con tarjetas de crédito por titulares europeos durante **dos días de septiembre de 2013**. Contiene **284.807 transacciones**, de las cuales apenas **492 son fraudes** (aproximadamente el **0,172%** del total). Esto hace que el desbalance de clases sea **extremo**.

Todas las variables de entrada son numéricas y resultado de una **transformación PCA** aplicada a los datos originales por razones de confidencialidad. Las únicas variables que no fueron transformadas son `Time` y `Amount`.

## Descripción de las Muestras en Este Directorio

Este directorio contiene **dos muestras independientes** del dataset original, destinadas a escenarios de evaluación y comparación:

- **`creditcard_sample.csv`**: 10.000 transacciones, muestreadas de forma **estratificada** respecto a la variable `Class`, preservando la proporción original de fraudes (~0,172%).
- **`creditcard_sample_2.csv`**: 10.000 transacciones adicionales, muestreadas de forma **estratificada** de la misma manera, con el fin de simular un segundo lote de datos o un escenario de evaluación diferido.

Ambas muestras **no se solapan** y mantienen la distribución natural de fraudes del dataset original.

## Diccionario de Datos

Cada muestra contiene **10.000 filas** y **31 columnas**:

*   **`Time`**: (Numérica, Continua) Segundos transcurridos entre cada transacción y la primera transacción del dataset.
*   **`V1` – `V28`**: (Numéricas, Continuas) Componentes principales obtenidas mediante PCA sobre los datos originales. Las características subyacentes son confidenciales.
*   **`Amount`**: (Numérica, Continua) Importe monetario de la transacción. Puede utilizarse para aprendizaje sensible al costo.
*   **`Class` (Variable Objetivo / Target)**: (Categórica/Binaria) Resultado de la transacción: `1` indica **fraude**, `0` indica **transacción legítima**.

## Consideraciones para Ingeniería y Casos de Uso

> ⚠️ **Este dataset está diseñado para tareas de detección de anomalías, no de clasificación supervisada convencional.** El desbalance extremo (~0,17% de positivos) y la naturaleza cambiante del fraude hacen que las técnicas estándar de clasificación sean inapropiadas en producción.

- **Detección de Anomalías / Novelty Detection:** Modelar la distribución de las transacciones normales y tratar el fraude como una desviación estadística. Algoritmos como Isolation Forest, One-Class SVM o Autoencoders son enfoques correctos para este problema.
- **Métricas Apropiadas:** Dado el desbalance extremo, la accuracy convencional es una métrica engañosa. Se recomienda el uso del **Área Bajo la Curva de Precisión-Recall (AUPRC)**, junto con métricas como F1-score, Precisión y Recall evaluadas sobre la clase positiva.
- **Riesgo del Balanceo Artificial de Clases:** Aplicar técnicas de sobremuestreo (SMOTE, ADASYN, etc.) o submuestreo para balancear las clases puede generar modelos que funcionan bien en validación cruzada pero **fallan en producción**, dado que el modelo aprende patrones artificiales que no reflejan la dinámica real del fraude.
- **Concepto Drift:** El fraude evoluciona continuamente. Los modelos entrenados con datos históricos pueden degradarse ante nuevas tipologías de fraude. El uso de dos muestras independientes permite simular escenarios de evaluación diferida o *temporal holdout*.
- **Sensibilidad al Costo:** El importe de la transacción (`Amount`) permite diseñar funciones de pérdida o criterios de evaluación que ponderen el costo real de los errores (un falso negativo en una transacción de $5.000 tiene mayor impacto que uno en una de $5).
