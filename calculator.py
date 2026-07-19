class Calculator:

    def tokenize(self, expression):
        tokens = []
        number = ""
        
        for char in expression:
            if char.isspace():
                continue
            if char.isdigit():
                number += char
            elif char in ["+", "-", "*", "/"]:
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
    
    def calculate(self, expression):
        if expression == "":
            return "Cannot Be Empty"
        tokens = self.tokenize(expression=expression)
        return self.evaluate(tokens)

