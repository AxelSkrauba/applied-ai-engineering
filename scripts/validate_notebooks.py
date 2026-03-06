import argparse
import sys
import nbformat
from pathlib import Path

def validate_notebook(nb_path):
    """
    Realiza una validación estructural rápida de un notebook.
    Retorna True si es válido, False en caso contrario.
    """
    try:
        # Intentar leer el notebook
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        errors = []
        
        # 1. Verificar celdas vacías
        for i, cell in enumerate(nb.cells):
            if not cell.source.strip():
                errors.append(f"Celda {i} está vacía.")
                
        # 2. (Opcional) Verificar otras reglas...
        # Por ejemplo, que la primera celda sea de tipo markdown (título)
        if not nb.cells:
            errors.append("El notebook no tiene celdas.")
        elif nb.cells[0].cell_type != 'markdown':
            errors.append("La primera celda debería ser Markdown (para el título).")
            
        if errors:
            print(f"-- {nb_path} tiene errores de formato:")
            for e in errors:
                print(f"  - {e}")
            return False
            
        print(f"# {nb_path} es válido.")
        return True
        
    except Exception as e:
        print(f"-- Error crítico leyendo {nb_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Validación rápida de formato de Jupyter Notebooks.")
    parser.add_argument('path', nargs='?', default='notebooks', help="Ruta al archivo o directorio a validar.")
    args = parser.parse_args()
    
    target_path = Path(args.path)
    
    # Determinar si el script se llama desde la raíz del repo o desde la carpeta scripts
    # Si la ruta proporcionada no existe relativamente, probamos con la raíz del repo
    if not target_path.exists():
        repo_root = Path(__file__).parent.parent
        target_path = repo_root / args.path
        if not target_path.exists():
            print(f"Error: No se encontró la ruta {args.path}")
            sys.exit(1)

    notebooks_to_check = []
    
    if target_path.is_file() and target_path.suffix == '.ipynb':
        notebooks_to_check.append(target_path)
    elif target_path.is_dir():
        notebooks_to_check = list(target_path.rglob('*.ipynb'))
        # Excluir la carpeta _templates
        notebooks_to_check = [nb for nb in notebooks_to_check if '_templates' not in nb.parts]
    else:
        print(f"Error: {target_path} no es un archivo .ipynb ni un directorio.")
        sys.exit(1)
        
    if not notebooks_to_check:
        print(f"No se encontraron notebooks en {target_path}")
        sys.exit(0)
        
    print(f"Validando {len(notebooks_to_check)} notebooks...")
    
    all_valid = True
    for nb_path in notebooks_to_check:
        if not validate_notebook(nb_path):
            all_valid = False
            
    if not all_valid:
        print("\n--  La validación falló. CORREGIR los errores.")
        sys.exit(1)
        
    print("\n# Todos los notebooks PASARON la validación rápida.")
    sys.exit(0)

if __name__ == "__main__":
    main()
