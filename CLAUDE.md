# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX thesis template for TFG (Trabajo Final de Grado) from Universidad de Cádiz. The document is written in Spanish and follows a structure suitable for software development projects.

## Build Commands

```bash
# Compile the document (run twice for references)
pdflatex main.tex

# Full build with bibliography
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Using latexmk (recommended)
latexmk -pdf main.tex

# Clean auxiliary files
latexmk -c
```

## Document Structure

```
main.tex                    # Entry point - configures metadata and includes parts
config/
  packages.tex              # LaTeX package imports
  styles.tex                # Visual styling (margins, headings, code blocks)
sections/
  1-frontmatter.tex         # Covers, abstract, acknowledgments (unnumbered)
  2-preface.tex             # Introduction, context, project plan
  3-development.tex         # Requirements, analysis, design, implementation, testing, deployment
  4-epilogue.tex            # Conclusions, license
  5-backmatter.tex          # Annexes (user guide, developer guide)
figures/                    # Images (JPG format, includes UCA logos)
bibliography.bib            # BibTeX references (uses natbib with numeric style)
apalike7.bst                # Bibliography style file
```

## Key Conventions

- **Language**: All content is in Spanish. Use `\selectlanguage{spanish}` and babel's `es-tabla` option.
- **Bibliography**: Uses natbib with numeric citations. Add references to `bibliography.bib`.
- **Code listings**: Use `lstlisting` environment. Style defined in `config/styles.tex`.
- **Figures**: Place in `figures/` directory. Use `\includegraphics` with `graphicx` package.
- **PDF metadata**: Update `\hypersetup` in `main.tex` with actual author, title, and keywords.
