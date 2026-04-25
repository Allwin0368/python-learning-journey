# Simple Add Function
def add(a, b):
    return a + b

result = add(10, 5)
print("Addition:", result)


# Function to find square
def square(num):
    return num * num

number = int(input("Enter a number: "))
print("Square is:", square(number))


# Factorial using function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter number for factorial: "))
print("Factorial is:", factorial(num))


# Simple Calculator using functions
def calculator(a, b, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "Invalid operator"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(a, b, operator))
