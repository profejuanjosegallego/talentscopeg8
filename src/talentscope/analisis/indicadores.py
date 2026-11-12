"""Indicadores del Squad C: convierten los datos limpios en respuestas para el cliente."""
import pandas as pd


def rango_experiencia(anios: pd.Series) -> pd.Series:  # HU-51
    """Clasifica los años de experiencia en los rangos "0-1", "2-4" y "5+"."""
    return pd.cut(anios, bins=[-1, 1, 4, float("inf")], labels=["0-1", "2-4", "5+"])


def resumen_salarios_por_rol(encuestas: pd.DataFrame) -> pd.DataFrame:  # HU-51
    """Mediana, percentil 25 y percentil 75 del salario por rol (columnas: rol, mediana, p25, p75)."""
    return encuestas.groupby("rol").agg(
        mediana=("salario_mensual_cop", "median"),
        p25=("salario_mensual_cop", lambda s: s.quantile(0.25)),
        p75=("salario_mensual_cop", lambda s: s.quantile(0.75)),
    ).reset_index()


def salario_por_rol_y_experiencia(encuestas: pd.DataFrame) -> pd.DataFrame:  # HU-51
    """Tabla rol x rango de experiencia con la mediana del salario; vacía (NaN) si no hay datos."""
    datos = encuestas.assign(rango=rango_experiencia(encuestas["anios_experiencia"]))
    return datos.pivot_table(index="rol", columns="rango", values="salario_mensual_cop",
                             aggfunc="median", observed=False)