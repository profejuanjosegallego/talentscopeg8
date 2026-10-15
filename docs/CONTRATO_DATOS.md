# Contrato de datos

Los squads se comunican **solo** a través de estos archivos. Mientras una fuente real no esté lista,
cada squad trabaja con los archivos de `data/sample/`, que ya cumplen el contrato.

Reglas generales: UTF-8, separador coma, fechas ISO `AAAA-MM-DD`, listas separadas por barra vertical
(`Python|SQL`), ciudades canónicas (`Bogotá`, `Medellín`, `Cali`, `Barranquilla`, `Remoto`).

## `data/processed/ofertas.csv` · dueño: Squad A

| Columna | Tipo | Ejemplo | Obligatoria |
|---|---|---|---|
| id_oferta | texto | ET-10450 | sí |
| fuente | texto | empleostech, fakejobs | sí |
| titulo | texto | Desarrollador Python Junior | sí |
| rol | texto | Desarrollador Python | sí |
| nivel | texto | Junior, Semi Senior, Senior | no |
| empresa | texto | AgroData | sí |
| ciudad | texto canónico | Medellín | sí |
| modalidad | texto | Presencial, Híbrido, Remoto | no |
| salario_min | entero | 4500000 | no |
| salario_max | entero | 6000000 | no |
| moneda | texto | COP, USD | si hay salario |
| fecha_publicacion | fecha | 2026-10-12 | sí |
| skills | lista | Python, SQL y Docker separados por barra | no |
| fecha_extraccion | fecha-hora | 2026-10-15T08:00:00 | sí |

## `data/processed/encuestas.csv` · dueño: Squad B

| Columna | Tipo | Ejemplo | Obligatoria |
|---|---|---|---|
| id_registro | texto | ENC-0001 | sí |
| fuente | texto | uniandina, talentia | sí |
| rol | texto | Analista de Datos | sí |
| anios_experiencia | entero | 3 | no |
| salario_mensual_cop | entero | 5200000 | sí |
| ciudad | texto canónico | Cali | no |
| skills | lista | Python y Pandas separados por barra | no |
| modalidad | texto | Remoto | no |

## `data/processed/egresados.csv` · dueño: Squad B

| Columna | Tipo | Ejemplo |
|---|---|---|
| programa | texto | Analítica de Datos |
| fecha_grado | fecha | 2025-06-15 |
| empleado | booleano | True |
| cargo | texto | Analista de Datos |
| salario | entero | 3600000 |
