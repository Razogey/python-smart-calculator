class BaseConverter:
    
    def to_decimal(self, number: str, base: int) -> int:
        decimal_number=0
        number = [int(bit) for bit in number]
        number.reverse()
        for i in range(len(number)):
            bit = number[i] * (base**i)
            decimal_number += bit
        return decimal_number
        
    
    def from_decimal(self, number: int, base: int) -> str:
        if number == 0:
            return 0
        result = []
        while number:
            result.append(number % base)
            number //= base
        result.reverse()
        result = "".join(map(str, result))
        return result
        