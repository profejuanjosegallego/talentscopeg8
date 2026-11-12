from pathlib import Path

from talentscope.scraping.portal_scraper import parsear_detalle, parsear_listado

FIXTURES = Path(__file__).parent / "fixtures"


def test_parsear_listado_devuelve_20_ofertas():
    html = (FIXTURES / "listado_pagina1.html").read_text(encoding="utf-8")
    ofertas = parsear_listado(html)
    assert len(ofertas) == 20
    assert ofertas[0]["id_oferta"] == "ET-10450"
    assert ofertas[0]["titulo"] == "Desarrollador Python Junior"


def test_parsear_detalle_extrae_skills_modalidad_y_descripcion():
    html = (FIXTURES / "detalle_oferta.html").read_text(encoding="utf-8")
    detalle = parsear_detalle(html)
    assert detalle["skills"] == "JavaScript|React|Java"
    assert detalle["modalidad"] == "Remoto"
    assert detalle["descripcion"].startswith("En Retail Andino buscamos")


def test_parsear_detalle_sin_skills_ni_modalidad_devuelve_vacios():
    detalle = parsear_detalle("<div class='card detalle'><h1>Oferta</h1></div>")
    assert detalle == {"skills": "", "modalidad": "", "descripcion": ""}


def test_parsear_detalle_quita_espacios_de_las_skills():
    html = '<ul class="skills"><li>  Docker </li><li>\n  AWS \n</li></ul>'
    detalle = parsear_detalle(html)
    assert detalle["skills"] == "Docker|AWS"


def test_parsear_detalle_ignora_skills_vacias():
    html = '<ul class="skills"><li></li><li>Git</li><li>   </li></ul>'
    detalle = parsear_detalle(html)
    assert detalle["skills"] == "Git"


def test_parsear_detalle_limpia_espacios_de_la_modalidad():
    html = '<dd class="modalidad">   Híbrido  </dd>'
    detalle = parsear_detalle(html)
    assert detalle["modalidad"] == "Híbrido"

