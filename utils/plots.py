import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def setup_plot_style():
    """
    Configura el estilo visual estándar para todas las gráficas del repositorio.
    Debe llamarse al inicio de cada notebook.
    """
    # Estilo general
    sns.set_theme(style="whitegrid", palette="deep")
    
    # Configuraciones específicas de matplotlib
    plt.rcParams.update({
        "figure.figsize": (10, 6),
        "figure.dpi": 100,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "axes.labelweight": "bold",
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "legend.fontsize": 11,
        "legend.title_fontsize": 12,
        "lines.linewidth": 2.5,
        "lines.markersize": 8,
        "font.family": "sans-serif",
    })

def plot_confusion_matrix(y_true, y_pred, classes=None, title="Matriz de Confusión", cmap="Blues", normalize=False):
    """
    Renderiza una matriz de confusión estética y estandarizada.
    
    Parámetros:
    -----------
    y_true : array-like
        Etiquetas verdaderas.
    y_pred : array-like
        Etiquetas predichas.
    classes : list, opcional
        Nombres de las clases. Si es None, se infieren de los datos.
    title : str
        Título del gráfico.
    cmap : str
        Colormap de seaborn/matplotlib.
    normalize : bool
        Si es True, muestra porcentajes en lugar de conteos absolutos.
    """
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_true, y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fmt = '.2%'
    else:
        fmt = 'd'
        
    if classes is None:
        classes = np.unique(np.concatenate((y_true, y_pred)))
        
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(cm, annot=True, fmt=fmt, cmap=cmap,
                     xticklabels=classes, yticklabels=classes,
                     cbar_kws={'label': 'Escala'})
    
    plt.title(title, pad=20)
    plt.ylabel('Etiqueta Verdadera')
    plt.xlabel('Etiqueta Predicha')
    plt.tight_layout()
    plt.show()

def render_classification_report(y_true, y_pred, classes=None):
    """
    Genera y muestra un reporte de clasificación en formato de tabla HTML estética
    en lugar del texto plano de scikit-learn.
    """
    from sklearn.metrics import classification_report
    import pandas as pd
    from IPython.display import display
    
    report_dict = classification_report(y_true, y_pred, target_names=classes, output_dict=True)
    df_report = pd.DataFrame(report_dict).transpose()
    
    # Formateo
    styled_df = df_report.style.format({
        'precision': '{:.4f}',
        'recall': '{:.4f}',
        'f1-score': '{:.4f}',
        'support': '{:.0f}'
    }).background_gradient(cmap='Blues', subset=['precision', 'recall', 'f1-score']) \
      .set_caption("Reporte de Clasificación")
      
    display(styled_df)
