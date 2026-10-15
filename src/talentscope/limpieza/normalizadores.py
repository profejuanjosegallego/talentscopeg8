"""Funciones puras de limpieza. Son las más fáciles de probar: ¡escribe tests!"""
import pandas as pd


def normalizar_ciudad(texto):
    """Devuelve el nombre canónico de la ciudad: Bogotá, Medellín, Cali, Barranquilla o Remoto."""
    if pd.isna(texto):
        return None
    t = texto.strip().lower()
    # FIXME BUG-01: solo cubre algunos casos. Falla con "Bogotá D.C.", "MEDELLIN",
    # "medellín - Antioquia", "Santiago de Cali", "Teletrabajo"... (ver tests)
    if t == "bogota":
        return "Bogotá"
    if t == "medellin":
        return "Medellín"
    if t == "remoto":
        return "Remoto"
    return texto


def parsear_salario(texto):
    """
    Convierte el texto del salario en (minimo, maximo, moneda).

    Ejemplos esperados (HU-13):
        "$ 4.500.000 - 6.000.000 COP"   -> (4500000, 6000000, "COP")
        "$4.500.000"                    -> (4500000, 4500000, "COP")
        "USD 1,100 - 1,500 / mes"       -> (1100, 1500, "USD")
        "4,5 a 6,1 millones"            -> (4500000, 6100000, "COP")
        "A convenir"                    -> (None, None, None)
    """
    raise NotImplementedError("HU-13: pendiente")
