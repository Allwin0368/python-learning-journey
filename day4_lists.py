# 1. Create a list and print max + min
numbers = [3, 6, 8, 19, 15]

print("List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# 2. Take 10 numbers from user and store in list
user_num = []

for i in range(10):
    n = int(input("Enter number: "))
    user_num.append(n)

print("User List:", user_num)


# 3. Sum of all elements
print("Sum of elements:", sum(user_num))


# 4. Count even numbers in list
count = 0

for num in user_num:
    if num % 2 == 0:
        count += 1

print("Even numbers count:", count)


# 5. Reverse the list
user_num.reverse()
print("Reversed List:", user_num)
