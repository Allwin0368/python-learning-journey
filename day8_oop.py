# 1. Simple Class and Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating object
s1 = Student("Allwin", 22)
s1.show_details()


# 2. Simple Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))


# 3. Bank Account Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Balance:", self.balance)


acc = BankAccount("Allwin", 50000)
acc.deposit(5000)
acc.show_balance()
