# CLAUDE.md

TFG (Trabajo Final de Grado) de la Universidad de Cádiz. Documento LaTeX en español sobre un proyecto de desarrollo de software.

## Flujo de escritura

El flujo principal para escribir o actualizar secciones del TFG es el agente **thesis-writer**. Este agente orquesta automáticamente tres fases: revisar lo existente, escribir/reescribir, y verificar el resultado. Úsalo siempre que haya que modificar contenido del documento.

Flujo: **revisar** → **planificar** → **escribir** → **verificar**

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
| ARASAAC | Portal Aragonés de la Comunicación Aumentativa y Alternativa |
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
