import argparse
import sys
import nbformat
from pathlib import Path

def clean_notebook(nb_path):
    """
    Limpia todos los outputs y metadata de ejecución de un notebook.
    Útil si se decide no versionar los notebooks ejecutados, o para resetear el estado.
    """
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        modified = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if cell.outputs:
                    cell.outputs = []
                    modified = True
                if cell.execution_count is not None:
                    cell.execution_count = None
                    modified = True
                    
        if modified:
            with open(nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f"# {nb_path} limpiado.")
        else:
            print(f"# {nb_path} ya estaba limpio.")
            
        return True
        
    except Exception as e:
        print(f"-- Error limpiando {nb_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Limpia los outputs de los Jupyter Notebooks.")
    parser.add_argument('path', nargs='?', default='notebooks', help="Ruta al archivo o directorio a limpiar.")
    args = parser.parse_args()
    
    target_path = Path(args.path)
    
    if not target_path.exists():
        repo_root = Path(__file__).parent.parent
        target_path = repo_root / args.path
        if not target_path.exists():
            print(f"Error: No se encontró la ruta {args.path}")
            sys.exit(1)

    notebooks_to_clean = []
    
    if target_path.is_file() and target_path.suffix == '.ipynb':
        notebooks_to_clean.append(target_path)
    elif target_path.is_dir():
        notebooks_to_clean = list(target_path.rglob('*.ipynb'))
    else:
        print(f"Error: {target_path} no es un archivo .ipynb ni un directorio.")
        sys.exit(1)
        
    if not notebooks_to_clean:
        print(f"No se encontraron notebooks en {target_path}")
        sys.exit(0)
        
    print(f"Limpiando outputs de {len(notebooks_to_clean)} notebooks...")
    
    all_success = True
    for nb_path in notebooks_to_clean:
        if not clean_notebook(nb_path):
            all_success = False
            
    if not all_success:
        print("\n--  Ocurrieron errores al limpiar algunos notebooks.")
        sys.exit(1)
        
    print("\n# Limpieza completada.")
    sys.exit(0)

if __name__ == "__main__":
    main()