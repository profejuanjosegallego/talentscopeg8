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

def limpiar_salarios(serie: pd.Series) -> pd.Series:
    """'$5.200.000' -> 5200000, '5,5 millones' -> 5500000. Lo que no se entiende queda NaN."""
    ya_numero = pd.to_numeric(serie, errors="coerce")           # 7586721 ya sirve
    texto = serie.astype(str).str.lower()
    pesos = pd.to_numeric(texto.str.replace(r"[$.\s]", "", regex=True), errors="coerce")
    # 👉 TU CÓDIGO AQUÍ: millones = texto.str.extract(r"([\d,]+)\s*millones")[0]
    #    luego coma por punto, pd.to_numeric(..., errors="coerce") y por 1_000_000
    millones = ...
    return ya_numero.fillna(pesos).fillna(millones)


def limpiar_experiencia(serie: pd.Series) -> pd.Series:
    """'3 años' -> 3, 7 -> 7. Lo que no tiene número queda NaN."""
    # 👉 TU CÓDIGO AQUÍ: saca el primer grupo de dígitos y conviértelo a número
    #    pista: serie.astype(str).str.extract(r"(\d+)")[0], luego pd.to_numeric(..., errors="coerce")