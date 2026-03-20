import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Sequence, Literal

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
        "figure.dpi": 150,
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
    Renderiza una matriz de confusión de calidad científica siguiendo principios de Data-Ink Ratio.
    
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
        Colormap de seaborn/matplotlib. Recomendado: 'Blues', 'Greens', 'cividis'.
    normalize : bool
        Si es True, muestra porcentajes en lugar de conteos absolutos.
    """
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(y_true, y_pred)
    
    if classes is None:
        classes = np.unique(np.concatenate((y_true, y_pred)))
    
    n_classes = len(classes)
    
    # Tamaño de figura adaptativo
    fig_size = max(6, min(12, n_classes * 1.5))
    
    # Tamaño de fuente adaptativo (más pequeño para matrices grandes)
    if n_classes <= 3:
        annot_fontsize = 16
        label_fontsize = 12
    elif n_classes <= 6:
        annot_fontsize = 14
        label_fontsize = 11
    else:
        annot_fontsize = 10
        label_fontsize = 10
    
    fig, ax = plt.subplots(figsize=(fig_size, fig_size * 0.85))
    
    # Normalización y formato
    if normalize:
        cm_display = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fmt = '.2%'
        cbar_label = 'Proporción'
    else:
        cm_display = cm
        fmt = 'd'
        cbar_label = 'Cantidad'
    
    # Crear heatmap
    sns.heatmap(
        cm_display, 
        annot=True, 
        fmt=fmt, 
        cmap=cmap,
        xticklabels=classes, 
        yticklabels=classes,
        cbar_kws={'label': cbar_label, 'shrink': 0.8},
        annot_kws={'fontsize': annot_fontsize, 'fontweight': 'bold'},
        linewidths=0.5,
        linecolor='white',
        square=True,
        ax=ax
    )
    
    # Mejorar contraste: texto blanco sobre celdas oscuras
    # Calcular umbral para cambiar color de texto
    threshold = cm_display.max() / 2.0
    for text in ax.texts:
        # Obtener coordenadas de la celda
        x, y = text.get_position()
        value = cm_display[int(y), int(x)]
        # Cambiar color según intensidad de fondo
        text.set_color('white' if value > threshold else 'black')
    
    # Etiquetas y título
    ax.set_ylabel('Etiqueta Verdadera', fontsize=label_fontsize, fontweight='bold')
    ax.set_xlabel('Etiqueta Predicha', fontsize=label_fontsize, fontweight='bold')
    ax.set_title(title, fontsize=label_fontsize + 2, fontweight='bold', pad=15)
    
    # Rotar etiquetas del eje X para mejor legibilidad
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    
    plt.tight_layout()
    plt.show()


def render_classification_report(
    y_true,
    y_pred,
    classes: Sequence[str] | None = None,
    *,
    caption: str = "Reporte de Clasificación",
    show_support: bool = False,
    highlight_best: bool = True,
    summary_row: Literal["weighted avg", "macro avg", "both"] | None = "weighted avg",
    digits: int = 2,
) -> None:
    """
    Muestra un reporte de clasificación en formato de tabla con calidad científica.

    Los colores de texto y fondo se heredan automáticamente del entorno Jupyter
    (compatible con tema claro y oscuro sin configuración adicional).

    Parámetros
    ----------
    y_true : array-like
        Etiquetas verdaderas.
    y_pred : array-like
        Etiquetas predichas.
    classes : list[str], opcional
        Nombres de las clases en orden. Si es None se infieren automáticamente.
    caption : str
        Texto de la leyenda (ej. "Table 2: Per-class metrics on ...").
    show_support : bool, default False
        Incluir columna de soporte. Generalmente omitida en papers.
    highlight_best : bool, default True
        Negrita sobre el valor máximo por columna (solo clases individuales).
    summary_row : "weighted avg" | "macro avg" | "both" | None
        Fila de resumen a mostrar.
    digits : int, default 2
        Decimales (2 = estándar papers, 3 = técnico).
    """

    import uuid

    import pandas as pd
    from IPython.display import display, HTML
    from sklearn.metrics import classification_report

    # DataFrame
    report_dict = classification_report(
        y_true, y_pred,
        target_names=classes,
        output_dict=True,
        zero_division=0,
    )
    df = pd.DataFrame(report_dict).T

    _skip = {"accuracy", "macro avg", "weighted avg"}
    class_rows = [r for r in df.index if r not in _skip]

    if summary_row == "both":
        summary_keys = [k for k in ["macro avg", "weighted avg"] if k in df.index]
    elif summary_row in _skip and summary_row in df.index:
        summary_keys = [summary_row]
    else:
        summary_keys = []

    col_rename = {"precision": "Precision", "recall": "Recall", "f1-score": "F-score"}
    cols_show  = list(col_rename.values())
    if show_support:
        col_rename["support"] = "Support"
        cols_show.append("Support")

    df_classes = df.loc[class_rows].rename(columns=col_rename)[cols_show]
    df_summary = (
        df.loc[summary_keys].rename(columns=col_rename)[cols_show]
        if summary_keys else pd.DataFrame()
    )

    fmt = f"{{:.{digits}f}}"

    # Redondear antes de comparar para evitar errores de precisión flotante
    best: dict[str, float] = {}
    if highlight_best:
        for col in ["Precision", "Recall", "F-score"]:
            if col in df_classes.columns:
                best[col] = round(df_classes[col].max(), digits)

    # HTML
    def _td(val: float, col: str) -> str:
        if col == "Support":
            return f"<td>{int(val)}</td>"
        s = fmt.format(val)
        is_best = col in best and round(val, digits) == best[col]
        return f'<td class="b">{s}</td>' if is_best else f"<td>{s}</td>"

    def _tr(label: str, series: pd.Series, summary: bool = False) -> str:
        tds = "".join(_td(series[c], c) for c in cols_show)
        cls = ' class="sep"' if summary else ""
        return f"<tr{cls}><td>{label}</td>{tds}</tr>"

    ths   = "".join(f"<th>{c}</th>" for c in cols_show)
    thead = f"<thead><tr><th>Class</th>{ths}</tr></thead>"

    rows = [_tr(idx, df_classes.loc[idx]) for idx in df_classes.index]
    summary_labels = {"weighted avg": "Avg.", "macro avg": "Macro Avg."}
    for i, idx in enumerate(df_summary.index if not df_summary.empty else []):
        rows.append(_tr(summary_labels.get(idx, idx), df_summary.loc[idx], summary=(i == 0)))

    tbody = "<tbody>" + "".join(rows) + "</tbody>"

    # CSS con uid como atributo directo en la tabla
    # Se usa un atributo data-* único como selector para aislar los estilos
    uid = uuid.uuid4().hex[:10]

    css = f"""
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── wrapper ── */
div[data-clf="{uid}"] {{
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 11pt;
  line-height: 1.6;
  max-width: 580px;
  margin: 1.2em 0;
  color: inherit;
}}

/* ── caption ── */
div[data-clf="{uid}"] .cap {{
  font-size: 10.5pt;
  font-style: italic;
  opacity: 0.75;
  margin-bottom: 6px;
  letter-spacing: 0.01em;
}}

/* ── tabla ── */
div[data-clf="{uid}"] table {{
  border-collapse: collapse;
  width: 100%;
  font-size: 11pt;
}}

/* ── toprule + midrule (thead) ── */
div[data-clf="{uid}"] thead th {{
  border-top: 2px solid currentColor;
  border-bottom: 1px solid currentColor;
  border-left: none;
  border-right: none;
  padding: 5px 16px;
  text-align: center;
  font-weight: 600;
  background: transparent !important;
  color: inherit;
  letter-spacing: 0.02em;
  white-space: nowrap;
}}

div[data-clf="{uid}"] thead th:first-child {{
  text-align: left;
  padding-left: 0;
}}

/* ── celdas del cuerpo ── */
div[data-clf="{uid}"] tbody td {{
  padding: 3.5px 16px;
  text-align: center;
  border: none !important;
  background: transparent !important;
  color: inherit;
  font-variant-numeric: tabular-nums;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 10.5pt;
}}

div[data-clf="{uid}"] tbody td:first-child {{
  text-align: left;
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 11pt;
  padding-left: 0;
}}

/* ── midrule antes del resumen ── */
div[data-clf="{uid}"] tr.sep td {{
  border-top: 1px solid currentColor !important;
  padding-top: 5px;
}}

/* ── bottomrule ── */
div[data-clf="{uid}"] tbody tr:last-child td {{
  border-bottom: 2px solid currentColor !important;
  padding-bottom: 5px;
}}

/* ── negrita para mejor valor ── */
div[data-clf="{uid}"] td.b {{
  font-weight: 700;
}}
"""

    html = f"""
<style>{css}</style>
<div data-clf="{uid}">
  <div class="cap">{caption}</div>
  <table>{thead}{tbody}</table>
</div>
"""
    display(HTML(html))
