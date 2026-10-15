# Backlog de TalentScope

> Generado desde `docs/backlog.json`. Lo mantiene el Product Owner (el docente). Si ves algo raro, avísalo en el daily.

## Sprint 0 (equipo anterior) (2026-09-17 → 2026-10-14)

**Objetivo:** Prototipo: scraper de una página, lector de una encuesta y reporte básico.

### HU-01 · Scraper básico del listado
`Squad A` · `3 pts` · `Hecha` · Asignado: **equipo anterior**

**Como** analista del cliente, **quiero** obtener las ofertas publicadas en EmpleosTech, **para** no copiarlas a mano.

Criterios de aceptación:
- [ ] Extrae título, empresa, ciudad, salario y fecha de la página 1
- [ ] Guarda un CSV en data/processed

### HU-02 · Lector de la encuesta Universidad Andina
`Squad B` · `2 pts` · `Hecha` · Asignado: **equipo anterior**

**Como** analista del cliente, **quiero** cargar la encuesta salarial de Universidad Andina, **para** usarla en el análisis.

Criterios de aceptación:
- [ ] Lee la hoja Respuestas
- [ ] Renombra columnas al contrato (tiene BUG-02)

### HU-03 · Prototipo de reporte semanal
`Squad C` · `2 pts` · `Hecha` · Asignado: **equipo anterior**

**Como** coordinador de empleabilidad, **quiero** un Excel con las skills más pedidas, **para** discutirlo en el comité.

Criterios de aceptación:
- [ ] Genera reporte_semanal.xlsx con top 10 skills (tiene BUG-03)

## Sprint 1 · Onboarding y deuda (2026-10-15 → 2026-10-28)

**Objetivo:** Entender el código heredado, corregir los bugs conocidos y dejar los tests en verde.

### BUG-04 · El scraper se puede colgar y daña las tildes
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A1**

**Como** equipo de desarrollo, **quiero** que el scraper no se quede esperando para siempre, **para** poder dejarlo corriendo solo.

Criterios de aceptación:
- [ ] requests.get usa timeout=10
- [ ] Si falla, reintenta hasta 3 veces con un for y time.sleep
- [ ] Las tildes salen bien: hoy el CSV trae MedellÃ­n en vez de Medellín (pista: response.encoding)
- [ ] Si después de 3 intentos no funciona, lanza una excepción con un mensaje claro

### HU-10 · Recorrer todas las páginas del listado
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A2**

**Como** analista del cliente, **quiero** las ofertas de todas las páginas, **para** no perder el 80% de los datos.

Criterios de aceptación:
- [ ] Sigue el enlace 'Siguiente' (a[rel=next]) hasta que no exista
- [ ] Arma la URL completa con urljoin
- [ ] Con el portal actual obtiene 118 ofertas
- [ ] Tiene un máximo de páginas para no quedar en un ciclo infinito

### HU-11 · Leer el detalle de cada oferta
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A3**

**Como** analista del cliente, **quiero** las habilidades y la modalidad de cada oferta, **para** saber qué tecnologías pide el mercado.

Criterios de aceptación:
- [ ] Función parsear_detalle(html) que devuelve skills, modalidad y descripción
- [ ] Las skills se unen con | (contrato de datos)
- [ ] Test con tests/fixtures/detalle_oferta.html

### HU-13 · Convertir el texto del salario en números
`Squad A` · `5 pts` · `Por hacer` · Asignado: **A4**

**Como** analista del cliente, **quiero** el salario como mínimo, máximo y moneda, **para** poder calcular medianas.

Criterios de aceptación:
- [ ] Implementa parsear_salario en limpieza/normalizadores.py
- [ ] Pasan los 5 casos de tests/test_normalizadores.py
- [ ] Agrega al menos 3 casos de prueba con formatos reales del portal

### HU-14 · Convertir la fecha de publicación
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A5**

**Como** analista del cliente, **quiero** fechas reales en formato AAAA-MM-DD, **para** saber qué tan recientes son las ofertas.

Criterios de aceptación:
- [ ] Convierte 'Hoy', 'Hace N días' y 'dd/mm/aaaa'
- [ ] Recibe la fecha de hoy como parámetro para poder probarla
- [ ] Un test por cada formato

### HU-12 · Scraping responsable
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A6**

**Como** equipo de desarrollo, **quiero** respetar las reglas del portal, **para** no saturarlo ni ser bloqueados.

Criterios de aceptación:
- [ ] Lee robots.txt con urllib.robotparser y no descarga lo prohibido
- [ ] Pausa configurable entre peticiones (0.1 s por defecto, o el Crawl-delay si existe)
- [ ] User-Agent que identifica al proyecto
- [ ] Explica en el README por qué se hace cada cosa

### BUG-02 · El lector de Universidad Andina toma mal los encabezados
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B1**

**Como** analista del cliente, **quiero** que la encuesta se cargue con las columnas correctas, **para** no perder respuestas.

Criterios de aceptación:
- [ ] Pasan los 2 tests de tests/test_lector_encuestas.py
- [ ] Excluye la fila 'Total respuestas'
- [ ] Usa header= de pd.read_excel (no editar el Excel a mano)

### HU-31 · Lector del estudio Talentia (una hoja por ciudad)
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B2**

**Como** analista del cliente, **quiero** cargar el estudio de Talentia, **para** tener más datos salariales.

Criterios de aceptación:
- [ ] Lee todas las hojas con sheet_name=None, menos Notas
- [ ] Agrega la columna ciudad con el nombre de la hoja
- [ ] Quita filas vacías y la fila TOTAL
- [ ] Renombra columnas al contrato

### BUG-01 · normalizar_ciudad no cubre las variantes reales
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B3**

**Como** analista del cliente, **quiero** una sola forma de escribir cada ciudad, **para** que los conteos por ciudad sean correctos.

Criterios de aceptación:
- [ ] Pasan los 10 casos de test_normalizar_ciudad
- [ ] Ignora tildes y mayúsculas
- [ ] Si no reconoce la ciudad, la devuelve en formato título y escribe un warning en el log

### HU-33 · Limpiar salarios y experiencia escritos como texto
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B4**

**Como** analista del cliente, **quiero** salarios y años de experiencia como números, **para** poder sacar medianas.

Criterios de aceptación:
- [ ] '$5.200.000' pasa a 5200000 y '4,5 millones' a 4500000
- [ ] '3 años' pasa a 3
- [ ] Usa .str y pd.to_numeric(errors='coerce')
- [ ] Tests con al menos 6 casos

### HU-34 · Unificar nombres de skills con el catálogo
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B5**

**Como** analista del cliente, **quiero** que 'springboot', 'Spring' y 'spring-boot' cuenten como Spring Boot, **para** que el ranking de skills sea correcto.

Criterios de aceptación:
- [ ] Lee data/referencia/catalogo_skills.xlsx y arma un diccionario sinónimo → nombre oficial
- [ ] normalizar_skills('java / spring') devuelve 'Java|Spring Boot'
- [ ] Vive en limpieza/ para que la use también el Squad A

### HU-35 · Limpiar la base de egresados
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B6**

**Como** coordinador de empleabilidad, **quiero** la base de egresados limpia, **para** medir cuántos consiguen empleo.

Criterios de aceptación:
- [ ] 'Sí', 'si', 'SI' pasan a True; 'No', 'no' a False; vacío y 'N/A' a vacío
- [ ] Fechas de grado en 5 formatos pasan a fecha (pd.to_datetime con format='mixed')
- [ ] Elimina duplicados exactos
- [ ] Guarda data/processed/egresados.csv

### BUG-03 · El reporte usa una ruta del PC del desarrollador anterior y cuenta mal
`Squad C` · `1 pts` · `Por hacer` · Asignado: **C1**

**Como** equipo de desarrollo, **quiero** que el reporte corra en cualquier computador, **para** poder automatizarlo.

Criterios de aceptación:
- [ ] Usa las rutas de config.py
- [ ] Pasa tests/test_reporte.py
- [ ] Separa las skills por | como dice el contrato

### HU-50 · Top de skills: general y por rol
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C2**

**Como** estudiante, **quiero** saber qué skills piden para cada cargo, **para** decidir qué aprender.

Criterios de aceptación:
- [ ] Usa data/sample/ofertas_sample.csv
- [ ] str.split + explode + value_counts
- [ ] Columnas: skill, ofertas, pct_ofertas
- [ ] Versión por rol con groupby, 5 skills por rol
- [ ] Exporta top_skills.xlsx con to_excel

### HU-51 · Salario por rol y experiencia
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C3**

**Como** estudiante, **quiero** saber cuánto se gana en cada cargo según la experiencia, **para** tener expectativas realistas.

Criterios de aceptación:
- [ ] Usa data/sample/encuestas_sample.csv
- [ ] Mediana, percentil 25 y 75 por rol con groupby().agg
- [ ] Rangos 0-1, 2-4 y 5+ años con pd.cut
- [ ] Tabla rol × rango con pivot_table, exportada con to_excel

### HU-52 · Ofertas por ciudad y modalidad
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C4**

**Como** estudiante, **quiero** saber dónde están las ofertas y cuántas son remotas, **para** saber si tengo que mudarme.

Criterios de aceptación:
- [ ] pd.crosstab de ciudad × modalidad con totales
- [ ] Porcentaje de ofertas remotas
- [ ] Exporta a Excel con to_excel

### HU-53 · Tasa de empleabilidad por programa
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C5**

**Como** director de programa, **quiero** saber qué porcentaje de egresados de mi programa está empleado, **para** compararme con otros programas.

Criterios de aceptación:
- [ ] Usa data/sample/egresados_sample.csv
- [ ] Egresados, empleados, tasa % y salario mediano por programa
- [ ] Ordenado de mayor a menor tasa
- [ ] Exporta a Excel con to_excel

### HU-54 · ¿Qué skill paga más?
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C6**

**Como** estudiante, **quiero** saber qué skills están en las ofertas mejor pagadas, **para** priorizar qué aprender.

Criterios de aceptación:
- [ ] Salario medio de cada oferta = (mínimo + máximo) / 2
- [ ] Mediana del salario por skill (explode + groupby)
- [ ] Solo skills con al menos 5 ofertas con salario
- [ ] Exporta a Excel con to_excel

### HU-80 · Gráfico de skills más pedidas
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D1**

**Como** coordinador de empleabilidad, **quiero** un gráfico del top de skills, **para** mostrarlo en el comité.

Criterios de aceptación:
- [ ] Barras horizontales con matplotlib, usando ofertas_sample.csv
- [ ] Título, nombre de los ejes y fuente
- [ ] Se guarda como PNG en reportes/

### HU-81 · Gráfico de salarios por rol
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D2**

**Como** coordinador de empleabilidad, **quiero** ver cómo varían los salarios por rol, **para** explicar los rangos a los estudiantes.

Criterios de aceptación:
- [ ] Boxplot con matplotlib usando encuestas_sample.csv
- [ ] Roles ordenados por mediana
- [ ] Eje en millones de pesos
- [ ] PNG en reportes/

### HU-82 · Reporte semanal en Excel con varias hojas
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D3**

**Como** coordinador de empleabilidad, **quiero** un solo Excel con todo, **para** no buscar en varios archivos.

Criterios de aceptación:
- [ ] pd.ExcelWriter + to_excel, una hoja por tabla
- [ ] Hojas mínimas: Resumen, Top skills, Salarios, Datos
- [ ] El nombre del archivo lleva la fecha: reporte_semanal_AAAA-MM-DD.xlsx

### HU-83 · Logging para todo el proyecto
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D4**

**Como** operador del sistema, **quiero** que el programa deje registro de lo que hace, **para** saber qué pasó cuando algo falla.

Criterios de aceptación:
- [ ] logging.basicConfig en un solo lugar, a consola y a logs/talentscope_AAAA-MM-DD.log
- [ ] Reemplaza los print del código heredado
- [ ] Guía corta en el README de cómo usar log.info / log.warning

### HU-84 · Carpeta de reportes por fecha
`Squad D` · `1 pts` · `Por hacer` · Asignado: **D5**

**Como** coordinador de empleabilidad, **quiero** los reportes de cada semana en su propia carpeta, **para** no sobrescribir los anteriores.

Criterios de aceptación:
- [ ] Función que crea y devuelve reportes/AAAA-MM-DD/ con pathlib
- [ ] Todos los módulos guardan ahí sus archivos
- [ ] Test con tmp_path

### HU-85 · Instalación paso a paso probada
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D6**

**Como** nuevo integrante del equipo, **quiero** instalar el proyecto sin ayuda, **para** empezar a trabajar el mismo día.

Criterios de aceptación:
- [ ] Script instalar.bat (y instalar.sh) que crea el venv e instala dependencias
- [ ] README probado por un compañero de otro squad en su computador
- [ ] Sección de errores comunes

## Sprint 2 · Datos confiables (2026-10-29 → 2026-11-11)

**Objetivo:** Cada fuente entrega datos limpios en CSV y Excel; primeros indicadores y reportes.

### HU-15 · Entregar ofertas.csv y ofertas.xlsx según el contrato
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A1**

**Como** Squad C, **quiero** recibir las ofertas con las columnas acordadas, **para** calcular indicadores sin limpiar de nuevo.

Criterios de aceptación:
- [ ] Aplica normalizar_ciudad, parsear_salario y la fecha de HU-14
- [ ] Columnas y orden de docs/CONTRATO_DATOS.md
- [ ] Guarda data/processed/ofertas.csv y ofertas.xlsx (to_excel)

### HU-16 · Segunda fuente: Fake Jobs de Real Python
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A2**

**Como** analista del cliente, **quiero** ofertas de una segunda fuente, **para** no depender de un solo portal.

Criterios de aceptación:
- [ ] Scrapea https://realpython.github.io/fake-jobs/ (sitio hecho para practicar)
- [ ] Columnas del contrato con fuente='fakejobs'; lo que no exista queda vacío
- [ ] Exporta fakejobs.xlsx con to_excel

### HU-17 · Separar rol y nivel del título
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A3**

**Como** Squad C, **quiero** el rol y el nivel en columnas separadas, **para** analizar por cargo y por seniority.

Criterios de aceptación:
- [ ] 'Desarrollador Python Semi Senior' → rol 'Desarrollador Python', nivel 'Semi Senior'
- [ ] Cuidado: 'Semi Senior' contiene 'Senior'
- [ ] Tests parametrizados

### HU-18 · Tests del scraper sin internet
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A4**

**Como** equipo de desarrollo, **quiero** probar el scraper con HTML guardado, **para** que los tests no dependan de la red.

Criterios de aceptación:
- [ ] Fixtures de listado, detalle y última página
- [ ] monkeypatch reemplaza la descarga
- [ ] Prueba que la paginación se detiene

### HU-19 · Histórico de ofertas sin duplicados
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A5**

**Como** analista del cliente, **quiero** acumular las ofertas de cada semana, **para** ver tendencias.

Criterios de aceptación:
- [ ] Lee el histórico, pd.concat con lo nuevo y drop_duplicates por id_oferta
- [ ] Solo visita el detalle de ofertas que no conoce (menos peticiones)
- [ ] Guarda ofertas_historico.csv

### HU-20 · Bitácora de cada corrida del scraper
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A6**

**Como** operador del sistema, **quiero** un registro de cada corrida, **para** saber si funcionó sin leer el código.

Criterios de aceptación:
- [ ] Una fila por corrida: fecha, páginas, ofertas, peticiones, errores, segundos
- [ ] Se agrega al final de scraping_corridas.xlsx (leer, concat, to_excel)

### HU-40 · Consolidado de encuestas
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B1**

**Como** Squad C, **quiero** un solo archivo con todas las encuestas, **para** analizar salarios sin importar quién las envió.

Criterios de aceptación:
- [ ] pd.concat de Uniandina y Talentia ya limpias
- [ ] id_registro único ENC-0001, ENC-0002...
- [ ] Guarda encuestas.csv y encuestas.xlsx (to_excel)

### HU-41 · Egresados en Excel con una hoja por programa
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B2**

**Como** director de programa, **quiero** ver solo los egresados de mi programa, **para** hacer seguimiento.

Criterios de aceptación:
- [ ] pd.ExcelWriter: hoja 'Todos' + una hoja por programa con un for sobre groupby
- [ ] Nombres de hoja de máximo 31 caracteres

### HU-38 · Separar filas válidas de rechazadas
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B3**

**Como** coordinador de empleabilidad, **quiero** saber qué respuestas se descartaron y por qué, **para** pedir correcciones a los aliados.

Criterios de aceptación:
- [ ] Reglas: sin rol, sin salario, salario fuera de 1 a 60 millones, duplicado
- [ ] Las rechazadas van a rechazados.xlsx con una columna motivo
- [ ] Encuentra los 8 errores que traen los archivos actuales

### HU-36 · Reporte de calidad por aliado
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B4**

**Como** coordinador de empleabilidad, **quiero** saber qué tan buenos son los datos de cada aliado, **para** mostrárselo en la reunión con ellos.

Criterios de aceptación:
- [ ] Por fuente: filas leídas, rechazadas, duplicados y % de vacíos por columna
- [ ] Exporta calidad_datos.xlsx con to_excel

### HU-39 · Capacidad reservada para requerimientos del cliente
`Squad B` · `5 pts` · Asignado: **B5, B6**

El cliente suele traer requerimientos a mitad de proyecto. Esta capacidad queda libre para eso.

### HU-55 · Brecha entre lo que se enseña y lo que se pide
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C1**

**Como** director de programa, **quiero** saber qué skills pide el mercado que mi programa no enseña, **para** actualizar el plan de estudios.

Criterios de aceptación:
- [ ] Lee data/referencia/plan_estudios_programas.xlsx
- [ ] Faltantes: skills en más del 10% de ofertas que el programa no enseña (resta de conjuntos)
- [ ] Poco demandadas: enseñadas pero en menos del 5%
- [ ] Exporta brecha.xlsx

### HU-56 · Salario ofrecido vs salario reportado
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C2**

**Como** estudiante, **quiero** comparar lo que ofrecen las empresas con lo que ganan los egresados, **para** saber si negociar.

Criterios de aceptación:
- [ ] Mediana por rol en ofertas y en encuestas, unidas con merge
- [ ] Diferencia en %
- [ ] Solo roles con al menos 5 datos en cada lado

### HU-57 · Skills que se piden juntas
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C3**

**Como** estudiante, **quiero** saber qué aprender después de lo que ya sé, **para** armar un perfil coherente.

Criterios de aceptación:
- [ ] Pares de skills con itertools.combinations
- [ ] Top 15 pares más frecuentes
- [ ] Exporta a Excel

### HU-58 · ¿Qué piden para un cargo junior?
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C4**

**Como** estudiante a punto de graduarse, **quiero** saber qué piden en ofertas junior, **para** prepararme para mi primer empleo.

Criterios de aceptación:
- [ ] Filtra nivel == 'Junior'
- [ ] Top 10 skills y roles con más vacantes junior
- [ ] Exporta perfil_junior.xlsx con dos hojas

### HU-59 · Salario por ciudad y modalidad
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C5**

**Como** estudiante, **quiero** comparar salarios entre ciudades y trabajo remoto, **para** decidir dónde buscar.

Criterios de aceptación:
- [ ] Mediana por ciudad y por modalidad
- [ ] Convierte USD a COP antes de comparar
- [ ] Exporta a Excel

### HU-60 · Libro de indicadores
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C6**

**Como** Squad D, **quiero** todos los indicadores en un solo Excel, **para** armar los reportes desde un solo lugar.

Criterios de aceptación:
- [ ] Función calcular_todo() que devuelve un diccionario {nombre de hoja: DataFrame}
- [ ] indicadores.xlsx con una hoja por indicador (ExcelWriter + to_excel)

### HU-86 · Reporte semanal en HTML
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D1**

**Como** coordinador de empleabilidad, **quiero** un reporte que se abra en el navegador, **para** enviarlo por correo.

Criterios de aceptación:
- [ ] Tablas con DataFrame.to_html
- [ ] Gráficos incrustados en base64 (un solo archivo)
- [ ] Se guarda en la carpeta del día

### HU-87 · Hallazgos en texto
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D2**

**Como** coordinador de empleabilidad, **quiero** frases que resuman la semana, **para** no tener que interpretar las tablas.

Criterios de aceptación:
- [ ] 5 frases armadas con f-strings a partir de los indicadores
- [ ] Ejemplo: 'La skill más pedida es Git: aparece en el 31% de las ofertas'
- [ ] Van en la hoja Resumen y en el HTML

### HU-88 · Comando 'todo' del pipeline
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D3**

**Como** operador del sistema, **quiero** correr todo con un comando, **para** no ejecutar cada etapa a mano.

Criterios de aceptación:
- [ ] python -m talentscope.pipeline todo corre scraping, excel y reporte en orden
- [ ] Si una etapa falla, se registra y las demás siguen
- [ ] Termina con código 1 si algo falló

### HU-89 · Bitácora de corridas del pipeline
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D4**

**Como** operador del sistema, **quiero** un historial de todas las corridas, **para** saber cuándo falló algo.

Criterios de aceptación:
- [ ] corridas.xlsx: inicio, etapa, estado, segundos, detalle del error
- [ ] Cada corrida agrega filas (leer + concat + to_excel)

### HU-90 · Ficha por cargo
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D5**

**Como** estudiante, **quiero** un Excel por cargo con lo esencial, **para** tener todo de ese cargo en un archivo.

Criterios de aceptación:
- [ ] Un archivo por rol con un for sobre groupby('rol')
- [ ] Hojas: Resumen (ofertas, salario mediano, % remoto, ciudad principal), Skills, Niveles, Ofertas
- [ ] Nombres de archivo sin tildes ni espacios

### HU-91 · Gráfico de empleabilidad por programa
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D6**

**Como** director de programa, **quiero** ver la empleabilidad de los programas en un gráfico, **para** presentarlo al consejo académico.

Criterios de aceptación:
- [ ] Barras horizontales de 0 a 100%
- [ ] Título y fuente
- [ ] PNG en la carpeta del día

## Sprint 3 · Automatización (2026-11-12 → 2026-11-25)

**Objetivo:** El sistema corre solo, aguanta cambios en las fuentes y entrega reportes útiles para los estudiantes.

### HU-23 · Capacidad reservada para requerimientos del cliente
`Squad A` · `5 pts` · Asignado: **A1, A2**

El cliente suele traer requerimientos a mitad de proyecto. Esta capacidad queda libre para eso.

### HU-24 · Alerta cuando no llegan ofertas
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A3**

**Como** operador del sistema, **quiero** enterarme cuando el scraper deja de encontrar datos, **para** reaccionar el mismo día.

Criterios de aceptación:
- [ ] Si una página trae 0 ofertas, log.error con la URL
- [ ] Escribe alertas/AAAA-MM-DD.txt
- [ ] El proceso termina con código 1

### HU-25 · Detectar skills en la descripción
`Squad A` · `3 pts` · `Por hacer` · Asignado: **A4**

**Como** analista del cliente, **quiero** encontrar skills mencionadas en el texto de la oferta, **para** completar las que no traen lista.

Criterios de aceptación:
- [ ] Usa el catálogo de HU-34
- [ ] Busca palabras completas con re y \b
- [ ] Une skills de la lista y de la descripción sin repetir

### HU-26 · Completitud de los datos web
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A5**

**Como** coordinador de empleabilidad, **quiero** saber qué tan completos vienen los datos del portal, **para** confiar en los reportes.

Criterios de aceptación:
- [ ] % de ofertas con salario, con skills y con ciudad reconocida
- [ ] Una fila por corrida en completitud_web.xlsx

### HU-27 · Empresas que más publican
`Squad A` · `2 pts` · `Por hacer` · Asignado: **A6**

**Como** estudiante, **quiero** una lista de empresas que están contratando, **para** enviarles mi hoja de vida.

Criterios de aceptación:
- [ ] Por empresa: número de ofertas, roles, ciudades y cuántas son junior
- [ ] Ordenado por número de ofertas
- [ ] Exporta empresas.xlsx

### HU-37 · Procesar todos los Excel de una carpeta
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B1**

**Como** analista del cliente, **quiero** dejar los Excel en una carpeta y que se procesen solos, **para** no pedirle nada al equipo técnico.

Criterios de aceptación:
- [ ] Recorre data/raw/excel con glob('*.xlsx')
- [ ] Elige el lector según el nombre del archivo
- [ ] Si un archivo falla, lo registra y sigue con los demás

### HU-42 · Encontrar la fila de encabezados sola
`Squad B` · `3 pts` · `Por hacer` · Asignado: **B2**

**Como** equipo de desarrollo, **quiero** que el lector encuentre dónde empiezan los datos, **para** soportar archivos con títulos arriba.

Criterios de aceptación:
- [ ] Lee las primeras 10 filas con header=None
- [ ] Elige la fila que más coincide con las columnas esperadas
- [ ] Funciona para todos los aliados recibidos hasta la fecha

### HU-43 · Tests con Excel creados con to_excel
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B3**

**Como** equipo de desarrollo, **quiero** probar los lectores con archivos pequeños, **para** probar casos raros fácilmente.

Criterios de aceptación:
- [ ] Cada test crea su Excel con DataFrame.to_excel en tmp_path
- [ ] Casos: fila TOTAL, columna faltante, hoja vacía, encabezado en la fila 5

### HU-44 · Plantilla Excel para los aliados
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B4**

**Como** coordinador de empleabilidad, **quiero** mandarles a los aliados una plantilla, **para** recibir datos limpios desde el origen.

Criterios de aceptación:
- [ ] Generada con to_excel: hoja Datos con las columnas del contrato y 2 filas de ejemplo
- [ ] Hoja Instrucciones con qué va en cada columna
- [ ] plantilla_aliados.xlsx en data/referencia/

### HU-45 · TRM desde un Excel
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B5**

**Como** analista del cliente, **quiero** actualizar la tasa del dólar sin tocar el código, **para** convertir con el valor del mes.

Criterios de aceptación:
- [ ] data/referencia/trm.xlsx con columnas mes y valor
- [ ] Usa la TRM del mes más reciente
- [ ] Si el archivo no existe, usa la de config.py y avisa en el log

### HU-46 · Diccionario de datos automático
`Squad B` · `2 pts` · `Por hacer` · Asignado: **B6**

**Como** nuevo integrante del equipo, **quiero** saber qué contiene cada columna de los archivos finales, **para** usarlos sin preguntar.

Criterios de aceptación:
- [ ] Por archivo y columna: tipo, % vacíos, valores de ejemplo
- [ ] Exporta diccionario_datos.xlsx con una hoja por archivo

### HU-61 · Skills que suben y bajan
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C1**

**Como** coordinador de empleabilidad, **quiero** ver qué skills ganan demanda, **para** anticipar cambios.

Criterios de aceptación:
- [ ] Compara las dos últimas fechas del histórico
- [ ] Variación absoluta por skill
- [ ] Exporta tendencia.xlsx

### HU-62 · Top 5 de skills recomendadas por programa
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C2**

**Como** director de programa, **quiero** una lista corta de qué agregar al programa, **para** tomar decisiones rápido.

Criterios de aceptación:
- [ ] A partir de la brecha de HU-55
- [ ] 5 skills por programa ordenadas por demanda
- [ ] Exporta recomendadas.xlsx

### HU-63 · Empresas que contratan juniors
`Squad C` · `2 pts` · `Por hacer` · Asignado: **C3**

**Como** estudiante a punto de graduarse, **quiero** saber qué empresas abren vacantes junior, **para** enfocar mi búsqueda.

Criterios de aceptación:
- [ ] Por empresa: vacantes junior, roles y ciudades
- [ ] Exporta a Excel

### HU-64 · Tests de los indicadores
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C4**

**Como** equipo de desarrollo, **quiero** probar que los indicadores dan lo correcto, **para** confiar en los números del cliente.

Criterios de aceptación:
- [ ] DataFrames pequeños hechos a mano con resultados calculados en papel
- [ ] Un test por indicador

### HU-65 · API Spring Boot: top de skills
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C5**

**Como** desarrollador del portal del cliente, **quiero** consultar el top de skills por HTTP, **para** mostrarlo en la web de la universidad.

Criterios de aceptación:
- [ ] Proyecto Spring Boot en api/ (Spring Web)
- [ ] GET /api/skills/top?n=10 lee la tabla top_skills de data/processed/talentscope.db
- [ ] Respuesta según api/README.md

### HU-66 · API Spring Boot: salarios por rol
`Squad C` · `3 pts` · `Por hacer` · Asignado: **C6**

**Como** desarrollador del portal del cliente, **quiero** consultar salarios por rol, **para** mostrar rangos salariales.

Criterios de aceptación:
- [ ] GET /api/salarios?rol= lee la tabla salarios_por_rol
- [ ] 404 con mensaje si el rol no existe
- [ ] Test con MockMvc

### HU-92 · Ejecución programada
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D1**

**Como** operador del sistema, **quiero** que el pipeline corra solo cada mañana, **para** no depender de que alguien lo lance.

Criterios de aceptación:
- [ ] ejecutar_pipeline.bat que activa el venv y corre 'todo'
- [ ] Programado con schtasks (o cron en Linux)
- [ ] Evidencia de dos corridas automáticas en corridas.xlsx

### HU-93 · Archivar reportes viejos
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D2**

**Como** operador del sistema, **quiero** que no se acumulen reportes para siempre, **para** no llenar el disco.

Criterios de aceptación:
- [ ] Carpetas de reportes de más de 8 semanas se comprimen en reportes/archivo/ (shutil.make_archive)
- [ ] Se registra en el log qué se archivó

### HU-94 · Guardar los resultados en SQLite
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D3**

**Como** Squad C (API), **quiero** los resultados en una base de datos, **para** que la API de Spring Boot los lea.

Criterios de aceptación:
- [ ] DataFrame.to_sql en data/processed/talentscope.db
- [ ] Tablas: ofertas, encuestas, egresados, top_skills, salarios_por_rol, brecha
- [ ] Consulta de ejemplo en el README

### HU-95 · Mi ruta: reporte personal para un estudiante
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D4**

**Como** estudiante, **quiero** decir mi programa y el cargo que quiero y recibir un Excel, **para** saber qué me falta aprender.

Criterios de aceptación:
- [ ] python -m talentscope.pipeline mi-ruta --programa "..." --rol "..."
- [ ] Excel con las skills del rol y si las ve o no en su programa
- [ ] Incluye salario mediano del rol
- [ ] Mensaje claro si el programa o el rol no existen

### HU-96 · Índice de reportes
`Squad D` · `2 pts` · `Por hacer` · Asignado: **D5**

**Como** coordinador de empleabilidad, **quiero** una página con todos los reportes de cada semana, **para** encontrarlos fácil.

Criterios de aceptación:
- [ ] reportes/index.html con enlaces a cada carpeta y archivo
- [ ] Se regenera en cada corrida

### HU-97 · Test del pipeline completo
`Squad D` · `3 pts` · `Por hacer` · Asignado: **D6**

**Como** equipo de desarrollo, **quiero** probar el pipeline de punta a punta, **para** detectar si un squad rompe a otro.

Criterios de aceptación:
- [ ] Corre las etapas excel y reporte con los datos de data/sample
- [ ] Verifica que se crean los archivos esperados
- [ ] Usa tmp_path para no ensuciar el proyecto

## Sprint 4 · Integración y entrega (2026-11-26 → 2026-12-09)

**Objetivo:** Pipeline de punta a punta, QA cruzado y demo final al cliente.

### HU-70 · Integración de punta a punta
`Squad Todos` · `5 pts` · `Por hacer` · Asignado: **A1, B1, C1, D1**

**Como** operador del sistema, **quiero** que todo funcione junto con datos reales, **para** entregar el producto.

Criterios de aceptación:
- [ ] python -m talentscope.pipeline todo funciona en un computador limpio
- [ ] Si una etapa falla, las demás usan los últimos datos buenos
- [ ] Resultado igual o mejor que la versión de referencia mostrada en el kickoff

### HU-71 · QA cruzado entre squads
`Squad Todos` · `3 pts` · `Por hacer` · Asignado: **A2, A3, B2, B3, C2, C3, D2, D3**

**Como** cliente, **quiero** que otro equipo pruebe cada módulo, **para** recibir un producto sin sorpresas.

Criterios de aceptación:
- [ ] A prueba a B, B a C, C a D y D a A
- [ ] Cada bug se registra con pasos para reproducirlo
- [ ] Los bugs críticos se corrigen antes de la demo

### HU-72 · Manual de operación
`Squad Todos` · `2 pts` · `Por hacer` · Asignado: **A4, B4, C4, D4**

**Como** nuevo integrante del equipo, **quiero** operar el sistema siguiendo un documento, **para** no depender de quien lo construyó.

Criterios de aceptación:
- [ ] Instalación desde cero
- [ ] Cómo agregar un aliado nuevo y qué hacer si el portal cambia
- [ ] Problemas frecuentes y solución

### HU-73 · Informe final y demo al cliente
`Squad Todos` · `3 pts` · `Por hacer` · Asignado: **A5, B5, C5, D5**

**Como** cliente, **quiero** una presentación con los hallazgos, **para** decidir cambios en los programas.

Criterios de aceptación:
- [ ] Responde las 3 preguntas del cliente con datos
- [ ] Demo en vivo del pipeline
- [ ] Máximo 15 minutos

### HU-74 · Limpieza final del código
`Squad Todos` · `2 pts` · `Por hacer` · Asignado: **A6, B6, C6, D6**

**Como** equipo de desarrollo, **quiero** entregar un código ordenado, **para** que otro equipo lo pueda mantener.

Criterios de aceptación:
- [ ] Sin print, sin rutas quemadas, sin código comentado
- [ ] pytest completo en verde
- [ ] Docstring en cada función pública
