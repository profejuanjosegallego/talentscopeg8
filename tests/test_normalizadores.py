import pytest

from talentscope.limpieza.normalizadores import normalizar_ciudad, parsear_salario


@pytest.mark.parametrize("entrada, esperado", [
    ("Bogota", "Bogotá"),
    ("Medellin", "Medellín"),
    ("Remoto", "Remoto"),
    # --- casos que hoy fallan (BUG-01) ---
    ("Bogotá D.C.", "Bogotá"),
    ("BOGOTA", "Bogotá"),
    ("medellín - Antioquia", "Medellín"),
    ("Santiago de Cali", "Cali"),
    ("B/quilla", "Barranquilla"),
    ("Teletrabajo", "Remoto"),
    ("100% remoto", "Remoto"),
])
def test_normalizar_ciudad(entrada, esperado):
    assert normalizar_ciudad(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    ("$ 4.500.000 - 6.000.000 COP", (4500000, 6000000, "COP")),
    ("$4.500.000", (4500000, 4500000, "COP")),
    ("USD 1,100 - 1,500 / mes", (1100, 1500, "USD")),
    ("4,5 a 6,1 millones", (4500000, 6100000, "COP")),
    ("A convenir", (None, None, None)),
])
def test_parsear_salario(entrada, esperado):
    assert parsear_salario(entrada) == esperado
