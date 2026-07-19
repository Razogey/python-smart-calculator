from numeral_system_converter import BaseConverter

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