from datetime import date

import pytest

from talentscope.limpieza.normalizadores import parsear_fecha_publicacion

HOY = date(2026, 10, 15)


@pytest.mark.parametrize("texto, esperado", [
    ("Hoy", "2026-10-15"),
    ("Hace 8 días", "2026-10-07"),
    ("Hace 1 día", "2026-10-14"),
    ("29/09/2026", "2026-09-29"),
])
def test_parsear_fecha(texto, esperado):
    assert parsear_fecha_publicacion(texto, HOY) == esperado
