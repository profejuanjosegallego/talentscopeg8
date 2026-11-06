"""
Lectura de las encuestas salariales que envían los aliados del cliente.

Estado (Sprint 0, equipo anterior):
  - Solo existe el lector de Universidad Andina y tiene un bug (BUG-02).
  - Falta el lector de Talentia (una hoja por ciudad).        -> ver HU-31
"""
import pandas as pd

COLUMNAS_UNIANDINA = {
    "Cargo actual": "rol",
    "Años de experiencia": "anios_experiencia",
    "Salario mensual (COP)": "salario_mensual_cop",
    "Ciudad": "ciudad",
    "Tecnologías que usa": "skills",
    "Modalidad": "modalidad",
}


def leer_encuesta_uniandina(ruta) -> pd.DataFrame:
    # FIXME BUG-02: el archivo trae un título y notas arriba; los encabezados reales
    # están en la fila 4 de Excel. Así como está, las columnas salen como "Unnamed: 1"...
    df = pd.read_excel(ruta, sheet_name="Respuestas")
    df = df.rename(columns=COLUMNAS_UNIANDINA)
    df["fuente"] = "uniandina"
    return df

COLUMNAS_TALENTIA = {
    "Rol": "rol",
    "Exp (años)": "anios_experiencia",
    "Sueldo": "salario_mensual_cop",
    "Stack": "skills",
    "¿Remoto?": "remoto",
}


def leer_estudio_talentia(ruta) -> pd.DataFrame:
    hojas = pd.read_excel(ruta, sheet_name=None)
    partes = []
    for nombre, df in hojas.items():
        if nombre == "Notas":
            continue
        df = df.dropna(how="all")
        df = df[~df["Rol"].astype(str).str.strip().str.upper().str.startswith("TOTAL")]
        df = df.assign(ciudad=nombre)
        partes.append(df)
    todo = pd.concat(partes, ignore_index=True)
    todo = todo.rename(columns=COLUMNAS_TALENTIA)
    todo["fuente"] = "talentia"
    return todo