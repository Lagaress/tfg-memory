---
name: presubmit
description: Checklist de pre-entrega del TFG. Consolida verificaciones sobre integridad bibliográfica, referencias cruzadas, figuras, reglas duras de estilo y antipatrones IA. Devuelve un informe con severidad por categoría. Úsalo antes de cerrar una entrega o versión final cuando el usuario diga "checklist de entrega", "¿está lista?", "pre-entrega" o similar.
argument-hint: ""
user-invocable: true
---

# Skill de pre-entrega

Realizas la última pasada antes de una entrega del TFG. Tu objetivo es detectar cualquier problema sistémico que un tribunal o un lector atento podría señalar: citas huérfanas, referencias rotas, figuras sin referenciar, antipatrones IA sin depurar, infracciones de la guía de estilo.

## Fase 1: Inventario

Carga en paralelo:
- `main.tex`
- Todos los `.tex` bajo `sections/` (incluido `sections/backmatter/`)
- `bibliography.bib`

## Fase 2: Verificaciones

Ejecuta todas las comprobaciones. No pares en el primer error; haz un barrido completo y agrupa los hallazgos por categoría.

### A. Bibliografía

1. Extrae todas las claves citadas con `\cite{clave}`, `\citep{clave}`, `\citet{clave}` en cualquier `.tex`.
2. Extrae todas las entradas de `bibliography.bib` (líneas que empiezan por `@tipo{clave,`).
3. Reporta:
   - **Huérfanos en bibliography.bib**: entradas que nunca se citan en el documento.
   - **Citas rotas**: claves usadas en el texto que no existen en `bibliography.bib`.

### B. Referencias cruzadas

1. Extrae todos los `\label{X}` del documento.
2. Extrae todos los `\ref{X}`, `\eqref{X}`, `\autoref{X}`, `\pageref{X}`.
3. Reporta:
   - **Labels huérfanos**: existen pero nadie los referencia. Excepción: los labels de capítulo y sección pueden quedar sin referenciar; no los marques como huérfanos salvo que el usuario pida un modo estricto.
   - **Referencias rotas**: `\ref{}` a un label que no existe.

### C. Figuras y tablas

Por cada `\begin{figure}` y `\begin{table}`:
- Comprueba que tiene `\caption{}`.
- Comprueba que tiene `\label{fig:...}` o `\label{tab:...}`.
- Comprueba que ese label aparece referenciado en el cuerpo del texto con `\ref{}`, `Figura~\ref{}`, `Tabla~\ref{}`, `\autoref{}` o `\eqref{}`.

Reporta toda figura o tabla que incumpla al menos una condición.

### D. Reglas duras del proyecto

Busca en todas las secciones:
- `\textbf{` (prohibido: solo `\textit{}`).
- `\begin{lstlisting}` fuera de `sections/development/gramatica-formal.tex`.
- Comillas rectas `"..."` en lugar de ``...''.
- `\cite{` sin `~` previo (salvo al inicio de una oración tras paréntesis o llave).
- Paths o extensiones técnicas en prosa (`.tex`, `.py`, `.json`, `.md`, `.bib`, `.yaml`) fuera de comandos LaTeX legítimos (`\input`, `\includegraphics`, `\bibliography`, `\url`, `\href`).
- Texto en idioma distinto al español (salvo citas literales entrecomilladas, términos en `\textit{}`, acrónimos, o fragmentos de código).
- `%` de comentario en medio de una línea de prosa (los comentarios LaTeX son aceptables solo en `config/` o antes de bloques, no colgados de párrafos ya escritos).

### E. Antipatrones IA

Delega en el subagente `thesis-reviewer` un barrido sobre todas las secciones buscando las categorías de antipatrones de `.claude/skills/escribir/antipatterns.md`. Consolida los hallazgos en un resumen por categoría con el conteo por capítulo.

### F. Integridad estructural

- `main.tex` incluye todos los archivos esperados en `sections/` (listar los `\input{}` y verificar existencia).
- No hay archivos `.tex` en `sections/` que nadie importe (huérfanos en disco).
- Orden de `\input{}` coherente con la numeración y estructura del documento.
- El parte y capítulos del backmatter están conectados (revisión rápida de `sections/5-backmatter.tex` y sus dependencias).

### G. Bibliografía: calidad de metadatos

Comprobaciones rápidas sobre `bibliography.bib` sin modificarlo:
- Entradas sin campo `title`.
- Entradas sin campo `author` o `editor`.
- Entradas con año fuera del rango razonable (pre-1950 o futuro).
- Entradas duplicadas por título o DOI.

## Fase 3: Informe

Devuelve el informe con esta estructura:

```
## Checklist de pre-entrega del TFG

**Fecha**: [fecha actual]
**Estado global**: [LISTO / CON HALLAZGOS MENORES / HALLAZGOS IMPORTANTES / BLOQUEANTE]

### A. Bibliografía
- N entradas en bibliography.bib
- N claves citadas en el documento
- Huérfanos (en .bib sin citar): [lista]
- Citas rotas (en texto sin entrada): [lista con archivo y línea]

### B. Referencias cruzadas
- N labels totales, N referencias totales
- Labels huérfanos: [lista, excluyendo capítulos/secciones]
- Referencias rotas: [lista con archivo y línea]

### C. Figuras y tablas
- N figuras, N tablas
- Incumplimientos: [cada uno con identificación]

### D. Reglas duras
- \textbf{} encontrados: [lista]
- lstlisting fuera de sitio: [lista]
- Comillas rectas: [lista]
- Citas sin tilde: [lista]
- Paths en prosa: [lista]
- Comentarios LaTeX en prosa: [lista]
- Idiomas extraños: [lista]

### E. Antipatrones IA
- Resumen por categoría (del informe de thesis-reviewer)
- Capítulos con mayor densidad de antipatrones

### F. Integridad estructural
- Archivos en sections/ sin \input{}: [lista]
- \input{} a archivos inexistentes: [lista]

### G. Calidad de bibliografía
- Entradas sin title: [lista]
- Entradas sin author: [lista]
- Años sospechosos: [lista]
- Duplicados probables: [lista]

### Resumen ejecutivo
- Bloqueantes: N
- Importantes: N
- Menores: N

### Siguientes pasos recomendados
1. [acción más urgente]
2. [siguiente]
3. [puede esperar]
```

## Reglas

- No edites nada. Solo diagnosticas.
- Marca como BLOQUEANTE cualquier cita rota, referencia rota, figura huérfana, `\textbf{}` o archivo referenciado con `\input{}` que no exista.
- Marca como IMPORTANTE todo lo que un tribunal notaría sin esfuerzo (huérfanos en `.bib`, densidad alta de antipatrones, figuras sin label).
- Marca como MENOR los detalles de estilo revisables en una siguiente ronda.
- Si el estado global es LISTO, dilo claramente: todo verde.
- Si hay bloqueantes, no concluyas con "está lista para entregar" aunque el resto esté bien.
