# Material de la clase · TalentScope

| Archivo | Qué es |
|---|---|
| `TalentScope_Kickoff.pptx` | La presentación del kickoff, incluidos los pasos de **Manos a la obra** |
| `TalentScope_presentacion.mp4` | El video de presentación del proyecto (3 min) |
| `calendario.html` | Calendario de clases: jueves de 6:30 a 9:00 p. m., dos virtuales y una presencial (aula 407) |
| `../docs/guia_tecnica.html` | Guía técnica: scraping, Excel con pandas, `to_excel`, tests |
| `../docs/BACKLOG.md` y `../docs/tablero.html` | Las HU de cada squad y sprint |

## Apenas clones

```bash
git clone [URL]
cd talentscope-estudiantes
code .                                # abre el proyecto en VS Code
```

Antes de instalar nada, en este orden:

1. Lee `README.md`, sección **“Lo que ya existe”**: es lo que dejó el equipo anterior.
2. Abre `docs/tablero.html` en el navegador y busca tu código (A1…D6).
3. Lee los criterios de aceptación de tu HU.

Reglas de la casa: no edites a mano los Excel de `data/raw/` y nunca subas la carpeta `.venv`.

## Instala y prueba, todos juntos

```bash
python --version                      # 3.10 o más nuevo
python -m venv .venv
.venv\Scripts\activate                # verás (.venv) al inicio de la línea
python -m pip install --upgrade pip   # ¡no te lo saltes!
pip install -r requirements.txt
pip install -e .
pytest                                # debe decir: 14 failed, 5 passed
```

En una **segunda terminal**, dentro de esta misma carpeta:

```bash
python -m http.server 8000 --directory portal_mock    # abre http://127.0.0.1:8000
```

De vuelta en la primera terminal, conoce lo que dejó el equipo anterior:

```bash
python -m talentscope.pipeline scraping    # solo trae 20 ofertas… ¿y las otras 98?
python -m talentscope.pipeline excel       # columnas "Unnamed" → BUG-02
python -m talentscope.pipeline reporte     # busca un archivo en el PC de Andrés → BUG-03
```

Después, busca tu HU en Kaizen y el archivo de tu squad (diapositiva “Encuentra tu HU en el código”).
