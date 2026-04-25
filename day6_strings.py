# 1. Reverse a String
word = input("Enter a string: ")

reversed_word = word[::-1]
print("Reversed String:", reversed_word)


# 2. Palindrome Check
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 3. Count Vowels
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


# 4. Uppercase and Lowercase
name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())


# 5. String Length
message = input("Enter a message: ")

print("Length of string:", len(message))
