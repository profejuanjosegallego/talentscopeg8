"""Funciones puras de limpieza. Son las más fáciles de probar: ¡escribe tests!"""
import logging
import re
import unicodedata

import pandas as pd

log = logging.getLogger(__name__)

ALIAS_CIUDAD = {
    "bogota": "Bogotá",
    "medellin": "Medellín",
    "cali": "Cali",
    "barranquilla": "Barranquilla",
    "b/quilla": "Barranquilla",
    "remoto": "Remoto",
    "remote": "Remoto",
    "teletrabajo": "Remoto",
}


def normalizar_ciudad(texto):
    """Devuelve el nombre canónico de la ciudad: Bogotá, Medellín, Cali, Barranquilla o Remoto."""
    if pd.isna(texto):
        return None
    nombre = texto.strip()
    normalizado = unicodedata.normalize("NFD", nombre.casefold())
    normalizado = "".join(
        caracter
        for caracter in normalizado
        if unicodedata.category(caracter) != "Mn"
    )
    tokens = re.findall(r"[a-z0-9]+(?:/[a-z0-9]+)?", normalizado)
    for token in tokens:
        ciudad = ALIAS_CIUDAD.get(token)
        if ciudad is not None:
            return ciudad
    log.warning("Ciudad no reconocida: %s", texto)
    return nombre.title()


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
