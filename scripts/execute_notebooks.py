import argparse
import sys
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError
from pathlib import Path

def execute_notebook(nb_path):
    """
    Ejecuta un notebook completamente usando nbclient.
    """
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        print(f"Ejecutando {nb_path}...")
        client = NotebookClient(nb, timeout=600, kernel_name='python3')
        client.execute()
        print(f"# {nb_path} ejecutado exitosamente sin errores.")
        return True
        
    except CellExecutionError as e:
        print(f"-- Error ejecutando celda en {nb_path}:")
        print(e)
        return False
    except Exception as e:
        print(f"-- Error inesperado ejecutando {nb_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Ejecuta Jupyter Notebooks de principio a fin.")
    parser.add_argument('path', nargs='?', default='notebooks', help="Ruta al archivo o directorio a ejecutar.")
    args = parser.parse_args()
    
    target_path = Path(args.path)
    
    if not target_path.exists():
        repo_root = Path(__file__).parent.parent
        target_path = repo_root / args.path
        if not target_path.exists():
            print(f"Error: No se encontró la ruta {args.path}")
            sys.exit(1)

    notebooks_to_run = []
    
    if target_path.is_file() and target_path.suffix == '.ipynb':
        notebooks_to_run.append(target_path)
    elif target_path.is_dir():
        notebooks_to_run = list(target_path.rglob('*.ipynb'))
        # Excluir la carpeta _templates
        notebooks_to_run = [nb for nb in notebooks_to_run if '_templates' not in nb.parts]
    else:
        print(f"Error: {target_path} no es un archivo .ipynb ni un directorio.")
        sys.exit(1)
        
    if not notebooks_to_run:
        print(f"No se encontraron notebooks en {target_path}")
        sys.exit(0)
        
    print(f"Se encontraron {len(notebooks_to_run)} notebooks. Comenzando ejecución...")
    
    all_success = True
    for nb_path in notebooks_to_run:
        if not execute_notebook(nb_path):
            all_success = False
            
    if not all_success:
        print("\n--  Algunos notebooks fallaron durante la ejecución.")
        sys.exit(1)
        
    print("\n# Todos los notebooks se ejecutaron correctamente.")
    sys.exit(0)

if __name__ == "__main__":
    main()
