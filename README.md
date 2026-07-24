# Calculator Engine

A Python calculator engine that supports arithmetic expression evaluation and numeral system conversion.

## Features

- Basic arithmetic operations (+, -, *, /)
- Operator precedence
- Parentheses support
- Implicit multiplication (e.g. `2(3+4)`)
- Negative numbers
- Expression validation
- Numeral system conversion
  - Binary
  - Octal
  - Decimal
  - Hexadecimal
- Unit tests with Pytest

## Project Structure

```
calculator.py                 # Calculator engine
numeral_system_converter.py   # Base converter
tests/
    test_calculator.py
    test_converter.py
```

## Requirements

- Python 3.11+
- pytest

## Run Tests

```bash
python -m pytest
```

## Future Plans

- Flet GUI
- Decimal number support
- Calculation history
- Scientific functions