from numeral_system_converter import BaseConverter
import pytest

converter = BaseConverter()

def test_binary_to_decimal():
    assert converter.to_decimal("1010", 2) == 10
    
def test_octal_to_decimal():
    assert converter.to_decimal("17", 8) == 15

def test_hex_to_decimal():
    assert converter.to_decimal("FF", 16) == 255
    
def test_decimal_to_binary():
    assert converter.from_decimal(10, 2) == "1010"

def test_decimal_to_octal():
    assert converter.from_decimal(15, 8) == "17"

def test_decimal_to_hex():
    assert converter.from_decimal(255, 16) == "FF"
    
def test_zero_to_binary():
    assert converter.from_decimal(0, 2) == "0"
    
def test_invalid_digit_for_binary():
    with pytest.raises(ValueError):
        converter.to_decimal("29", 2)
        
def test_invalid_digit_for_octal():
    with pytest.raises(ValueError):
        converter.to_decimal("8", 8)
        
def test_invalid_digit_for_hex():
    with pytest.raises(ValueError):
        converter.to_decimal("G", 16)
        
def test_invalid_base_low():
    with pytest.raises(ValueError):
        converter.to_decimal("1010", 1)
        
def test_invalid_base_high():
    with pytest.raises(ValueError):
        converter.to_decimal("1010", 17)

def test_invalid_base_from_decimal():
    with pytest.raises(ValueError):
        converter.from_decimal(10, 20)

def test_lowercase_hex():
    assert converter.to_decimal("ff", 16) == 255



