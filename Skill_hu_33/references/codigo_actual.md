# Mi código actual · HU-33

Así estaba mi código cuando armé la skill. Si ya lo cambié, te pego la versión nueva.

## src/talentscope/limpieza/normalizadores.py
```python
"""Tests para la limpieza de salarios y experiencia (HU-33)."""
import math
import pandas as pd

from talentscope.limpieza.normalizadores import limpiar_experiencia, limpiar_salarios


def test_limpiar_salarios():
    s = pd.Series(["$5.200.000", "5,5 millones", 7586721, "no sabe", None, "$12.627.092"])
    r = limpiar_salarios(s)
    assert r[0] == 5200000
    assert r[1] == 5500000
    assert r[2] == 7586721
    assert math.isnan(r[3])
    assert math.isnan(r[4])
    assert r[5] == 12627092


def test_limpiar_experiencia():
    s = pd.Series(["3 años", 7, "11 años", 5.0, None, "0 años"])
    r = limpiar_experiencia(s)
    assert r.tolist()[:4] == [3, 7, 11, 5]
    assert math.isnan(r[4])
    assert r[5] == 0
def limpiar_salarios(serie: pd.Series) -> pd.Series:
    """
    '$5.200.000' -> 5200000, '5,5 millones' -> 5500000. Lo que no se entiende queda NaN.
    """
    ya_numero = pd.to_numeric(serie, errors="coerce")
    texto = serie.astype(str).str.lower()

Manejo de formatos tipo pesos: quita '$', '.', espacios
    pesos = pd.to_numeric(texto.str.replace(r"[$.\s]", "", regex=True), errors="coerce")

Manejo de formatos en millones: '5,5 millones' -> 5.5 * 1_000_000 = 5500000
    millones_raw = texto.str.extract(r"([\d,]+)\smillones")[0]
    millones_val = pd.to_numeric(
        millones_raw.str.replace(",", ".", regex=False), errors="coerce"
    ) 1_000_000

    return ya_numero.fillna(pesos).fillna(millones_val)


def limpiar_experiencia(serie: pd.Series) -> pd.Series:
    """
    '3 años' -> 3, 7 -> 7. Lo que no tiene número queda NaN.
    """
    digitos = serie.astype(str).str.extract(r"(\d+)")[0]
    return pd.to_numeric(digitos, errors="coerce")
```
