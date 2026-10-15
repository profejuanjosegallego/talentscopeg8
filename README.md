# TalentScope · Observatorio del mercado laboral tech

**Cliente:** Red de Empleabilidad Universitaria (ficticio)
**Proveedor:** DataNexo S.A.S. (ustedes)
**Estado:** en curso · versión 0.3.0 · Sprint 0 cerrado por el equipo anterior

## El problema del cliente

La oficina de empleabilidad quiere responder cada semana tres preguntas:

1. ¿Qué habilidades están pidiendo las empresas para cargos de tecnología?
2. ¿Cuánto se paga por cada rol, ciudad y nivel de experiencia?
3. ¿Qué tan alineados están nuestros programas académicos con eso?

Hoy lo hacen a mano: copian ofertas de portales de empleo y juntan Excel que les mandan
universidades aliadas y consultoras, cada uno en un formato distinto. Tardan dos días por semana.

## Lo que ya existe (Sprint 0)

El equipo anterior dejó un prototipo y fue reasignado. **No está disponible para preguntas.**

| Módulo | Estado |
|---|---|
| `scraping/portal_scraper.py` | Lee solo la página 1 del portal. Sin timeout. |
| `excel/lector_encuestas.py` | Solo lee Universidad Andina y lo hace mal (BUG-02). |
| `limpieza/normalizadores.py` | `normalizar_ciudad` incompleta, `parsear_salario` sin implementar. |
| `reportes/reporte_semanal.py` | Ruta quemada del PC del dev anterior, conteo de skills erróneo. |
| `pipeline.py` | CLI con etapas sueltas, sin orquestación. |
| `tests/` | **14 tests en rojo.** Cada uno corresponde a un bug o HU del backlog. |

## Arranque rápido

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (Linux/Mac: source .venv/bin/activate)
python -m pip install --upgrade pip   # sin esto, "pip install -e ." falla con el pip que trae Python 3.10
pip install -r requirements.txt
pip install -e .

pytest                            # verás tests en rojo: es el punto de partida

# en otra terminal: levantar el portal de empleos simulado
python -m http.server 8000 --directory portal_mock
# abrir http://127.0.0.1:8000

python -m talentscope.pipeline scraping
python -m talentscope.pipeline excel
```

## Estructura

```
talentscope/
├── portal_mock/            Portal EmpleosTech simulado (HTML estático) para scraping
├── data/
│   ├── raw/excel/          Excel tal como los mandan los aliados (¡no editarlos a mano!)
│   ├── referencia/         Catálogo de skills y planes de estudio
│   ├── sample/             Datos LIMPIOS de ejemplo que cumplen el contrato
│   └── processed/          Salidas del pipeline (no se versionan)
├── src/talentscope/        Código Python
├── tests/                  pytest
├── api/                    API Spring Boot (la crea el Squad C, HU-65 y HU-66)
└── docs/                   Onboarding, contrato de datos, backlog
```

## Cómo trabajamos

- Lean primero [`docs/ONBOARDING.md`](docs/ONBOARDING.md).
- El backlog está en [`docs/BACKLOG.md`](docs/BACKLOG.md).
- Los squads se comunican a través del [contrato de datos](docs/CONTRATO_DATOS.md). Si necesitan cambiarlo, se negocia en el refinamiento, no por WhatsApp.
