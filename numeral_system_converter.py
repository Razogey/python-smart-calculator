
'''
hex  = A B C D E F
digit = 0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9 A B C D E F
hex_values = {"A": 10 "B": 11 "C": 12 "D": 13 "E": 14 "F": 15}
to_decimal:
    اذا كان الرقم المستقبل يحتوي على اي من hex:
        hex_digit = القيمة المساوية له في hex_values
'''

class BaseConverter:
    DIGITS = "0123456789ABCDEF"
    
    def to_decimal(self, number: str, base: int) -> int:
        decimal_number=0
        number = number.upper()
        number = list(number)
        number.reverse()
        for i in range(len(number)):
            value = self.DIGITS.index(number[i])
            bit = value * (base**i)
            decimal_number += bit
        return decimal_number
        
    
    def from_decimal(self, number: int, base: int) -> str:  
        if number == 0:
            return "0"
        result = []
        while number:
            result.append(self.DIGITS[number % base])
            number //= base
        result.reverse()
        result = "".join(result)
        return result
        