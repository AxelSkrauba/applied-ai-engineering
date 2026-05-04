# Deep Learning

Este capítulo completa el puente que comenzó el Machine Learning Clásico. Si el capítulo anterior nos enseñó a construir sistemas predictivos con geometría, probabilidad y árboles de decisión, aquí aprendemos a **componer esas unidades en topologías que aprenden representaciones automáticamente**. No se trata de abandonar lo anterior: se trata de entender exactamente en qué situaciones el Deep Learning justifica su costo computacional, y en cuáles un modelo clásico sigue siendo la decisión correcta de ingeniería.

Nuestro objetivo no es memorizar arquitecturas de moda; es desarrollar **criterio de ingeniería** para decidir cuándo usar una red profunda, cómo estabilizar su entrenamiento sin recurrir a magia negra, y cómo aprovechar el ecosistema *open source* (Hugging Face, Keras Applications) para resolver problemas complejos con fracciones del costo original. El *data hunger*, la sensibilidad a la inicialización y el riesgo de sobreajuste en redes profundas son trampas reales que un ingeniero debe saber identificar antes de escribir la primera línea de código.

## Contenido del Capítulo

- **Fundamentos y Estabilidad Matemática:** De la neurona individual al entrenamiento estable del MLP. Forward pass, backpropagation e inicialización (Xavier, He). Normalización de capas (Batch, Layer), optimizadores (SGD, Adam), regularización (Dropout) y la ingeniería del ciclo de entrenamiento: callbacks, monitoreo y recuperación ante desastres.
- **El Puente al No Supervisado:** Autoencoders como herramienta de aprendizaje de representaciones. El espacio latente como extractor de características no lineales y el error de reconstrucción como detector de anomalías.
- **Arquitecturas Especializadas:** Redes convolucionales (CNN) para extracción jerárquica de características espaciales; embeddings y redes recurrentes (LSTM/GRU) para secuencias temporales y texto; el mecanismo de auto-atención y la construcción de un bloque Transformer Encoder.
- **Estado del Arte y Productividad:** Transfer Learning y Fine-Tuning: cuándo congelar, cuándo descongelar y por qué. Feature Extraction con el ecosistema Hugging Face para traducir datos no estructurados (texto, visión, audio) en vectores densos alimentables por los modelos clásicos del Capítulo 3.

---

*Nota: El Deep Learning no es magia. Es Machine Learning con más hiperparámetros, más datos y una curva de entrenamiento mucho más traicionera. Te recomendamos ejecutar cada notebook, modificar la profundidad de la red, cambiar la tasa de aprendizaje y observar cómo colapsa o converge. Un buen ingeniero de IA sabe cuándo una red neuronal es la respuesta correcta — y, lo que es más importante, sabe cuándo un Random Forest de 100 árboles sigue siendo la mejor decisión de producción.*
