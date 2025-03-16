class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)
    
    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)
    
    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)
    
    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return Calculator(self.value / other.value)
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Calculator(self.value / other)
    
    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value ** other.value)
        return Calculator(self.value ** other)
    
    def log(self, base=2.718281828459045):
        if self.value <= 0:
            raise ValueError("Logarithm is undefined for non-positive values")
        result = 0
        num = (self.value - 1) / (self.value + 1)
        term = num
        n = 1
        while abs(term) > 1e-10:
            result += term / n
            term *= (num * num)
            n += 2
        return Calculator(2 * result)
    
    def __str__(self):
        return str(self.value)


num1 = Calculator(10)
num2 = Calculator(5)

print(num1 + num2)  # Output: 15
print(num1 - num2)  # Output: 5
print(num1 * num2)  # Output: 50
print(num1 / num2)  # Output: 2.0
print(num1 ** num2) # Output: 100000
print(num1.log())   # Output: log(10) dalam basis e
