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

def test_empty_expression():
    with pytest.raises(ValueError):
        calculator.calculate("")
    
    with pytest.raises(ValueError):
        calculator.calculate(" ")
    
def test_start_with_operator():
    with pytest.raises(ValueError):
        calculator.calculate("+10")    

def test_expression_starts_with_multiply():
    with pytest.raises(ValueError):
        calculator.calculate("*10")

def test_expression_ends_with_operator():
    with pytest.raises(ValueError):
        calculator.calculate("10+")

def test_expression_ends_with_division():
    with pytest.raises(ValueError):
        calculator.calculate("10/")

def test_invalid_character():
    with pytest.raises(ValueError):
        calculator.calculate("10+a")

def test_invalid_symbol():
    with pytest.raises(ValueError):
        calculator.calculate("10&5")

def test_two_consecutive_operators():
    with pytest.raises(ValueError):
        calculator.calculate("10++5")

def test_invalid_expression():
    with pytest.raises(ValueError):
        calculator.calculate("5/*2")

def test_simple_addition():
    assert calculator.calculate("10+5") == 15

def test_operator_precedence():
    assert calculator.calculate("10+8*5") == 50

def test_expression_with_spaces():
    assert calculator.calculate("10 + 8 * 5") == 50


