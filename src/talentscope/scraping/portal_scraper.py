"""
Scraper del portal EmpleosTech.

Estado (Sprint 0, equipo anterior):
  - Descarga y parsea SOLO la primera página del listado.   -> ver HU-10
  - No entra al detalle de cada oferta (faltan skills).      -> ver HU-11
  - No tiene timeout, reintentos ni pausa entre peticiones.  -> ver BUG-04
"""
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
import pandas as pd
import requests
from bs4 import BeautifulSoup

from talentscope.config import DATA_PROCESSED, PAUSA_SEGUNDOS, PORTAL_URL, USER_AGENT

def cargar_robots(url_inicial: str) -> RobotFileParser:
    """Descarga y lee el robots.txt del sitio una sola vez."""
    rp = RobotFileParser()
    rp.set_url(urljoin(url_inicial, "/robots.txt"))
    rp.read()
    return rp

def puede_descargar(rp: RobotFileParser, url: str) -> bool:
    """Dice si el robots.txt permite que nuestro bot visite esa url."""
    return rp.can_fetch(USER_AGENT, url)

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


def scrapear(url_inicial: str = PORTAL_URL) -> pd.DataFrame:
    # Leemos las reglas del portal una sola vez, al comienzo
    rp = cargar_robots(url_inicial)
    # Si el robots.txt pide una pausa (Crawl-delay), la usamos; si no, la de config
    pausa = rp.crawl_delay(USER_AGENT) or PAUSA_SEGUNDOS

    # Antes de descargar, revisamos que esté permitido
    if not puede_descargar(rp, url_inicial):
        print(f"robots.txt no permite {url_inicial}: se salta")
        return pd.DataFrame()

    time.sleep(pausa)  # pausa para no saturar el portal
    html = descargar(url_inicial)
    ofertas = parsear_listado(html)
    # TODO HU-10: seguir el enlace "Siguiente" hasta la última página.
    return pd.DataFrame(ofertas)


def guardar(df: pd.DataFrame) -> None:
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    # TODO HU-15: deduplicar por id_oferta y no pisar el histórico.
    df.to_csv(DATA_PROCESSED / "ofertas_crudas.csv", index=False, encoding="utf-8")
