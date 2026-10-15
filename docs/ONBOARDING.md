# Onboarding · Tu primera semana en TalentScope

Bienvenido a DataNexo. Llegas a un proyecto que **ya está en marcha**: hay código, hay deuda técnica
y hay un cliente esperando resultados. Así es la mayoría de trabajos reales.

## Día 1 (15 de octubre)

1. Clona el repositorio y sigue el *Arranque rápido* del README.
2. Corre `pytest`. Anota cuántos tests fallan y en qué archivos.
3. Levanta el portal simulado y navega las ofertas. Abre las herramientas de desarrollador (F12) e inspecciona el HTML de una tarjeta de oferta.
4. Abre los tres Excel de `data/raw/excel/` en Excel o LibreOffice. Anota todo lo "raro" que veas.
5. Lee tu HU asignada en `docs/BACKLOG.md` y escribe en el canal del squad qué entendiste y qué dudas tienes.

## Reglas del equipo

| Tema | Regla |
|---|---|
| Ramas | `feature/HU-13-parsear-salario`, `fix/BUG-02-encabezado-uniandina` |
| Commits | En español e imperativo: `Corrige encabezado de encuesta Uniandina (BUG-02)` |
| Pull requests | Mínimo **1 aprobación** de alguien de tu squad. El PR enlaza la HU. |
| Definición de Hecho | Criterios de aceptación cumplidos · tests nuevos en verde · `pytest` completo en verde · PR aprobado · documentación actualizada |
| Datos crudos | Nunca se editan a mano. Si un Excel viene mal, el código lo maneja. |
| Bloqueos | Si llevas más de 2 horas atascado, dilo en la daily. Pedir ayuda es parte del trabajo. |

## Ceremonias (sprints de 2 semanas)

| Ceremonia | Cuándo | Duración |
|---|---|---|
| Sprint planning | Primer día del sprint | 45 min |
| Daily (escrita) | Cada día de trabajo, en el canal del squad: ¿qué hice?, ¿qué haré?, ¿qué me bloquea? | 5 min |
| Refinamiento | Mitad del sprint | 30 min |
| Sprint review (demo al cliente) | Último día del sprint | 10 min por squad |
| Retrospectiva | Último día del sprint, después de la review | 20 min |

El **Scrum Master rota** cada sprint dentro del squad. El docente actúa como **Product Owner y cliente**.

## A quién preguntar

- Dudas de negocio ("¿qué significa X?", "¿esto es prioridad?"): al Product Owner.
- Dudas técnicas: primero a tu squad, después al Scrum Master del sprint, después al docente.
- Dudas sobre datos de otro squad: revisa el contrato de datos y luego pregunta al squad dueño.
