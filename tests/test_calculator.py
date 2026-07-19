import pytest
from calculator import Calculator

calculator = Calculator()

def test_addition():
    assert calculator.calculate("5+3") == 8

def test_precedence():
    assert calculator.calculate("10+8*5") == 50

def test_division():
    assert calculator.calculate("20/5") == 4

def test_complex_expression():
    assert calculator.calculate("10+8*5-9/3") == 47

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.calculate("10/0")





