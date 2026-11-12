"""
Scraper del portal EmpleosTech.

Estado (Sprint 0, equipo anterior):
  - Descarga y parsea SOLO la primera página del listado.   -> ver HU-10
  - Entra al detalle de cada oferta: skills, modalidad y descripción (HU-11).
  - No tiene timeout, reintentos ni pausa entre peticiones.  -> ver BUG-04
"""
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

from talentscope.config import DATA_PROCESSED, PORTAL_URL, USER_AGENT


def descargar(url: str) -> str:
    # FIXME BUG-04: sin timeout. Si el servidor no responde, el proceso se queda colgado.
    respuesta = requests.get(url, headers={"User-Agent": USER_AGENT})
    return respuesta.text


def parsear_listado(html: str) -> list[dict]:
    """Convierte el HTML de una página de listado en una lista de diccionarios."""
    soup = BeautifulSoup(html, "html.parser")
    ofertas = []
    for tarjeta in soup.select("article.oferta"):
        enlace = tarjeta.select_one("h2.titulo a")
        ofertas.append({
            "id_oferta": tarjeta["id"],
            "titulo": enlace.get_text(strip=True),
            "url_detalle": enlace["href"],
            "empresa": tarjeta.select_one(".empresa").get_text(strip=True),
            "ciudad": tarjeta.select_one(".ciudad").get_text(strip=True),
            "salario_texto": tarjeta.select_one(".salario").get_text(strip=True),
            "fecha_texto": tarjeta.select_one(".fecha").get_text(strip=True),
        })
    return ofertas


def _texto(soup: BeautifulSoup, selector: str) -> str:
    """Texto limpio del primer elemento que cumple el selector, o "" si no existe."""
    elemento = soup.select_one(selector)
    return elemento.get_text(strip=True) if elemento else ""


def parsear_detalle(html: str) -> dict:
    """Extrae skills, modalidad y descripción del HTML del detalle de una oferta.

    Las skills se unen con "|" como pide el contrato de datos (ej. "JavaScript|React|Java").
    """
    soup = BeautifulSoup(html, "html.parser")
    skills = [li.get_text(strip=True) for li in soup.select("ul.skills li")]
    return {
        "skills": "|".join(s for s in skills if s),
        "modalidad": _texto(soup, ".modalidad"),
        "descripcion": _texto(soup, ".descripcion"),
    }


def scrapear(url_inicial: str = PORTAL_URL) -> pd.DataFrame:
    html = descargar(url_inicial)
    ofertas = parsear_listado(html)
    # HU-11: entrar al detalle de cada oferta para sacar skills, modalidad y descripción
    for oferta in ofertas:
        url_detalle = urljoin(url_inicial, oferta["url_detalle"])  # ../oferta/ET-10450.html → URL completa
        oferta.update(parsear_detalle(descargar(url_detalle)))
    # TODO HU-10: seguir el enlace "Siguiente" hasta la última página.
    return pd.DataFrame(ofertas)


def guardar(df: pd.DataFrame) -> None:
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    # TODO HU-15: deduplicar por id_oferta y no pisar el histórico.
    df.to_csv(DATA_PROCESSED / "ofertas_crudas.csv", index=False, encoding="utf-8")
