"""
Reporte semanal para el cliente.

Estado (Sprint 0, equipo anterior): prototipo que funcionaba "en el PC de Andrés".
  - BUG-03: ruta absoluta quemada y el conteo de skills está mal.
  - Sin gráficos ni salarios.                 -> ver HU-80..82 (Squad D) y HU-50..54 (Squad C)
"""
from collections import Counter

import pandas as pd

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


if __name__ == "__main__":
    generar_reporte()
