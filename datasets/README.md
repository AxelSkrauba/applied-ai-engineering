Este directorio está reservado para almacenar conjuntos de datos (datasets) que se consideren pequeños (estrictamente **menores a 20MB**) para evitar sobrecargar el repositorio y respetar los límites de GitHub.

Para datasets más grandes, el código dentro de los notebooks se encarga de descargarlos dinámicamente desde fuentes externas, según el caso (Kaggle, Google Drive, etc.).

## Reglas
1. **Límite de tamaño:** < 20MB por archivo.
2. **Subdirectorios:** Cada dataset debe estar en su propio subdirectorio con un README propio.
2. **Documentación:** Cada dataset debe incluir un breve comentario en su README, detallando su origen (referencia a la fuente original), el significado de las columnas y el contexto disponible.
3. **Formato:** Preferentemente `.csv`, `.parquet`, o `.json`. Si amerita, omprimidos en `.zip` para eficiencia en la transferencia.
