# Python Smart Calculator

A Python smart calculator that supports arithmetic expression evaluation and numeral system conversion.
A smart calculator built with Python that supports arithmetic expression evaluation and numeral system conversion. The project focuses on clean architecture, input validation, and unit testing.

## Features

### Calculator Engine

- Evaluate arithmetic expressions
- Operator precedence (`*` and `/` before `+` and `-`)
- Parentheses support (including nested parentheses)
- Negative number support
- Decimal number support
- Implicit multiplication
  - `2(3+4)`
  - `(2)(3)`
  - `2.5(4+2)`

### Expression Validation

- Rejects empty expressions
- Detects invalid characters
- Detects consecutive operators
- Detects unmatched parentheses
- Rejects empty parentheses
- Rejects invalid decimal numbers (`5..3`, `5.4.2`)
- Prevents division by zero

### Numeral System Converter

- Binary ↔ Decimal
- Octal ↔ Decimal
- Hexadecimal ↔ Decimal
- Conversion between any supported bases (2–16)

## Unit Tests

The project includes comprehensive unit tests using **pytest**.

Current test coverage includes:

- Arithmetic operations
- Operator precedence
- Parentheses
- Nested expressions
- Negative numbers
- Decimal numbers
- Implicit multiplication
- Expression validation
- Numeral system conversion

## Technologies

- Python 3
- Pytest
- Git & GitHub

## Calculator Engine Content

The calculator engine is responsible for:

- Tokenizing expressions
- Validating expressions
- Evaluating arithmetic operations
- Supporting parentheses and negative numbers

## Project Structure

``` python
.
├── calculator.py
├── numeral_system_converter.py
├── tests/
│   ├── test_calculator.py
│   └── test_converter.py
├── README.md
└── requirements.txt
```

## Running Tests

```bash
python -m pytest
```

## Future Improvements

- Flet graphical user interface (GUI)
- Scientific calculator functions
- Calculation history
- Scientific functions
- Memory operations
- Support for additional mathematical operators
