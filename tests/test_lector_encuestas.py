from talentscope.config import DATA_RAW_EXCEL
from talentscope.excel.lector_encuestas import leer_encuesta_uniandina, leer_estudio_talentia


def test_uniandina_tiene_columnas_del_contrato():
    df = leer_encuesta_uniandina(DATA_RAW_EXCEL / "encuesta_salarial_uniandina_2026.xlsx")
    for col in ["rol", "anios_experiencia", "salario_mensual_cop", "ciudad", "skills"]:
        assert col in df.columns, f"falta la columna {col} (ver BUG-02)"


def test_uniandina_no_incluye_fila_de_total():
    df = leer_encuesta_uniandina(DATA_RAW_EXCEL / "encuesta_salarial_uniandina_2026.xlsx")
    assert len(df) == 86          # 85 respuestas + 1 duplicada (la validación la marca después)


TALENTIA = DATA_RAW_EXCEL / "estudio_salarios_talentia_Q3.xlsx"


def test_talentia_une_las_3_ciudades():
    df = leer_estudio_talentia(TALENTIA)
    assert len(df) == 73
    assert df["ciudad"].value_counts().to_dict() == {"Cali": 29, "Bogotá": 23, "Medellín": 21}


def test_talentia_sin_fila_total_y_con_columnas_del_contrato():
    df = leer_estudio_talentia(TALENTIA)
    assert not df["rol"].astype(str).str.upper().eq("TOTAL").any()
    for col in ["rol", "anios_experiencia", "salario_mensual_cop", "skills", "ciudad", "fuente"]:
        assert col in df.columns