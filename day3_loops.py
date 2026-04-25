
#Day 3: Python Loops Practice
#Topics:
# for loop
#while loop
# multiplication table
# factorial
# sum of numbers


# 1. Print numbers from 1 to 50 using for loop
print("Numbers from 1 to 50:")
for i in range(1, 51):
    print(i)


# 2. Multiplication Table
num = int(input("Enter a number for multiplication table: "))

print("Multiplication Table of", num)
for i in range(1, 21):
    print(num, "a", i, "=", num * i)


# 3. Sum of numbers from 1 to n
n = int(input("Enter a number for sum: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)


# 4. Factorial of a number
fact_num = int(input("Enter a number for factorial: "))
factorial = 1

for i in range(1, fact_num + 1):
    factorial *= i

print("Factorial is:", factorial)


# 5. Reverse a number using while loop
number = int(input("Enter a number to reverse: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number is:", reverse)
