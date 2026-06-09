# Optimización Evolutiva y Algoritmos Genéticos

Los capítulos anteriores nos enseñaron a construir modelos predictivos entrenados con descenso del gradiante y a ajustar sus hiperparámetros mediante búsquedas sistemáticas o bayesianas. Ese enfoque es poderoso cuando la función es diferenciable y el espacio de búsqueda es continuo y manejable. Pero la ingeniería real no siempre coopera: los problemas de *scheduling* son combinatorios, la selección de características es discreta, los sistemas multiobjetivo no admiten una única función de pérdida, y muchas funciones de costo son ruidosas, discontinuas o cuya evaluación requiere simulaciones costosas.

Este capítulo abre una caja de herramientas fundamentalmente diferente: **la optimización inspirada en la evolución biológica**. No se trata de abandonar el gradiente; se trata de entender exactamente en qué situaciones un Algoritmo Genético, una Estrategia Evolutiva o un Enjambre de Partículas justifican su costo computacional, y en cuáles una búsqueda en grilla o un optimizador bayesiano siguen siendo la decisión correcta de ingeniería.

Nuestro objetivo no es memorizar pseudocódigo de selección por ruleta; es desarrollar **criterio de ingeniería** para decidir cuándo una población de soluciones es mejor que un punto de inicio, cómo evitar la convergencia prematura sin recurrir a magia negra, y cómo aprovechar el ecosistema *open source* (DEAP) para resolver problemas complejos con fracciones del costo de implementación original.

## Contenido del Capítulo

- **Fundamentos y Primera Implementación:** Algoritmos Genéticos desde cero en Python puro. Codificación, selección, cruce y mutación. *Benchmarks* sistemáticos contra búsqueda por fuerza bruta y *Grid Search* para entender cuándo (y por qué) una población evolutiva justifica su costo.
- **Ecosistema DEAP y Variantes Evolutivas:** Transición del código artesanal al framework DEAP. Estrategias Evolutivas (ES) y Differential Evolution (DE) para optimización continua de alta dimensionalidad. NSGA-II para problemas multiobjetivo con frentes de Pareto. PSO como optimización por enjambre. Programación Genética para la evolución automática de estructuras simbólicas.
- **Aplicaciones de Ingeniería:** Resolución de problemas combinatorios reales (TSP y *Scheduling*), *Feature Selection*, Optimización de Hiperparámetros con DEAP integrado en sklearn e identificación de funciones de transferencia H(s) mediante DEAP y scipy, demostrando que las metaheurísticas no son simples juguetes académicos, sino herramientas capaces de resolver problemas de producción reales.

---

*Nota: Los algoritmos evolutivos tampoco son magia. Son búsqueda inteligente con más parámetros de control y una curva de convergencia mucho más traicionera que la de un optimizador de primer orden. Te recomendamos ejecutar cada notebook, modificar el tamaño de la población, variar la tasa de mutación y observar cómo una población converge prematuramente a un óptimo local o, peor aún, oscila sin progreso. Un buen ingeniero de IA sabe cuándo un Algoritmo Genético es la respuesta correcta y, lo que es más importante, sabe cuándo un simple Random Forest con RandomizedSearchCV sigue siendo la mejor decisión de producción.*
