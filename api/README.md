# API TalentScope (Spring Boot) · dueño: Squad C

Esta carpeta está vacía a propósito: el Squad C crea el proyecto en la HU-65 con
[Spring Initializr](https://start.spring.io) (Maven, Java 17+, Spring Web, Spring Boot DevTools).

## Contrato acordado con el cliente

### `GET /api/skills/top?n=10&rol=`

```json
{
  "generado": "2026-10-15T08:00:00",
  "fuente": "ofertas",
  "total_ofertas": 118,
  "items": [
    {"skill": "Python", "ofertas": 41, "porcentaje": 34.7},
    {"skill": "SQL", "ofertas": 38, "porcentaje": 32.2}
  ]
}
```

### `GET /api/salarios?rol=Analista%20de%20Datos&ciudad=Bogotá`

```json
{"rol": "Analista de Datos", "ciudad": "Bogotá", "n": 23,
 "mediana": 4100000, "p25": 3500000, "p75": 5200000, "moneda": "COP"}
```

Si no hay datos: `404` con `{"error": "No hay datos para rol=... ciudad=..."}`.

### `GET /api/brecha?programa=Analítica%20de%20Datos` (reto opcional)

```json
{"programa": "Analítica de Datos",
 "faltantes": [{"skill": "AWS", "demanda_pct": 21.4}],
 "poco_demandadas": [{"skill": "Excel", "demanda_pct": 3.1}]}
```

## Fuente de datos

La API lee `../data/processed/talentscope.db` (SQLite) con JdbcTemplate y el driver `org.xerial:sqlite-jdbc`.
Esa base la genera el Squad D (HU-94) con `DataFrame.to_sql`; las tablas son `top_skills`, `salarios_por_rol`,
`ofertas`, `encuestas`, `egresados` y `brecha`. Mientras HU-94 no esté lista, pídele al docente la base de la
versión de referencia para desarrollar.
