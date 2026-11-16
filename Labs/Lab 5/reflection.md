# Reflection

## 1. What did you learn from static code analysis?

I learned that static analysis tools detect code-quality problems and potential security vulnerabilities without executing the program.

## 2. What is the purpose of each tool?

Pylint checks code quality and maintainability. Bandit identifies potential Python security issues. Flake8 checks style and common code-quality violations.

## 3. Which issues were most important?

The most important issues included unsafe eval() usage, MD5 hashing, shell command execution, insecure random number generation, and hardcoded secrets.

## 4. How did you improve the code?

I improved naming and documentation, removed unused code, corrected exception handling, replaced unsafe operations, and improved PIN hashing and temporary PIN generation.

## 5. What were the final results?

Pylint scored 10.00/10, Bandit reported no issues, and Flake8 reported no errors.
