"""Funciones puras de limpieza. Son las más fáciles de probar: ¡escribe tests!"""
import re
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

    # Si el valor está vacío (NaN o None), no hay salario
    if pd.isna(texto):
        return (None, None, None)

    # Buscamos los números dentro del texto, ej: "4.500.000" o "1,100"
    numeros = re.findall(r"\d[\d.,]*", texto)
    if not numeros:                       # "A convenir", "Confidencial"
        return (None, None, None)
    
    if "millones" in texto.lower():
        # Millones: la coma es decimal, ej: "4,5" -> 4500000
        valores = [int(round(float(n.replace(",", ".")) * 1_000_000)) for n in numeros]
        moneda = "COP"
    elif "USD" in texto.upper():
        # Dólares: la coma separa miles, ej: "1,100" -> 1100
        valores = [int(n.replace(",", "")) for n in numeros]
        moneda = "USD"
    else:
        # Pesos: el punto separa miles, ej: "4.500.000" -> 4500000
        valores = [int(n.replace(".", "")) for n in numeros]
        moneda = "COP"

    return (valores[0], valores[-1], moneda)   # con un solo número, mínimo = máximo
