from datetime import date
from pathlib import Path

from talentscope.config import carpeta_reporte_del_dia


def test_crea_carpeta_con_la_fecha(tmp_path):
    carpeta = carpeta_reporte_del_dia(date(2026, 10, 28), base=tmp_path)
    assert carpeta == tmp_path / "2026-10-28"  # el nombre es AAAA-MM-DD
    assert carpeta.exists()  # la carpeta quedó creada
    assert isinstance(carpeta, Path)  # devuelve un Path


def test_llamarla_dos_veces_no_falla(tmp_path):
    primera = carpeta_reporte_del_dia(date(2026, 10, 28), base=tmp_path)
    segunda = carpeta_reporte_del_dia(date(2026, 10, 28), base=tmp_path)  # misma fecha
    assert primera == segunda
    assert segunda.is_dir()