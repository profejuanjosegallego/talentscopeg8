from pathlib import Path

from talentscope.scraping.portal_scraper import parsear_listado

FIXTURES = Path(__file__).parent / "fixtures"


def test_parsear_listado_devuelve_20_ofertas():
    html = (FIXTURES / "listado_pagina1.html").read_text(encoding="utf-8")
    ofertas = parsear_listado(html)
    assert len(ofertas) == 20
    assert ofertas[0]["id_oferta"] == "ET-10450"
    assert ofertas[0]["titulo"] == "Desarrollador Python Junior"
