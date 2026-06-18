# Casos de Estudio Avanzados: Computación Evolutiva Aplicada

Los notebooks del capítulo de Optimización Evolutiva y Algoritmos Genéticos siguen un hilo secuencial deliberado: desde la codificación de un individuo hasta operadores de cruce y mutación, pasando por variantes como ES, DE, NSGA-II y PSO. Esa linealidad es necesaria para construir intuición, pero obliga a dejar afuera todo lo que no encaja limpiamente en el recorrido obligatorio: problemas con restricciones duras, codificaciones mixtas, integración con pipelines de ML, y la tensión real entre la calidad de la solución y el tiempo de cómputo disponible.

Este espacio existe para cubrir ese margen.

Aquí se abordan proyectos **end-to-end con restricciones de ingeniería reales**. No se trata de demostrar que un GA converge en una función multimodal de juguete; se trata de decidir si un GA justifica su costo frente a una optimización bayesiana, de diseñar funciones de fitness que penalicen restricciones duras sin romper la selección, y de integrar la computación evolutiva como **wrapper** de modelos clásicos de ML, no como reemplazo de ellos.

No hay un orden de lectura impuesto. Cada notebook es autocontenido y referencia explícitamente qué conocimiento previo asume. La única condición es haber transitado los notebooks del capítulo que se indiquen como prerrequisito.

## Qué se encontrará aquí

- **Optimización combinatoria con restricciones:** Problemas de scheduling y planificación donde el espacio de búsqueda es discreto y las restricciones duras (penalización estricta) coexisten con las blandas (preferencias suaves). Diseño de fitness que no permita soluciones inválidas sin dejar de explorar.
- **Metaheurísticas como wrapper de ML:** *Feature Selection* con cromosomas binarios y Optimización de Hiperparámetros con codificación mixta (enteros, reales, categóricos). La pregunta central no es "¿funciona?" sino "¿justifica su costo frente a Optuna o RandomizedSearchCV?".
- **Modelado de sistemas físicos:** Identificación de sistemas dinámicos a partir de datos de sensores con ruido inyectado. Uso de NSGA-II para balancear el error de ajuste (RMSE) vs. la complejidad del modelo (orden de H(s)).
- **Ingeniería de características automatizada:** Programación Genética para la creación de nuevas variables predictivas interpretables. Pipeline híbrido: GP construye características, GA selecciona las mejores, y un modelo clásico de ML clasifica.

---

*Nota: Esta sección está pensada para quienes terminan un notebook del capítulo y se quedan con ganas de más. No reemplaza al material principal ni lo complementa como si fuera un apéndice de relleno. Cada caso tiene valor propio y fue incluido porque genuinamente aporta perspectiva que el recorrido secuencial no da: cómo una metaheurística bien diseñada resuelve un problema que un optimizador de gradiente no puede ni siquiera plantear. Si llegaste hasta acá, probablemente estás construyendo el tipo de criterio que caracteriza a un buen ingeniero.*
