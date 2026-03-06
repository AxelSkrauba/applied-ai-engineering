import sys
import importlib
import importlib.metadata
import platform
import pandas as pd
from IPython.display import display

def get_imported_packages_versions():
    """
    Devuelve un diccionario con versiones de los paquetes importados 
    durante la sesión actual de Python.
    """
    versions = {}
    
    # Paquetes a ignorar por ser internos/builtins muy básicos de python
    ignore_packages = {'sys', 'os', 'pathlib', 'importlib', 'subprocess', 'platform', 'builtins', 'typing'}

    for module_name, module in sys.modules.items():
        if module_name.startswith("_"):
            continue

        root_package = module_name.split(".")[0]

        if root_package in versions or root_package in ignore_packages:
            continue

        version = None

        # Try __version__
        if hasattr(module, "__version__"):
            version = getattr(module, "__version__")

        # Fallback to importlib.metadata
        if version is None:
            try:
                version = importlib.metadata.version(root_package)
            except importlib.metadata.PackageNotFoundError:
                pass

        if version is not None:
            versions[root_package] = version

    return dict(sorted(versions.items()))

def print_environment():
    """
    Imprime los paquetes importados y sus versiones junto con la información del sistema.
    """
    print("=" * 40)
    print("Environment Information")
    print("=" * 40)
    print(f"Python:   {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print("-" * 40)
    
    packages = get_imported_packages_versions()
    for pkg, version in packages.items():
        print(f"{pkg:20s} {version}")
    print("=" * 40)

def environment_table():
    """
    Muestra una tabla HTML estilizada con los paquetes importados y sus versiones,
    junto con información del sistema, adecuada para Jupyter Notebooks.
    """
    packages = get_imported_packages_versions()
    
    df = pd.DataFrame(
        list(packages.items()),
        columns=["Package", "Version"]
    )
    
    # Inserta información del sistema como filas en la parte superior
    sys_info = pd.DataFrame([
        {"Package": "Python", "Version": sys.version.split()[0]},
        {"Package": "Platform", "Version": platform.platform()}
    ])
    
    df = pd.concat([sys_info, df], ignore_index=True)
    
    # Estilo de la tabla para Jupyter
    styled_df = df.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#f4f4f4'), ('color', '#333'), ('font-weight', 'bold'), ('text-align', 'left')]},
        {'selector': 'td', 'props': [('text-align', 'left')]}
    ]).hide(axis="index").set_caption("Reproducibility Environment Information")
    
    display(styled_df)
