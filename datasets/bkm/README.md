# Bank Marketing Dataset (BKM)

Este directorio contiene los archivos del clásico dataset de marketing bancario directo de la UCI Machine Learning Repository, relacionado con campañas de llamadas telefónicas de una institución bancaria portuguesa.

[📥 Descargar `bank.csv` (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/bkm/bank.zip)
[📥 Descargar `bank-full.csv` (ZIP)](https://raw.githubusercontent.com/AxelSkrauba/applied-ai-engineering/main/datasets/bkm/bank-full.zip)

## Origen y Cita Recomendada

Este dataset fue creado por **Paulo Cortez** (Universidade do Minho) y **Sérgio Moro** (ISCTE-IUL) en 2012, a partir de datos reales de campañas de marketing directo de una institución bancaria portuguesa. Está disponible públicamente en el UCI Machine Learning Repository.

**Cita recomendada (paper primario):**
> *S. Moro, R. Laureano and P. Cortez. "Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology." In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference — ESM'2011, pp. 117–121, Guimarães, Portugal, October, 2011. EUROSIS.*
> Disponible en: http://hdl.handle.net/1822/14838

**Paper extendido (versión 2014, dataset adicional):**
> *S. Moro, P. Cortez and P. Rita. "A data-driven approach to predict the success of bank telemarketing." Decision Support Systems, Elsevier, 62, pp. 22–31, June 2014.*

**Fuente del dataset:**
> *"Bank Marketing." UCI Machine Learning Repository. Disponible en: https://archive.ics.uci.edu/dataset/222/bank+marketing*

## Descripción del Dataset

Los datos corresponden a campañas de **marketing directo por llamadas telefónicas** de un banco portugués, llevadas a cabo entre **mayo de 2008 y noviembre de 2010**. El objetivo es predecir si un cliente contratará un **depósito a plazo fijo** (`yes` / `no`) como resultado de la campaña. En muchos casos, fue necesario contactar al mismo cliente más de una vez.

### Archivos disponibles

Este directorio contiene los **dos archivos de la versión original** (versión de 17 atributos), con el separador convertido de `;` al estándar `,`:

| Archivo | Muestras | Descripción |
|---|---|---|
| `bank.csv` | 4.521 | 10% del dataset completo, seleccionado aleatoriamente. Ideal para algoritmos computacionalmente exigentes (ej. SVM). |
| `bank-full.csv` | 45.211 | Dataset completo, ordenado por fecha. |

> **Nota sobre versiones:** El repositorio UCI también distribuye versiones extendidas (`bank-additional.csv` y `bank-additional-full.csv`) con 20 atributos de entrada, correspondientes al análisis de [Moro et al., 2014]. Los archivos en este directorio corresponden a la **versión original de 16 atributos de entrada** descrita en [Moro et al., 2011].

## Diccionario de Datos

Cada archivo contiene **17 columnas** (16 de entrada + 1 objetivo):

### Datos del cliente bancario

*   **`age`**: (Numérica) Edad del cliente en años.
*   **`job`**: (Categórica) Tipo de empleo. Categorías: `"admin."`, `"blue-collar"`, `"entrepreneur"`, `"housemaid"`, `"management"`, `"retired"`, `"self-employed"`, `"services"`, `"student"`, `"technician"`, `"unemployed"`, `"unknown"`.
*   **`marital`**: (Categórica) Estado civil: `"married"`, `"divorced"`, `"single"`. *(Nota: `"divorced"` incluye también a viudos/as).*
*   **`education`**: (Categórica) Nivel educativo: `"primary"`, `"secondary"`, `"tertiary"`, `"unknown"`.
*   **`default`**: (Binaria) ¿Tiene crédito en mora? `"yes"` / `"no"`.
*   **`balance`**: (Numérica) Saldo medio anual de la cuenta bancaria, en euros. Puede ser negativo.
*   **`housing`**: (Binaria) ¿Tiene préstamo hipotecario? `"yes"` / `"no"`.
*   **`loan`**: (Binaria) ¿Tiene préstamo personal? `"yes"` / `"no"`.

### Datos del último contacto de la campaña

*   **`contact`**: (Categórica) Tipo de medio de contacto: `"cellular"`, `"telephone"`, `"unknown"`.
*   **`day`**: (Numérica) Día del mes del último contacto (1–31).
*   **`month`**: (Categórica) Mes del año del último contacto: `"jan"`, `"feb"`, ..., `"dec"`.
*   **`duration`**: (Numérica) Duración del último contacto en segundos.

### Otros atributos

*   **`campaign`**: (Numérica) Número total de contactos realizados durante esta campaña para este cliente (incluye el último contacto).
*   **`pdays`**: (Numérica) Días transcurridos desde el último contacto en una campaña anterior. `-1` indica que el cliente no fue contactado previamente.
*   **`previous`**: (Numérica) Número de contactos realizados antes de esta campaña para este cliente.
*   **`poutcome`**: (Categórica) Resultado de la campaña de marketing anterior: `"success"`, `"failure"`, `"other"`, `"unknown"`.

### Variable objetivo

*   **`y` (Variable Objetivo / Target)**: (Binaria) ¿El cliente contrató un depósito a plazo fijo? `"yes"` / `"no"`.

## Consideraciones para Ingeniería y Casos de Uso

- **Clasificación Binaria con Desbalance Moderado:** La clase positiva (`"yes"`) representa aproximadamente el 11–12% de las muestras. Si bien no es un desbalance extremo, es suficiente para que la accuracy no sea la métrica más informativa; se recomienda evaluar con **F1-score, Precision, Recall y AUC-ROC**.
- **Uso de `duration` como Variable Problemática:** La duración del último llamado tiene una correlación muy alta con el resultado (una llamada larga usualmente implica que el cliente mostró interés), pero esta variable **no se conoce antes de realizar el contacto**. Incluirla en producción sería un caso de *data leakage*; es habitual utilizarla en análisis exploratorio pero excluirla de los modelos productivos.
- **Variables con Categoría `"unknown"`:** Las columnas `job`, `education`, `contact` y `poutcome` contienen la categoría `"unknown"` que representa información faltante codificada como categoría. Requieren decisiones de imputación o tratamiento explícito.
- **`pdays = -1` como Valor Centinela:** El valor `-1` en `pdays` indica ausencia de contacto previo y no es comparable numéricamente con el resto de los valores. Es habitual transformarlo (ej. con una variable binaria adicional `was_contacted_before`).
- **Análisis de Campañas y Segmentación:** El dataset es ideal para estudiar la **efectividad de campañas de marketing** en función del perfil del cliente, el mes de contacto y el historial de campañas anteriores.
- **Comparación de Subsets:** La disponibilidad de un subset del 10% (`bank.csv`) permite experimentar con algoritmos computacionalmente costosos (SVM, redes neuronales) y comparar resultados con el dataset completo (`bank-full.csv`).
