import pytest
from calculator import Calculator

calculator = Calculator()

def test_addition():
    assert calculator.calculate("5+3") == 8

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

def test_negative_number_at_begining():
    assert calculator.calculate("-5*8")  == -40

def test_calculate_negatvive_number():
    assert calculator.calculate("5*-8")  == -40

def test_pair_or_parentheses():
    assert calculator.calculate("2*(3+2)") == 10
    
def test_single_parentheses():
    assert calculator.calculate("(5*8)") == 40

def test_parentheses_with_multiplication():
    assert calculator.calculate("(2+3)*4") == 20

def test_nested_parentheses():
    assert calculator.calculate("2*(3+(4*5))") == 46

def test_multiple_parentheses():
    assert calculator.calculate("(2+3)*(4+1)") == 25

def test_double_nested_parentheses():
    assert calculator.calculate("((2+3)*4)+1") == 21

def test_missing_closing_parenthesis():
    with pytest.raises(ValueError):
        calculator.calculate("(5+3")

def test_missing_opening_parenthesis():
    with pytest.raises(ValueError):
        calculator.calculate("5+3)")

def test_empty_parentheses():
    with pytest.raises(ValueError):
        calculator.calculate("()")

def test_invalid_parentheses_content():
    with pytest.raises(ValueError):
        calculator.calculate("(+)")

def test_insert_multiplication():
    assert calculator.calculate("3(2+3)") == 15
    assert calculator.calculate("2(3+4)") == 14
    assert calculator.calculate("(3+4)5") == 35
    assert calculator.calculate("(2+3)(4+5)") == 45
    assert calculator.calculate("2(3)(4)") == 24
    assert calculator.calculate("(2+3)(4+5)(2)") == 90



