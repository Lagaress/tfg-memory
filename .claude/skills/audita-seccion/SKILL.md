---
name: audita-seccion
description: Orquesta el flujo completo de revisión iterativa de una sección o capítulo del TFG. Encadena thesis-reviewer, /revisar y greps targeted, consolida los hallazgos en un MD auxiliar (en .reviews/), espera las decisiones del usuario, delega al thesis-writer y verifica el resultado. Úsalo cuando el usuario pida revisar, auditar o pulir una sección concreta del TFG.
argument-hint: "[sección, capítulo o archivo .tex a revisar]"
user-invocable: true
---

# Skill de auditoría de sección del TFG

Este skill encapsula el flujo iterativo de revisión sección a sección que el usuario tiene fijado para el TFG. Orquesta los subagentes y skills existentes (`thesis-reviewer`, `/revisar`, `thesis-writer`), produce un informe auxiliar en MD para que el usuario lo lea fuera del terminal, espera decisiones y aplica los cambios.

El usuario es el árbitro final. La skill no toma decisiones de fondo por su cuenta. Tampoco aplica cambios mecánicos por adelantado: pasa por el flujo siempre.

## Fase 1: Definir alcance

1. El usuario indica la sección, capítulo o archivo a auditar (ej. "1.2 Alcance y objetivos", "Capítulo de antecedentes", "sections/preface/projectplan.tex"). Si solo da un nombre, localiza el archivo `.tex` correspondiente.
2. Identifica las líneas exactas que cubren el alcance: `\section`, `\subsection` y, si aplica, el párrafo introductorio anterior. Usa `grep -n "^\\\\section{\|^\\\\subsection{"` sobre el archivo si necesitas mapearlo.
3. Verifica tamaño y estructura. Si el alcance supera ~80-100 líneas con varias subsecciones densas, avisa al usuario y propón partirlo en sub-pases. No avances hasta confirmar.
4. Si el alcance es ambiguo (por ejemplo "el capítulo entero" cuando contiene cuatro secciones grandes), pregunta antes de seguir.

## Fase 2: Auditoría exhaustiva

Ejecuta los tres pasos en orden. Los tres son obligatorios.

### 2.1. `thesis-reviewer`

Lanza el subagente `thesis-reviewer` sobre el rango confirmado. El prompt debe cubrir:

- **Antipatrones IA**: muletillas ("es importante señalar", "cabe destacar", "resulta pertinente", "en este sentido", "en definitiva", "Al tratarse de", "En conjunto", "como se ha visto"); "no obstante" y "sin embargo" como muletillas o aperturas repetidas; léxico IA ("robusto" como adjetivo vacío, "panorama", "crucial", "holístico", "multifacético", "pivotal"); tricolon abusivo; antítesis sistemática "no X, sino Y"; aperturas mecánicas; voz pasiva refleja en cascada; listas disfrazadas de prosa; gerundios de modo o consecuencia.
- **Reglas duras del proyecto**: sin `\textbf{}`; comillas LaTeX dobles ``texto''; em-dashes con `---`, máximo una pareja por párrafo; cursiva con `\textit{}` para anglicismos y términos en otro idioma; citas con `~\cite{}` (espacio no separable previo); `%` escapado con `\%`; sin paths ni nombres de archivo en prosa; acrónimos introducidos en primera aparición.
- **Convención terminológica del proyecto** (memoria `project_dixi_terminology`): técnica (estrategia conceptual), motor (implementación ejecutable), híbrido (combinación), sistema o Dixi (producto global). Prohibido "enfoque" como sinónimo de técnica. "Hibridaciones" como sustantivo concreto, también fuera.
- **Coherencia con secciones adyacentes y resumen**: cifras compartidas, acrónimos ya introducidos en capítulos previos, terminología consistente.
- **Citas e integridad bibliográfica**: lista de claves citadas, presencia en `bibliography.bib`, formato `~\cite{}`, posición correcta.
- **Cifras y afirmaciones verificables**: cada cifra con su cita asociada y marca de "verificar contra fuente" o "verificar contra implementación".
- **Cohesión y arquitectura**: progresión, longitud por párrafo, ritmo, paralelismos, transiciones.
- **Tono académico**: voz, marketing latente, autoexcusa, hedging excesivo.

El reviewer devuelve hallazgos por severidad (alta / media / baja) con cita textual, ubicación y sugerencia.

### 2.2. `/revisar` (siempre)

Lanza la skill `/revisar` sobre la misma sección. La verificación contra implementación nunca sobra. Si la salida es escueta (porque la sección es contextual o de gestión sin claims técnicos directos), basta con apuntarlo en el informe.

### 2.3. Greps targeted cuando aplique

Si el reviewer flaggea cifras o claims que dependen de otras secciones, lanza greps directos para verificar coherencia. Casos típicos:

- Cifras compartidas (ej. número de pictogramas, motores, métricas).
- Coherencia de tests estadísticos u otras decisiones metodológicas entre capítulos.
- Definiciones de acrónimos en varios sitios.
- Nombres propios o términos terminológicos que pueden divergir entre archivos.
- Formato de precios, fechas, decimales.

Anota los resultados de los greps en el informe.

## Fase 3: Consolidar el informe auxiliar en MD

Crea el archivo `thesis/.reviews/<archivo-base>-<seccion-opcional>-<fecha>.md`. Si la carpeta `.reviews/` no existe, créala. Ejemplos:

- Auditoría completa de `sections/preface/projectplan.tex` → `.reviews/projectplan-2026-04-25.md`
- Solo subsección 1.2 de `introduction.tex` → `.reviews/introduction-1-2-alcance-2026-04-25.md`

Si ya existe un archivo con el mismo nombre, añade un sufijo `-v2`, `-v3` o similar para no sobrescribir.

Estructura del MD (ordenada para que el usuario pueda leer y anotar):

```markdown
# Auditoría: <Sección o Capítulo>

- Archivo: `<ruta>`
- Alcance: líneas X a Y
- Fecha: YYYY-MM-DD

## Resumen ejecutivo

- Hallazgos altos: N
- Hallazgos medios: N
- Hallazgos bajos: N
- Valoración global: <una línea>

## Cross-checks ejecutados

- `/revisar`: <síntesis breve de lo que aportó o no>
- Greps: <lista de los greps lanzados y qué buscaron>

## Hallazgos altos

### A.1 — <título corto>
- Ubicación: línea X
- Texto actual: "<cita>"
- Diagnóstico: <qué falla>
- Sugerencia: "<reformulación>"
- **Voto del agente**: <actuar / dejar / decisión del usuario>
- [ ] Decisión: ___

(repetir por hallazgo)

## Hallazgos medios

(mismo formato)

## Hallazgos bajos

(mismo formato, puede ser más resumido)

## Decisiones que necesitan input del usuario

(listado explícito de los puntos donde el agente no puede decidir solo)

## Pendientes para futuras pasadas

(hallazgos detectados que quedan fuera del alcance actual)
```

El **voto del agente** es razonado y honesto. Distingue:

- "Actuar": hallazgo claro, mecánico o con sugerencia que se sostiene.
- "Dejar": el hallazgo es discutible y la versión actual es defendible.
- "Decisión del usuario": no hay base para que el agente decida (cifras, decisiones de fondo, elecciones estilísticas con tradeoffs reales).

## Fase 4: Esperar decisiones del usuario

En el chat, avisa al usuario con un mensaje breve:

- Ruta del MD generado.
- Recuento de severidades.
- Puntos concretos que requieren decisión explícita (de la sección "Decisiones que necesitan input").

NO apliques nada hasta que el usuario te dé sus decisiones (en chat). El usuario lee el MD por su lado y te copia decisiones o las marca con respuestas tipo "1: sí, 2: no, 3: ajustar a X".

## Fase 5: Aplicar cambios

Una vez recibidas las decisiones, distingue:

1. **Cambios mecánicos**: renames, erratas, comillas, escapado de `%`, sustitución de un término por otro, cambio de un cite por otro, expansión de un acrónimo. Aplícalos con `Edit` directamente.
2. **Reescritura de prosa**: reformular párrafos, partir o fusionar, cambiar aperturas, romper tricolon, reescribir conectores, ajustar longitud, mejorar transiciones. Delega SIEMPRE al subagente `thesis-writer` con un prompt que incluya:
   - Lista numerada y exacta de cambios a aplicar.
   - Reglas duras del proyecto.
   - Convención terminológica.
   - Lo que NO debe tocar.
3. **Cambios estructurales mayores**: reorganizar varios párrafos, mover bloques entre subsecciones. Delega al thesis-writer con un plan claro de la nueva estructura y la justificación.

Si el usuario propone cambios adicionales sobre la marcha (durante la sección 5), aplícales la regla de "evaluar antes de aplicar": razona si tienen sentido y, si no, dilo en lugar de ejecutar a ciegas (memoria `feedback_evaluate_user_proposals`).

## Fase 6: Verificar

Tras el thesis-writer, lee el archivo en disco con `Read`. Confirma:

- Que las líneas cambiadas coinciden con el plan.
- Que las decisiones del writer que se apartan del plan están justificadas (en general el writer las explica al final de su salida).
- Que no se introdujeron antipatrones nuevos.
- Que el resto del archivo no se tocó por error.

## Fase 7: Resumen y commit

Presenta al usuario un resumen breve en chat:

- Qué cambió, agrupado por punto del plan original.
- Decisiones del writer que se apartaron del plan, si las hubo.
- Pendientes que quedan fuera y que conviene apuntar.

Opcional: actualiza el MD del informe con un apéndice de cierre tipo "Aplicado: ... / Descartado: ... / Pendiente para próxima pasada: ...".

Pregunta al usuario por commit y push. Si confirma:

- `git add` solo los archivos tocados.
- Mensaje en inglés siguiendo el estilo del repo: título en imperativo, cuerpo con bullets descriptivos, trailer `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`.
- Push.
- Verifica con `git status`.

Si Overleaf ha empujado en paralelo y origin tiene una rama de Overleaf con cambios diverged, evalúa si la versión local debe ganar. Si es así, resuelve con `git merge -s ours <rama-overleaf>` para registrar la integración sin perder el trabajo local. Confirma con el usuario antes de hacerlo.

## Reglas transversales

- **No deshacer decisiones explícitas del usuario por sugerencias posteriores del reviewer** (memoria `feedback_no_undo_user_decisions`). Si el reviewer propone algo que contradice una elección que el usuario ya validó, márcalo como conflicto en el informe y NO lo apliques sin consultar.
- **Evaluar antes de aplicar las propuestas del usuario** (memoria `feedback_evaluate_user_proposals`). Si el usuario propone un cambio en forma de pregunta o sugerencia abierta, razona pros y contras antes de tocar nada.
- **Las skills y subagentes son herramientas, no autoridad**. Sus salidas se cruzan contra las decisiones del usuario y la coherencia del proyecto.
- **Sin em-dashes en chat** (memoria `feedback_no_em_dashes_chat`). En el MD del informe sí se pueden usar si los necesitas (es un archivo, no chat).
- **No paths ni nombres de archivo en el cuerpo del TFG** (memoria `feedback_no_code_file_references`). Esta regla NO aplica al MD del informe (donde sí citas rutas).

## Cuando NO aplicar este flujo

- Cambios mecánicos puntuales aislados (un label, una errata concreta, un cite roto): edición directa, sin pase de auditoría.
- Edición de `.bib`, `config/*.tex`, imágenes: edición directa.
- Cuando el usuario pide algo que no es una auditoría de sección (escribir desde cero, ampliar, resumir, etc.): redirige al subagente o skill apropiado.
