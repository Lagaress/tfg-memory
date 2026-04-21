#!/usr/bin/env python3
"""Hook PostToolUse que verifica reglas duras de estilo LaTeX del TFG.

Se dispara tras cada Edit, Write o MultiEdit sobre archivos `.tex`. Solo avisa,
nunca bloquea. Los avisos aparecen en el chat como salida del hook.

Reglas comprobadas:
  1. `\\textbf{}` prohibido (usar `\\textit{}`).
  2. `\\cite{}` debe ir precedido de `~` (espacio no separable).
  3. Comillas rectas `"..."` en vez de ``...''.
  4. `\\begin{lstlisting}` solo está permitido en `gramatica-formal.tex`.
  5. Paths o extensiones técnicas en prosa fuera de comandos LaTeX legítimos.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ALLOWED_PREFIX_CITE = {"", "~", "{"}
EXT_PATTERN = re.compile(r"\b\w+\.(tex|py|json|md|bib|yaml|yml|bst|jsonl)\b")
LEGIT_COMMAND = re.compile(
    r"\\(input|include|includegraphics|bibliography|addbibresource|href|url|ref|cite|label|texttt|textit|footnote)\{"
)
STRAIGHT_QUOTES = re.compile(r'"[^"\n]{1,200}"')
LSTLISTING_OPEN = re.compile(r"\\begin\{lstlisting\}")
CITE_CALL = re.compile(r"(^|.)\\cite\{")
TEXTBF = re.compile(r"\\textbf\{")


def read_hook_input() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def extract_file_path(data: dict) -> str:
    tool_input = data.get("tool_input") or {}
    return tool_input.get("file_path", "") or ""


def lint(path: Path) -> list[tuple[int, str, str]]:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return []

    warnings: list[tuple[int, str, str]] = []
    file_name = path.name

    for i, line in enumerate(content.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("%"):
            continue

        if TEXTBF.search(line):
            warnings.append((i, "\\textbf prohibido: usar \\textit{}", line.strip()))

        for match in CITE_CALL.finditer(line):
            prev = match.group(1)
            if prev not in ALLOWED_PREFIX_CITE:
                warnings.append(
                    (i, "cita sin tilde no separable previa: usar ~\\cite{}", line.strip())
                )
                break

        if STRAIGHT_QUOTES.search(line):
            warnings.append((i, "comillas rectas: usar ``texto''", line.strip()))

        if file_name != "gramatica-formal.tex" and LSTLISTING_OPEN.search(line):
            warnings.append(
                (i, "lstlisting solo permitido en gramatica-formal.tex", line.strip())
            )

        if not LEGIT_COMMAND.search(line) and EXT_PATTERN.search(line):
            warnings.append(
                (i, "path o extensión de archivo en prosa", line.strip())
            )

    return warnings


def main() -> int:
    data = read_hook_input()
    tool_name = data.get("tool_name", "")
    if tool_name not in {"Edit", "Write", "MultiEdit"}:
        return 0

    file_path = extract_file_path(data)
    if not file_path or not file_path.endswith(".tex"):
        return 0

    path = Path(file_path)
    if not path.is_file():
        return 0

    warnings = lint(path)
    if not warnings:
        return 0

    print(f"Avisos de estilo LaTeX en {file_path}:")
    shown = warnings[:20]
    for lineno, msg, text in shown:
        snippet = text if len(text) <= 140 else text[:137] + "..."
        print(f"  línea {lineno} [{msg}]: {snippet}")
    if len(warnings) > 20:
        print(f"  ... y {len(warnings) - 20} avisos más.")
    print("")
    print("El hook solo avisa; la edición se ha aplicado correctamente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
