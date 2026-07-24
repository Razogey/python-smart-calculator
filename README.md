# Python Smart Calculator

A Python smart calculator that supports arithmetic expression evaluation and numeral system conversion.

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

## Calculator Engine

The calculator engine is responsible for:
- Tokenizing expressions
- Validating expressions
- Evaluating arithmetic operations
- Supporting parentheses and negative numbers

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
