from pathlib import Path
from urllib.robotparser import RobotFileParser


from talentscope.scraping.portal_scraper import parsear_listado, puede_descargar

ROBOTS = Path(__file__).parents[1] / "portal_mock" / "robots.txt"

FIXTURES = Path(__file__).parent / "fixtures"


def test_parsear_listado_devuelve_20_ofertas():
    html = (FIXTURES / "listado_pagina1.html").read_text(encoding="utf-8")
    ofertas = parsear_listado(html)
    assert len(ofertas) == 20
    assert ofertas[0]["id_oferta"] == "ET-10450"
    assert ofertas[0]["titulo"] == "Desarrollador Python Junior"

def test_robots_prohibe_admin_y_permite_ofertas():
  rp = RobotFileParser()
  rp.parse(ROBOTS.read_text(encoding="utf-8").splitlines())
  assert not puede_descargar(rp, "http://127.0.0.1:8000/admin/panel.html")
  assert puede_descargar(rp, "http://127.0.0.1:8000/ofertas/pagina-1.html")
