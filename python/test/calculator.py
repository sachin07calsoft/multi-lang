class Calculator:

    # Method to add two numbers
    def add(self, a, b):
        return a + b

    # Method to subtract two numbers
    def subtract(self, a, b):
        return a - b

    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b

    # Method to divide two numbers
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
