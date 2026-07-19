class BaseConverter:
    DIGITS = "0123456789ABCDEF"
    
    def validate_base(self, base: int):
        if not 2 <= base <= len(self.DIGITS):
            raise ValueError(f"Base must be between 2 and {len(self.DIGITS)}.")
    
    @staticmethod
    def validate_digit(value: int, base: int):
        if value >= base:
            raise ValueError(f"{value} is not valid for base {base}.")
    
    def to_decimal(self, number: str, base: int) -> int:
        self.validate_base(base)
        decimal_number=0
        number = number.upper()
        for power, digit in enumerate(reversed(number)):
            try:
                value = self.DIGITS.index(digit)
            except ValueError:
                raise ValueError(f"Invalid digit: {digit}")
            self.validate_digit(value, base)
            decimal_number += value * (base**power)
        return decimal_number
        
    
    def from_decimal(self, number: int, base: int) -> str:  
        self.validate_base(base)
        if number == 0:
            return "0"
        result = []
        while number:
            result.append(self.DIGITS[number % base])
            number //= base
        result.reverse()
        result = "".join(result)
        return result
        