# IA Aplicada a Ingeniería - Guía Práctica

Repositorio de Jupyter Notebooks orientados a estudiantes avanzados de ingeniería y profesionales, abarcando temas vinculados a la Inteligencia Artificial (EDA, Machine Learning, Deep Learning, Algoritmos Genéticos, MLOps, Despliegue y otros).

## Sobre el proyecto

Este repositorio está construido bajo el estándar de **"Notebooks como paper reproducible"**. El objetivo es proporcionar material educativo de alta calidad técnica que cumpla simultáneamente con tres objetivos:

1. **Leer:** Narrativa pedagógica clara y estructurada.
2. **Ejecutar:** Total reproducibilidad de los resultados.
3. **Explorar:** Entornos preparados (como Google Colab) para la modificación e investigación por parte del usuario.

El contenido se puede visualizar en formato de libro interactivo mediante [Jupyter Book](https://jupyterbook.org/).

## Estructura del Repositorio

*   `/notebooks/`: Contiene todos los Jupyter Notebooks organizados por capítulos numéricos (ej. `01_introduccion`, `02_eda`).
    *   **Concept Notebooks:** Cortos (15-30 min), enfocados en teoría o técnicas específicas.
    *   **Case Study Notebooks:** Largos (1-2 horas), enfocados en problemas de ingeniería reales, trade-offs y consideraciones de despliegue.
*   `/utils/`: Funciones comunes estandarizadas (ej. visualizaciones uniformes, escaneo de entorno).
*   `/scripts/`: Herramientas de automatización para generar el índice (`_toc.yml`) y validar/testear los notebooks.
*   `/datasets/`: Datasets pequeños (<20MB) utilizados en los notebooks. (Los datasets mayores se descargan vía código desde fuentes externas).

## Cómo utilizar este material

### Online (Recomendado)
Se puede leer la versión renderizada (e-book) en: **[Enlace a GitHub Pages pendiente]**.
Dentro de cada notebook se puede encontrar un botón `Open in Colab` para experimentar con el código inmediatamente en la nube.

### Localmente
Para ejecutar los notebooks en tu propia máquina, es una excelente práctica utilizar un entorno virtual (como `venv`) para instalar las dependencias, evitando así utilizar el entorno Python global de tu sistema. 

Se requiere tener Python 3.9+ instalado:

```bash
git clone https://github.com/AxelSkrauba/applied-ai-engineering.git
cd applied-ai-engineering

# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual (Windows)
venv\Scripts\activate
# O en Linux/macOS:
# source venv/bin/activate

# 3. Instalar dependencias en el entorno aislado
pip install -r requirements.txt
```

NOTA: estas dependencias corresponden a los paquetes necesarios para la compilación del e-book, no para la ejecución de los notebooks. Para ejecutar los notebooks localmente, se deben instalar las dependencias específicas de cada notebook. En un futuro, se planea disponibilizar un conjunto de dependencias para cada capítulo o área temática.

## Licencias

Este proyecto utiliza un modelo de licencia dual:
*   **Código Fuente** (Scripts, funciones en `/utils/`, y celdas de código en notebooks): [MIT License](LICENSE).
*   **Contenido Textual** (Narrativa, explicaciones teóricas, diagramas): [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT).
