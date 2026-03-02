#!/usr/bin/env python3
"""Chatu CLI.

Translate a `.ch` script written with Swahili keywords into Python and execute it.
"""

from __future__ import annotations

import argparse
import io
import subprocess
import sys
import tokenize
from pathlib import Path

import translations as TRANS


DEFAULT_TRANSLATIONS_FILE = "translations.csv"


def translate_source(source: str, swa_to_eng: dict[str, str]) -> str:
    """Translate Swahili identifiers in Python source code to English.

    Uses Python tokenization so only identifier tokens are translated.
    String literals, comments, and partial-word substrings are left intact.
    """
    translated_tokens = []
    stream = io.StringIO(source)

    for token in tokenize.generate_tokens(stream.readline):
        tok_type, tok_string, start, end, line = token

        if tok_type == tokenize.NAME and tok_string in swa_to_eng:
            tok_string = swa_to_eng[tok_string]

        translated_tokens.append((tok_type, tok_string, start, end, line))

    return tokenize.untokenize(translated_tokens)


def compile_script(script_path: Path, translations_file: Path, output_path: Path | None = None) -> Path:
    """Compile a Chatu script to a Python file and return compiled file path."""
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")
    if not translations_file.exists():
        raise FileNotFoundError(f"Translations file not found: {translations_file}")

    swa_to_eng = TRANS.gen_map(str(translations_file))[0]
    source = script_path.read_text(encoding="utf-8")
    converted = translate_source(source, swa_to_eng)

    compiled_path = output_path or script_path.with_name(f"{script_path.name}c")
    compiled_path.write_text("#!/usr/bin/env python3\n\n" + converted, encoding="utf-8")
    return compiled_path


def execute_python_script(script_path: Path) -> int:
    """Execute a Python script and return its exit code."""
    result = subprocess.run([sys.executable, str(script_path)], check=False)
    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Translate and execute a Chatu (.ch) script")
    parser.add_argument("chatu_script", type=Path, help="Path to .ch script")
    parser.add_argument(
        "-t",
        "--translations",
        default=DEFAULT_TRANSLATIONS_FILE,
        type=Path,
        help="Path to translations CSV file (default: translations.csv)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path for compiled Python output (default: <script>.chc)",
    )
    parser.add_argument(
        "--compile-only",
        action="store_true",
        help="Only compile the script; do not execute it",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        compiled_path = compile_script(args.chatu_script, args.translations, args.output)
    except (FileNotFoundError, tokenize.TokenError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.compile_only:
        print(f"Compiled: {compiled_path}")
        return 0

    return execute_python_script(compiled_path)


if __name__ == "__main__":
    raise SystemExit(main())
