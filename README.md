# Trial Repo

This repository contains a few simple Python utilities.

## Modules

- `add.py` – provides a function to add two numbers.
- `subtract.py` – subtract two numbers.
- `naked_math.py` – basic algebra functions supporting any number of arguments.
- `pdf_generator.py` – create a PDF using the `itextpdf` package.

## Using `naked_math.py`

```
from naked_math import add, subtract, multiply, div, exponential

print(add(1, 2, 3))          # -> 6
print(subtract(10, 5, 2))    # -> 3
print(multiply(2, 3, 4))     # -> 24
print(div(100, 2, 5))        # -> 10.0
print(exponential(2, 3))     # -> 8
```
