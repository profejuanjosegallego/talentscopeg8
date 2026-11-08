from pathlib import Path

from talentscope.scraping.portal_scraper import parsear_listado, url_siguiente

FIXTURES = Path(__file__).parent / "fixtures"


def test_parsear_listado_devuelve_20_ofertas():
    html = (FIXTURES / "listado_pagina1.html").read_text(encoding="utf-8")
    ofertas = parsear_listado(html)
    assert len(ofertas) == 20
    assert ofertas[0]["id_oferta"] == "ET-10450"
    assert ofertas[0]["titulo"] == "Desarrollador Python Junior"

def test_url_siguiente_en_pagina_1():
    html = (FIXTURES / "listado_pagina1.html").read_text(encoding="utf-8")
    assert url_siguiente(html, "http://127.0.0.1:8000/ofertas/pagina-1.html") == \
        "http://127.0.0.1:8000/ofertas/pagina-2.html"

def test_url_siguiente_en_la_ultima_es_none():
    html = (FIXTURES / "listado_ultima.html").read_text(encoding="utf-8")
    assert url_siguiente(html, "http://127.0.0.1:8000/ofertas/pagina-6.html") is None
