"""
Reporte semanal para el cliente.

Estado (Sprint 0, equipo anterior): prototipo que funcionaba "en el PC de Andrés".
  - BUG-03: ruta absoluta quemada y el conteo de skills está mal.
  - Sin gráficos ni salarios.                 -> ver HU-80..82 (Squad D) y HU-50..54 (Squad C)
"""
from collections import Counter
from datetime import date
from pathlib import Path

import pandas as pd

from talentscope.config import DATA_SAMPLE

RUTA_OFERTAS = "C:/Users/andres.dev/Desktop/talentscope/data/sample/ofertas_sample.csv"


def top_skills(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    contador = Counter()
    for celda in df["skills"].dropna():
        # FIXME BUG-03: el contrato de datos dice que las skills van separadas por "|"
        contador.update(celda.split(","))
    return pd.DataFrame(contador.most_common(n), columns=["skill", "ofertas"])


def generar_reporte(salida="reporte_semanal.xlsx"):
    df = pd.read_csv(RUTA_OFERTAS)
    top_skills(df).to_excel(salida, index=False)
    print(f"Reporte generado: {salida}")

def reporte_excel(tablas: dict[str, pd.DataFrame], carpeta: Path, dia: date) -> Path:  # HU-82
    ruta = Path(carpeta) / f"reporte_semanal_{dia.isoformat()}.xlsx"
    with pd.ExcelWriter(ruta) as writer:
        for nombre, tabla in tablas.items():
            tabla.to_excel(writer, sheet_name=nombre, index=False)
    return ruta

def tablas_temporales() -> dict[str, pd.DataFrame]:  # HU-82
    ofertas = pd.read_csv(DATA_SAMPLE / "ofertas_sample.csv")
    encuestas = pd.read_csv(DATA_SAMPLE / "encuestas_sample.csv")
    top = (ofertas["skills"].str.split("|").explode().value_counts()
           .rename_axis("skill").reset_index(name="ofertas"))
    salarios = encuestas.groupby("rol")["salario_mensual_cop"].median().reset_index()
    resumen = pd.DataFrame({
        "indicador": ["Total de ofertas", "Total de encuestas"],
        "valor": [len(ofertas), len(encuestas)],
    })
    return {"Resumen": resumen, "Top skills": top, "Salarios": salarios, "Datos": ofertas}

if __name__ == "__main__":
    generar_reporte()
