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