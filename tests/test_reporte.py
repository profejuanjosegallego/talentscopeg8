from datetime import date

import pandas as pd

from talentscope.reportes.reporte_semanal import reporte_excel, top_skills


def test_top_skills_separa_por_barra():
    df = pd.DataFrame({"skills": ["Java|SQL", "Java|Docker", "Python"]})
    top = top_skills(df, n=1)
    assert top.iloc[0]["skill"] == "Java"
    assert top.iloc[0]["ofertas"] == 2


def test_reporte_excel_con_fecha_y_hojas(tmp_path):
    tablas = {"Resumen": pd.DataFrame({"a": [1]}), "Datos": pd.DataFrame({"b": [2]})}
    ruta = reporte_excel(tablas, tmp_path, date(2026, 10, 28))
    assert ruta.name == "reporte_semanal_2026-10-28.xlsx"
    with pd.ExcelFile(ruta) as libro:
        assert libro.sheet_names == ["Resumen", "Datos"]