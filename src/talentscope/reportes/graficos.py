"""Gráficos del proyecto (Squad D). Se guardan como PNG, sin abrir ventanas."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

def barras_top_skills(top, carpeta: Path) -> Path:  # HU-80
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top["skill"], top["ofertas"], color="#6a3fc9")
    ax.invert_yaxis()
    ax.set_title("Top 10 de skills más pedidas en ofertas de tecnología")
    ax.set_xlabel("Número de ofertas que piden la skill")
    ax.set_ylabel("Skill")
    fig.text(0.01, 0.01, "Fuente: ofertas_sample.csv (TalentScope)")
    ruta = Path(carpeta) / "top_skills.png"
    fig.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return ruta