class Calculator:
    OPERATORS  = "+-*/"

    def tokenize(self, expression):
        tokens = []
        number = ""
        
        for char in expression:
            if char.isspace():
                continue
            if char.isdigit():
                number += char
            elif char in self.OPERATORS:
                tokens.append(int(number))
                tokens.append(char)
                number = ""
        if number:
            tokens.append(int(number))
        return tokens
                
    
    def evaluate(self, tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                result = tokens[i - 1] * tokens[i + 1]
                tokens[i-1 : i+2] = [result]
            elif tokens[i] == "/":
                if tokens[i+1] == 0:
                    raise ZeroDivisionError
                result = tokens[i - 1] / tokens[i + 1]
                tokens[i-1 : i+2] = [result]
            else:
                i += 1
                
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                result = tokens[i - 1] + tokens[i + 1]
                tokens[i-1 : i+2] = [result]
            elif tokens[i] == "-":
                result = tokens[i - 1] - tokens[i + 1]
                tokens[i-1 : i+2] = [result]
            else:
                i += 1
        return tokens[0]
    
    def validate_expression(self, expression: str):
        expression = expression.strip()

        if not expression:
            raise ValueError("Expression cannot be empty.")
        
        if expression == "":
            raise ValueError("Expression cannot be empty.")
        
        if expression[0] in self.OPERATORS:
            raise ValueError("Expression cannot start with an operator.")
        
        if expression[-1] in self.OPERATORS:
            raise ValueError("Expression cannot end with an operator.")
        
        for char in expression:
            if char not in "0123456789+-*/ ":
                raise ValueError(f"Invalid character: {char}")

        for i in range(len(expression) - 1):
            if (expression[i] in self.OPERATORS and expression[i + 1] in self.OPERATORS):
                raise ValueError("Two consecutive operators are not allowed.")
        
            
    
    def calculate(self, expression):
        expression = expression.replace(' ', '')
        self.validate_expression(expression)
        tokens = self.tokenize(expression=expression)
        return self.evaluate(tokens)

calc = Calculator()
print(calc.calculate(expression="10 + 8 * 5"))