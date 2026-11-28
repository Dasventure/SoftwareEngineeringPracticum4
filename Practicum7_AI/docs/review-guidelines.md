# Review Guidelines

## Packages to ignore

A number of packages need to be ignored:

- `src.utils`: legacy code that does not conform to modern standards.
- `src.network`: an external package bought from another company.
- `src.user_registration.signup_form`: still a work in progress.

## What to keep in mind when reviewing

### Python version

- Use Python 3.10.

### Typing

Typing should be as strict as possible:

- No functions without fully typed arguments and return value.
- No function calls to untyped functions.
- Even if a function is not typed, its contents should be type-checked.
- No `Any`.

### Legacy code

We employ old code:

- Deprecated methods should not raise an error.
- Raising integers as an exception should be ignored.

### Other checks

- Exceptions should be checked.
- We wish to reduce code duplication. Similarities should be detected.
- All TODOs and FIXMEs should be listed.

### Reproducibility and reporting

- All checks should be reproducible. All options need to be coded inside a config file.
- Automated checks should produce:
  - a human-readable HTML report, and
  - a structured report (e.g. a JSON file).
- The human-readable report should be as complete as possible and easy to read, with line numbers, context, coloring, etc.