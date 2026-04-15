import os
import yaml
from pathlib import Path

def get_notebook_files(directory, base_dir):
    """
    Obtiene los archivos .ipynb directos de un directorio (sin recursión),
    ordenados alfabéticamente (lo que garantiza el orden por prefijo numérico).
    Excluye directorios que comiencen con '_' como _templates.
    Usado para recoger notebooks planos dentro de un capítulo o sub-sección.
    """
    paths = []
    for entry in sorted(os.scandir(directory), key=lambda e: e.name):
        if entry.name.startswith('_'):
            continue
        if entry.is_file() and entry.name.endswith('.ipynb'):
            rel_path = os.path.relpath(entry.path, start=base_dir)
            paths.append(str(Path(rel_path).with_suffix('')).replace('\\', '/'))
    return paths


def get_chapter_sections(chapter_dir, base_dir):
    """
    Genera la lista de secciones para un capítulo dado, distinguiendo entre:
    - Archivos .ipynb directos: se añaden como entradas planas (comportamiento anterior).
    - Subdirectorios con intro.md: se añaden como sub-secciones anidadas y colapsables
      en el sidebar del libro (ej: carpeta 'aplicaciones/' dentro de un capítulo).
    Los subdirectorios sin intro.md se ignoran con una advertencia.
    El orden alfabético se preserva entre archivos y subdirectorios conjuntamente.
    """
    sections = []
    for entry in sorted(os.scandir(chapter_dir), key=lambda e: e.name):
        if entry.name.startswith('_'):
            continue

        if entry.is_dir():
            sub_intro = Path(entry.path) / 'intro.md'
            if sub_intro.exists():
                rel_intro = os.path.relpath(sub_intro, start=base_dir)
                sub_dict = {
                    'file': str(Path(rel_intro).with_suffix('')).replace('\\', '/')
                }
                sub_notebooks = get_notebook_files(entry.path, base_dir)
                if sub_notebooks:
                    sub_dict['sections'] = [{'file': nb} for nb in sub_notebooks]
                sections.append(sub_dict)
            else:
                print(f"Advertencia: subdirectorio '{entry.name}' en '{chapter_dir.name}' no tiene intro.md — ignorado.")

        elif entry.is_file() and entry.name.endswith('.ipynb'):
            rel_path = os.path.relpath(entry.path, start=base_dir)
            sections.append({'file': str(Path(rel_path).with_suffix('')).replace('\\', '/')})

    return sections


def get_dataset_readmes(directory, base_dir):
    """
    Obtiene los README.md dentro de la carpeta de datasets.
    """
    paths = []
    for entry in sorted(os.scandir(directory), key=lambda e: e.name):
        if entry.is_dir():
            readme_path = Path(entry.path) / 'README.md'
            if readme_path.exists():
                rel_path = os.path.relpath(readme_path, start=base_dir)
                paths.append(str(Path(rel_path).with_suffix('')).replace('\\', '/'))
    return paths

def generate_toc():
    """
    Genera el archivo _toc.yml leyendo la estructura de la carpeta notebooks y datasets.
    """
    base_dir = Path(__file__).parent.parent
    notebooks_dir = base_dir / 'notebooks'
    datasets_dir = base_dir / 'datasets'

    if not notebooks_dir.exists():
        print(f"Error: No se encontró el directorio {notebooks_dir}")
        return

    # La estructura base del TOC
    toc = {
        'format': 'jb-book',
        'root': 'README',
        'chapters': []
    }

    # Procesar cada subdirectorio de primer nivel en notebooks/
    for chapter_dir in sorted(notebooks_dir.iterdir()):
        if chapter_dir.is_dir() and not chapter_dir.name.startswith('_'):
            # Buscar el intro.md del capítulo
            intro_file = chapter_dir / 'intro.md'
            chapter_dict = {}

            if intro_file.exists():
                rel_intro = os.path.relpath(intro_file, start=base_dir)
                chapter_dict['file'] = str(Path(rel_intro).with_suffix('')).replace('\\', '/')
            else:
                print(f"Advertencia: No se encontró intro.md en {chapter_dir.name}")
                continue

            # Obtener las secciones del capítulo (notebooks planos y sub-secciones anidadas)
            sections = get_chapter_sections(chapter_dir, base_dir)
            if sections:
                chapter_dict['sections'] = sections
                
            toc['chapters'].append(chapter_dict)
            
    # Añadir sección de Datasets como Anexo
    if datasets_dir.exists():
        dataset_intro = datasets_dir / 'README.md'
        if dataset_intro.exists():
            ds_dict = {}
            rel_intro = os.path.relpath(dataset_intro, start=base_dir)
            ds_dict['file'] = str(Path(rel_intro).with_suffix('')).replace('\\', '/')
            
            readmes = get_dataset_readmes(datasets_dir, base_dir)
            if readmes:
                ds_dict['sections'] = [{'file': rm} for rm in readmes]
                
            toc['chapters'].append(ds_dict)

    # Escribir el _toc.yml en la raíz del proyecto
    toc_path = base_dir / '_toc.yml'

    # Custom dumper para evitar referencias (alias) en el YAML y mantener el orden
    class NoAliasDumper(yaml.SafeDumper):
        def ignore_aliases(self, data):
            return True

    with open(toc_path, 'w', encoding='utf-8') as f:
        f.write("# Auto-generated by scripts/generate_toc.py\n")
        yaml.dump(toc, f, Dumper=NoAliasDumper, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
    print(f"Generado exitosamente: {toc_path}")

if __name__ == '__main__':
    generate_toc()