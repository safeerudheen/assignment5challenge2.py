# Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
    
num1 = int(input("\nEnter the value for num1: "))
num2 = int(input("Enter the value for num2: "))

obj = Calculator(num1, num2)

print(f"\n{num1} + {num2} = {obj.add()}")
print(f"{num1} - {num2} = {obj.subtract()}")
print(f"{num1} * {num2} = {obj.multiply()}")
print(f"{num1} / {num2} = {obj.divide()}")

obj = Calculator(num2, num1)
print(f"\n{num2} - {num1} = {obj.subtract()}")
print(f"{num2} / {num1} = {obj.divide()}\n")
