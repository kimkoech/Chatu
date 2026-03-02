# Chatu
A Swahili-to-Python translator and runner.

## Purpose

Chatu lets people write Python-like programs using Swahili keywords and built-in names,
then translates that source to standard Python so it can run on a normal Python interpreter.
This makes it useful as an educational bridge for Swahili speakers learning Python syntax
and programming fundamentals.

## Basic usage

Run a Chatu script directly:

```bash
python chatu.py examples/hujambo_dunia.ch
```

Compile only (do not execute):

```bash
python chatu.py examples/hujambo_dunia.ch --compile-only
```

Set a custom output file:

```bash
python chatu.py examples/hujambo_dunia.ch --output out.py
```

Set a custom translations CSV:

```bash
python chatu.py examples/hujambo_dunia.ch --translations translations.csv
```

## How it works

- Loads a Swahili→English keyword dictionary from `translations.csv`.
- Tokenizes the `.ch` source and translates only identifier tokens.
- Writes compiled Python to `<input>.chc` by default.
- Executes the compiled file unless `--compile-only` is provided.

## History

0.2.1

- Clarified project purpose and intended educational use.
- Added user-friendly CLI error handling for missing files/tokenization errors.

0.2.0

- Added token-based translation (prevents accidental substring replacements).
- Added safer CSV parsing for translations.
- Added CLI options for compile-only mode, output path, and translation path.
