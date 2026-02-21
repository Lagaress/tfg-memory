# CLAUDE.md

TFG (Trabajo Final de Grado) de la Universidad de Cádiz. Documento LaTeX en español sobre un proyecto de desarrollo de software.

## Commands

```bash
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

## Gotchas

- Always run build twice (or use `latexmk`) to resolve cross-references
- Babel requires `es-tabla` option to correctly label tables in Spanish
- `apalike7.bst` is a custom bibliography style — do not replace it
