import pandas as pd

from talentscope.reportes.reporte_semanal import top_skills


def test_top_skills_separa_por_barra():
    df = pd.DataFrame({"skills": ["Java|SQL", "Java|Docker", "Python"]})
    top = top_skills(df, n=1)
    assert top.iloc[0]["skill"] == "Java"
    assert top.iloc[0]["ofertas"] == 2
