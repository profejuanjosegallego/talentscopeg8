"""Rutas y parámetros compartidos del proyecto."""
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DATA_RAW_EXCEL = RAIZ / "data" / "raw" / "excel"
DATA_REFERENCIA = RAIZ / "data" / "referencia"
DATA_PROCESSED = RAIZ / "data" / "processed"
DATA_SAMPLE = RAIZ / "data" / "sample"
CARPETA_REPORTES = RAIZ / "reportes"

# Portal servido localmente con:  python -m http.server 8000 --directory portal_mock
PORTAL_URL = "http://127.0.0.1:8000/ofertas/pagina-1.html"
USER_AGENT = "TalentScopeBot/0.3 (proyecto educativo)"

def carpeta_reporte_del_dia(dia: date | None = None, base: Path = CARPETA_REPORTES) -> Path:
    """Crea y devuelve la carpeta del día: base/AAAA-MM-DD."""
    # Si no nos dan fecha, usamos la de hoy
    if dia is None:
        dia = date.today()
    carpeta = base / dia.isoformat()
    # parents=True crea "reportes" si no existe; exist_ok=True no falla si la carpeta ya existe
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta