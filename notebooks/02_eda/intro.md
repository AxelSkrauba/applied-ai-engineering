# Análisis Exploratorio de Datos (EDA) y Preprocesamiento

El Análisis Exploratorio de Datos (EDA, por sus siglas en inglés) y el Preprocesamiento conforman la base sobre la cual se construye cualquier sistema de Inteligencia Artificial exitoso. En este capítulo, dejamos de ver los datos como simples tablas para empezar a entenderlos como espacios geométricos y distribuciones matemáticas. 

No nos limitamos a usar librerías para trazar gráficos; nuestro objetivo es desarrollar **criterio de ingeniería** para auditar, limpiar y esculpir la materia prima antes de alimentar cualquier algoritmo, evitando trampas mortales como el *Data Leakage* o la ceguera ante relaciones no lineales.

## Contenido del Capítulo

- **Inspección y Limpieza Base:** Identificación y tratamiento fundamentado de valores faltantes, codificación de variables categóricas (*Encoding*) y la prevención temprana de fugas de datos por dependencias funcionales.
- **Relaciones y Transformaciones Matemáticas:** Más allá de la correlación lineal de Pearson. Uso de Información Mutua y transformaciones matemáticas (Logarítmicas, Polinómicas) para corregir asimetrías y "doblar el espacio", volviendo linealmente separables problemas complejos.
- **Geometría, Dimensionalidad y Casos Extremos:** El impacto crítico de las escalas dispares, compresión de información mediante PCA, detección de anomalías multivariadas (*Isolation Forest*) y estrategias a nivel de datos frente al desbalance severo de clases (SMOTE).
- **Herramientas Profesionales y Comunicación:** Uso con escepticismo profesional de frameworks de Auto-EDA para maximizar la productividad, y principios de visualización efectiva (*Storytelling* y *Data-Ink Ratio*) para comunicar hallazgos técnicos a tomadores de decisiones.

---
*Nota: Los datos del mundo real son ruidosos, incompletos y a menudo engañosos. Te recomendamos fuertemente ejecutar los notebooks, alterar las variables, inyectar ruido a propósito y observar cómo se rompen las distribuciones o cambian las correlaciones. Un buen ingeniero de IA pasa la mayor parte del tiempo en esta fase; dominar el EDA es lo que separa a un simple "tirador de código" (o "copiador de lo que me dice el LLM de confianza de turno...") de un verdadero profesional.*
