# Chatu TODOs

This list captures practical next steps for improving Chatu as a Swahili-to-Python learning tool.

## Translation coverage

- Audit `translations.csv` against modern Python 3 keywords and built-ins.
- Remove or clearly mark Python 2-only names such as `long`, `xrange`, `raw_input`, and `has_key`.
- Add common Python 3 built-ins, exceptions, and standard-library teaching examples.
- Decide on one Swahili spelling style for multi-word names and document the convention.
- Add tests for comments, strings, identifiers, attributes, and mixed translated/untranslated code.

## Compiler and runtime behavior

- Add a `--no-shebang` option for generated files when a plain Python module is preferred.
- Preserve source file metadata in compiled output, such as the input path and generation timestamp.
- Improve error messages by reporting the Chatu source line when Python compilation fails.
- Add an option to print translated Python to stdout instead of writing a `.chc` file.
- Make the default compiled-output suffix configurable.

## Command-line experience

- Add `--version` output and keep it in sync with release notes.
- Add a `chatu` console-script entry point so users do not need to call `python chatu.py` directly.
- Expand `--help` examples to show compile-only, custom translations, and custom output flows.
- Return clearer exit codes for missing files, translation errors, compile errors, and runtime failures.
- Consider a `--strict` mode that fails when an unknown Swahili identifier looks like a typo.

## Documentation and examples

- Add a quick-start tutorial that introduces variables, conditionals, loops, functions, and lists.
- Add more `.ch` examples under `examples/`, including one interactive program and one data-structure example.
- Document the CSV translation format, including comments, whitespace handling, and duplicate entries.
- Add a glossary mapping Swahili terms to Python concepts for learners.
- Include troubleshooting notes for common syntax and translation mistakes.

## Packaging and quality

- Add project metadata with `pyproject.toml`, including package name, supported Python versions, and test commands.
- Configure formatting and linting tools, such as Ruff, to keep style consistent.
- Add continuous integration that runs the unit test suite on supported Python versions.
- Add type-checking coverage for public functions.
- Add release notes for every user-facing change.

## Community and learning support

- Add contribution guidelines explaining how to suggest new translations.
- Define review criteria for Swahili terminology changes.
- Add issue templates for bug reports, translation requests, and learning-material requests.
- Identify beginner-friendly tasks for contributors.
- Gather feedback from Swahili-speaking learners and educators before expanding the language surface.
