import pandas as pd

from talentscope.analisis.indicadores import rango_experiencia, resumen_salarios_por_rol


def test_rangos_en_los_bordes():
    r = rango_experiencia(pd.Series([0, 1, 2, 4, 5, 9]))
    assert list(r) == ["0-1", "0-1", "2-4", "2-4", "5+", "5+"]


def test_resumen_por_rol():
    df = pd.DataFrame({"rol": ["A"] * 4, "salario_mensual_cop": [1, 2, 3, 100]})
    fila = resumen_salarios_por_rol(df).iloc[0]
    assert fila["mediana"] == 2.5
    assert list(resumen_salarios_por_rol(df).columns) == ["rol", "mediana", "p25", "p75"]