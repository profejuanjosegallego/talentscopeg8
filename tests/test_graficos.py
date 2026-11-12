import pandas as pd

from talentscope.reportes.graficos import barras_top_skills


def test_barras_top_skills_crea_png(tmp_path):
    top = pd.DataFrame({"skill": ["A", "B"], "ofertas": [5, 3]})
    ruta = barras_top_skills(top, tmp_path)
    assert ruta.exists()
    assert ruta.suffix == ".png"

    