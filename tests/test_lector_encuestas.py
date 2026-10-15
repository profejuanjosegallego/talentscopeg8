from talentscope.config import DATA_RAW_EXCEL
from talentscope.excel.lector_encuestas import leer_encuesta_uniandina


def test_uniandina_tiene_columnas_del_contrato():
    df = leer_encuesta_uniandina(DATA_RAW_EXCEL / "encuesta_salarial_uniandina_2026.xlsx")
    for col in ["rol", "anios_experiencia", "salario_mensual_cop", "ciudad", "skills"]:
        assert col in df.columns, f"falta la columna {col} (ver BUG-02)"


def test_uniandina_no_incluye_fila_de_total():
    df = leer_encuesta_uniandina(DATA_RAW_EXCEL / "encuesta_salarial_uniandina_2026.xlsx")
    assert len(df) == 86          # 85 respuestas + 1 duplicada (la validación la marca después)
