import os
import zipfile
import pandas as pd

def load_dataset(dataset_path: str) -> pd.DataFrame:
    """
    Carga un dataset CSV, manejando automáticamente la descompresión si está en un archivo ZIP.
    Diseñado para funcionar tanto en local como en Google Colab.
    
    Args:
        dataset_path (str): Ruta relativa al archivo CSV desde la raíz del proyecto.
            Ejemplo: "datasets/acv/datos_acv.csv"
            
    Returns:
        pd.DataFrame: DataFrame de pandas con los datos cargados.
        
    Raises:
        FileNotFoundError: Si no se encuentra ni el CSV ni el ZIP correspondiente.
        Exception: Para otros errores durante la carga o descompresión.
    """
    # Construir la ruta completa del archivo CSV (asumiendo que el CWD es la raíz del repo)
    full_csv_path = os.path.join(os.getcwd(), dataset_path)
    
    # Derivar la ruta del archivo ZIP
    dataset_dir = os.path.dirname(full_csv_path)
    csv_filename_base = os.path.splitext(os.path.basename(full_csv_path))[0]
    zip_filename = csv_filename_base + ".zip"
    full_zip_path = os.path.join(dataset_dir, zip_filename)
    
    try:
        # Si el archivo CSV no existe, verificar y descomprimir el ZIP
        if not os.path.exists(full_csv_path):
            if os.path.exists(full_zip_path):
                print(f"Archivo CSV no encontrado. Descomprimiendo {full_zip_path}...")
                with zipfile.ZipFile(full_zip_path, 'r') as zip_ref:
                    zip_ref.extractall(dataset_dir)
                print("Descompresión completa. Intentando cargar el CSV.")
            else:
                # Si no hay CSV ni ZIP, intentar buscar relativo al directorio actual por si acaso
                # Esto es útil si el script se ejecuta desde una subcarpeta
                alt_csv_path = os.path.abspath(dataset_path)
                if os.path.exists(alt_csv_path):
                    full_csv_path = alt_csv_path
                else:
                    alt_zip_path = os.path.abspath(os.path.join(os.path.dirname(dataset_path), zip_filename))
                    if os.path.exists(alt_zip_path):
                        print(f"Archivo CSV no encontrado. Descomprimiendo {alt_zip_path}...")
                        with zipfile.ZipFile(alt_zip_path, 'r') as zip_ref:
                            zip_ref.extractall(os.path.dirname(alt_zip_path))
                        print("Descompresión completa. Intentando cargar el CSV.")
                        full_csv_path = alt_csv_path
                    else:
                        raise FileNotFoundError(f"Ni el archivo CSV ni el ZIP fueron encontrados en las rutas esperadas:\n- {full_csv_path}\n- {full_zip_path}")
        
        # Intentar cargar el CSV después de asegurar que existe
        dataset = pd.read_csv(full_csv_path)
        print(f"Dataset cargado exitosamente con {dataset.shape[0]} filas y {dataset.shape[1]} columnas.")
        return dataset
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar el dataset: {e}")
        raise
