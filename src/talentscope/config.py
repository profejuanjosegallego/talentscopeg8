"""Rutas y parámetros compartidos del proyecto."""
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
