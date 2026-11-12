# Tests y plantillas de la HU-33

## Tests que mi código debe pasar
Son la especificación. No se cambian para que pasen; se cambia el código.

### tests/test_limpieza_numeros.py
```python
import math

import pandas as pd

from talentscope.limpieza.normalizadores import limpiar_experiencia, limpiar_salarios


def test_limpiar_salarios():
    s = pd.Series(["$5.200.000", "5,5 millones", 7586721, "no sabe", None, "$12.627.092"])
    r = limpiar_salarios(s)
    assert r[0] == 5200000
    assert r[1] == 5500000
    assert r[2] == 7586721
    assert math.isnan(r[3]) and math.isnan(r[4])
    assert r[5] == 12627092


def test_limpiar_experiencia():
    s = pd.Series(["3 años", 7, "11 años", 5.0, None, "0 años"])
    assert limpiar_experiencia(s).tolist()[:4] == [3, 7, 11, 5]
    assert math.isnan(limpiar_experiencia(s)[4])
    assert limpiar_experiencia(s)[5] == 0
```

## Estructura que me dio el tutorial
Se completa donde dice 👉 TU CÓDIGO AQUÍ. Respeta los nombres de funciones, parámetros y constantes.

### src/talentscope/limpieza/normalizadores.py
```python
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
```
