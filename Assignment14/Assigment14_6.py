class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"

calc = Calculator()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))
