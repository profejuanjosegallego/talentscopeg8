"""
Punto de entrada único del proyecto.

    python -m talentscope.pipeline scraping
    python -m talentscope.pipeline excel
    python -m talentscope.pipeline reporte
    python -m talentscope.pipeline todo        # HU-88 (Squad D, Sprint 2)
"""
import argparse
import logging

from talentscope.config import DATA_RAW_EXCEL

log = logging.getLogger("talentscope")


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
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Pipeline TalentScope")
    parser.add_argument("etapa", choices=[*ETAPAS, "todo"])
    args = parser.parse_args()
    if args.etapa == "todo":
        raise NotImplementedError("HU-88: orquestar las tres etapas con manejo de errores")
    ETAPAS[args.etapa]()


if __name__ == "__main__":
    main()
