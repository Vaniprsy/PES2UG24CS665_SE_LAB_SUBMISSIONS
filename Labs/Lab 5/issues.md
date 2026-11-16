# Static Code Analysis Issues

## Pylint

- Before: 5.62/10
- After: 10.00/10

Issues fixed:
- Missing module and function docstrings.
- Function naming convention violations.
- Mutable default argument.
- Unsafe eval() usage.
- Bare exception handling.
- Comparison with None using ==.
- Unused imports and variables.
- File handling without a context manager and explicit encoding.

## Bandit

- Before: 6 potential security issues.
- After: No issues identified.

Security issues fixed:
- B110: try/except/pass.
- B307: eval().
- B324: MD5 hashing.
- B311: insecure random number generation.
- B605: shell command execution.
- B105: hardcoded token.

Improvements included safer PIN hashing, cryptographically secure temporary PIN generation, removal of the hardcoded token, and safer file handling.

## Flake8

- Before: Multiple code-quality and formatting violations.
- After: No errors reported.

Issues fixed included unused imports, long lines, bare except clauses, unused variables, incorrect None comparisons, and missing final newline.
