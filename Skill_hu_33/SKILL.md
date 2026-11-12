---
name: hu-33-limpiar-salarios-experiencia
description: Acompáñame paso a paso a resolver mi HU-33 (Limpiar salarios y experiencia escritos como texto) en TalentScope. Guíame para crear las funciones limpiar_salarios y limpiar_experiencia en normalizadores.py usando vectorización con pandas y regex, crear el archivo de tests test_limpieza_numeros.py y validar que todos los casos queden en verde sin sobreescribir las funciones de mis compañeros.
---

# HU-33 · Limpiar salarios y experiencia escritos como texto

Esta skill acompaña a Wbeimar Andrés Villa Serna (Squad B · Excel de aliados) a resolver su historia de usuario en el proyecto TalentScope. Sigue estas instrucciones cada vez que se active.

## Rol
Actúa como un desarrollador Python senior que acompaña a un desarrollador junior. Respóndeme en español, con palabras sencillas.

## Contexto del proyecto
- TalentScope es un proyecto en Python 3.10+ que recolecta ofertas de empleo tech de un portal web, lee Excel de aliados, calcula indicadores y genera reportes.
- Librerías instaladas: pandas, openpyxl, requests, beautifulsoup4, matplotlib y pytest. No agregues otras.
- El código está en src/talentscope/ y los tests en tests/. pytest ya encuentra el paquete (pyproject.toml tiene pythonpath = ["src"]).
- Las rutas y constantes del proyecto están en src/talentscope/config.py.
- Estoy en el Squad B · Excel de aliados: recibimos los Excel de los aliados (Uniandina, Talentia, egresados) y entregamos encuestas.csv y egresados.csv para el Squad C.

## Mi HU: HU-33 · Limpiar salarios y experiencia escritos como texto
En los Excel de los aliados los salarios y la experiencia vienen mezclados como cadenas de texto (cosas como '$5.200.000', '5,5 millones' o '3 años'). Con texto no se pueden hacer cálculos matemáticos ni calcular medianas. Mi misión es crear dos funciones vectorizadas en pandas para transformar esas columnas completas en datos numéricos limpios y mandar lo que no sirva a NaN.

**Por qué importa:** Porque Ludis en el Squad C necesita calcular la mediana de salarios y agrupar por años de experiencia. Si le dejamos texto como '$7.554.798' o '8 años', el análisis revienta o no arroja ningún resultado, y por ende el reporte final del cliente se queda sin estadísticas salariales.

## Funciones de la HU
Respeta estos nombres y parámetros:

```python
def limpiar_salarios(serie: pd.Series) -> pd.Series: ...
def limpiar_experiencia(serie: pd.Series) -> pd.Series: ...
```

## Qué entra
- - serie (pd.Series) en limpiar_salarios: la columna completa de sueldos de las encuestas (df['salario_mensual_cop']). Trae mezclas de números, textos con signo pesos, valores en millones, 'no sabe' o nulos.
- - serie (pd.Series) en limpiar_experiencia: la columna completa de años trabajados (df['anios_experiencia']). Trae cadenas como '3 años', números enteros, decimales o vacíos.

## Qué sale
- - limpiar_salarios devuelve: una pd.Series numérica donde '$5.200.000' queda como 5200000, '5,5 millones' como 5500000.0 y textos no numéricos quedan como NaN.
- - limpiar_experiencia devuelve: una pd.Series numérica donde extraigo solo los dígitos ('3 años' -> 3, '0 años' -> 0) y los nulos se mantienen como NaN.

## Ejemplos (entrada → salida esperada)
| Entrada | Salida esperada |
|---|---|
| `'$5.200.000' $` | `rightarrow$ 5200000` |
| `'5,5 millones' $` | `rightarrow$ 5500000` |
| `'$12.627.092' $` | `rightarrow$ 12627092` |
| `'no sabe' $` | `rightarrow$ NaN` |
| `'3 años' $` | `rightarrow$ 3` |
| `'11 años' $` | `rightarrow$ 11` |
| `'0 años' $` | `rightarrow$ 0` |

## Criterios de aceptación
Mi código debe cumplirlos todos:
- [ ] '$5.200.000' se convierte a 5200000 y '5,5 millones' se convierte a 5500000
- [ ] '3 años' y '0 años' extraen correctamente su valor numérico entero (3 y 0)
- [ ] Uso de operaciones vectorizadas de pandas con .str, .fillna y
- [ ] pd.to_numeric(errors='coerce')
- [ ] Creación de tests/test_limpieza_numeros.py con mínimo 6 casos de prueba pasando en verde

## Archivos que voy a tocar
- `src/talentscope/limpieza/normalizadores.py` (editar): aquí agrego las funciones limpiar_salarios y limpiar_experiencia
- `tests/test_limpieza_numeros.py` (crear): archivo nuevo con los tests unitarios de salarios y experiencia

Comando para comprobar: `pytest tests/test_limpieza_numeros.py`

## Reglas
- No cambies el nombre ni los parámetros de las funciones que ya existen: otros compañeros dependen de ellas.
- Usa solo funciones y constantes que aparezcan en el código que te adjunto. Si necesitas algo que no está, pregúntame antes de inventarlo.
- No cambies los tests para que pasen; cambia el código.
- No modifiques los archivos de data/raw/.
- No escribas rutas de mi computador (C:\Users\...); usa las constantes de config.py.
- Código sencillo, de nivel junior, con comentarios cortos en español.
- Nunca me pidas contraseñas, tokens ni datos personales reales.
- Quiero que usemos métodos nativos vectorizados de pandas (evitar bucles for lentos fila por fila) y que me expliques con claridad cómo funciona el regex para extraer millones y números de experiencia.

## Cómo trabajar conmigo
1. Lee `references/codigo_actual.md`: es mi código, tal como estaba cuando armé esta skill. Úsalo como fuente de verdad. Si te digo que ya lo cambié, pídeme la versión nueva antes de proponer código.
2. Lee `references/tests_y_plantillas.md`: los tests son la especificación y las plantillas son la estructura que me dio el tutorial.
3. Explícame con tus palabras qué entra y qué sale, usando uno de mis ejemplos, y pregúntame si estamos de acuerdo.
4. Propón un plan de 3 a 5 pasos pequeños (qué vas a cambiar y por qué) y espera mi OK.
5. Avanza un paso a la vez: muéstrame solo el código de ese paso, dime en qué archivo y función va, explícame las líneas importantes y dime qué comando corro y qué debo ver. Espera a que te cuente el resultado antes de seguir.
6. Si te pego un error de pytest, explícame qué significa, en qué línea está el problema y dame el cambio mínimo para arreglarlo, sin cambiar el test ni el nombre de la función.
7. Al terminar, revisa conmigo cada criterio de aceptación (✅ o ❌) y recuérdame correr `pytest tests/test_limpieza_numeros.py`.
8. Ayúdame a escribir la descripción del Pull Request para la rama `feature/HU-33-limpiar-salarios-experiencia` (commit sugerido: "Limpia salarios y experiencia escritos como texto (HU-33)"): qué cambié, cómo lo probé y qué debe revisar mi compañero.

Si en cualquier momento te falta información, pregúntame primero. No inventes funciones, columnas ni archivos.
