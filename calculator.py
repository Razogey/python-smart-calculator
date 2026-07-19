class Calculator:
    OPERATORS  = "+-*/"
    VALID_CHARS = "0123456789+-*/() "

    def tokenize(self, expression):
        tokens = []
        number = ""
        expect_minus = True
        
        for char in expression:
            if char.isspace():
                continue
            if char.isdigit():
                number += char
                expect_minus = False
            elif char in self.OPERATORS:
                if char == "-" and expect_minus:
                    number += char
                else:
                    tokens.append(int(number))
                    tokens.append(char)
                    number = ""
                    expect_minus = True
        
        tokens.append(int(number))
        return tokens
    
    def evaluate_parentheses(self, expression):
        # 10+2*(4/2+3*2)
        while ")" in expression:
            close = expression.find(")")
            open = expression.rfind("(", 0, close)
            inside_parentheses = expression[open+1:close]
            if inside_parentheses == "":
                raise ValueError("Empty parentheses are not allowed.")
            result = self.calculate(inside_parentheses)
            expression = (expression[:open] + str(result) + expression[close+1:])
        return expression
        
    
    def evaluate(self, tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                result = tokens[i - 1] * tokens[i + 1]
                tokens[i-1 : i+2] = [result]
            elif tokens[i] == "/":
                if tokens[i+1] == 0:
                    raise ZeroDivisionError("Cannot divide By Zero.")
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
        # Remove spaces from both start and end of expression
        expression = expression.strip()

        # check if expression is empty
        if not expression:
            raise ValueError("Expression cannot be empty.")
        
        # check if start of expression is not an operator except '-' 
        if expression[0] in self.OPERATORS and expression[0] != '-':
            raise ValueError("Expression cannot start with an operator.")
        
        # check if end of expression is not an operator
        if expression[-1] in self.OPERATORS:
            raise ValueError("Expression cannot end with an operator.")
        
        # check if expression only include 0123456789+-*/() 
        for char in expression:
            if char not in self.VALID_CHARS:
                raise ValueError(f"Invalid character: {char}")
            
        # check if number of opend and closed parentheses matches
        balance = 0
        for char in expression:
            if char == "(":
                balance += 1

            elif char == ")":
                balance -= 1

                if balance < 0:
                    raise ValueError("Unmatched parentheses.")

        if balance != 0:
            raise ValueError("Unmatched parentheses.")

        # check if there is a consecutive operators excluding one '-' after different operator
        for i in range(len(expression) - 1):
            if (expression[i] in self.OPERATORS and expression[i + 1] in self.OPERATORS):
                if not (expression[i+1] == "-" and expression[i] != "-"):
                    raise ValueError("Two consecutive operators are not allowed.")
    
    def calculate(self, expression):
        expression = expression.replace(' ', '')
        self.validate_expression(expression)
        expression = self.evaluate_parentheses(expression)
        tokens = self.tokenize(expression=expression)
        return self.evaluate(tokens)

