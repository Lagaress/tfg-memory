# CLAUDE.md

TFG (Trabajo Final de Grado) de la Universidad de Cádiz. Documento LaTeX en español sobre un proyecto de desarrollo de software.

## Orquestación automática del sistema

Este proyecto tiene agentes y skills interconectados. El Claude principal NO escribe ni edita prosa de la memoria por su cuenta: delega automáticamente en la pieza adecuada a partir de la intención del usuario, sin pedir confirmación previa y entendiendo lenguaje natural.

### Qué llamar según la intención

| Intención del usuario | Acción automática |
|---|---|
| Escribir, reescribir, editar, mejorar, ampliar, resumir o actualizar prosa en `sections/**.tex` o `main.tex` ("arregla esto", "reformula", "amplía la sección X") | Subagente `thesis-writer` |
| Cerrar bloque de edición, pedir commit, "revisa lo tocado", "¿está bien?", "¿ves algo raro?" | Subagente `thesis-reviewer` sobre los archivos modificados |
| "Revisa toda la memoria", "pase global", "auditoría transversal", "busca incoherencias entre capítulos" | Skill `/auditoria-global` |
| "Checklist de entrega", "¿está lista para entregar?", "pre-entrega", "pase final" | Skill `/presubmit` |
| Cambios mecánicos (renombrar un label, corregir una errata puntual), ficheros `.bib`, `config/*.tex`, imágenes | Edición directa, sin delegar |

Si la intención es ambigua, pregunta antes de actuar. No arranques `thesis-writer` "por si acaso" cuando la petición es una consulta o una lectura.

### Flujo interno de `thesis-writer`

Cuando delegas en `thesis-writer`, este ejecuta internamente: revisar → planificar → escribir → verificar. No micro-gestiones esos pasos.

### Hook de estilo LaTeX

Un hook `PostToolUse` (`.claude/hooks/check-latex-style.py`) audita cada edición de `.tex` y avisa por reglas duras (`\textbf{}`, `\cite{}` sin tilde, comillas rectas, `lstlisting` fuera de `gramatica-formal.tex`, paths en prosa). Solo avisa, nunca bloquea. Si salta, corrige en la siguiente iteración.

### Compilación

**IMPORTANTE: NO compilar localmente.** El usuario compila en Overleaf. No ejecutar `latexmk`, `pdflatex` ni ningún comando de build.

## Las 5 reglas de estilo críticas

1. **Todo en español**. Sin excepciones.
2. **NUNCA `\textbf{}`**. Usar `\textit{}` para énfasis y términos en otros idiomas.
3. **Prosa, no listas**. En el cuerpo del texto, integrar la información en párrafos. Sin viñetas.
4. **Sin muletillas IA**. Prohibido: "Es importante señalar", "Cabe destacar", "Resulta pertinente", "En este sentido", "En definitiva". Ver `antipatterns.md` para el catálogo completo.
5. **Datos reales**. No inventar cifras, porcentajes ni resultados. Si no se tiene el dato, dejarlo pendiente.

## Glosario del proyecto

| Término | Significado |
|---------|-------------|
| SAAC | Sistema Aumentativo y Alternativo de Comunicación |
| CAA | Comunicación Aumentativa y Alternativa |
| ARASAAC | Centro Aragonés para la Comunicación Aumentativa y Alternativa |
| Pictograma | Símbolo gráfico que representa un concepto, acción u objeto |
| NLG | Natural Language Generation (Generación de Lenguaje Natural) |
| CFG | Context-Free Grammar (Gramática Libre de Contexto) |
| FastText | Modelo de embeddings de palabras (Facebook/Meta) |
| BLEU / ROUGE / BERTScore | Métricas de evaluación de texto generado |
| Dixi | Nombre del sistema desarrollado en este TFG |

## Commands

```bash
# NO compilar localmente — el usuario compila en Overleaf
# Los comandos siguientes son solo referencia:

# Build (recommended)
latexmk -pdf main.tex

# Full build with bibliography
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Clean auxiliary files
latexmk -c
```

## Key Files

- `main.tex` — Entry point, metadata and `\input` calls
- `config/packages.tex` — Package imports
- `config/styles.tex` — Margins, headings, code block styles
- `sections/` — Content files numbered 1 through 5
- `bibliography.bib` — BibTeX references (natbib, numeric style)

## IMPORTANT: Conventions

- All content MUST be written in Spanish
- NEVER use `\textbf{}` — use `\textit{}` for emphasis instead
- Figures go in `figures/` directory (JPG format)
- Code listings use `lstlisting` environment (style in `config/styles.tex`)
- Add references to `bibliography.bib` using natbib numeric citations
- Comillas LaTeX: ``texto''
- Em-dash con `---` y espacios: `texto ---inciso--- texto`
- Acrónimos: definir en la primera aparición (nombre completo + sigla entre paréntesis)
- Citas con espacio no separable: `~\cite{}`

## Gotchas

- Always run build twice (or use `latexmk`) to resolve cross-references
- Babel requires `es-tabla` option to correctly label tables in Spanish
- `apalike7.bst` is a custom bibliography style — do not replace it
