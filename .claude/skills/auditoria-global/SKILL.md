---
name: auditoria-global
description: Ejecuta una auditoría transversal de toda la memoria del TFG cargando todas las secciones a la vez. Detecta incoherencias que solo se ven con la vista completa: términos con nombres distintos, acrónimos introducidos tarde, cifras que no casan entre capítulos, repetición de contenido, rupturas de tono, citas huérfanas. Úsalo cuando el usuario pida "revisa toda la memoria", "pase global", "auditoría transversal" o cuando se cierre una fase importante.
argument-hint: "[opcional: foco, por ejemplo 'terminología', 'figuras', 'citas', 'cifras', 'tono']"
user-invocable: true
---

# Skill de auditoría global

Aprovechas el contexto de 1M de Opus para leer la memoria completa de una sola vez y detectar inconsistencias que un barrido por capítulos no encuentra.

## Fase 1: Carga total

Lee en paralelo:
- `main.tex`
- Todos los `.tex` bajo `sections/` (incluido `sections/backmatter/`)
- `bibliography.bib`
- `.claude/skills/escribir/antipatterns.md` (guía)
- `.claude/skills/escribir/writing-samples.md` (calibración)

## Fase 2: Análisis transversal

Si el usuario pasa un foco como argumento, limita el análisis a esa categoría. Si no, recorre todas.

### Terminología

Construye un mini-glosario de los términos técnicos del TFG a partir de su primer uso. Marca:
- Conceptos con variantes léxicas ("gramática formal" vs "gramática libre de contexto" vs "CFG") que no se aclaran como sinónimos.
- Acrónimos definidos más de una vez.
- Acrónimos usados antes de definirse.
- Nombres del sistema o de componentes que cambian entre capítulos.

### Cifras y datos

Extrae todas las cifras numéricas del documento (porcentajes, conteos, tamaños de corpus, número de participantes, tiempos, cifras de resultados). Agrúpalas por magnitud descrita. Reporta cualquier divergencia entre capítulos. Ejemplo: si la introducción dice "232 pictogramas" y un capítulo posterior "230 pictogramas", eso es un hallazgo crítico.

### Citas bibliográficas

- Extrae todas las claves usadas con `\cite{clave}`, `\citep`, `\citet`.
- Extrae todas las entradas de `bibliography.bib`.
- Reporta:
  - Entradas huérfanas: están en `bibliography.bib` pero nadie las cita.
  - Citas rotas: claves usadas en el texto que no existen en `bibliography.bib`.

### Figuras y tablas

Recorre todo `\begin{figure}` y `\begin{table}`. Por cada una comprueba:
- Tiene `\caption{}`.
- Tiene `\label{fig:...}` o `\label{tab:...}`.
- Su label aparece citado con `\ref{}`, `Figura~\ref{}` o `Tabla~\ref{}` en el texto.

Reporta cualquier incumplimiento.

### Tiempo verbal y voz

Revisa si el tiempo verbal dominante es consistente dentro de cada tipo de contenido:
- Descripción de decisiones de diseño: pasado o presente (mantener elegido).
- Descripción de resultados: pasado.
- Descripción del sistema actual: presente.

Reporta saltos inconsistentes (por ejemplo, un capítulo en pasado y el siguiente en presente sin motivo estructural).

### Cohesión entre capítulos

- Contenido duplicado: misma explicación en dos capítulos.
- Referencias cruzadas: `\ref{}` a labels inexistentes.
- Transiciones entre capítulos: ¿la primera frase del capítulo N engancha con la idea de cierre del capítulo N-1?
- Terminología divergente: ¿el capítulo de evaluación usa términos distintos a los del capítulo de diseño para lo mismo?

### Tono y estilo global

Compara el tono de capítulos aleatorios con `writing-samples.md`. Marca capítulos que se desvían (demasiado formal, demasiado coloquial, demasiado abstracto, exceso de antipatrones).

## Fase 3: Delegación selectiva

Para el análisis detallado de antipatrones por capítulo, delega en el subagente `thesis-reviewer` pasándole lotes de 2-3 secciones relacionadas. Consolida los resultados en tu informe final.

## Fase 4: Informe consolidado

```
## Auditoría global del TFG

**Fecha**: [fecha actual]
**Alcance**: [todos los capítulos / foco indicado]
**Archivos analizados**: N

### Terminología
- [hallazgo 1 con cita y ubicaciones]
- ...

### Cifras y datos
- [divergencia encontrada, con las dos ubicaciones y los dos valores]
- ...

### Citas bibliográficas
- Entradas huérfanas en bibliography.bib: [lista de claves]
- Citas a claves inexistentes: [lista con archivo y línea]

### Figuras y tablas
- [cada incumplimiento con figura/tabla identificada]

### Tiempo verbal y voz
- [saltos detectados, con ubicaciones]

### Cohesión entre capítulos
- [hallazgos con secciones implicadas]

### Tono y estilo global
- Capítulos más alineados con writing-samples: [lista]
- Capítulos con desviación significativa: [lista con descripción]

### Resumen ejecutivo
- Hallazgos críticos: N (bloquean calidad del documento)
- Hallazgos de coherencia: N
- Hallazgos de estilo: N
- Valoración global: [una frase]

### Prioridades recomendadas
1. [acción más urgente]
2. [siguiente acción]
3. [acción que puede esperar]
```

## Reglas

- No edites archivos en esta skill. Solo diagnosticas.
- Si el usuario quiere corregir un hallazgo concreto, el Claude principal delega en `thesis-writer` con instrucciones específicas.
- Prioriza hallazgos que afectan a la corrección del documento (cifras inconsistentes, citas rotas) sobre detalles de estilo.
- Si un hallazgo se repite mucho (ej. 30 em-dashes en un capítulo), agrúpalo con conteo en vez de listarlo entero.
- Si el alcance es demasiado grande para un único informe legible, agrupa por capítulo dentro de cada categoría.
