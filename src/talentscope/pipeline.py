"""
Punto de entrada único del proyecto.

    python -m talentscope.pipeline scraping
    python -m talentscope.pipeline excel
    python -m talentscope.pipeline reporte
    python -m talentscope.pipeline todo        # HU-88 (Squad D, Sprint 2)
"""
import argparse
import logging
from datetime import date

from talentscope.config import DATA_RAW_EXCEL, CARPETA_LOGS, DATA_RAW_EXCEL

log = logging.getLogger("talentscope")

def configurar_logging():
    # Crea la carpeta logs/ si no existe (si ya existe, no da error)
    CARPETA_LOGS.mkdir(exist_ok=True)
    # Un archivo por día, por ejemplo: talentscope_2026-11-12.log
    ruta_del_log = CARPETA_LOGS / f"talentscope_{date.today().isoformat()}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),                           # a la pantalla
            logging.FileHandler(ruta_del_log, encoding="utf-8"),  # al archivo
        ],
    )

def etapa_scraping():
    from talentscope.scraping import portal_scraper
    df = portal_scraper.scrapear()
    portal_scraper.guardar(df)
    log.info("Scraping: %s ofertas", len(df))


def etapa_excel():
    from talentscope.excel.lector_encuestas import leer_encuesta_uniandina
    df = leer_encuesta_uniandina(DATA_RAW_EXCEL / "encuesta_salarial_uniandina_2026.xlsx")
    log.info("Excel: %s filas leídas. Columnas: %s", len(df), list(df.columns))


def etapa_reporte():
    from talentscope.reportes.reporte_semanal import generar_reporte
    generar_reporte()


ETAPAS = {"scraping": etapa_scraping, "excel": etapa_excel, "reporte": etapa_reporte}


def main():
    configurar_logging()  # un solo lugar para configurar el logging
    parser = argparse.ArgumentParser(description="Pipeline TalentScope")
    parser.add_argument("etapa", choices=[*ETAPAS, "todo"])
    args = parser.parse_args()
    if args.etapa == "todo":
        raise NotImplementedError("HU-88: orquestar las tres etapas con manejo de errores")
    ETAPAS[args.etapa]()


if __name__ == "__main__":
    main()
