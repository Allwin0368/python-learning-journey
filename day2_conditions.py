#Day 2: Python If-Else Practice
#Topics:
# Conditions
# Logical operators
# Decision making


# 1. Even or Odd
num = int(input("Enter a number- "))
if num % 2 == 0:
    print("The no is even")
else:
    print("The no is odd")
  
# 2. Largest of Two Numbers
a = int(input("Enter first number- "))
b = int(input("Enter second number- "))

if a > b:
    print("Largest is:", a)
else:
    print("Largest is:", b)


# 3. Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 4. Simple Calculator
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    print("Result:", x / y)
else:
    print("Invalid operator")
